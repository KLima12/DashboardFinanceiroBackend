from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, max_length=36, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)

    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    receita = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    despesas = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Transacoes(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = "INCOME", "Receita"
        EXPENSE = "EXPENSE", "Despesa"

    class TransactionCategoria(models.TextChoices): 
        ALIMENTACAO = "Alimentacao", "Alimentação"
        MORADIA = "Moradia", "Moradia"
        TRANSPORTE = "Transporte", "Transporte"
        SAUDE = "Saude", "Saúde"
        LAZER = "Lazer", "Lazer"
        OUTROS = "Outros", "Outros"

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    descricao = models.CharField(max_length=255, null=True, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    tipo = models.CharField(max_length=7, choices=TransactionType.choices)
    categoria = models.CharField(max_length=100, choices=TransactionCategoria.choices)
    data = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.descricao} ({self.tipo}): {self.valor}"
