from rest_framework import generics

from .serializers import CoachSerializer
from .models import Coach


class CoachView(generics.ListAPIView):
    """コーチ一覧API

    https://tracery.jp/s/3b41ac0d4d334a2d9a2a68eba29d1f86
    """
    serializer_class = CoachSerializer

    def get_queryset(self):
        return Coach.objects.all().order_by("-review_point")
