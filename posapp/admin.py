from django.contrib import admin

from .models import Category, SubCategory, Product
from sell.models import Sale

class ProductAdmin(admin.ModelAdmin):
    #raw_id_fields = ('product',)
    list_display = ['date_updated', 'sub_category', 'name', 'bought_with']

    list_filter = ['name' ]
    search_fields = ['name']

    def bought_with(self, obj):
        print(obj)
        sales = [product.product.all() for product in Sale.objects.filter(product = obj)]
        print(len(sales))
        result = []
        for sale in sales:
            product_list = [product.name for product in sale]
            result.extend(product_list)
        
        #index = list(set(result)).index(obj.name)
        print(obj.name , ' ', list(set(result)))
        my_list = list(set(result))
        if (obj.name in my_list):
            my_list.remove(obj.name)
        else:
            pass
        print(my_list)
        return my_list


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'name']


# Register your models here.
#admin.site.register(Category)
#admin.site.register(SubCategory, SubCategoryAdmin)
#admin.site.register(Product, ProductAdmin)