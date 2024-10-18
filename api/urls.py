from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *
router = DefaultRouter()
router.register(r'userips', UserIpViewSet)
router.register(r'apiinfos', APIInfoViewSet)
router.register(r'sponsorinfos', SponsorInfoViewSet)
router.register(r'news', NewViewSet)
router.register(r'todos', TodoViewSet)
router.register(r'shortcuts', ShortcutViewSet)
router.register(r'alarms', AlarmViewSet)
router.register(r'financecategories', FinanceCategoryViewSet)
router.register(r'finances', FinanceViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'getups', GetUpViewSet)
router.register(r'images', ImageViewSet)
router.register(r'quotes', QuotesViewSet)


# URLs
urlpatterns = [
    path('', include(router.urls)),
]
