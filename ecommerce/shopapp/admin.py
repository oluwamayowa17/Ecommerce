from django.contrib import admin
from shopapp.models import *
# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('prod_name', )

    prepopulated_fields = {'slug':('prod_name',)}



# admin.site.register(UserProfile)
admin.site.register(Category) 
admin.site.register(News)
admin.site.register(Contact)
admin.site.register(HotDeal)
admin.site.register(Subscriber)



