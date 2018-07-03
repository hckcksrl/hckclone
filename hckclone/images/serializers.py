from rest_framework import serializers
from . import models
from hckclone.users import models as user_models

# class ImageFileSerializer(serializers.ModelSerializer):

#     class Meta : 

#         model = models.Image
#         fields = (
#             'file',
#         )


class CommentSerializer(serializers.ModelSerializer):

    class Meta :

        model = models.Comment
        fields = (
            'creator',
            'image',
            'message',

        )

class LikeSerializer(serializers.ModelSerializer):

    class Meta :

        model = models.Like
        fields = (
            'image',
            'creator',
        )

class LikeListSerializer(serializers.ModelSerializer):

    class Meta : 

        model = user_models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name'
        )


class ImageSerializer(serializers.ModelSerializer):

    comment = CommentSerializer(many = True)

    class Meta : 
        
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'content',
            'comment',
            'creator',
            'like_count',
            'create_at',
        )

class ImageListSerializer(serializers.ModelSerializer):

    class Meta : 

        model = user_models.User
        fields = (
            'file',
            'like_count',
            'comment_count',
        )


class ImageViewSerializer(serializers.ModelSerializer):

    class Meta : 

        model = models.Image
        fields = (
            'id',
            'location',
            'content'
        )