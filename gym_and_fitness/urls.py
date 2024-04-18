from django.contrib import admin
from django.urls import path, include


from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Gym & Fitness Admin"
admin.site.site_title = "Gym & Fitness Admin Portal"
admin.site.index_title = "Welcome to Gym & Fitness Admin Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls"))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
