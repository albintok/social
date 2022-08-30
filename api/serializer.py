from rest_framework import serializers
from api.models import Posts

class PostSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Posts
        exclude=("date",)