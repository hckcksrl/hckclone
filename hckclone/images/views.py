from django.shortcuts import render
from . import models , serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from hckclone.users import models as user_models

class Image(APIView):   # username 이 username 인 유저의 image 모두 불러오기

    def get(self , request , username , format=None):
        
        user = request.user
        
        try:

            users = user_models.User.objects.get(username = username)

        except user_models.User.DoesNotExist:
            
            return Response(status = status.HTTP_404_NOT_FOUND)

        images = models.Image.objects.filter(creator_id = users)       

        if images is not None:

            serializer = serializers.ImageSerializer(images , many = True)
            
            return Response(data = serializer.data ,status = status.HTTP_200_OK)

        else :

            return Response(status = status.HTTP_404_NOT_FOUND)


class ImageComment(APIView):    #   image_id 인 image의 comment 불러오기

    def post(self , request , image_id , format=None):

        user = request.user

        try:

            images = models.Image.objects.get(id = image_id)

        except models.Image.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)
        
        serializer = serializers.CommentSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save(creator = user , image = images)

            return Response(data = serializer.data ,status = status.HTTP_200_OK)

        else :

            return Response(status = status.HTTP_404_NOT_FOUND)
    
class DeleteComment(APIView):   #   Comment Delete

    def delete(self , request , comment_id , format=None):

        user = request.user

        try:

            comment = models.Comment.objects.get(id = comment_id)

        except models.Comment.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)

        comment.delete()

        return Response(status = status.HTTP_200_OK)
    

class LikeImage(APIView):   #   Image에 Like 하기 또는 Unlike하기

    def exist(self , image_id, user_id):

            try : 
                
                like = models.Like.objects.get(image_id = image_id , creator_id = user_id)

                return like

            except models.Like.DoesNotExist :

                return None
    
    def post(self , request , image_id , format=None):

        user = request.user

        like = self.exist(image_id , user.id)

        image = models.Image.objects.get(id = image_id)

        if like is None :

            image_like = models.Like.objects.create(
                image = image,
                creator = user
            )

            image_like.save()

            return Response(status=status.HTTP_201_CREATED)
            
        else :

            like.delete()

            return Response(status = status.HTTP_404_NOT_FOUND)


class ImageView(APIView):       #   Image를 클릭하면 나오는 ImageView창

    def get(self , request , image_id , format=None):

        user = request.user

        try : 

            image = models.Image.objects.get(id = image_id)

            serializer = serializers.ImageSerializer(image)

            return Response(data = serializer.data , status = status.HTTP_200_OK)

        except models.Image.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)

    
    def put(self , request , image_id , format=None):

        user = request.user

        try :

            image = models.Image.objects.get(id = image_id)

            if image.creator_id == user.id :

                serializer = serializers.ImageViewSerializer(image ,data = request.data , partial=True)

                if serializer.is_valid():

                    serializer.save(creator = user)

                    return Response(data = serializer.data , status = status.HTTP_200_OK)

                else : 

                    return Response(status = status.HTTP_404_NOT_FOUND)

            else : 

               return Response(status = status.HTTP_401_UNAUTHORIZED)

        except models.Image.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)


    def delete(self , request , image_id , format=None):

        user = request.user

        try : 

            image = models.Image.objects.get(id = image_id)

            if image.creator_id == user.id : 

                image.delete()

                return Response(status = status.HTTP_200_OK)

            else :

               return Response(status = status.HTTP_401_UNAUTHORIZED)

        except models.Image.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)


        


