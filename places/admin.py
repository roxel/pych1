from django.contrib import admin, gis


from places.models import Place, Category, Rating


class RatingInlineAdmin(admin.TabularInline):
    model = Rating
    fields = ('value', 'comment', 'user')


class PlaceAdmin(gis.admin.OSMGeoAdmin):
    inlines = [RatingInlineAdmin]
    fields = ('name', 'established', 'description', 'categories', 'location')


admin.site.register(Place, PlaceAdmin)
admin.site.register(Category)
