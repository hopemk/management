from django.contrib import admin
from .models import CheckInOut
# Register your models here.

class CheckInOutAdmin(admin.ModelAdmin):
    #raw_id_fields = ('product',)
    list_display = ['employee', 'product', 'serial_number', 'check_in', 'checkin_time', 'check_out', 'checkout_time']

    list_filter = ['checkin_time' ]
    search_fields = ['name']

admin.site.register(CheckInOut, CheckInOutAdmin)
