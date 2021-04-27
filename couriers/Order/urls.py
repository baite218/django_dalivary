from django.urls import path

from Order.views import OrderView

urlpatterns = [
    path('', OrderView.as_view({'get': 'list'})),
    path('create/', OrderView.as_view({'post': 'create'})),
    path('<int:pk>/', OrderView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]