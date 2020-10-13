from django.urls import path
from .views import wszystkie_wpisy, nowy_wpis, edytuj_wpis, usun_wpis, login_request, logout_request, filtrowanie


urlpatterns = [
    path('', nowy_wpis, name='home'),
    path('wszystkie/', wszystkie_wpisy, name='wszystkie_wpisy'),
    path('eksport/', filtrowanie, name='filtrowanie'),
    path('edytuj/<int:id>/',edytuj_wpis, name='edytuj_wpis'),
    path('usun/<int:id>/', usun_wpis, name='usun_wpis'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
]