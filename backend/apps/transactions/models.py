from django.db import models


# Create your models here.
class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = "income", "Income"
        EXPENSE = "expense", "Expense"

    class Category(models.TextChoices):
        # Income Categories
        SALARY = "salary", "Salary"
        FREELANCE = "freelance", "Freelance"
        INVESTMENTS = "investments", "Investments"
        OTHER_INCOME = "other_income", "Other Income"
        # Expense categories
        FOOD = "food", "Food & Dining"
        TRANSPORTATION = "transportation", "Transportation"
        UTILITIES = "utilities", "Utilities"
        RENT = "rent", "Rent/Mortgage"
        ENTERTAINMENT = "entertainment", "Entertainment"
        SHOPPING = "shopping", "Shopping"
        HEALTHCARE = "healthcare", "Healthcare"
        EDUCATION = "education", "Education"
        OTHER_EXPENSE = "other_expense", "Other Expense"

    amount = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Transaction amount in your currency"
    )
    transaction_type = models.CharField(
        max_length=10,
        choices=TransactionType.choices,
        help_text="Whether this is income or expense",
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        help_text="Catrgory of the transaction",
    )
    description = models.TextField(
        blank=True, default="", help_text="OPtional description or notes"
    )
    date = models.DateField(help_text="Date when the transaction occured")
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="Timestamp when this record was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="Timestamp when this record was last updated"
    )

    class Meta:
        ordering = ["-date", "-created_at"]
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        return f"{self.get_transaction_type_display()}: {self.amount} - {self.get_category_display()}"  # pyright: ignore[reportAttributeAccessIssue]
