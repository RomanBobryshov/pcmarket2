
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('account/', include('account.urls')),
    path('cart/', include('cart.urls')),
    path('', include('products.urls')),
    path('admin/', admin.site.urls),
]
