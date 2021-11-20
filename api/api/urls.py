from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import SpectacularJSONAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularYAMLAPIView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path("docs/yaml/", SpectacularYAMLAPIView.as_view(), name="swagger-yaml"),
    # Open API Document UI로 조회: Swagger, Redoc
    path("docs/swagger/", SpectacularSwaggerView.as_view(url_name="schema-json"), name="swagger-ui", ),
    path("docs/redoc/", SpectacularRedocView.as_view(url_name="schema-json"), name="redoc", ),
]