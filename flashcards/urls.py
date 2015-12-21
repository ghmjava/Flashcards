"""mobica URL Configuration

"""
from django.conf.urls import url, include
from flashcards import views_rest
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views_rest.UserViewSet)
router.register(r'dictionaries', views_rest.DictionaryViewSet)
router.register(r'languages', views_rest.LanguageViewSet)
router.register(r'flashcards', views_rest.FlashcardViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
