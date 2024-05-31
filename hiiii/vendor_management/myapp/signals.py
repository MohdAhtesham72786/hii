from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder, Vendor

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_metrics(sender, instance, **kwargs):
    if instance.status == 'completed':
        vendor = instance.vendor

        # On-Time Delivery Rate
        completed_orders = vendor.purchase_orders.filter(status='completed').count()
        on_time_orders = vendor.purchase_orders.filter(status='completed', delivery_date__lte=timezone.now()).count()
        vendor.on_time_delivery_rate = on_time_orders / completed_orders if completed_orders else 0

        # Quality Rating Average
        quality_ratings = vendor.purchase_orders.filter(status='completed').values_list('quality_rating', flat=True)
        vendor.quality_rating_avg = sum(quality_ratings) / len(quality_ratings) if quality_ratings else 0

        # Average Response Time
        response_times = vendor.purchase_orders.filter(acknowledgment_date__isnull=False).values_list(
            'issue_date', 'acknowledgment_date'
        )
        total_response_time = sum([(ack - issue).total_seconds() for issue, ack in response_times])
        vendor.average_response_time = total_response_time / len(response_times) if response_times else 0

        # Fulfillment Rate
        fulfilled_orders = vendor.purchase_orders.filter(status='completed').count()
        vendor.fulfillment_rate = fulfilled_orders / completed_orders if completed_orders else 0

        vendor.save()
