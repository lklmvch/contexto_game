# from rest_framework import serializers
# from .models import Word, Game
#
# class WordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Word
#         fields = ['id', 'word', 'description', 'guessed']
#
#
# class GameSerializer(serializers.ModelSerializer):
#     words = WordSerializer(many=True)
#
#     class Meta:
#         model = Game
#         fields = ['id', 'player', 'words', 'score', 'status']
