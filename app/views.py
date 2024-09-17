from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from app.models import Team, Pro


class IndexView(ListView):
    template_name = 'index.html'
    model = Team
    context_object_name = 'teams'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Pro.objects.all()
        return context
class AboutView(ListView):
    template_name = 'about.html'
    model = Team
    context_object_name = 'teams'

class ServiceView(TemplateView):
    template_name = 'service.html'
    model = Pro
    context_object_name = 'comment'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Pro.objects.all()
        return context

class FeatureView(TemplateView):
    template_name = 'feature.html'

class TeamView(ListView):
    template_name = 'team.html'
    model = Team
    context_object_name = 'teams'

class AppointmentView(TemplateView):
    template_name = 'appointment.html'

class TestimonialView(TemplateView):
    template_name = 'testimonial.html'
    model = Pro
    context_object_name = 'comment'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Pro.objects.all()
        return context
class PageView(TemplateView):
    template_name = '404.html'


class ContactView(TemplateView):
    template_name = 'contact.html'



