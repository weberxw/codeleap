from rest_framework import serializers
from careers.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
                'id', 'title', 'created_datetime', 'username', 'content'
                )