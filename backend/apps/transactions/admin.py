from django.contrib import admin
from .models import Transaction

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "date",
        "transaction_type",
        "category",
        "amount",
        "description",
        "created_at"
    ]
    list_filter = [
        "transaction_type",
        "category",
        "date"
    ]
    search_fields = [
        "description",
        "category"
    ]
    ordering = ["-date", "-created_at"]
    date_hierarchy = "date"
    readonly_fields = ["created_at", "updated_at"]
