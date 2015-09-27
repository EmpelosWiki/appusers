# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import UserAppForm, LoginForm
from django.http import HttpResponseRedirect
from .models import UserApp
from empresas.models import Vacante

# Create your views here.
def home( request ) :
    """ home for the start view """
    # context variable
    context = {
        'title' : 'Inicio'    
    }
    #render the view
    return render( request, "home/index.html", context )

#End of home function controller

def signin( request ) :
    """ signin for registration """
    #method validation
    if request.method == 'POST' :
        userapp_form = UserAppForm( request.POST, prefix = "userapp_form" )
        instance = userapp_form.save( commit = False)
        instance.save()
        if instance.tipo_usuario.id == 1 :
            return HttpResponseRedirect( ( "/empresa/new/{0}" ).format( instance.id ) )
        elif instance.tipo_usuario.id == 2 :
            request.session['session_user_id'] = instance.id
            context = {
            }
            
            return render( request, "appusers/dashboard.html", context )
    else : 
        userapp_form = UserAppForm( prefix="userapp_form" )
        
    #context variable
    context = {
        'title' : 'Registrarse',
        'form' : userapp_form
    }
    #render the view
    return render( request, "authentication/signin.html", context )

#End of signin function controller

def login( request ) :
    """ signin for registration """
    #Validate if the user is already logged in
    if 'session_user_id' in request.session :
        user = UserApp.objects.get( pk = int( request.session['session_user_id'] ) )
        if user.tipo_usuario.id == 1 :
           return HttpResponseRedirect( "/empresa/dashboard/" )
        #context variable
        context = {
            "title" : "Dashboard"    
        }
        # render view
        return render( request, "appusers/dashboard.html", context )
    else :
        #context variable
        error = ""
        if request.method == 'POST' :
            form = LoginForm( request.POST, prefix="login_form" )
            user = None
            try:
                user = UserApp.objects.get( email = request.POST.get("login_form-email") )
            except UserApp.DoesNotExist:
                error = "No existe un usuario con este correo electronico, intente de nuevo"
            
            if user :
                if user.password == request.POST.get('login_form-password') :
                    request.session['session_user_id'] = user.id
                    return HttpResponseRedirect( "/empresa/dashboard/" )
                else : 
                    error = "Contraseña incorrecta, por favor inténtelo de nuevo"
            else :
                error = "No existe un usuario con este correo electronico, intente de nuevo"
            
                    
        form = LoginForm( prefix = "login_form" )
        
        context = {
            'title' : 'login',
            'form' : form,
            'error' : error
        }
        #render the view
        return render( request, "authentication/login.html", context )

#End of signin function controller

def dashboard( request ) :
    """ new controller function for adding a new empresa object """
    user = UserApp.objects.get( pk = int( request.session['session_user_id'] ) )
    
    if user.tipo_usuario.id == 1 :
       return HttpResponseRedirect( "/empresa/dashboard/" )
    #Get the user
    user = UserApp.objects.get( pk = int( request.session['session_user_id'] ) )
    #Get vacantes of the user
    vacantes = Vacante.objects.filter( oficio = user.oficio.id ).reverse()[:15]
    #context variable
    context = {
        "title" : "Dashboard",
        'current_user' : user,
        'vacantes' : vacantes
    }
    # render view
    return render( request, "appusers/dashboard.html", context )
#End of new function controller

def logout( request ) :
    """ Controller for the log out view """
    if 'session_user_id' in request.session :
        request.session.pop( "session_user_id", None )
        
        # context variable
        context = {
            'title' : 'Inicio'    
        }
        #render the view
        return render( request, "home/index.html", context )
        
    else :
            
        # context variable
        context = {
            'title' : 'Inicio'    
        }
        #render the view
        return render( request, "home/index.html", context )

#End of log out funciton 

