import django_filters as filters
from ..models import MeterBoard



#implement metersearch  based name or number
class MeterBoardFilterSet(filters.FilterSet):
    class Meta:
        model = MeterBoard
        fields = ["board_name","board_number"]

