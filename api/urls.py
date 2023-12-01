""" api.urls """

from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from api.views import (BookmarkCreateView,
                       BookmarkDestroyView,
                       BookmarkDetailView,
                       BookmarkListView,
                       BookmarkToCollectionView,
                       CollectionCreateView,
                       CollectionDestroyView,
                       CollectionDetailView,
                       CollectionListView,
                       CollectionUpdateView,
                       Logout, RegisterCustomUserView,

                       )

urlpatterns = [
    path('register/',
         RegisterCustomUserView.as_view(),
         name='register'
         ),
    path('bookmark-create/',
         BookmarkCreateView.as_view()
         ),
    path('bookmark-delete/<int:pk>/',
         BookmarkDestroyView.as_view()
         ),
    path('collection-create/',
         CollectionCreateView.as_view()
         ),
    path('bookmark-to-collection/<int:pk>/',
         BookmarkToCollectionView.as_view()
         ),
    path('collection-delete/<int:pk>/',
         CollectionDestroyView.as_view()
         ),
    path('collection-update/<int:pk>/',
         CollectionUpdateView.as_view()
         ),
    path('collection/',
         CollectionListView.as_view()
         ),
    path('collection-detail/<int:pk>/',
         CollectionDetailView.as_view(),
         name='collection_detail'
         ),
    path('bookmark/',
         BookmarkListView.as_view()
         ),
    path('bookmark-detail/<int:pk>/',
         BookmarkDetailView.as_view()
         ),
    path('logout/', Logout.as_view()),
    ]
