from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Gym, Member
from django.shortcuts import render

# Create your views here.
class GymListView(ListView):
    model = Gym
    template_name = 'gym_list.html'
    context_object_name = 'all_gyms_list'

class GymDetailView(DetailView):
    model = Gym
    template_name = 'gym_detail.html'

class GymCreateView(CreateView):
    model = Gym
    template_name = 'gym_create.html'
    fields = ['name', 'location']

class GymUpdateView(UpdateView):
    model = Gym
    template_name = 'gym_edit.html'
    fields = ['location']

class GymEquipListView(ListView):
    model = Gym
    template_name = 'gym_equip_list.html'
    context_object_name = 'all_gyms_list'

def query1(request):
    try:
        member = Member.objects.earliest('dob')
    except Member.DoesNotExist:
        raise Http404("Member does not exist")
    return render(request, 'query1.html', {'name': member.name})

def query2(request):
    try:
        num = Member.objects.all().count()
    except Member.DoesNotExist:
        raise Http404("Member does not exist")
    return render(request, 'query2.html', {'number': num})