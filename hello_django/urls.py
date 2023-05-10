from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from upload.views import image_upload
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("upload/", image_upload, name="upload"),
    path("admin/", admin.site.urls),
    re_path("", TemplateView.as_view(template_name="index.html"), name=""),
    # re_path(r"^.*$", TemplateView.as_view(template_name="index.html")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
