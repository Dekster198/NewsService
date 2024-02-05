from django.db.models import Count, Subquery
from rest_framework import serializers

from .models import *

class NewsSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    like = serializers.SerializerMethodField()
    last_comments = serializers.SerializerMethodField()

    def get_comment(self, obj):
        comments = Comment.objects.filter(news=obj).aggregate(comments_count=Count('news__comment', distinct=True)).values()

        return comments

    def get_like(self, obj):
        like = Like.objects.filter(news=obj).aggregate(likes_count=Count('news__like', distinct=True)).values()

        return like

    def get_last_comments(self, obj):
        last_comments = Comment.objects.filter(news=obj).reverse().values()[:10]

        return last_comments

    class Meta:
        model = News
        fields = '__all__'


class NewsSerializerWithoutAuthor(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ('author', )


class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request', None)

        if not request.method == 'GET':
            fields['author'] = serializers.HiddenField(default=serializers.CurrentUserDefault())

        return fields

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Like
        fields = '__all__'
