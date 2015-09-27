# -*- coding: utf-8 -*-
from django import forms
from .models import TipoUserApp, UserApp, Oficio, Media

"""
AppUser Form
"""
class UserAppForm( forms.ModelForm ) :
    
    name = forms.CharField( widget=forms.TextInput( attrs = { 'placeholder' : 'Nombre' } ), label="" )
    last_name = forms.CharField( widget=forms.TextInput( attrs = { 'placeholder' : 'Apellidos' } ), label="" )
    password = forms.CharField( widget=forms.PasswordInput( attrs = { 'placeholder' : 'Password' } ), label="" )
    email = forms.CharField( widget=forms.TextInput( attrs = { 'placeholder' : 'Correo electronico' } ), label="" )
    phone_number = forms.CharField( widget=forms.TextInput( attrs = { 'placeholder' : 'Telefono' } ), label="" )
    ciudad = forms.CharField( widget=forms.TextInput( attrs = { 'placeholder' : 'Ciudad' } ), label="" )
    estado = forms.CharField( widget=forms.TextInput( attrs = { 'placeholder' : 'Estado' } ), label="" )
    
    class Meta :
        
        model = UserApp
        fields = [ 'name', 'last_name', 'email', 'password', 'phone_number', 'tipo_usuario', 
            'ciudad', 'estado', 'oficio' ]
        
    #End of meta class
    
#End of app user form class

"""
Tipo Usuario Form
"""
class TipoUserAppForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta :
        
        model = TipoUserApp
        fields = [ 'description' ]
        
    #End of meta class
    
#End of tipo usuario form class


"""
Oficio form class
"""
class OficioForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta :
        
        model = Oficio
        fields = [ 'description' ]
    
    #End of meta class
    
#End of Oficio form class    

"""
Media  Form Class
"""
class MediaForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta :
        
        model = Media
        fields = [ 'url', 'user' ]
    
    #End of meta class

#End of media form class

"""
Login form class
"""
class LoginForm( forms.Form ) :
    
    email = forms.CharField( widget=forms.TextInput( attrs = { 'placeholder' : 'Correo electronico' } ), label="" )
    password = forms.CharField( widget=forms.PasswordInput( attrs = { 'placeholder' : 'Password' } ), label="" )

#End of login form    