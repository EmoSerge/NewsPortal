from celery import shared_task
import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from NewsPaper.settings import SITE_URL, DEFAULT_FROM_EMAIL
from news.models import Post, Category


@shared_task
def send_notification(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=subscribers,

    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
def weekly_notify():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    post = Post.objects.filter(time_add__gte=last_week)
    categories = set(post.values_list('post_category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': SITE_URL,
            'post': post,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю по вашей подписке',
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
