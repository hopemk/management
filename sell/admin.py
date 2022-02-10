from django.contrib import admin

from .models import Sell, Sale

# Register your models here.

class SellAdmin(admin.ModelAdmin):
    #raw_id_fields = ('product',)
    list_display = ['time','category','sub_category','product','procure_price','unit_price', 'items_sold', 'paid', 'sale_profit']
    list_filter = ['product__name', 'items_sold', 'time']
    search_fields = ['product__name']
    #prepopulated_fields = {'slug':('product',)}

    def sub_category(self, obj):
        return obj.product.sub_category.name
    def category(self, obj):
        return obj.product.sub_category.category.name
    def unit_price(self, obj):
        return obj.product.price_per_item
        '''
    def quantity(self, obj):
        return obj.product.quantity_before_sale - obj.items_sold
    def remaining_items(self, obj):
        return obj.product.quantity_after_sale
        '''
    def procure_price(self, obj):
        return obj.product.procure_price_per_item
    def sale_profit(self, obj):
        return obj.items_sold * (obj.product.price_per_item - obj.product.procure_price_per_item)
    class Meta:
        model = Sell
        '''
class Sold(admin.ModelAdmin):
    list_display = ['product', 'sums']

    
    def get_queryset(self, request):
        qs = super(Sold, self).get_queryset(request)
        qs = qs.annotate(product=)

        return set(qs)
        

'''

class SaleAdmin(admin.ModelAdmin):
    #raw_id_fields = ('product',)
    list_display = ['time','products']
    list_filter = ['product__name', 'time']
    search_fields = ['product__name']
    #prepopulated_fields = {'slug':('product',)}

    def products(self, obj):
        product_list = [product for product in obj.product.all()]
        return product_list


admin.site.register(Sell, SellAdmin)
admin.site.register(Sale, SaleAdmin)