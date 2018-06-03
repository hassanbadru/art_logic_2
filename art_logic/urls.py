"""art_logic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# from django.contrib import admin



# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^', include('art_logic_app.urls'))
# ]
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.urls import path, re_path
# from django.views.generic import TemplateView

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  # path('api/', include('mynewapp.urls')),
  url(r'^', include('art_logic_app.urls'))
  # url(r'^', TemplateView.as_view(template_name='index.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)