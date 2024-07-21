from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('books.urls')),
    path('admin/', admin.site.urls),
    path('', auth_view.LoginView.as_view(redirect_authenticated_user=True)),
    path('auth/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
