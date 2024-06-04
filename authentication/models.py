from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


def post_image_path(instance, filename):
    # This function generates the file path where the images will be stored.
    return f"post-images/{instance.author.username}/{filename}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    post_details = models.TextField()
    photo = models.ImageField(upload_to=post_image_path)

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name
    
# models.py


# class checkout(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     contact = models.CharField(max_length=15)
#     address = models.TextField()
#     payment_method = models.CharField(max_length=20)

#     def __str__(self):
#         return self.name
    


