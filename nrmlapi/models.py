import uuid
from django.db import models

# Create your models here.

class BaseModel(models.Model):
    UID = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    created_at = models.DateField(("CREATED"), auto_now=True)
    # updated_at = models.DateField(auto_now_add=True)
    
    class Meta:
        abstract = True  #make it True ,So that we can treat above basemodel as class
        
class Company(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField(max_length=100)
    type = models.CharField(max_length=100, choices=(('IT','IT'), ('NON-IT','NON-IT')))
    # created_at = models.DateField(("CREATED"), auto_now=True)
    
    
    
    