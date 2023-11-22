from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['little', 'content']
    prepopulated_fields= {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields =('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')  # Define fields to display in the list
    list_filter = ('approved', 'created_on')  # Add filters for better navigation
    search_fields = ('name', 'email', 'body')  # Add fields to search
    action = ['approve_comment']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)



