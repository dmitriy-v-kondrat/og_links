from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Bookmark, Collection, CustomUser

from api.serializers import (BookmarkDestroySerializer,
                             BookmarkCreateSerializer,
                             CollectionDestroySerializer,
                             CollectionUpdateSerializer,
                             RegisterCustomUserSerializer,
                             CollectionCreateSerializer,
                             BookmarkToCollectionSerializer,
                             CollectionListSerializer,
                             CollectionDetailSerializer,
                             BookmarkListSerializer,
                             BookmarkDetailSerializer,
                             )


class RegisterCustomUserView(generics.CreateAPIView):
    """ Register customuser. """
    queryset = CustomUser.objects.all()
    serializer_class = RegisterCustomUserSerializer


class BookmarkCreateView(generics.CreateAPIView):
    """ Bookmark create. """
    permission_classes = [IsAuthenticated]
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkCreateSerializer


class BookmarkDestroyView(generics.DestroyAPIView):
    """ Bookmark destroy. """
    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkDestroySerializer

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class CollectionCreateView(generics.CreateAPIView):
    """ Collection create. """
    permission_classes = [IsAuthenticated]
    queryset = Collection.objects.all()
    serializer_class = CollectionCreateSerializer


class BookmarkToCollectionView(generics.UpdateAPIView):
    """ Add bookmark instance to collection. """
    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkToCollectionSerializer

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class CollectionDestroyView(generics.DestroyAPIView):
    """ Collection destroy. """
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionDestroySerializer

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)


class CollectionUpdateView(generics.UpdateAPIView):
    """ Collection update. """
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionUpdateSerializer

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)


class CollectionListView(generics.ListAPIView):
    """ Collection list. """
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionListSerializer

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)


class CollectionDetailView(generics.RetrieveAPIView):
    """ Collection detail. """
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionDetailSerializer

    def get_queryset(self):
        return Collection.objects.filter(owner=self.request.user)


class BookmarkListView(generics.ListAPIView):
    """ Bookmark list. """
    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkListSerializer

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkDetailView(generics.RetrieveAPIView):
    """ Bookmark detail. """
    permission_classes = [IsAuthenticated]
    serializer_class = BookmarkDetailSerializer

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class Logout(APIView):
    """ Users logout. """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': "Logout successful"})
