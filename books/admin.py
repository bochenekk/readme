from django.contrib import admin

from books.models import Author, Book, Category

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'web_site')
    fieldsets = [
        ('Name', {'fields': ['first_name', 'last_name']}),
        ('Born', {'fields': ['birth_date']}),
        ('Website', {'fields': ['web_site']}),
    ]
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'description')
    # 'categories'  "The value of list_display[2] must not be a ManytoManyField"
    list_filter = ('title', 'author', 'categories')
    search_fields = ('title', 'author', 'categories')
    autocomplete_fields = ('author',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)



admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)