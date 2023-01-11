from django.contrib import admin

from . models import Post,PostFile


class PstFileInlineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('file',)
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user','title','is_active','is_public')
    inlines = [PstFileInlineAdmin,]


