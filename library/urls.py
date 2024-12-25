from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, MemberViewSet, LoanViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'loans', LoanViewSet)

urlpatterns = router.urls
