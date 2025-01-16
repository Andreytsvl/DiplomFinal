from django.contrib import admin
from django.utils.html import format_html
from products_app.models import Categories, Recipe_status, Storage_conditions, Price_category, Products

#admin.site.register(Categories)
admin.site.register(Recipe_status)
admin.site.register(Storage_conditions)
admin.site.register(Price_category)
#admin.site.register(Products)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["name", "quantity", "price", "discount"]
    list_editable = ["discount",] #изменение поля дисконт
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]
    fields = [
        "name",
        "category",
        "slug",
        "description",
        "image",
        ("price", "discount"),
        "quantity",
        "price_category",
        "storage_conditions",
        "recipe_status"
  ] # порядок размещения полей внутри

    # def view_on_site_link(self, obj):  не работает
    #     if obj.pk:
    #         url = obj.get_absolute_url()
    #         return format_html('<a href="{}" target="_blank">Смотреть на сайте</a>', url)
    #     return "—"
    #
    # view_on_site_link.short_description = 'Ссылка на сайте'

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    ordering = ["name"]
    list_display = ["name", "id"]