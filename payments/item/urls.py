from django.urls import path
from . import views

urlpatterns = [
    path('buy/<pk>/', views.StipeSessionId.as_view(), name = 'stripe_session_id' ),
    path('item/<pk>/', views.ItemView.as_view(), name='item'),
    path('success/', views.SuccessView.as_view(), name = 'success'),
    path('cancel/', views.CancelView.as_view(), name = 'cancel')
]
