from django.contrib import admin

#import models
from .models import BookCategory,BookDeatils

# Book_category admin
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name","slug",)
    search_fields = ("category_name",)
    readonly_fields = ("slug",)

# Book_Deatils Admin
class BookDeatilsAdmin(admin.ModelAdmin):
    list_display = ("title","slug","author_name","thumbnail_image","category",)
    search_fields = ("author_name","title",)
    readonly_fields = ("slug",)

# admin register
admin.site.register(BookCategory,BookCategoryAdmin)
admin.site.register(BookDeatils,BookDeatilsAdmin)
