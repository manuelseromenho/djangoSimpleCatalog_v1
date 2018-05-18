from django.conf.urls import url
from django.contrib import admin
#from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

    # url(r'^adicionar/(?P<product_slug>[-\w]+)/$', views.adicionar_carrinho, name="adicionar_carrinho"),
    url(r'^atualizar/$', views.atualizar_carrinho, name="atualizar_carrinho"),
    url(r'^adicionar/$', views.adicionar_carrinho, name="adicionar_carrinho"),
    url(r'^$', views.mostrar_carrinho, name="mostrar_carrinho"),
    #url(r'^carrinho/delete/(?P<pk>\d+)/$', views.ItemDelete.as_view(), name='cart_item_delete'),
    url(r'^carrinho/delete/(?P<pk>\d+)/$', views.delete_item, name='cart_item_delete'),


]
