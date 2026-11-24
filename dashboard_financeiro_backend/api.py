from ninja import NinjaAPI

api = NinjaAPI()

api.add_router("financeiro/", "financeiro.api.router")
