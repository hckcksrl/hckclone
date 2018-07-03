from django.urls import path
from . import views

app_name = "images"


urlpatterns = [
    path(
        "",
        view = views.Image.as_view(),
        name = "images"
    ),
    path(
        "<str:username>",
        view = views.Image.as_view(),
        name = "user_image"
    ),
    path(
        "<int:image_id>/comment",
        view = views.ImageComment.as_view(),
        name = "comment_create"
    ),
    path(
        "<int:comment_id>/delcomment",
        view = views.DeleteComment.as_view(),
        name = "comment_delete"
    ),
    path(
        "<int:image_id>/like",
        view = views.LikeImage.as_view(),
        name = "image_like"
    ),
    path(
        "<int:image_id>/image",
        view = views.ImageView.as_view(),
        name = "image_view"
    )

]