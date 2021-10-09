from posts.models import Comment, Group, Post
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(read_only=True, many=True)
    group = serializers.SlugRelatedField(
        slug_field='slug', queryset=Group.objects.all(), required=False)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'group', 'comment')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('slug', 'title', 'id', 'description')
