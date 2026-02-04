from rest_framework import viewsets

from .models import Transaction
from .serializer import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Transaction model.

    Provides these actions automatically:
    - list:    GET    /transactions/      (get all transactions)
    - create:  POST   /transactions/      (create new transaction)
    - retrieve: GET   /transactions/{id}/ (get one transaction)
    - update:  PUT    /transactions/{id}/ (update entire transaction)
    - partial: PATCH  /transactions/{id}/ (update some fields)
    - destroy: DELETE /transactions/{id}/ (delete transaction)
    """

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
