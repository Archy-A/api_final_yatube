from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from posts.models import Comment, Post, Group, Follow
from django.contrib.auth import get_user_model

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = "__all__"
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")

    class Meta:
        fields = "__all__"
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "description", "slug")


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field="username", read_only=True)
    following = SlugRelatedField(slug_field="username", queryset=User.objects.all())

    def validate_following(self, value):
        if (self.context["request"].user.username == value.username) or (
            Follow.objects.filter(
                user=self.context["request"].user.id, following=value.id
            ).exists()
        ):
            raise serializers.ValidationError("Невозможно подписаться на самого себя")
        return value

    class Meta:
        fields = ("user", "following")
        model = Follow
