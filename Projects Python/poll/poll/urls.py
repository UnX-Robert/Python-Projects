from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # allows referencing other URLconfs from polls
    path('polls/', include('polls.urls')),
    
    path('admin/', admin.site.urls),
]
