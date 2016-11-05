from __future__ import unicode_literals
from time import time
from django.db import models

def get_upload_file_name(instance,filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'),filename)

# Create your models here.
class Article(models.Model):
	title=models.CharField(max_length=200)
	body=models.TextField()
	pub_date=models.DateTimeField('date published')
	likes=models.IntegerField()
	#hh=models.TextField()
	#thumbnail=models.FileField(upload_to=get_upload_file_name)
	
	def __unicode__(self):
		return self.title
