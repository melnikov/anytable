 function register(){
            var name = $('#name').val();
            var email = $('#email').val();
            var pwd = $('#pwd').val();
             $.ajax({
                     type: 'POST',
                     url: '/customer/register/',
                     data: 'name='+name+'&email='+email+'&pwd='+pwd,
                     dataType: 'html',
                     success: function(email, pwd){
                                 window.location = '/customer/profile/';

                     }
                 });
        }