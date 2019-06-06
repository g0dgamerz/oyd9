from django.urls import path
from . import views

urlpatterns = [
    path('',views.journal,name='journal'),
    path('add',views.add,name="add"),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy)
]