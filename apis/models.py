from pyexpat import model
from django.db import models
from django.core.validators import MaxValueValidator
import datetime
import uuid

# Create your models here.
######## Brand ORM ###############
class Brands(models.Model):
    brandID=models.AutoField(primary_key=True)
    brandName=models.CharField(max_length = 255)
    def __str__(self):
        return self.brandName

######## Plans ORM ###############  
class Plans(models.Model):
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE)
    planID=models.AutoField(primary_key=True)
    planName=models.CharField(max_length = 255)
    amountOptions=models.CharField(max_length = 128)
    tentureOptions=models.CharField(max_length = 128)
    benefitPercentage=models.IntegerField(validators=[MaxValueValidator(100)])
    benefitType=models.CharField(max_length = 128)
    ####### Self #############
    def __str__(self):
        return self.planName

######## Promotions ORM ###############
class Promotions(models.Model):
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE)
    promotionId=models.AutoField(primary_key=True)
    limitedBy=models.CharField(max_length =64)
    ### We can also take date field but for now taken charField
    promotionValue=models.CharField(max_length = 255,null=True,blank=True)
    def __int__(self):
        return self.promotionId
    @property
    def plans_id(self):
        return self.Plans.planID
######## User ORM ###############
class User(models.Model):
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE)
    userID=models.AutoField(primary_key=True)
    userName=models.CharField(max_length = 255)
    userEmail=models.CharField(max_length = 255)
    userPassword=models.CharField(max_length = 255)
    def __str__(self):
        return self.userName
######## CustomerGoals ORM ###############
class CustomerGoals(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plans = models.ForeignKey(Plans, on_delete=models.CASCADE)
    brands = models.ForeignKey(Brands, on_delete=models.CASCADE)
    selectedAmount=models.CharField(max_length = 255)
    selectedTenture=models.CharField(max_length = 255)
    startedDate=models.DateTimeField('Start Date')
    depositedAmount=models.IntegerField(validators=[MaxValueValidator(9999999999)])
    benefitPercentage=models.IntegerField(validators=[MaxValueValidator(100)])
    benefitType=models.CharField(max_length = 128)
    def __int__(self):
        return self.id




