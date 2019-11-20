from rest_framework import routers
from Forms.viewsets import FormularioViewSet, PreguntaViewSet, RespuestaViewSet, AsigPreguntaViewSet
from users.viewsets import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'formulario', FormularioViewSet)
router.register(r'pregunta', PreguntaViewSet)
router.register(r'respuesta', RespuestaViewSet)
router.register(r'asigpregunta', AsigPreguntaViewSet)
router.register(r'profile', ProfileViewSet)