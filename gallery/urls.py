from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from gallery.views import ColoringPageDetailView, ColoringPageListView, UserColoringPageListView
from . import views

urlpatterns = [

    path('', ColoringPageListView.as_view(), name='gallery-home'),
    path('user/<str:username>', UserColoringPageListView.as_view(), name='user-pages'),
    path('coloring/page/<int:pk>/', ColoringPageDetailView.as_view(), name='page-detail'),
    path('coloring/page/<int:pk>/download/', views.DownloadColoringPageView, name='page-download'),

]
