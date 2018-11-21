from django.contrib import admin, gis


from places.models import Place, Category

admin.site.register(Place, gis.admin.OSMGeoAdmin)
admin.site.register(Category)
