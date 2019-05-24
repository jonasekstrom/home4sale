from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date',
                    'salesman')
    list_display_links = ('id', 'title')
    list_filter = ('salesman', )
    list_editable = ('is_published', )
    search_fields = ('title', 'description', 'adress', 'city', 'state',
                     'zipcode', 'price')


admin.site.register(Listing, ListingAdmin)