from django.urls import path

from forms import views

urlpatterns = [
    path('', views.FormList.as_view()),
    path('next_time_slot/', views.GetNextTimeSlot.as_view()),
    path('calls/<int:pk>/', views.UpdateCall.as_view()),
    path('calls/<int:pk>/finish_scenario/', views.FinishScenario.as_view()),
    path('get_agent_token/', views.GetAgentToken.as_view()),
]
