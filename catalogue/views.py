from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from catalogue.models import Observation, Reference
import django_tables2 as tables

class ObservationTable(tables.Table):
    class Meta:
        model = Observation

def index(request):
#    table = ObservationTable(Observation.objects.all())
#    table.paginate(paginate=False)
    return render(request, 'index.html', {'observations': Observation.objects.all(), 'references': Reference.objects.all()})

