from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path(
        "api/",
        include(
            [
                path("v100/", include("users.urls.v100")),
                path("v110/", include("users.urls.v110")),
            ]
        ),
        name="api",
    ),
]
