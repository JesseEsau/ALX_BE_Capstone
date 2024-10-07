from django.urls import path
from .views import EventCreateAPIView, EventListAPIView, EventDetailView, EventRegistrationView, CommentCreateView, CommentRetrieveUpdateDestroyAPIView, PastEventListView

urlpatterns = [
    path('events/create/', EventCreateAPIView.as_view(), name="create_event"),
    path('events/', EventListAPIView.as_view(), name="events_list"),
    path("past-events/", PastEventListView.as_view(), name='past_events'),
    path('events/<int:pk>/', EventDetailView.as_view(), name="event_detail"),
    path('events/<int:event_id>/register/', EventRegistrationView.as_view(), name="register_for_event"),

    path('events/<int:event_pk>/comments/create/', CommentCreateView.as_view(), name='create_comment'),
    path('events/<int:event_pk>/comment/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),

]
