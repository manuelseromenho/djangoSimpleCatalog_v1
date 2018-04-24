from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name="product_list"),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.product_details, name='product_details'),
    url(r'^(?P<sub_category_slug>[-\w]+)/$', views.product_list, name='product_list_by_subcategory'),
    #url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),

]
