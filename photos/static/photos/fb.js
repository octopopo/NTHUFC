// Load the SDK asynchronously
(
	function(d, s, id) {
		var js, fjs = d.getElementsByTagName(s)[0];
		if (d.getElementById(id)) return;
		js = d.createElement(s); js.id = id;
		js.src = "//connect.facebook.net/en_US/sdk.js";
		fjs.parentNode.insertBefore(js, fjs);
	}(document, 'script', 'facebook-jssdk')
);

//每次執行FB API時先檢查權限，如果還沒登入或權限不足就先要求使用者登入
function loginFB(todo){
	console.log('loginFB...');
	FB.login(function(response) {
		if (response.status === 'connected') {
			__facebook_user_id = response.authResponse.userID;
			console.log(response);
	      	if (response && !response.error) {
	        	if (response.authResponse.grantedScopes.indexOf('publish_actions') > -1){
	        		console.log(__facebook_user_id+'login successfully!')
					if (todo)
						todo();
				}
				else{
					console.log('Please login and grant the permission');
	        		alert('Please login and grant the permission');
				}
	      	}
	      	else{
	      		console.log('login failed');
	      		console.log(response);
	      	}
		}
		else{
		   	console.log('Please login and grant the permission');
		}
	}, {auth_type: 'rerequest', scope: 'publish_actions',return_scopes: true});
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
