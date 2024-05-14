# myapp/admin.py
from django.contrib import admin

from .models import Contact, sponsorship, volunteer

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    # Customize the display fields
    list_display = ('name', 'email', 'phone', 'query')

    # Add search functionality
    search_fields = ('name', 'email')

    # Add filters
    list_filter = ('name',)

# Register the model with the customized admin class
admin.site.register(Contact, ContactAdmin)


class volunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address','availability')
    search_fields = ('name', 'email')
    list_filter = ('name',)
    
admin.site.register(volunteer, volunteerAdmin)

class sponsorshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address','availability')
    search_fields = ('name', 'email')
    list_filter = ('name',)

admin.site.register(sponsorship, sponsorshipAdmin)