from django.contrib import admin
from django.urls import path, include
from quote_generator import views
from portfolio import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', include('blog.urls')),
    #path('', views.index, name='index'),
    #path('about/', views.about, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
