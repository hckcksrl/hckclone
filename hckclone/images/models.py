from django.db import models
from hckclone.users import models as user_models
# Create your models here.

class TimeStamp(models.Model):

    create_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Image(TimeStamp):

    creator = models.ForeignKey(user_models.User,related_name = 'images' , on_delete = models.CASCADE, null =True)
    file = models.ImageField()
    location = models.CharField(max_length=1000 , null = True)
    content = models.TextField()

    def __str__(self):
        
        return '{} - {}'.format(self.location,self.content)

    @property
    def like_count(self):

        return self.like.all().count()

    @property
    def comment_count(self):

        return self.comment.all().count()


class Comment(TimeStamp):

    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE , null =True)
    image = models.ForeignKey(Image, related_name='comment', on_delete=models.CASCADE, null =True)
    message = models.TextField()

    def __str__(self):

        return self.message

class Like(TimeStamp):

    image = models.ForeignKey(Image , related_name='like', on_delete=models.CASCADE, null =True)
    creator = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null =True)

    def __str__(self):

        return 'User : {} - Image Content {}'.format(self.creator.username , self.image.content)