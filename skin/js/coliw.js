



$(function() {
     $('#command-window').on('keypress', function (e) {
         if(e.which === 13){

            //Disable textbox to prevent multiple submit
            $(this).attr("disabled", "disabled");
            //alert('enter key pressed.');
            var content = $(this).val();
            var lastLine = content.substr(content.lastIndexOf("\n")+1);
            $.ajax({
                url: '/processCommand',
                data: {'command':lastLine},
                type: 'POST',
                success: function(response) {
                    console.log(response);
                },
                error: function(error) {
                    console.log(error);
                }
            });
         }
   });
});