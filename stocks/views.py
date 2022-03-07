from django.shortcuts import render

from .models import Quanity
# Create your views here.
class QuanityView(APIView):
    model = Quantity

    def get(self, request, id = None):
        if id:
            quantity = Quantity.get_object(id)
            serializer = QuanitySerializer(quantity)   
        else:
            quantities = Quanity.objects.all()
            serializer = QuantitySerializer(quantities, many = True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):
        data = request.data
        product = Product.get_object(data['product'])
        if not product:
            return  Response({"error": "Product not Found"},status=status.HTTP_404_NOT_FOUND)
        quantity = data['quantity']
        if not quantity and typeof(quantity) != int:
            return  Response({"error": "Quanityt not defined or Wrong type"},status=status.HTTP_404_NOT_FOUND)
        Quanity(
            product = product,
            quantity = quantity
        ).save()
        return Response({"message": "saved"}, status=status.HTTP_201_CREATED )
    def put(self, request):
        data = request.data
        quantity = Quanity.get_object(data['quantity'])
        if not quantity:
            return  Response({"error": "Quanity object not defined"},status=status.HTTP_404_NOT_FOUND)
        product = Product.get_object(data['product'])
        if not product:
            return  Response({"error": "Product not Found"},status=status.HTTP_404_NOT_FOUND)
        quantity_ = data['quantity']
        if not quantity_ and typeof(quantity_) != int:
            return  Response({"error": "Quanityt not defined or Wrong type"},status=status.HTTP_404_NOT_FOUND)
        
        time_updated = datetime.now() 
        quantity.product = product
        quantity.time_updated = time_updated
        quantity.quantity = quantity_
        category.save()
        return Response({"message": "updated"}, status=status.HTTP_201_CREATED )
    def delete(self, request):
        data = request.data
        quantity = Quanity.get_object(data['quantity'])
        if quanityt:
            quantity.delete()
        else:
            return Response({"error": "Quantity not available"}, status=status.HTTP_404_NOT_FOUND )
        return Response({"data": "deleted"}, status=status.HTTP_202_ACCEPTED )
