from flask import Flask, request
from flask import render_template
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__, static_folder='skin', static_url_path='/skin')
app.run(host='127.0.0.1', port=80)
CORS(app, origin='*')
@app.route("/coliw/")
# @app.route("/cmd")
# def cmd():
#     return render_template('index.html')
#
# def hello():
#     return "Welcome to Python Flask!"


@app.route('/processCommand', methods=['POST'])
#@cross_origin()
#@crossdomain(origin='*')

#@crossdomain('*')
def processCommand():
    command =  request.form['command'];
    return json.dumps({'status':'OK','command':command});

if __name__ == "__main__":
    app.run()



@app.route("/cmd")
def cmd():
        return render_template('index.html')



