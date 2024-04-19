from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets

from .serializers import *
from .models import *
from .permissions import *

# Create your views here.
class NewsViewset(viewsets.ModelViewSet):
    def get_serializer_class(self):
        print(self.action)
        if self.action in ['list', 'create', 'retrieve']:
            return NewsSerializer
        else:
            return NewsSerializerWithoutAuthor

    # def get_queryset(self):
    #     return News.objects.filter(comment__text='Прикольно')

    queryset = News.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'create', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwnerOrIsAdmin]

        return [permission() for permission in permission_classes]


class CommentAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated, )


class CommentDetailAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (IsOwnerOrIsAdminForNews, )


class LikeAPIView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
