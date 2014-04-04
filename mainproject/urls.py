from django.conf.urls import patterns, include, url

from django.contrib import admin
import TaskMan
admin.autodiscover()
# Insert email_login overrides
#from email_login import useradmin, adminsite
#site = adminsite.EmailLoginAdminSite()
## duplicate the normal admin's registry until ticket #8500 get's fixed
#site._registry = admin.site._registry

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'TaskMan.views.index', name='index'),
    url(r'^register', 'TaskMan.views.register', name='register'),
    url(r'^add', 'TaskMan.views.addUser', name='addUser'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^account/', include('email_login.urls')),
)
