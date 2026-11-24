from financeiro.models import User, Transacoes
from ninja.errors import HttpError
from django.db.models import Q, Sum

def get_dados(request, email):
    print(f"Email chegou aqui: {email}")
    user = User.objects.filter(email=email).first()
    if not user: 
        raise HttpError(404, "Usuário não existe.")

    filtros = Q(user=user, tipo__in=["INCOME", "EXPENSE"]) 
    
    dados = Transacoes.objects.filter(filtros).aggregate(
        total_income = Sum('valor', filter=Q(tipo="INCOME")), 
        total_expense = Sum('valor', filter=Q(tipo="EXPENSE"))
        )

    income = dados["total_income"]
    expense = dados["total_expense"]

    saldo = income - expense
    
    return { 
        "receita": income, 
        "despesa": expense, 
        "saldo": saldo
    }
