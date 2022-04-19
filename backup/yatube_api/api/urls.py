from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework import routers
from api.views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comment')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # базовые, для управления пользователями в Django:
    path('v1/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
]

# {
#     "username": "archy",
#     "password": "ass^s7ffffs67s7667dg7sfdg7sgd"
# }
# admin, 2521659
# {
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUwMTc3OTg1LCJqdGkiOiI0M2RkY2JmNzljYmU0ODQ0OWExZTg0ZWNhYTExYzMwNSIsInVzZXJfaWQiOjF9.
#                ovXM8OAkgUaf-xQbGMsZ0SJCpdGDN4cTtenbqTyU9-k"
# }

# urlpatterns = [
#     ...
#     # Djoser создаст набор необходимых эндпоинтов.
#     # базовые, для управления пользователями в Django:
#     path('auth/', include('djoser.urls')),
#     # JWT-эндпоинты, для управления JWT-токенами:
#     path('auth/', include('djoser.urls.jwt')),
# ] 


# from django.urls import include, path
# from rest_framework import routers
# from rest_framework.authtoken import views

# from api.views import CommentViewSet, GroupViewSet, PostViewSet

# router_v1 = routers.DefaultRouter()
# router_v1.register('posts', PostViewSet)
# router_v1.register('groups', GroupViewSet)
# router_v1.register(r'posts/(?P<post_id>\d+)/comments',
#                    CommentViewSet, basename='comment')

# urlpatterns = [
#     path('v1/', include(router_v1.urls)),
#     path('v1/api-token-auth/', views.obtain_auth_token),
# ]