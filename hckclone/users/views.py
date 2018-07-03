from django.shortcuts import render
from . import models , serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserProfile(APIView):

    def get(self , request , username , format = None):

        user = request.user
        try : 

            exist_user = models.User.objects.get(username = username)

            serializer = serializers.ProfileSerializer(exist_user)

            return Response(data = serializer.data , status = status.HTTP_200_OK)

        except models.User.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)

    def put(self , request , username , format=None):

        user = request.user

        try :

            exist_user = models.User.objects.get(username = username)

            if user.id == exist_user.id :

                serializer = serializers.ProfileSerializer(exist_user , data = request.data , partial = True)

                if serializer.is_valid():

                    serializer.save(username = username)

                    return Response(data = serializer.data , status = status.HTTP_200_OK)

                else :

                    return Response(data = serializer.error , status = status.HTTP_404_NOT_FOUND)

            else : 

                return Response(status = status.HTTP_401_UNAUTHORIZED)

        except models.User.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)


class UserFollowing(APIView):
    
    def exist_following(self , user , username):

        try :

            follow_user = models.User.objects.get(username=user).following.get(username=username)

            return follow_user

        except :

            return None

    def post(self , request , username , format=None):

        user = request.user

        try:

            user_follow = models.User.objects.get(username = username)

            exist_follow = self.exist_following(user , username)

            if exist_follow is None:

                if user.username == username :

                    return Response(status = status.HTTP_401_UNAUTHORIZED)

                else :    
            
                    user.following.add(user_follow)
                
                    user.save()

                    return Response(status = status.HTTP_200_OK)

            else :

                user.following.remove(user_follow)

                return Response(status = status.HTTP_200_OK)

        except models.User.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)


class UserFollowers(APIView):

    def exist_follower(self , user , username):

        try :

            follower_user = models.User.objects.get(username=user).followers.get(username=username)

            return follower_user

        except :

            return None

    def post(self , request , username , format=None):

        user = request.user

        try:

            user_follower = models.User.objects.get(username = username)

            exist_follower = self.exist_follower(user , username)

            if exist_follower is None:

                if user.username == username :

                    return Response(status = status.HTTP_401_UNAUTHORIZED)

                else :    
            
                    user.followers.add(user_follower)
                
                    user.save()

                    return Response(status = status.HTTP_200_OK)

            else :
                
                user.followers.remove(user_follower)

                user.save()

                return Response(status = status.HTTP_200_OK)

        except models.User.DoesNotExist :

            return Response(status = status.HTTP_404_NOT_FOUND)

        
class SearchUser(APIView):

    def get(self , request , format=None):

        search = request.query_params.get('username',None)

        if search is not None:

            user = models.User.objects.filter(username__istartswith = search)

            serializer = serializers.ProfileSerializer(user , many = True)

            return Response(data = serializer.data , status = status.HTTP_200_OK)

        else : 

            return Response(status = status.HTTP_404_NOT_FOUND)

    
class FollowCount(APIView):

    def get(self , request , username , format=None):

        try:

            user = models.User.objects.get(username = username)

            serializer = serializers.FollowCountSerializer(user , partial = True)

            return Response(data = serializer.data , status = status.HTTP_200_OK)

        except models.User.DoesNotExist:

            return Response(status = status.HTTP_404_NOT_FOUND)


class ChangePassword(APIView):

    def put(self , request , username , format=None):
        
        user = request.user

        print(user.password)

        if username == user.username :

            password = request.data.get('password',None)

            if password is not None :

                password_check = user.check_password(password)

                if password_check :

                    new_password : request.data.get('new_password',None)

                    if new_password is not None:

                        user.set_password(new_password)

                        return Response(status = status.HTTP_200_OK)

                    else : 

                        return Response(status = status.HTTP_404_NOT_FOUND)

                else : 

                    return Response(status = status.HTTP_401_UNAUTHORIZED)
            else :

                return Response(status = status.HTTP_400_BAD_REQUEST)
        else :

            return Response(status = status.HTTP_404_NOT_FOUND)
