from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import RentalPlace, Owner, Room

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_rentals = RentalPlace.objects.all().count()
    num_owners = Owner.objects.all().count()
    num_rooms = Room.objects.all().count()
    num_rooms_available = Room.objects.filter(status__exact='a').count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_rentals': num_rentals,
        'num_rooms': num_rooms,
        'num_rooms_available': num_rooms_available,
        'num_owners': num_owners,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class RentalListView(generic.ListView):
    model = RentalPlace
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(RentalListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context

class RentalDetailView(generic.DetailView):
    model = RentalPlace
    paginate_by = 10

class ReservedRoomsByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing rooms reserved by a current user."""
    model = Room
    template_name = 'catalog/room_list_reserved_user.html'
    paginate_by = 5

    def get_queryset(self):
        return (
            Room.objects.filter(client=self.request.user)
            .filter(status__exact='o')
            .order_by('due_back')
        )