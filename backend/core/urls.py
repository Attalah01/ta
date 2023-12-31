"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.social.urls")),
    path("api/users/wallet/", include("apps.user_wallet.urls")),
    path("api/category/", include("apps.category.urls")),
    path("api/courses/", include("apps.courses.urls")),
    path("api/coupons/", include("apps.coupons.urls")),
    path("api/cart/", include("apps.cart.urls")),
    path("api/payments/", include("apps.payments.urls")),
    path("api/orders/", include("apps.orders.urls")),
    path("api/reviews/", include("apps.reviews.urls")),
    path("api/tiers/", include("apps.tiers.urls")),
    path("api/contacts/", include("apps.contacts.urls")),
    path("api/blog/", include("apps.blog.urls")),
    path("api/newsletter/", include("apps.newsletter.urls")),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
