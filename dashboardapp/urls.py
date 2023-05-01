from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='index'),
    path('base/',views.base,name='base'),
    
    path('m-table/',views.mentorTable,name='m_table'),
    path('m-create/',views.mentorCreate,name='m_create'),
    
    path('1a-class/',views.a1_class,name='1a_class'),
    path('admin/',views.error,name='error'),
]