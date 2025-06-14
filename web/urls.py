from django.urls import path
from web.views.reserva_view import crear_reserva_view
from web.views.disponibilidad_view import ver_disponibilidad_view
from web.views.reserva_admin_view import ver_reservas_view


urlpatterns = [
    path('reservas/crear/', crear_reserva_view, name='crear_reserva'),
    path('espacios/disponibles/', ver_disponibilidad_view, name='ver_disponibilidad'),
    path("reservas/", ver_reservas_view, name="ver_reservas"),
]
