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
    url(r'^addUser', 'TaskMan.views.addUser', name='addUser'),
    url(r'^create', 'TaskMan.views.create', name='create'),
    url(r'^taskview', 'TaskMan.views.taskview', name='taskview'),
    url(r'^logout', 'TaskMan.views.logout', name='logout'),
    url(r'^addTask', 'TaskMan.views.addTask', name='addTask'),
    url(r'^showtask', 'TaskMan.views.showTask', name='showTask'),
    #url(r'^login', 'views.login', name='login'),
    #url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^account/', include('email_login.urls')),
)
