from rest_framework import serializers
from . import models
from hckclone.images import models as image_models
from hckclone.images import serializers as image_serializers


class ProfileSerializer(serializers.ModelSerializer):

    class Meta :
        model = models.User
        fields = (
            'profile_image',
            'name',
            'username',
            'website',
            'intro',
            'phone',
            'followers',
            'following',
        )

class FollowListSerializer(serializers.ModelSerializer):

    class Meta : 
        model = models.User
        fields = (
            'profile_image',
            'name',
            'username',
        )

class FollowCountSerializer(serializers.ModelSerializer):

    class Meta : 

        model = models.User
        fields = (
            'username',
            'followers_count',
            'following_count'
        )