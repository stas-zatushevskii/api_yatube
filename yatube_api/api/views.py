from posts.models import Comment, Group, Post
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request):
        response = {'message': 'Запрещено создание группы через APi'}
        return Response(response, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post_id=pk)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
