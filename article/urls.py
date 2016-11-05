from django.conf.urls import url,include
from article.views import article,articles,language,create,like_article,search_titles

urlpatterns = [
	url(r'^all/$',articles),
	url(r'^get/(?P<article_id>\d+)/$',article),
	url(r'^like/(?P<article_id>\d+)/$',like_article),
	url(r'^language/(?P<language>[a-z\-]+)/$',language),		 
	url(r'^create/$',create),
	url(r'^search/$',search_titles),
	#url(r'^admin/', admin.site.urls),
]
