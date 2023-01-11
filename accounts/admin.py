from django.contrib import admin

from . models import Profile,Country


# admin.site.register(Profile)
# admin.site.register(Country)



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbr', 'is_active']

# class CountryInlineAdmin(admin.StackedInline):
#     model = Country
#     fields = ('name','abbr','is-active')
#     extra = 0 

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','phone_number','country','avatar')
#     inlines = [CountryInlineAdmin]



