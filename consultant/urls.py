from django.urls import path
from consultant.views import AnswerListView, AnswerDetailView

urlpatterns = [
    path("answers/", AnswerListView.as_view(), name="answer_list"),
    path("answers/<int:pk>/", AnswerDetailView.as_view(), name="answer_detail"),
]

