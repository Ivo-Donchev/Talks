from django.urls import path

from .views import CRUDView

urlpatterns = [
    path(
        route='api/<int:create_queries_count>/<int:select_queries_count>/<int:update_queries_count>/<int:delete_queries_count>/',
        view=CRUDView.as_view(),
    )
]
