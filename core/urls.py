from django.contrib import admin
from django.urls import path,include
from tasks import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")), #Para que tailwind recargue la pag auto
    path('', views.index, name='index'),
    #menu paths ------------------------------------------------------------->
    path('menu',views.menu, name='menu'),
    path('post/<int:post_id>/',views.post_detail, name='post_detail'),
    #END menu paths ------------------------------------------------------------->
    path('logout/',views.log_out, name='logout'),
    path('reg',views.reg, name='reg'),
    path('login',views.log_in,name='login'),
    path('conocenos',views.conocenos,name='conocenos'),
    path('empresas',views.empresas,name='empresas'),
    path('novedades',views.novedades, name='novedades'),
    path('perfil', views.perfil, name='perfil'),
    path('mensajes',views.mensajes, name='mensajes'),
    path('tendencias',views.tendencias, name='tendencias'),
    #url-----------------------------------
    path('accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
