from django.contrib import admin

from books.models import Author, Book, Category

# Register your models here.
class BookInline(admin.TabularInline):
    model = Book
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'birth_date'
    list_display = ('first_name', 'last_name', 'birth_date', 'web_site')
    fieldsets = [
        ('Name', {'fields': ['first_name', 'last_name']}),
        ('Born', {'fields': ['birth_date']}),
        ('Website', {'fields': ['web_site']}),
    ]
    inlines = [BookInline]
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pages', 'get_categories', 'description_short')
    # 'categories'  "The value of list_display[2] must not be a ManytoManyField"
    list_filter = ('title', 'author', 'categories')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'categories', 'description')
    autocomplete_fields = ('author',)

    # Book.objects.filter(author__first_name__startswith='Andrzej')

    def description_short(self, obj): # obj - instancja naszego modelu
        return (
            f'{obj.description[:50]}...'
            if len(obj.description) > 50
            else obj.description
        )

    description_short.short_description = 'Description' # ustawia nazwę kolumny
    # dla tej metody wyświetlaną w tabeli a adminie


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)



admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)