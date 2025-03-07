from django.contrib import admin

from orders.models import Order, OrderItem

#admin.site.register(Order)
#admin.site.register(OrderItem)

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = "product", "name", "price", "quantity"
    search_fields = (
        "product",
        "name",
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = "order", "product", "name", "price", "quantity"
    search_fields = (
        "order",
        "product",
        "name",
    )


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (

        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
        "pharmacy"
    )

    search_fields = (

        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )
    readonly_fields = ("created_timestamp",)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "pharmacy",
        "status",
        "payment_on_get",
        "is_paid",
        "created_timestamp",
    )

    search_fields = (
        "id",
        "user",
    )
    readonly_fields = ("created_timestamp",)
    list_filter = (

        "status",
        "payment_on_get",
        "is_paid",
    )
#     inlines = (OrderItemTabulareAdmin,)
