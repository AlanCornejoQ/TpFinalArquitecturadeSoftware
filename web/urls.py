from django.urls import path
from web.views.reserva_view import crear_reserva_view

urlpatterns = [
    path('reservas/crear/', crear_reserva_view, name='crear_reserva'),
]
