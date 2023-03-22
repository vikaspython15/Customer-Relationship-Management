from django.contrib import admin
from django.urls import path, include
from crmapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('crmapp.urls')),
    
    # App Urls define here...
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('check_user', views.check_user, name='check_user'),
    path('user_login', views.user_login, name="user_login"),
    path('user_logout', views.user_logout, name="user_logout"),
    path('manager_dashboard', views.manager_dashboard, name="manager_dashboard"),
    path('emp_dashboard', views.emp_dashboard, name="emp_dashboard"),
    path('view_profile', views.view_profile, name="view_profile"),
    path('edit_profile', views.edit_profile, name="edit_profile"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)