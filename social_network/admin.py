from django.contrib import admin

from social_network.models import Post, Like, Comment, ScheduledPost


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    search_fields = ("title",)
    list_filter = ("user",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
    search_fields = ("user",)
    list_filter = ("post",)


@admin.register(ScheduledPost)
class ScheduledPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "user",
    )
    search_fields = ("title",)
    list_filter = ("user",)


admin.site.register(Like)
