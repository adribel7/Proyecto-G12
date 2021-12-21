

from django.conf.urls import url
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('Alta/', views.AltaPost.as_view(), name="alta_post"),
    path('Comentario/', views.Comentarios.as_view(), name="Comentario"), 
    path('ComentariosObj/', views.ComentariosObjetivos.as_view(), name="ComentariosObj"), 
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('enfoques/',  views.enfoques, name="enfoques"),
    path('registro/', views.registro, name="registro"),
    path('detalle/<int:pk>', views.DetalleCategoria, name="detalle"),
    path('detalleObjetivo/<int:pk>', views.DetalleObjetivo, name='detalleObjetivo'), 
    path('verComentarios/<int:pk>', views.VerComentarios, name='VerComentarios'), 
    path('verComentariosObj/<int:pk>', views.VerComentariosObjetivos, name='VerComentariosObj'), 
    path('reciente', views.FiltroXFechaReciente, name="filtro_fecha_reciente"),
    path('viejo', views.FiltroXFechaViejo, name="filtro_fecha_viejo"),
    path('detallePostBlog/<int:pk>', views.DetallePostBlog, name='detallePostBlog'),

    path('filtroCatPersonas/', views.FiltroCatPersonas, name='filtroCatPersonas'),
    path('filtroCatPlaneta/', views.FiltroCatPlaneta, name='filtroCatPlaneta'),
    path('filtroCatProsperidad/', views.FiltroCatProsperidad, name='filtroCatProsperidad'),
    path('filtroCatPaz/', views.FiltroCatPaz, name='filtroCatPaz'),
    path('filtroCatAlianzas/', views.FiltroCatAlianzas, name='filtroCatAlianzas'),

    path('comentariosRecientes', views.FiltroComentariosRecientes, name="filtro_comentarios_recientes"),
    path('comentariosAntiguos', views.FiltroComentariosAntiguos, name="filtro_comentarios_antiguos"),

]
