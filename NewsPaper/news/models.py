from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):

    authorRating = models.IntegerField(default=0)
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.authorUser}'

    def update_rating(self):

        post_rating = sum(Post.objects.filter(authorP=self).values_list('rating', flat=True))
        comment_rating = sum(Comment.objects.filter(userC__author=self).values_list('rating', flat=True))
        com_post_rating = sum(Comment.objects.filter(postC__in=Post.objects.filter(authorP=self)).values_list('rating', flat=True))
        self.authorRating = post_rating * 3 + comment_rating + com_post_rating
        self.save()


class Category(models.Model):

    name = models.CharField(max_length=127, unique=True)
    subscribers = models.ManyToManyField(User, through='SubscribeCategory')

    def __str__(self):
        return f'{self.name}'

    def get_subscribers(self):
        return ",\n".join([str(p) for p in self.subscribers.all()])


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

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


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


class SubscribeCategory(models.Model):
    sub_user = models.ForeignKey(User, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Category, on_delete=models.CASCADE)
