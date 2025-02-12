from django.contrib.auth.models import User
from rest_framework import serializers

from registration.models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'last_name', 'image' )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', lookup_field='username')

    post_set = serializers.HyperlinkedRelatedField(view_name='post-detail', read_only=True, many=True)
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = (
            'url',
            'id',
            'username',
            'name',
            'last_name',
            'post_set',
            'profile'
        )

        lookup_field = 'username'
