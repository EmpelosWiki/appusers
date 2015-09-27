from rest_framework import serializers
from .models import Oficio, UserApp, TipoUserApp

"""
Oficio serializers
"""
class OficioSerializer( serializers.ModelSerializer ) :
    
    """
    OficioSerializer class
    """
    class Meta :
        
        model = Oficio
        fields = ( 'id', 'description', )
        
    #End of meta class
    
#End of oficio serializer class
"""
Tipo user app serializer
"""
class TipoUserAppSerializer( serializers.ModelSerializer ) :

    """
    Meta class for the tipo user app serializer
    """
    class Meta :
        
        model = TipoUserApp
        fields = ( 'id', 'description', )
    
    #End of meta class 
    
#End of tipo user app serializer class

"""
User App serializer
"""
class UserAppSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for the user app serializer
    """
    class Meta :
        
        model = UserApp
        fields = ( 'id', 'name', 'last_name', 'email', 'phone_number', 'tipo_usuario', 
            'ciudad', 'estado', 'password', 'oficio', )
    
    #End of meta class 
    
#End of user app serializer class