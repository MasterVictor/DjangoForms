from django.urls import path
from . import views

app_name = "aplicacion"
urlpatterns = [
    path("usuario/",views.UsuarioListView.as_view(), name="indexUsu"),
    path("usuario/<int:pk>/",views.UsuarioDetailView.as_view(), name="detailUsu"),
    #path("<int:pk>/update/", views.RopaUpdateView.as_view(), name="update"),
    path("usuario/create/", views.UsuarioCreateView.as_view(), name="createUsu"),
    #path("<int:pk>/delete/", views.RopaDeleteView.as_view(), name="delete"),  
    #path("factura",views.FacturaListView.as_view(), name="indexf"),
    #path("factura/<int:pk>/",views.FacturaDetailView.as_view(), name="detailf"),
    #path("factura/create/", views.FacturaCreateView.as_view(), name="createf"),
    #path("factura/<int:pk>/delete", views.FacturaDeleteView.as_view(), name="deletef"),
    #path("factura/<int:pk>/update", views.FacturaUpdateView.as_view(), name="updatef"),
]