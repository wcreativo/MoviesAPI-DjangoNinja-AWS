from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from inventory.api import router as inventory_router

api = NinjaAPI()

api.add_router("/inventory/", inventory_router)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
