from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from blog.models import BlogPost, Comment


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


admin.site.register(BlogPost, PostAdmin)
admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
