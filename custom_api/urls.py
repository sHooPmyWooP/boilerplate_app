from django.urls import path
from custom_api.views import PlainTextDetail, PlainTextList
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("plain_text/", PlainTextList.as_view(), name="plain-text-list"),
    path("plain_text/<int:pk>/", PlainTextDetail.as_view(), name="plain-text-detail"),
]

urlpatterns += format_suffix_patterns(urlpatterns)
