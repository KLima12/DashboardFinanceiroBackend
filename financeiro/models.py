from django.db import models
from django.contrib.auth.models import User


class Transacoes(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = "INCOME", "Receita"
        EXPENSE = "EXPENSE", "Despesa"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    descricao = models.CharField(max_length=255)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    tipo = models.CharField(max_length=7, choices=TransactionType.choices)
    categoria = models.CharField(max_length=100)
    data = models.DateField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descricao} ({self.tipo}): {self.saldo}"
