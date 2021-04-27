from django.urls import path

from .views import ProductView
from .views import CategoryView


urlpatterns = [
	path('category', CategoryView.as_view({'get': 'list'})),
    path('category/create', CategoryView.as_view({'post': 'create'})),
    path('category/<int:pk>', CategoryView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('', ProductView.as_view({'get': 'list'})),
    path('create', ProductView.as_view({'post': 'create'})),
    path('<int:pk>', ProductView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]