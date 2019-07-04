from django.urls import path
from . import views

urlpatterns = [
    path('auth/account/', views.auth_account),
    path('reports/sort/', views.reports_sort),
    path('requests/sort/', views.requests_sort),
    path('reports/', views.ReportsViewAPI.as_view()),
    path('report/<int:pk>/', views.ReportViewAPI.as_view()),
    path('requests/', views.RequestsViewAPI.as_view()),
    path('request/<int:pk>/', views.RequestViewAPI.as_view()),
    path('db/', views.db_base),
    path('statistic/', views.statistic),
    path('floor/<int:pk>/rooms/', views.rooms_floor),
]
