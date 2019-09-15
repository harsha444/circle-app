from django.urls import path, include
from blog import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blog', views.BlogViewSet)

urlpatterns = [
    # path('user/', views.UserView.as_view()),
    path('', include(router.urls)),
    path('common/<int:pk>/', views.CommonBlog.as_view()),
]
