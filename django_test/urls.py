"""django_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
#from django.contrib import admin
from article.views import hello,hello_template,hello_template_simple,HelloTemplate,article,articles
from django.contrib import admin
from django_test.views import login,auth_view,logout,loggedin,invalid_login,register_user,register_success
admin.autodiscover()
from django.views.generic import RedirectView

urlpatterns = [
	url(r'^hello/$',hello), 
	url(r'^hello_template/$',hello_template),  
	url(r'^hello_template_simple/$',hello_template_simple),  
	#url(r'^hello_class_view/$',HelloTemplate.asview()),  
	url(r'^articles/',include('article.urls')),
			 
	url(r'^admin/', admin.site.urls),

	url(r'^accounts/login/$',login),
	url(r'^accounts/auth$', RedirectView.as_view(url = 'accounts/auth/')),
	url(r'^accounts/auth/$',auth_view),
	url(r'^accounts/logout/$',logout),
	url(r'^accounts/loggedin/$',loggedin),
	url(r'^accounts/invalid/$',invalid_login),
	url(r'^accounts/register/$',register_user),
	url(r'^accounts/register_success/$',register_success),
			

]
