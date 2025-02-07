from django.urls import path
from .views import index, cast_vote, display_results

urlpatterns = [
    path('', index, name="index"),
    path('vote/', cast_vote, name="cast_vote"),
    path('results/', display_results, name="display_results"),
]
