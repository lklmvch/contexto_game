from django.db import models

# models.py
from django.db import models
import random

class Game(models.Model):
    word_to_guess = models.CharField(max_length=100, blank=True, null=True)

    def generate_word(self):
        words = ['лампа', 'земля', 'мышка', 'окно', 'счастье']  # Надо обновить
        self.word_to_guess = random.choice(words)
        self.save()

    def __str__(self):
        return f"Game {self.id} - Word to guess: {self.word_to_guess}"



class Guess(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='guesses')
    user_word = models.CharField(max_length=100)
    similarity_score = models.FloatField()

    def __str__(self):
        return f"Guess: {self.user_word} - Similarity: {self.similarity_score}"
