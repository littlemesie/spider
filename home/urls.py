from django.conf.urls import url
from home import views

urlpatterns = [
    url(r'^index1$', views.index1, name='index1'),
    url(r'^index$', views.index, name='index'),
    url(r'^page_item$', views.page_item, name='page_item'),
    url(r'^test$', views.test, name='test'),
]