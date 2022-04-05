from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    # raw_id_fields = ['product'] # optionaly


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'processed', 'created', 'updated']
    list_filter = ['paid', 'processed', 'created', 'updated']
    
    inlines = [OrderItemInline]
