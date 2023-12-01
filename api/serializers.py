

import requests
from django.conf import settings
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from api.models import Bookmark, Collection, CustomUser
from api.parsers import og_parser


class RegisterCustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new custom user.
    """
    password1 = serializers.CharField(write_only=True, required=True,
                                      style={'input_type': 'password'},
                                      label='Password')
    password2 = serializers.CharField(write_only=True, required=True,
                                      style={'input_type': 'password'},
                                      label='Password repeat')

    class Meta:
        model = CustomUser
        fields = ('first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2'
                  )

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                    {'password2': "The two password fields didn't match."})
        return data

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name'],
                email=validated_data['email'],
                password=validated_data['password1']
                )
        return user


class BookmarkCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating a bookmark with Open Graph metadata extraction.

    Fields:
    - link (str): The URL of the bookmark.

    Additional Fields (auto-generated from Open Graph metadata):
    - title (str): The title of the webpage.
    - description (str): The description of the webpage.
    - link (str): The canonical URL of the webpage.
    - link_type (str): The type of the webpage (default is 'website').
    - owner (User): The user who owns the bookmark.
    - image (ImageField): The image associated with the webpage.
    """

    class Meta:
        model = Bookmark
        fields = ('link',)

    def to_internal_value(self, data):
        """
        Convert raw data to internal values.

        Parameters:
        - data (dict): Raw input data.

        Returns:
        dict: Processed data with additional Open Graph metadata.
        """
        data = super().to_internal_value(data)
        og_dict = og_parser(data['link'])
        if og_dict.get('og:image'):
            response = requests.get(og_dict['og:image'], stream=True)
            url = f"{settings.MEDIA_ROOT}/images/{response.url.split('/')[-1]}"
            with open(url, 'wb') as f:
                f.write(response.content)
                data['image'] = f"images/{response.url.split('/')[-1]}"
        data['title'] = og_dict.get('og:title', None)
        data['description'] = og_dict.get('og:description', None)
        data['link'] = og_dict.get('og:url', data['link'])
        data['link_type'] = og_dict.get('og:type', 'website')
        data['owner'] = self.context['request'].user
        return data

    def create(self, validated_data):
        return Bookmark.objects.create(**validated_data)


class BookmarkDestroySerializer(serializers.ModelSerializer):
    """
    Delete instance model.Bookmark.

    """

    class Meta:
        model = Bookmark
        fields = ('link',
                  'title',
                  )


class CollectionCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating instance model.Collection.
    """

    class Meta:
        model = Collection
        fields = ('name', 'description')

    def create(self, validated_data):
        collection = Collection.objects.create(
                owner=self.context['request'].user,
                **validated_data
                )
        return collection


class BookmarkToCollectionSerializer(serializers.ModelSerializer):
    """
    Add a bookmark to a collection.
    """

    class Meta:
        model = Bookmark
        fields = ('collections',)


class CollectionDestroySerializer(serializers.ModelSerializer):
    """
    Delete instance model.Collection.

    """

    class Meta:
        model = Collection
        fields = ('name',
                  'description',
                  )


class CollectionUpdateSerializer(serializers.ModelSerializer):
    """
    Update instance model.Collection.

    """
    name = serializers.CharField(required=False)
    description = serializers.CharField(required=False)

    class Meta:
        model = Collection
        fields = ('name',
                  'description',
                  )


class BookmarkListSerializer(serializers.ModelSerializer):
    """
    List model.Bookmark.
    """

    class Meta:
        model = Bookmark
        fields = '__all__'


class CollectionListSerializer(serializers.ModelSerializer):
    """
    List model.Collection.
    """

    detail = serializers.HyperlinkedIdentityField(
            view_name='collection_detail',
            read_only=True
            )

    class Meta:
        model = Collection
        fields = ('name',
                  'description',
                  'detail',
                  )


class CollectionDetailSerializer(serializers.ModelSerializer):
    """
    Detail instance model.Collection.
    """
    bookmarks = BookmarkListSerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ('name',
                  'description',
                  'bookmarks',
                  )


class BookmarkDetailSerializer(serializers.ModelSerializer):
    """
    Detail instance model.Collection.
    """

    class Meta:
        model = Bookmark
        fields = '__all__'
