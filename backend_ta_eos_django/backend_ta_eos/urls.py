from django.contrib import admin
from django.urls import path

import calculations.views as calculations_views
import users.views as users_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users/", users_views.UserCreateView.as_view()),
    path("api/v1/users/login/", users_views.LoginView.as_view()),
    path("api/v1/users/logout/", users_views.LogoutView.as_view()),
    path(
        "api/v1/calculations/direct_code/left_shift/",
        calculations_views.DirectCodeLeftShiftCalculation.as_view(),
    ),
    path(
        "api/v1/calculations/direct_code/right_shift/",
        calculations_views.DirectCodeRightShiftCalculation.as_view(),
    ),
]
