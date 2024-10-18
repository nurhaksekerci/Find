from .models import UserIp, APIInfo, SponsorInfo, New, Todo, Shortcut, Alarm, FinanceCategory, Finance, Note, GetUp, Image, Quotes
from .serializers import *
from rest_framework import viewsets
from .models import UserIp


class UserIpViewSet(viewsets.ModelViewSet):
    queryset = UserIp.objects.all()
    serializer_class = UserIpSerializer


class APIInfoViewSet(viewsets.ModelViewSet):
    queryset = APIInfo.objects.all()
    serializer_class = APIInfoSerializer


class SponsorInfoViewSet(viewsets.ModelViewSet):
    queryset = SponsorInfo.objects.all()
    serializer_class = SponsorInfoSerializer


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class ShortcutViewSet(viewsets.ModelViewSet):
    queryset = Shortcut.objects.all()
    serializer_class = ShortcutSerializer


class AlarmViewSet(viewsets.ModelViewSet):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer


class FinanceCategoryViewSet(viewsets.ModelViewSet):
    queryset = FinanceCategory.objects.all()
    serializer_class = FinanceCategorySerializer


class FinanceViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class GetUpViewSet(viewsets.ModelViewSet):
    queryset = GetUp.objects.all()
    serializer_class = GetUpSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class QuotesViewSet(viewsets.ModelViewSet):
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer