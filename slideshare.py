import sys, os, urllib, time
from hashlib import sha1
from xml2dict import fromstring
from urllib import request

API_VERSION = 2
service_url_dict = {
    'get_slideshow': 'https://www.slideshare.net/api/%d/get_slideshow' % API_VERSION,
    'get_slideshow_by_tag': 'https://www.slideshare.net/api/%d/get_slideshow_by_tag' % API_VERSION,
    'get_slideshow_by_user' : 'https://www.slideshare.net/api/%d/get_slideshow_by_user' % API_VERSION,
    'search_slideshows' : 'https://www.slideshare.net/api/%d/search_slideshows' % API_VERSION,
    'get_user_favorites' : 'https://www.slideshare.net/api/%d/get_user_favorites' % API_VERSION,
    'get_user_contacts' : 'https://www.slideshare.net/api/%d/get_user_contacts' % API_VERSION,
    'get_user_tags' : 'https://www.slideshare.net/api/%d/get_user_tags' % API_VERSION,
    'edit_slideshow' : 'https://www.slideshare.net/api/%d/edit_slideshow' % API_VERSION,
    'delete_slideshow' : 'https://www.slideshare.net/api/%d/delete_slideshow' % API_VERSION,
    'add_favorite' : 'https://www.slideshare.net/api/%d/add_favorite' % API_VERSION,
    'check_favorite' : 'https://www.slideshare.net/api/%d/check_favorite' % API_VERSION
}


def parsexml(xml):
        """
        Method which parses the xml returned by slideshare and returns a list of dict.
        Interestingly this is JSON representation of slideshare xml.
        """
        return fromstring(xml)

def return_data(json):
    """
    Method to trap slideshare error messages and return data if there are no errors
    """
    if 'SlideShareServiceError' in json:
        print('Slideshare returned the following error - {}'.format(json['SlideShareServiceError']['Message']['value']))
        return None
    return json

def get_request_params(encode=True, **args):
    """
    Method which returns the parameters required for an api call.
    """
    ts = str(time.time())
    ts_secret = ('vXa6gYOi' + ts).encode('utf-8')
    tmp_params_dict = {
        'api_key': 'Bu0pUo8w',
        'ts': ts,
        'hash': sha1(ts_secret).hexdigest()
    }
    # Add method specific parameters to the dict.
    for arg in args:
        # Include only params which has non-null value. Otherwise slideshare is getting screwed up!
        if args[arg] and arg != 'slideshow_srcfile':
            if isinstance(args[arg], bool):
                tmp_params_dict[arg] = '1' if args[arg] else '0'
            else:
                tmp_params_dict[arg] = str(args[arg])

    if not encode:
        return tmp_params_dict.encode('ascii') # data should be bytes

    request_params = urllib.parse.urlencode(tmp_params_dict)

    return request_params.encode('ascii') # data should be bytes

def call_api(service_url, **args):
    """
    Method used for calls which don't need user authentication
    prepares slideshare parameters accepting extra parameters,
    makes service call and returns JSON output
    """
    params = get_request_params(**args)
    req = urllib.request.Request(service_url_dict[service_url], params)
    data = urllib.request.urlopen(req).read()
    json = parsexml(data)
    return return_data(json)


def main():
    print("slideshow")

main()