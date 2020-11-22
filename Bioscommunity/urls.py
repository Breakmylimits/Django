
from django.contrib import admin
from django.urls import path ,include
from django.contrib.auth import views as auth_views #  as เป็นการตั้งชื่อเล่น 
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('school.urls')),
    path('login/', auth_views.LoginView.as_view(template_name = 'school/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'school/logout.html'),name='logout')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)