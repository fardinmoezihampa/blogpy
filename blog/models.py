from django.contrib.auth.models import User
from django.db import models
import os
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class UserProFile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='files/user_avatar/', null=False, blank=False)
    descriptions = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'لیست کاربران'


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    avatar = models.FileField(upload_to='files/category_avatar/', validators=[validate_file_extension])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'لیست دسته بندی ها'


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_cover/', null=False, blank=False,
                             validators=[validate_file_extension])
    created_at = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProFile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'لیست مقاله ها'
