
from django.urls import path 
from .import views
urlpatterns = [
    path("", views.index , name='index'),
    path("index-2", views.index2 , name='index-2'),
    path("contact/", views.contact , name='contact'),
    path("service", views.service , name='service'),
    path("404", views._404 , name='404'),
    path("about/", views.about , name='about'),
    path("accordion", views.accordion , name='accordion'),
    path("alert", views.alert , name='alert'),
    path("archive", views.archive , name='archive'),
    path("blog", views.blog , name='blog'),
    path("button", views.button , name='button'),
    path("comingsoon", views.comingsoon , name='comingsoon'),
    path("page-fullwidth", views.page_fullwidth , name='page-fullwidth'),
    path("page-sidebar", views.page_sidebar , name='page-sidebar'),
    path("pricing", views.pricing , name='pricing'),
    path("progress", views.progress , name='progress'),
    path("project", views.project , name='project'),
    path("service-item", views.service_item , name='service-item'),
    path("single-fullwidth", views.single_fullwidth , name='single-fullwidth'),
    path("single", views.single , name='single'),
    path("tab", views.tab , name='tab'),
    path("typography", views.typography , name='typography'),
]
