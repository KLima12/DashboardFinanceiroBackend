from ninja import Schema
from typing import Optional
class CreateTransactionSchema(Schema): 
    tipo: str
    valor: float
    descricao: Optional[str] = None

def create_transaction(request, data: CreateTransactionSchema): 
    pass