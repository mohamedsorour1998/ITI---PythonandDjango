from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    # this is the serializer for the Post model and it is used to convert the model to JSON
    # it's type is model serializer
    class Meta:
        model = Post
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    # this is the serializer for the Comment model and it is used to convert the model to JSON
    # it's type is model serializer
    class Meta:
        model = Comment
        fields = '__all__'