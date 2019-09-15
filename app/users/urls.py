from django.urls import path, include
from users import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    # path('user/', views.UserView.as_view()),
    path('', include(router.urls)),
]
