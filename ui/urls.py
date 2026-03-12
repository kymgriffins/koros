from django.urls import path
from . import views

app_name = 'ui'

urlpatterns = [
    path('index', views.index, name='index'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('budget-ndio-story/', views.budget_ndio_story, name='budget_ndio_story'),
    path('option1/', views.option1, name='option1'),
    path('option2/', views.option2, name='option2'),
    path('option3/', views.option3, name='option3'),
    path('option4/', views.option4, name='option4'),
    path('bnsclaude/', views.bnsclaude, name='bnsclaude'),
    path('', views.main, name='main'),
]
