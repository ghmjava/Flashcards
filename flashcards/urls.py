"""mobica URL Configuration

"""
from django.conf.urls import url, include
from flashcards import views_rest, views
from rest_framework.routers import DefaultRouter
from django.views.generic.base import RedirectView
from mobica import settings

router = DefaultRouter()
router.register(r'users', views_rest.UserViewSet)
router.register(r'dictionaries', views_rest.DictionaryViewSet)
router.register(r'dictionariesw', views_rest.Dictionary2ViewSet)
router.register(r'languages', views_rest.LanguageViewSet)
router.register(r'flashcards', views_rest.FlashcardViewSet)


urlpatterns = [
    url(r'^rest/', include(router.urls)),
    url(r'^$', views.index),
    url(r'^index.*$', RedirectView.as_view(url="/" + settings.APP_NAME)),
    url(r'^settings$', views.settings),
    url(r'^startQuiz$', views.start_quiz),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^', include('django.contrib.auth.urls')),
]
