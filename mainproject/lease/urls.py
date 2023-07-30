from django.urls import path
from.import views

urlpatterns = [
    path('', views.registerpageuser),
    path('userlog/',views.userlogin),
    path('adminlog/',views.adminlog),
    path('registerpagecontainer/',views.registerpagecontainer),
    path('pendinguser/', views.pendinguser),
    path('approveuser/<int:id>/', views.approveuser),
    path('approveduser/', views.approveduser),
    path('pending/', views.pending),
    path('approve/<int:id>/', views.approve),
    path('approved/', views.approved),
    path('operationuser/', views.operationuser),
    path('edituser/<int:id>/', views.edituser),
    path('deleteuser/<int:id>/', views.deleteuser),
    path('operationcontainer/', views.operationcontainer),
    path('editcontainer/<int:id>/', views.editcontainer),
    path('deletecontainer/<int:id>/', views.deletecontainer)
]