from django.conf.urls import url
from django.contrib import admin
#from django.contrib.auth import views as auth_views
from . import views


from django.contrib.auth.views import (
    password_change,
    password_change_done,
)

urlpatterns = [

    # edit user profile
    url(r'^edit/$', views.edit, name='edit'),

    # user registration
    url(r'^register/$', views.register, name='register'),

    # restore password urls
    url(r'^password-reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect': 'shop:password_reset_done'},
        name='password_reset'),

    url(r'^password-reset/done/$','django.contrib.auth.views.password_reset_done', name='password_reset_done'),

    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        {'post_reset_redirect': 'shop:password_reset_complete'},
        name='password_reset_confirm'),

    url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),

    url(r'^password-change/$',
        'django.contrib.auth.views.password_change',
        { 'post_change_redirect': 'shop:password_change_done'},
        name='password_change'),
    url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),


    # para login
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^loggedout/$', 'django.contrib.auth.views.logout', name='loggedout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),

    # show orders list
    url(r'^orderlist/$', views.order_list, name='order_list'),

    # products
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.product_details, name='product_details'),
    url(r'^$', views.product_list, name="product_list"),
    url(r'^(?P<sub_category_slug>[-\w]+)/$', views.product_list, name='product_list_by_subcategory'),



]
