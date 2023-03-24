from rest_framework import serializers
from .models import Post, Comment
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Comment.objects.all(),
                fields=['post', 'author'],
                message='You have already commented on this post.')
        ]


# checks if the current user is authenticated before allowing the comment

    def validate_author(self, value):
        if self.context['request'].user.is_authenticated:
            return value
        raise serializers.ValidationError(
            'You must be authenticated to comment.')
