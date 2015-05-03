from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    exclude = ['pub_date']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


