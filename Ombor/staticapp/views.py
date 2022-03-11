from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .models import Stats
from .serializers import StatsSerializer


class StatsAPIView(ListCreateAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["client",'product']



class StatsRUD(RetrieveUpdateDestroyAPIView):
    queryset = Stats.objects.all()
    serializer_class = StatsSerializer