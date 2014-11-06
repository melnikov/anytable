
function register(){
            var name = $('#name').val();
            var email = $('#email').val();
            var pwd = $('#pwd').val();
            var pwd_c = $('#pwd_c').val();
    if(pwd != pwd_c){
        $('#pwd_c').after('<span class="">Passwords do not match.</span>')

    }

             $.ajax({
                     type: 'POST',
                     url: '/customer/register/',
                     data: 'name='+name+'&email='+email+'&pwd='+pwd,
                     dataType: 'html',
                     success: function(response){
                                 //window.location = '/customer/profile/';
                         //var response = response.val();

                         if(response != 'done'){
                              $('<div style="background:red!important; font-size: 8px; width:262px;" >Please complete the field</div>').insertBefore('#'+response+'').fadeOut().fadeIn().fadeOut();
                             $('#'+response+'').addClass('er_missing_input').delay('1000').queue(function(){
                                 $(this).removeClass('er_missing_input');
                                 $(this).dequeue();
                             });
                            // $('<div style="background:red!important; font-size: 8px; " >Please complete the field</div>').insertAfter('#'+response+'').fadeOut().fadeIn().fadeOut();

                         }
                     },
                     error: function(response){
                         console.log(response)
                        // alert(response)
                     }
                 });


        }