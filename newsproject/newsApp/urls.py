from newsApp.views import add_category, add_post,  home,base,health,bussiness,politacal,football,world_news,update,delete,c_contact,dis_contact,userreg,login,logout
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',home,name='home' ),
    path('base/',base,name='base' ),
    path('categories/add/', add_category, name='category_add'),
    
    path('posts/add/', add_post, name='post_add'),
    path('health', health, name='health'),
    path('bussiness', bussiness, name='bussiness'),
    path('politacal', politacal, name='politacal'),
    path('football', football, name='football'),
    path('world-news', world_news, name='world-news'),
    path('update/<int:pk>',update, name='yupdate'),
    path('delete/<int:pk>',delete, name='udelete'),
    path('dis_contact',dis_contact, name='dis_contact'),
    path('contact/', c_contact, name='contact'),
    path('userreg', userreg, name='userreg'),
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

