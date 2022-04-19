from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


from posts.models import Comment, Post, Group, Follow


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


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
        fields = ('id', 'title', 'description', 'slug')



class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field='username', 
        read_only=True
    )
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    def validate_following(self, value):
        if self.context['request'].user.username == value.username or Follow.objects.filter(user=self.context['request'].user.id, following=value.id).exists():
                    # if self.context['request'].user.username == value.username:
            raise serializers.ValidationError("Невозможно подписаться на самого себя")

        # follow_qc = Follow.objects.filter(user=self.context['request'].user.id, following=value.id)
        # print('ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
        # print(self.context['request'].user, value.id)
        return value

 #       Follow.objects.filter(user=user, author=auth).exists()

    class Meta:
        fields = ('user', 'following')
        model = Follow


    # def validate_following(self, value):
    #     if self.context['request'].user.username == value.username:
    #         # ddd = serializers.ValidationError("Невозможно подписаться на самого себя")
    #         # print(ddd.status_code)
    #         # raise(ddd)
    #         # return ddd
    #         raise serializers.ValidationError("Невозможно подписаться на самого себя")
    #     return value