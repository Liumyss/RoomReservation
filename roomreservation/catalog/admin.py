from django.contrib import admin

from .models import Owner, RentalPlace, Room

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone_number')
    fields = ['first_name', 'last_name', ('phone_number')]

admin.site.register(Owner, OwnerAdmin)

class RoomInline(admin.TabularInline):
    model = Room

@admin.register(RentalPlace)
class RentalPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

    inlines = [RoomInline]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('rental_place', 'cost', 'status', 'client', 'due_back', 'is_premium', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('rental_place', 'id', 'cost', 'is_premium')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'client')
        }),
    )

