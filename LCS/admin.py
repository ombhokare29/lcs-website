# myapp/admin.py
from django.contrib import admin

from .models import Contact, sponsorship, volunteer
from .models import Donation,Review
from .models import GalleryEvent, Photo

# Register your models here.

class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone', 'query')
    search_fields = ('name', 'email')
    list_filter = ('name',)
admin.site.register(Contact, ContactAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'review')
    search_fields = ('name', 'email')
    list_filter = ('name',)
admin.site.register(Review, ReviewAdmin)


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


# admin.py
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'location')
    
admin.site.register(Event, EventAdmin)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'created_at')
    search_fields = ('name', 'email')



class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

class GalleryEventAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(GalleryEvent, GalleryEventAdmin)
admin.site.register(Photo)