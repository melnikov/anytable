 function login(){
            var email = $('#lGeM').val();
            var pwd = $('#lGpS').val();
             $.ajax({
                     type: 'POST',
                     url: '/customer/login/',
                     data: 'email='+email+'&pwd='+pwd,
                     dataType: 'html',
                     success: function(email, pwd){
                                 window.location = '/customer/profile/';

                     },
                     error: function(response){
                        // console.log(response)
                         alert(response)
                     }
                 });
        }