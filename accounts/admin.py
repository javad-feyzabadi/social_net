from django.contrib import admin

from . models import Profile,Country


admin.site.register(Profile)
admin.site.register(Country)




# class CountryInlineAdmin(admin.StackedInline):
#     model = Country
#     fields = ('name','abbr','is-active')
#     extra = 0 

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','phone_number','country','avatar')
#     inlines = [CountryInlineAdmin]



