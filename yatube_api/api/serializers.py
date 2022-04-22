from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.contrib.auth import get_user_model

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field="username")

    class Meta:
        fields = "__all__"
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "description", "slug")


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field="username", read_only=True)
    following = SlugRelatedField(slug_field="username",
                                 queryset=User.objects.all())

    def validate_following(self, value):
        if (self.context["request"].user.username == value.username) or (
            Follow.objects.filter(
                user=self.context["request"].user.id, following=value.id
            ).exists()
        ):
            raise serializers.ValidationError("Нет подписка на себя")
        return value

    class Meta:
        fields = ("user", "following")
        model = Follow
