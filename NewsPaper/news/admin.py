from django.contrib import admin
from .models import *


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(SubscribeCategory)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_subscribers', )


admin.site.register(Category, CategoryAdmin, )
