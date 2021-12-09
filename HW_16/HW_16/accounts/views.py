from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .froms import NameForm

def user_login(request):
    return HttpResponse('Login page')

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = NameForm()

    return render(request, "name.html", {"form":form})
