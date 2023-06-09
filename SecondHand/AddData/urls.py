from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
path('shop/', views.Add_store),
path('show/', views.Show_story),
path('chain/', views.CreateChain.as_view()),
path('showchain/', views.ShowChain.as_view()),
path('showshop/', views.ShowShop.as_view()),
path('showarrival/', views.ShowArrival.as_view()),
path('showarrivalchain/<int:pk>', views.Show_Arrival_Filtred_By_Chain),
path('showarrivalstore/<int:pk>', views.Show_Arrival_Filtred_By_Shop),
path('showdiscount/', views.ShowDiscount.as_view()),
path('showdiscountretiree/', views.ShowDiscountRetiree.as_view()),
path('showdiscountdisabled/', views.ShowDiscountDisabled.as_view()),
path('showdiscountparticipant/', views.ShowDiscountParticipant.as_view()),






]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)