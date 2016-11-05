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
var csrftoken = getCookie('csrftoken');
$(function(){
	$('#search').keyup(function(){
		
		$.ajax({
			type:"POST",
			beforeSend: function (request)
            		{
				request.setRequestHeader("X-CSRFTOKEN", csrftoken);
			},
			url:"/articles/search/",
			data:{
				'search_text':$('#search').val(),
				'csrfmiddlewaretoken':$('input[name="csrfmiddlewaretoken"]').val()
			},
			success:searchSuccess,
			dataType: 'html'
		});
	});
});
function searchSuccess(data,textStatus,jqXHR)
{
	$('#search-results').html(data);
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
