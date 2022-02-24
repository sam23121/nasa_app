from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.specific, name="specific")
]