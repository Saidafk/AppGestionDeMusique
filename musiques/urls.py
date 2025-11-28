from django.urls import path, include
from musiques.views import MorceauDetailView, MorceauList, MorceauCreateView, MorceauUpdateView, MorceauDeleteView, ArtisteListView, ArtisteDeleteView, ArtisteCreateView, ArtisteUpdateView, ArtisteDetailView, frencky_vincent_view
from rest_framework import routers
from musiques.api_views import ArtisteViewSet, MorceauViewSet
router = routers.DefaultRouter()
router.register(r'morceaux', MorceauViewSet)
router.register(r'artistes', ArtisteViewSet)

app_name = 'musiques'
urlpatterns = [
    path('frencky/', frencky_vincent_view, name='frencky-vincent'),

    path('<int:pk>/', MorceauDetailView.as_view(), name='morceau-detail'),
    path('', MorceauList.as_view(), name='morceau-list'),
    path('create/', MorceauCreateView.as_view(), name='morceau-create'),
    path('<int:pk>/update/', MorceauUpdateView.as_view(), name='morceau-update'),
    path('<int:pk>/delete/', MorceauDeleteView.as_view(), name='morceau-delete'),

    path('artistes/', ArtisteListView.as_view(), name='artiste-list'),
    path('artistes/create/', ArtisteCreateView.as_view(), name='artiste-create'),
    path('artistes/<int:pk>/modifier/', ArtisteUpdateView.as_view(), name='artiste-update'),
    path('artistes/<int:pk>/', ArtisteDetailView.as_view(), name='artiste-detail'),
    path('artistes/<int:pk>/delete/', ArtisteDeleteView.as_view(), name='artiste-delete'),
    path('api/', include((router.urls, 'api'), namespace='api')),
]
