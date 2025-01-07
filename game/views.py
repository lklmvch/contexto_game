# views.py
from django.shortcuts import render, redirect
from .models import Game, Guess
from .forms import GuessForm
from django.http import JsonResponse
import spacy  # библиотека для анализа сходства

# Загрузка модели
nlp = spacy.load('en_core_web_md')

def home(request):
    return render(request, 'home.html')

def start_game(request):
    # Создание игры и генерация слова
    game = Game.objects.create()
    game.generate_word()
    return redirect('play_game', game_id=game.id)

def play_game(request, game_id):
    game = Game.objects.get(id=game_id)
    form = GuessForm(request.POST or None)

    if form.is_valid():
        guess = form.save(commit=False)
        guess.game = game
        user_word = guess.user_word

        # Схожесть
        similarity_score = get_similarity_score(game.word_to_guess, user_word)
        guess.similarity_score = similarity_score
        guess.save()

        if similarity_score == 1.0:
            return redirect('won_game', game_id=game.id)

        # Отображение попыток
        guesses = game.guesses.all()
        return render(request, 'game.html', {'game': game, 'form': form, 'guesses': guesses})

    return render(request, 'game.html', {'game': game, 'form': form})

def get_similarity_score(word1, word2):
    # spacy для вычисления схожести между словами
    word1_doc = nlp(word1)
    word2_doc = nlp(word2)
    return word1_doc.similarity(word2_doc)


def won_game(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'won_game.html', {'game': game})
