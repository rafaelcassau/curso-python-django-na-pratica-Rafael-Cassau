#-*- encoding: utf-8 -*-

from django.contrib import admin
from library.models import Library

class LibraryAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'status', 'friend_name', 'friend_email')

admin.site.register(Library, LibraryAdmin)

