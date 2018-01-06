from django.conf.urls import url
from . import views

app_name = "mapa"

urlpatterns = [

    url(r'^$',views.index,name='index'),

    url(r'^acerca/$',views.acerca,name='acerca'),

    url(r'^contacto/$',views.contacto,name='contacto'),

    url(r'^desarrolladores/$',views.desarrolladores,name='desarrolladores'),

    url(r'^faq/$',views.faq,name='faq'),

    url(r'^galeria/$',views.galeria,name='galeria'),

    url(r'^programadores/$',views.programadores,name='programadores'),

    url(r'^lineaDeTiempo/$',views.timeline,name='timeline'),

]
