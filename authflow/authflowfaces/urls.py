from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', UserView.as_view(), name='sign_up'),
    path('signup', UserView.as_view(), name='sign_up'),
    path('login', UserLoginView.as_view(), name='sign_in'),
    path('permissions', PermissionView.as_view(), name='permission_fetch'),
    path('roles', RoleView.as_view(), name='role_fetch'),

    re_path(r'roles/(?P<id>[-\w]+)/permissions$', RolePermissionView.as_view(), name='role_permission_fetch'),
]