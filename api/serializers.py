from rest_framework import serializers
from accounts.models import CustomUserModel
from .models import UserIp, APIInfo, SponsorInfo, New, Todo, Shortcut, Alarm, FinanceCategory, Finance, Note, GetUp, Image, Quotes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['id', 'username', 'email']


class UserIpSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())


    class Meta:
        model = UserIp
        fields = '__all__'


class APIInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIInfo
        fields = '__all__'


class SponsorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorInfo
        fields = '__all__'


class NewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())

    class Meta:
        model = New
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())

    class Meta:
        model = Todo
        fields = '__all__'


class ShortcutSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())

    class Meta:
        model = Shortcut
        fields = '__all__'


class AlarmSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())

    class Meta:
        model = Alarm
        fields = '__all__'


class FinanceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceCategory
        fields = '__all__'


class FinanceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())
    categories = FinanceCategorySerializer(many=True)

    class Meta:
        model = Finance
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())

    class Meta:
        model = Note
        fields = '__all__'


class GetUpSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())

    class Meta:
        model = GetUp
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())

    class Meta:
        model = Image
        fields = '__all__'


class QuotesSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUserModel.objects.all())

    class Meta:
        model = Quotes
        fields = '__all__'
