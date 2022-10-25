from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView
from .views import PartnerUpdate, RegisterAccount, LoginAccount, APICategoryViewSet, APIShopViewSet, ProductInfoView, \
    BasketView, \
    AccountDetails, OrderView, PartnerState, PartnerOrders, ConfirmAccount, ContactView


app_name = 'backend'

router = DefaultRouter()
router.register('categories', APICategoryViewSet)
router.register('shops', APIShopViewSet)

urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/register', RegisterAccount.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset', PasswordResetView.as_view(), name='password-reset'),
    path('user/password_reset/confirm', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('products', ProductInfoView.as_view(), name='products'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', include(router.urls))
]
