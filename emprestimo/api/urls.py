from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('proposals', views.CreateProposal.as_view()),
    path('proposal_fields', views.ProposalField.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
