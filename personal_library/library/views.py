#-*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from library.models import Library
from library.forms import LibraryForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict


def index(request):

	book_list = Library.objects.all()

	library_form = LibraryForm()

	return render(request, 'library/library.html', {'book_list': book_list, 'library_form': library_form})


def save(request):

	library_form = LibraryForm(request.POST or None)

	if library_form.is_valid():

		form_clean = library_form.cleaned_data

		pk = form_clean.get('id', None)

		if not pk:
			library_model = Library(**form_clean)
			library_model.save()
		else:
			library_model = get_object_or_404(Library, pk=pk)

			library_model.title = form_clean.get('title', '')
			library_model.description = form_clean.get('description', '')
			library_model.status = form_clean.get('status', '')
			library_model.friend_name = form_clean.get('friend_name', '')
			library_model.friend_email = form_clean.get('friend_email', '')
			
			library_model.save()

		return HttpResponseRedirect(reverse('index'))

	book_list = Library.objects.all()

	return render(request, 'library/library.html', {'book_list': book_list, 'library_form': library_form})


def edit(request, book_id):
	
	book_list = Library.objects.all()

	book = model_to_dict(get_object_or_404(Library, pk=book_id))

	library_form = LibraryForm(initial=book)

	return render(request, 'library/library.html', {'book_list': book_list, 'library_form': library_form})


def remove(request, book_id):

	book = get_object_or_404(Library, pk=book_id)

	book.delete()

	library_form = LibraryForm()

	book_list = Library.objects.all()

	return render(request, 'library/library.html', {'book_list': book_list, 'library_form': library_form})