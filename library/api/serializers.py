from rest_framework import serializers
from library.models import Lidrary, Rent, Book


class LidrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Lidrary
        fields = '__all__'


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    library = LidrarySerializer(many=False)
    # rented_book = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name=''
    # )

    class Meta:
        model=Book
        # fields = ['name','is_rent']
        fields = '__all__'