from django.db.models.fields import DateField
from django.shortcuts import render, redirect
from .models import Objetivo, Altapost, Categoria ,Comentario, ComentariosObj
from .forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import CreateView
#Si la vista es basada en Funcion
from django.contrib.auth.decorators import login_required

#Si la vista es basada en Clase
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
def home(request):

	return render(request,'app/home.html')


def blog(request):
	posteos = Altapost.objects.all()

	
	ctx = {}
	ctx['post'] = posteos
	return render(request,'app/blog.html', ctx)



def enfoques(request):
	categorias=Categoria.objects.all()
	data={
		'categorias':categorias
	}
	return render(request,'app/enfoques.html',data)


def registro(request):
	data={
		'form':CustomUserCreationForm()
	}
	if request.method=='POST':
		formulario=CustomUserCreationForm(data=request.POST)
		if formulario.is_valid():
			formulario.save()
			user= authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
			login(request,user)
			messages.success(request,"te has registrado correctamente")
			return  redirect(to="home")
		data["form"]=formulario
	
	return render(request,'registration/registro.html',data)




def DetalleCategoria(request, pk):
	
	categoria = Categoria.objects.get(pk = pk)
	p = Objetivo.objects.filter(categoria = categoria)
	
	ctx = {}
	ctx['post'] = p

	return render( request, 'app/detalleCategoria.html', ctx)

def DetalleObjetivo(request, pk):
	p = Objetivo.objects.get(pk = pk)
	
	ctx = {}
	ctx['objetivo'] = p

	return render( request, 'app/detalleObjetivo.html', ctx)


#En el template voy a tener variables separadas
# 1 variacble que se llama post que contiene a p
# y otra variable que contiene lo que le ponga


#CLASE.objetcs.all() retorna todos los objetos de una clase
#CLASE.objects.get() retorna solo 1 objeto(solo funciona si estoy seguro que va a retornar uno)
#CLASE.objects.filter() retorna varios que cumplas con la condicion.

class AltaPost(LoginRequiredMixin ,CreateView):
	model='Altapost'
	template_name= 'app/nuevoPost.html'
	form_class= Formulario_alta_post
	
	def form_valid(self, form):
		f=form.save(commit=False)
		f.usuario=self.request.user
		form.save(commit=True)
		return super(AltaPost,self).form_valid(form)

class Comentarios(LoginRequiredMixin ,CreateView):
	model='Comentario'
	template_name= 'app/Comentarios.html'
	form_class= Formulario_comentario

class ComentariosObjetivos(LoginRequiredMixin ,CreateView):
	model='ComentariosObj'
	template_name= 'app/ComentariosObj.html'
	form_class= Formulario_comentarios_obj


def VerComentarios(request, pk):
	pk = Altapost.objects.get(pk = pk)
	comments = Comentario.objects.filter(post = pk)
	ctx = {}
	ctx['comentarios'] = comments
	return render(request,'app/verComentarios.html', ctx)

def VerComentariosObjetivos(request, pk):
	pk = Objetivo.objects.get(pk = pk)
	comments = ComentariosObj.objects.filter(post = pk)
	ctx = {}
	ctx['comentarios'] = comments
	return render(request,'app/verComentariosObj.html', ctx)

def FiltroXFechaReciente(request):
	fecha_post= Altapost.objects.all().order_by('-fecha_elaboracion')
	fecha_comment = Comentario.objects.all().order_by('-fecha_creacion')
	ctx={}
	ctx['post']=fecha_post
	ctx['comentario'] = fecha_comment
	return render(request,'app/filtroXFechaReciente.html', ctx)

def FiltroXFechaViejo(request):
	fecha= Altapost.objects.all().order_by('fecha_elaboracion')
	ctx={}
	ctx['post']=fecha
	return render(request,'app/filtroXFechaViejos.html', ctx)

def DetallePostBlog(request, pk):
	p = Altapost.objects.get(pk = pk)

	ctx = {}
	ctx['post'] = p

	return render( request, 'app/detallePostBlog.html', ctx)

#FILTRAR CATEGORIAS EN LA SECCION BLOG

def FiltroCatPersonas(request):
	c = Altapost.objects.filter(categoria = 1)

	ctx = {}
	ctx['post'] = c

	return render( request, 'app/FiltrosCategoriasBlog/filtroCatPersonas.html', ctx)

def FiltroCatPlaneta(request):
	c = Altapost.objects.filter(categoria = 2)

	ctx = {}
	ctx['post'] = c

	return render( request, 'app/FiltrosCategoriasBlog/filtroCatPlaneta.html', ctx)

def FiltroCatProsperidad(request):
	c = Altapost.objects.filter(categoria = 3)

	ctx = {}
	ctx['post'] = c

	return render( request, 'app/FiltrosCategoriasBlog/filtroCatProsperidad.html', ctx)

def FiltroCatPaz(request):
	c = Altapost.objects.filter(categoria = 4)

	ctx = {}
	ctx['post'] = c

	return render( request, 'app/FiltrosCategoriasBlog/filtroCatPaz.html', ctx)

def FiltroCatAlianzas(request):
	c = Altapost.objects.filter(categoria = 5)

	ctx = {}
	ctx['post'] = c

	return render( request, 'app/FiltrosCategoriasBlog/filtroCatAlianzas.html', ctx)

def FiltroComentariosRecientes(request):
	c = Comentario.objects.all().order_by('-fecha_creacion')

	ctx = {}
	ctx['comentarios'] = c

	return render( request, 'app/filtroComentariosRecientes.html', ctx)

def FiltroComentariosAntiguos(request):
	c = Comentario.objects.all().order_by('fecha_creacion')

	ctx = {}
	ctx['comentarios'] = c

	return render( request, 'app/filtroComentariosAntiguos.html', ctx)