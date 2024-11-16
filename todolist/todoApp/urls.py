from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import AllowAny
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Swagger 설정
schema_view = get_schema_view(
    openapi.Info(
        title="To-Do List API",
        default_version='v1',
        description="To-Do List API 문서",
        contact=openapi.Contact(email="gjtjqkr5880@gmail.com"),
    ),
    public=True,
    permission_classes=(AllowAny,)  # Swagger에 인증 없이 접근 가능
)

# REST API 라우터 설정
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')

# URL 패턴
urlpatterns = [
    # 일반 페이지 URL
    path('', views.task_list, name='task_list'),
    path('<int:pk>/', views.task_detail, name='task_detail'),
    path('add/', views.task_create, name='task_create'),
    path('<int:pk>/edit/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('<int:pk>/complete/', views.task_complete, name='task_complete'),
    path('<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
    path('task/<int:pk>/toggle/', views.task_toggle, name='toggle_complete'),

    # REST API URL
    path('api/', include(router.urls)),

    # Swagger와 Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
