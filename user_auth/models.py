from collections.abc import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.utils.text import slugify
import shortuuid

# Create your models here.

GENDER = (
    ("male", "Male"),
    ("female", "Female")
)

RELATIONSHIP = (
    ("married", "Married"),
    ("unmarried", "Unmarried")
)


def user_directory_path(instance, filename):
    extension = filename.split(".")[-1]
    filename = f"{instance.user.id}.{extension}"

    return f"user_{instance.user.id}/{filename}"

# Custom User model


class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, choices=GENDER, default="male")

    otp = models.CharField(max_length=10, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return str(self.username)


class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=25,
                         alphabet="abcdefghijklmnopqrstuvwxyz")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover_image = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True, default="cover.jpg")
    image = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True, default="default.jpg")
    full_name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDER, default="male")
    relationship = models.CharField(
        max_length=100, choices=RELATIONSHIP, default="unmarried")
    bio = models.CharField(max_length=100, null=True, blank=True)
    about_me = models.TextField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    working_at = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    verified = models.BooleanField(default=False)
    followers = models.ManyToManyField(
        User, blank=True, related_name="followers")
    following = models.ManyToManyField(
        User, blank=True, related_name="following")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")
    blocked = models.ManyToManyField(User, blank=True, related_name="blocked")
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)


    def __str__(self) -> str:
        return self.user.username
    

    def save(self, *args, **kwargs) -> None:
        if self.slug == "" or self.slug == None:
            self.slug = f"{slugify(self.full_name)}-{str(shortuuid.uuid()[:4].lower())}"
        super(Profile, self).save(*args, **kwargs)