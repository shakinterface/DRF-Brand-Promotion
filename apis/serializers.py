from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Brands, Plans,Promotions,User,CustomerGoals

# Brand model serializer
class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Brands
        fields=('brandID', 'brandName')

# Plan model serializer
class PlanSerializer(serializers.HyperlinkedModelSerializer):
    brands_id=serializers.RelatedField(source='brandID',read_only=True)
    brandID_id=serializers.ReadOnlyField()
    class Meta:
        model=Plans
        fields = "__all__"
        #fields=('planID', 'planName', 'amountOptions', 'tentureOptions', 'benefitPercentage', 'benefitType')

# Promotion model serializer
class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    plans_id=serializers.RelatedField(source='planID',read_only=True)
    plans_id=serializers.ReadOnlyField()
    class Meta:
        model=Promotions
        #fields=('promotionId', 'limitedBy', 'promotionValue', 'plans_id')
        fields = "__all__"
# User model serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields = "__all__"

# CustomerGoals model serializer
class CustomerGoalsSerializer(serializers.HyperlinkedModelSerializer):
    plans_id=serializers.RelatedField(source='planID',read_only=True)
    plans_id=serializers.ReadOnlyField()
    user_id=serializers.RelatedField(source='userID',read_only=True)
    user_id=serializers.ReadOnlyField()
    brands_id=serializers.RelatedField(source='brandID',read_only=True)
    brandID_id=serializers.ReadOnlyField()
    class Meta:
        model=CustomerGoals
        #fields=('promotionId', 'limitedBy', 'promotionValue', 'plans_id')
        fields = "__all__"

    
    