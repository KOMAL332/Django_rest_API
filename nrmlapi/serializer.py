from rest_framework import serializers
from .models import Company
import re

class CompanySerializer(serializers.ModelSerializer):
     
     class Meta:
         model = Company
         fields = '__all__'
        #  exclude = ['type', .....]  --> if we have n no of records and want to exclude some fields
        
# instead of creating logic in views, create logic over data in serializer via pre define validate method         
     def validate(self, validated_data): 
        print(validated_data)
        
        if validated_data.get('name'):
            Company_title = validated_data['name']
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if not regex.search(Company_title) == None:
                raise serializers.ValidationError("COMPANY NAME DO NOT CONTAIN SPECIAL CHARACTER")
            
        return validated_data
            
        
        
             
        
        
        
    
    