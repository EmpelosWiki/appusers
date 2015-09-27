# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

"""
Oficio
Modelo prara guardar el catalogo de oficios
"""
class Oficio( models.Model ) :
    
    description = models.CharField( max_length = 500, default = 1 )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ unidocde function """
        return self.description
    #End of unidocde function
        
#End of oficio model class

"""
Tipo usuario
"""
class TipoUserApp( models.Model ) :
    
    description = models.CharField( max_length = 500, default = '' )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Unicode for the tipo usuario model """
        return self.description
    #End of unicode function 
    
#End of itpo de usuario model

"""
App user
This is just for the user on the application
"""
class UserApp( models.Model ) :
    
    name = models.CharField( max_length = 200, unique = False, blank = True, default = '' )
    last_name = models.CharField( max_length = 200, unique = False, blank = True, default = '' )
    email = models.EmailField( max_length = 200, unique=True, default='' )
    password = models.CharField( max_length = 200 )
    direction = models.CharField( max_length= 500, default='' )
    phone_regex = RegexValidator( regex=r'^\+?1?\d{9,15}$', message="Número de teléfono incorrecto." )
    phone_number = models.CharField( max_length = 200, validators=[phone_regex], blank=True, default='' )
    tipo_usuario = models.ForeignKey( TipoUserApp, blank=True, default=1 )
    ciudad = models.CharField( max_length = 200, default = '', blank = True )
    estado = models.CharField( max_length = 200, default = '', blank = True )
    oficio = models.ForeignKey( Oficio, default=1, blank=True )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ unicode function for the app user model """
        return self.email
    #End of unicode funciton
    
#End of app user model

"""
Oficio
Modelo prara guardar el catalogo de oficios
"""
class Media( models.Model ) :
    
    url = models.CharField( max_length = 500, default = 1 )
    user = models.ForeignKey( UserApp, default=1, blank=True )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date uploaded
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ unidocde function """
        return self.url
    #End of unidocde function
        
#End of oficio model class