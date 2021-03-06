from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from forms import MyRegistrationForm


def login(request):
	c={}
	#c.update(get_token(request))
	#if request.method == 'POST': 
        #	form = forms.ContactForm(request.POST)
	#else:
	#	form=forms.ContactForm()
	#initial_data={'form':form}
	return render(request,'login.html',c)

def auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=username,password=password)
	
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
	return render_to_response('loggedin.html',
				 {'full_name':request.user.username})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')
def register_user(request):
	if request.method=="POST":
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')
	else:
		form=MyRegistrationForm()
	args={}
	#args.update(get_token(request))
	args['form']=form
	print args
	return render(request,'register.html',args)

def register_success(request):
	return render_to_response('register_success.html')
