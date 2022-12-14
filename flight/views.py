from collections.abc import Callable
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Airport, Flight, FlightInstance
from .forms import FlightForm, FlightInstanceFilterForm, FlightInstanceForm

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_flight = Flight.objects.all().count()
    num_flight_instance = FlightInstance.objects.all().count()

    context = {
        'num_flight': num_flight,
        'num_flight_instance': num_flight_instance,
    }

    return render(request, 'index.html', context=context)

# Flight
class FlightListView(PermissionRequiredMixin, generic.ListView):
    model = Flight
    paginate_by = 50
    permission_required = 'flight.view_flight'

class FlightDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Flight
    permission_required = 'flight.view_flight'

class FlightCreate(PermissionRequiredMixin, generic.CreateView):
    model = Flight
    permission_required = 'flight.add_flight'
    form_class = FlightForm

class FlightUpdate(PermissionRequiredMixin, generic.UpdateView):
    model = Flight
    fields = ('airport', 'direction', 'time')
    # readonly_fields = ('code', )
    permission_required = 'flight.change_flight'

class FlightDelete(PermissionRequiredMixin, generic.DeleteView):
    model = Flight
    success_url = reverse_lazy('flights')
    permission_required = 'flight.delete_flight'

# FlightInstance
class FlightInstanceListView(PermissionRequiredMixin, generic.ListView):
    model = FlightInstance
    paginate_by = 50
    permission_required = 'flight.view_flightinstance'

class FlightInstanceTableList(generic.ListView):
    model = FlightInstance
    template_name = 'flight/flightinstance_table.html'

class FlightInstanceDetailView(PermissionRequiredMixin, generic.DetailView):
    model = FlightInstance
    permission_required = 'flight.view_flightinstance'

class FlightInstanceCreate(PermissionRequiredMixin, generic.CreateView):
    model = FlightInstance
    fields = '__all__'
    permission_required = 'flight.view_flightinstance'

class FlightInstanceUpdate(PermissionRequiredMixin, generic.UpdateView):
    model = FlightInstance
    form_class = FlightInstanceForm
    permission_required = 'flight.change_flightinstance'

class FlightInstanceDelete(PermissionRequiredMixin, generic.DeleteView):
    model = FlightInstance
    success_url = reverse_lazy('flights')
    permission_required = 'flightinstance.delete_flightinstance'

# Airport
class AirportListView(PermissionRequiredMixin, generic.ListView):
    model = Airport
    paginate_by = 50
    permission_required = 'airport.can_list'

class AirportDetailView(PermissionRequiredMixin, generic.DetailView):
    model = Airport
    permission_required = 'airport.can_detail'

# Report
@permission_required('flight.can_list_report')
def report_view(request):
    f = FlightInstanceFilterForm(request.GET, queryset=FlightInstance.objects.all())
    return render(request, 'flight/report_index.html', {'filter': f})