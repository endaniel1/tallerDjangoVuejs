from rest_framework import routers

from .viewsets import BookViewSet

#Esta va a definir la rutas para nuestro modelo para trabajar con un Api
#las rutas basicas Post, Get, Put, Delete
router = routers.SimpleRouter() 

router.register("books", BookViewSet)

urlpatterns = router.urls