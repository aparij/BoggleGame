from django.http import HttpResponse

from django.template import Context, loader
from django.shortcuts import render_to_response, render, redirect
from . import boggle

def index(request):
    #game = boggle.Boggle()
    #return render(request, "home.html")
    #template = loader.get_template("home.html")
    #return HttpResponse(template.render)

    return render(request, 'index.html')
    #return HttpResponse("Welcome to  Boggle Game")

def word_list(request):
    if request.method == 'POST':
        letters = request.POST['letters']
        print letters
        game = boggle.Boggle(letters,4)
        context = {
            'words': game.get_all_possible_words()
        }
        #return render(request, "home.html")
        #template = loader.get_template("home.html")
        #return HttpResponse(template.render)

        return render(request, 'words.html',context)
