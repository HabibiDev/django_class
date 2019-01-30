from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
	list_display = ('title',
					'created_on',)
	list_filter = ('title',
		)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',
					'description',)
	list_filter = ('name',
		)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

# Register your models here.
