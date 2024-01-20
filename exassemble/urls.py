from . import views
from django.urls import path


# URLS que serão usadas a partir da URL padrão definida em 'exroutine/urls'
urlpatterns = [
    path('', views.index, name='index'),

    path('newsheet/', views.addSheet, name='add_sheet'),
    path('<int:pk>/', views.viewSheet, name='sheet_detail'),
    path('<int:pk>/update', views.updateSheet, name='update_sheet'),
    path('<int:pk>/delete', views.deleteSheet, name='delete_sheet'),

    path('exercises/', views.listExercises, name='exercises'),
    path('exercises/newexercise/', views.addExercise, name='add_exercise'),
    path('exercises/<int:pk>', views.viewExercise, name='exercise_detail'),
    path('exercises/<int:pk>/update', views.updateExercise, name='update_exercise'),
    path('exercises/<int:pk>/delete', views.deleteExercise, name='delete_exercise'),
]
