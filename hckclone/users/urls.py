from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path(
        "<str:username>",
        view = views.UserProfile.as_view(),
        name = "user_profile"
    ),
    path(
        "<str:username>/following",
        view = views.UserFollowing.as_view(),
        name = "user_following"
    ),
    path(
        "<str:username>/followers",
        view = views.UserFollowers.as_view(),
        name = "user_followers"
    ),
    path(
        "search/",
        view = views.SearchUser.as_view(),
        name = 'search_user'
    ),
    path(
        "follow/<str:username>",
        view = views.FollowCount.as_view(),
        name = 'follow_count'
    ),
    path(
        "change/<str:username>",
        view = views.ChangePassword.as_view(),
        name = 'change_password'
    )
]
