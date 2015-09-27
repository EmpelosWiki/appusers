from django.contrib import admin
from .models import TipoUserApp, UserApp, Oficio, Media
from .forms import TipoUserAppForm, UserAppForm, OficioForm, MediaForm

"""
Oficio Admin Class
"""
class OficioAdmin( admin.ModelAdmin ) :
    
    list_display = [ 'id', 'description' ]
    form = OficioForm
    
#End of oficio amdin class

"""
Tipo usuario admin
"""
class TipoUserAppAdmin( admin.ModelAdmin ) :
    
    list_display = [ 'id', 'description' ]
    form = TipoUserAppForm

#End of tipo usuario amdin class
    
"""
App user admin
"""
class UserAppAdmin( admin.ModelAdmin ) :
    
    list_display = [ 'id', 'name', 'last_name', 'email', 'password', 'phone_number', 'tipo_usuario', 
        'ciudad', 'estado', 'oficio' ]
    form = UserAppForm
    
#End of app user admin class

"""
App user admin
"""
class MediaAdmin( admin.ModelAdmin ) :
    
    list_display = [ 'id', 'url', 'user' ]
    form = MediaForm
    
#End of app user admin class

# Load on the admin panel
admin.site.register( TipoUserApp, TipoUserAppAdmin )
admin.site.register( UserApp, UserAppAdmin )
admin.site.register( Oficio, OficioAdmin )
admin.site.register( Media, MediaAdmin )