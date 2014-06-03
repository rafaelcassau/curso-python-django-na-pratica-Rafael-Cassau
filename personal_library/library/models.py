#-*- encoding: utf-8 -*-

from django.db import models

class Library(models.Model):	
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True, default='')
	status = models.BooleanField(default=False)
	friend_name = models.CharField(max_length=100, blank=True, default='')
	friend_email = models.EmailField(max_length=50, blank=True, default='')
	created_at  = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Livro'
		verbose_name_plural = 'Livros'		

	def __unicode__(self):
		return self.title

