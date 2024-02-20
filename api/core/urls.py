from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import AirlineViewSet, AirportViewSet, FlightViewSet, RunwayViewSet

router = DefaultRouter()
router.register(r'airports', AirportViewSet, basename='airport')
router.register(r'airlines', AirlineViewSet, basename='airline')
router.register(r'runways', RunwayViewSet, basename='runway')
router.register(r'flights', FlightViewSet, basename='flight')

urlpatterns = [
    path('', include(router.urls))
]