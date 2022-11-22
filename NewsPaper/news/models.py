from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):

    authorRating = models.IntegerField(default=0)
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def update_rating(self):
        pass


class Category(models.Model):

    name = models.CharField(max_length=127, unique=True)


class Post(models.Model):

    authorP = models.ForeignKey(Author, on_delete=models.CASCADE)

    articles = "AR"
    news = "NW"
    CATEGORY_TYPES = [
        (articles, 'Статья'),
        (news, 'Новость')
    ]

    category_type = models.CharField(max_length=2, choices=CATEGORY_TYPES, default=news)
    time_add = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:123]}...'


class PostCategory(models.Model):

    postPC = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryPC = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):

    postC = models.ForeignKey(Post, on_delete=models.CASCADE)
    userC = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_add = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


