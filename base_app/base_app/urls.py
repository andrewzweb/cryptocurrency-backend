from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# api
from currency import api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('currency/', include('currency.urls', namespace='currency')),
    path('account/', include('account.urls', namespace='account')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('api/currency/', api_views.currency_list, name='api_currency_list'),
    path('api/currency/<int:pk>', api_views.currency_detail, name='api_currency_detail'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
