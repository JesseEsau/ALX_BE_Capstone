from django.urls import path
from .views import home, EventCreateAPIView, EventListAPIView, EventDetailView, EventRegistrationView, CommentCreateView, CommentRetrieveUpdateDestroyAPIView, PastEventListView

urlpatterns = [
    path('', home, name="home"),
    path('event/create/', EventCreateAPIView.as_view(), name="create_event"),
    path('events/', EventListAPIView.as_view(), name="events_list"),
    path("past-events/", PastEventListView.as_view(), name='past_events'),
    path('event/<int:pk>/', EventDetailView.as_view(), name="event_detail"),
    path('event/<int:event_id>/register/', EventRegistrationView.as_view(), name="register_for_event"),

    path('event/<int:event_pk>/comments/create/', CommentCreateView.as_view(), name='create_comment'),
    path('event/<int:event_pk>/comment/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view()),

]
