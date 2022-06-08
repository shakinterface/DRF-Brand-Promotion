from django import views
from django.urls import include, path
# import routers
from rest_framework import routers
from .views import *

# defining the router
router = routers.DefaultRouter()
 # define the router path and viewset to be used
router.register(r'tortoise/brands',BrandViewSet)
router.register(r'tortoise/plans',PlanViewSet)
router.register(r'tortoise/promotions',PromotionViewSet)
router.register(r'tortoise/users',UserViewSet)
#router.register(r'tortoise/CustomerGoalsByUserId/<int:id>',CustomerGoalsViewSet.byUserId))
router.register(r'tortoise/CustomerGoals',CustomerGoalsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
