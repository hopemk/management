from django.contrib import admin
from .models import CheckInOut, ProductCheckInOut
# Register your models here.

class CheckInOutAdmin(admin.ModelAdmin):
    #raw_id_fields = ('product',)
    list_display = ['employee', 'check_in', 'checkin_time', 'check_out', 'checkout_time']

    list_filter = ['checkin_time' ]
    search_fields = ['name']

class ProductCheckInOutAdmin(admin.ModelAdmin):
    #raw_id_fields = ('product',)
    list_display = ['employee','product', 'check_in', 'checkin_time', 'check_out', 'checkout_time']

    list_filter = ['checkin_time' ]
    search_fields = ['name']

admin.site.register(CheckInOut, CheckInOutAdmin)
admin.site.register(ProductCheckInOut, ProductCheckInOutAdmin)
