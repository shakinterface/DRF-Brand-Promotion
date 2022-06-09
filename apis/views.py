#from django.shortcuts import render
import json
from rest_framework import viewsets
from .serializers import BrandSerializer, CustomerGoalsSerializer, PlanSerializer,PromotionSerializer, UserSerializer
from .models import Brands, Plans,Promotions,User,CustomerGoals
from django.contrib.auth.hashers import make_password
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect

# Create your views here.
#### Brands View Sets ##########################
class BrandViewSet(viewsets.ModelViewSet):
    queryset=Brands.objects.all()
    serializer_class=BrandSerializer

#### Plans View Sets ##########################
class PlanViewSet(viewsets.ModelViewSet):
    queryset=Plans.objects.all()
    serializer_class = PlanSerializer
    filter_fields = (
        'brands_id',
    )

#### Promotions View Sets ##########################
class PromotionViewSet(viewsets.ModelViewSet):
    queryset=Promotions.objects.all()
    #queryset=Promotions.objects.select_related('plans')
    #queryset = Promotions.objects.get(plans_id=plans_id).all()
    serializer_class=PromotionSerializer

#### User View Sets ##########################
class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    def createUser(self,validated_data):
        user = User.objects.create(
        userEmail=validated_data['userEmail'],
        userName=validated_data['userName'],
        userPassword = make_password(validated_data['userPassword']))
        user.save()
#### CustomerGoalsViewSet ##########################
class CustomerGoalsViewSet(viewsets.ModelViewSet):
    queryset=CustomerGoals.objects.all()
    serializer_class=CustomerGoalsSerializer
    filter_fields = (
        'user_id',
        'brands_id',
        'plans_id',
    )




