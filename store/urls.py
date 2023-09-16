from django.urls import path
from django.urls.conf import include
from rest_framework.routers import SimpleRouter,DefaultRouter
from . import views

router = DefaultRouter()
router.register("products", views.ProductViewSet)
router.register("collections", views.CollectionViewSet)


urlpatterns = router.urls
