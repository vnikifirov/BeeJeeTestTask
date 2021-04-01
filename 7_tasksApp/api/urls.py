from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from .views import current_user, UserList

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
	
	path('token-auth/', obtain_jwt_token),
	path('current_user/', current_user),
    path('users/', UserList.as_view()),

	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),
	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]