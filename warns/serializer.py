from rest_framework import serializers
from warns.models import Warns

class WarnsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Warns
        fields = "__all__"