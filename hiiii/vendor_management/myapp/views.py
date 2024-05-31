from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


    

# class PurchaseOrderViewSet(viewsets.ModelViewSet):
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer



#     def update(self, request, *args, **kwargs):
#         # Custom behavior for PUT request
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
        
#         if getattr(instance, '_prefetched_objects_cache', None):
#             # If 'prefetch_related' has been applied to a queryset, we need to forcibly
#             # invalidate the prefetch cache on the instance.
#             instance._prefetched_objects_cache = {}

#         return Response(serializer.data)

#     def destroy(self, request, *args, **kwargs):
#         # Custom behavior for DELETE request
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        # Custom behavior for PUT request
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to forcibly
            # invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # Custom behavior for DELETE request
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)