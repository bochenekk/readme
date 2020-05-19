from django.contrib import admin

from reviews.models import Review

# Register your models here.
class ReviewAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('user', 'book', 'title', 'content_short', 'pub_date', 'state', 'grade')
    list_filter = ('user', 'book','state', 'grade')
    search_fields = ('user', 'book', 'title', 'content')

    def content_short(self, obj):
        return (
            f'{obj.content[:50]}...'
            if len(obj.content) > 50
            else obj.content
        )

    content_short.short_description = 'Content'


admin.site.register(Review, ReviewAdmin)
