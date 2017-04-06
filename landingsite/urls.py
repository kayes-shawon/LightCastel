import patterns as patterns
from django.conf.urls import url
from django.conf.urls.static import static


from LightCastleWebsite import settings
from landingsite import views

urlpatterns = [

    url(r'^$', views.index_view),
    url(r'^about', views.about_view),
    url(r'^in-the-media', views.media_view),
    url(r'^case-studies/([0-9])', views.case_studies_expanded_view),
    url(r'^case-studies-json/([0-9])', views.case_studies_details_json),
    url(r'^case-studies', views.case_studies_view),
    url(r'^subscribe', views.subscribe_newsletter),
    url(r'^request-callback', views.request_callback),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)