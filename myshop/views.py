from django.shortcuts import render

#from .models import Topic, Entry
#from .forms import TopicForm, EntryForm


from django.urls import reverse


def index(request):
	#return render(request, '')
	#return HttpResponse('<h2>hello</h2>')
	return render(request, 'index.html', {'name': 'john'})   
