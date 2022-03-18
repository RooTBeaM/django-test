from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('all-test', views.all_test, name='test'),
    path('query-data', views.query_data, name='query'),
    path('table', views.table, name='table'),
    path('post-details/<int:id>', views.post_details, name='post'),
    path('export-csv',views.export_csv,name='csv'),
    path('contact',views.contact,name='contact'),
    path('thanks',views.thanks,name='thanks'),
]