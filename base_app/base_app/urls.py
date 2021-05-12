from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# api currency
from currency import api_views as currency_api
from dashboard import api_views as dashboard_api

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

from account.api_views import current_user, UserList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),

    # page create default tools django
    path('currency/', include('currency.urls', namespace='currency')),
    path('account/', include('account.urls', namespace='account')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),

    # api currency
    path('api/currency/redoc', schema_view),
    path('api/currency/', currency_api.currency_list, name='api_currency_list'),
    path('api/currency/<int:pk>', currency_api.currency_detail, name='api_currency_detail'),

    # api dashboard
    path('api/dashboard/', dashboard_api.dashboard_list, name='api_dashboard_list'),
    
    # api user
    path('api/current_user/', current_user),
    path('api/users/', UserList.as_view())
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
