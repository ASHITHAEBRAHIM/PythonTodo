from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.add,name='add'),
    # path('detail/',views.detail,name='detail')
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvadd/',views.Tasllistview.as_view(),name='cbvadd'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete')
]
