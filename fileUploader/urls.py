from django.conf.urls import include, url
from django.contrib import admin
from fileUploader import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'fileUploader.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'$',views.index)
]
