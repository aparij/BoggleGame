from django.shortcuts import render
from . import boggle

def index(request):
    return render(request, 'index.html')

def word_list(request):
    if request.method == 'POST':
        letters = request.POST['letters']
        print letters
        game = boggle.Boggle(letters,4)
        context = {
            'words': game.get_all_possible_words()
        }
        return render(request, 'words.html',context)
