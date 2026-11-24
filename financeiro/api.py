from ninja import Router

router = Router()
from financeiro.functionsFinanceiro import get_dados, create_transaction

# TODO utilizar token JWT
router.get("get-info-user/")(get_dados.get_dados)

router.post("create-transaction")(create_transaction.create_transaction)
