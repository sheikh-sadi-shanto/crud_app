from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',crud,name='home'),
    path('o',index,name='index'),
    path('m',modal),
    path('c',home,name='crud'),
    path('<int:id>',edit,name='edit'),
    path('del<int:id>',delete,name='delete'),
    path('apk',apk,name='apk')
]+static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT) 