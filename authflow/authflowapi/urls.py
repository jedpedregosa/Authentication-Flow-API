from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('signup', UserApiView.as_view()),
    path('login', UserLoginApiView.as_view()),
    path('permissions', PermissionApiView.as_view()),
    path('roles', RoleApiView.as_view()),

    re_path(r'roles/(?P<id>[-\w]+)$', RoleIdApiView.as_view()),
    re_path(r'roles/(?P<id>[-\w]+)/permissions$', RolePermissionApiView.as_view()),
    re_path(r'users/(?P<id>[-\w]+)/roles$', UserRoleApiView.as_view()),
    re_path(r'users/(?P<id>[-\w]+)/permissions$', UserPermissionApiView.as_view()),
]