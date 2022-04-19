from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model

User = get_user_model()


from posts.models import Comment, Post, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post

# class PostSerializer(serializers.ModelSerializer):
#     author = serializers.SlugRelatedField(read_only=True, slug_field='username')

#     class Meta:
#         model = Post
#         fields = '__all__'
#         read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        # fields = ('id', 'title', 'description', 'slug')

# class GroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('id', 'title', 'description', 'slug')


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', 
        read_only=True
    )
    following = SlugRelatedField(
        slug_field='username', 
        queryset=User.objects.all()
    )

    class Meta:
        fields = ('user', 'following')
        model = Follow

