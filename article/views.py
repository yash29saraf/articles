from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from article.models import Article
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from forms import ArticleForm

# Create your views here.

def hello(request):
	name="Yash"
	html="<html><body>Hi %s,this seems to have worked!</body></html>"%name
	return HttpResponse(html)

def hello_template(request):
	name="Yash"
	t=get_template('hello.html')
	html=t.render(Context({'name': name}))
	return HttpResponse(html)

def hello_template_simple(request):
	name="Yash"
	return render_to_response('hello.html',{'name':name})

class HelloTemplate(TemplateView):

	template_name='hello_class.html'
	def get_context_data(self,**kwargs):
		context=super(HelloTemplate,self).get_context_data(**kwargs)
		context['name']="Yash"
		return context


def articles(request):
	language='en-gb'
	session_language='en-gb'
	if 'lang' in request.COOKIES:
		language=request.COOKIES['lang']
	
	if 'lang' in request.session:
		session_language=request.session['lang']

	return render_to_response('articles.html',
				 {'articles':Article.objects.all(),
				  'language': language,
			          'session_language': session_language})

def article(request,article_id=1):
	return render_to_response('article.html',
				 {'article':Article.objects.get(id=article_id)})

def language(request,language='en-gb'):
	response=HttpResponse("setting language to %s" % language)
	response.set_cookie('lang',language)
	request.session['lang']=language 
	return response

def create(request):
	if request.POST:
		form = ArticleForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/articles/all')
		else:
			form=ArticleForm() 
	else:
		form = ArticleForm()	
	args={}
	args['form']=form
	return render(request,'create_article.html',args)

def like_article(request,article_id):
	if article_id:
		a=Article.objects.get(id=article_id)
		count=a.likes
		count+=1
		a.likes=count
		a.save()
	return HttpResponseRedirect('/articles/get/%s' % article_id)

def search_titles(request):
	if request.method=="POST":
		search_text=request.POST['search_text']
	else:
		search_text=''
	articles=Article.objects.filter(title__contains=search_text)
	return render(request,'ajax_search.html',{'articles':articles})
