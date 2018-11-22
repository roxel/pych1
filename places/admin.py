from django.contrib import admin, gis


from places.models import Place, Category, Rating


class RatingInlineAdmin(admin.TabularInline):
    model = Rating
    fields = ('value', 'comment', 'user')
    extra = 1


class PlaceAdmin(gis.admin.OSMGeoAdmin):
    inlines = [RatingInlineAdmin]
    fields = ('name', 'established', 'description', 'categories', 'website', 'location')
    list_display = ('__str__', 'website', 'established', 'location', 'average_rating', 'rating_quantity')


admin.site.register(Place, PlaceAdmin)
admin.site.register(Category)
admin.site.register(Rating)
