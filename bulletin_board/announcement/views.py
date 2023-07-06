from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import ResponseFilter
from .forms import ResponseCreateForm, AnnouncementCreateForm
from .models import Announcement, Response


# Create your views here.
class AnnoList(ListView):
    model = Announcement
    ordering = '-dateCreation'
    template_name = 'announcement/announcement.html'
    context_object_name = 'announcements'
    paginate_by = 3


class AnnoDetail(DetailView):
    model = Announcement
    template_name = 'announcement/anno_detail.html'
    context_object_name = 'anno_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        replies_to_this_anno = Response.objects.filter(announcement__id=self.kwargs['pk'])
        context['replies_to_this_anno'] = replies_to_this_anno
        return context


class AnnoCreate(PermissionRequiredMixin, CreateView):
    model = Announcement
    form_class = AnnouncementCreateForm
    permission_required = ('announcement.add_announcement',)
    template_name = 'announcement/anno_create.html'
    context_object_name = 'anno_create'
    success_url = reverse_lazy('personal_area')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            resp = form.save(commit=False)
            resp.author = self.request.user
            resp.save()
            return self.form_valid(form)
        else:
            form.invalid(form)
        return redirect('personal_area')


class AnnoUpdate(PermissionRequiredMixin, UpdateView):
    model = Announcement
    form_class = AnnouncementCreateForm
    permission_required = ('announcement.change_post',)
    template_name = 'announcement/anno_create.html'
    success_url = reverse_lazy('personal_area')


class AnnoDelete(PermissionRequiredMixin, DeleteView):
    model = Announcement
    permission_required = ('announcement.delete_post',)
    template_name = 'announcement/anno_delete.html'


class ResponseList(ListView):
    model = Response
    ordering = '-dateCreation'
    template_name = 'announcement/anno_detail.html'
    context_object_name = 'responses'

    def get_queryset(self):
        return Response.objects.all()


class ResponseCreate(CreateView):
    model = Response
    form_class = ResponseCreateForm
    template_name = 'announcement/response_create.html'
    context_object_name = 'response_create'
    success_url = reverse_lazy('anno_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            resp = form.save(commit=False)
            resp.author = self.request.user
            resp.announcement_id = self.kwargs['pk']
            resp.save()
            return self.form_valid(form)
        else:
            form.invalid(form)


class ResponseUpdate(PermissionRequiredMixin, UpdateView):
    model = Response
    form_class = ResponseCreateForm
    permission_required = ('response.change_response',)
    template_name = 'announcement/response_create.html'
    context_object_name = 'response_update'
    success_url = reverse_lazy('anno_list')


class ResponseDelete(PermissionRequiredMixin, DeleteView):
    model = Response
    permission_required = ('response.delete_response',)
    template_name = 'announcement/response_delete.html'
    context_object_name = 'response_delete'
    success_url = reverse_lazy('anno_list')


class PersonalArea(ListView):
    model = Announcement
    template_name = 'announcement/personal_area.html'
    context_object_name = 'personal_area'
    filter_class = ResponseFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Announcement.objects.filter(author=self.request.user)
        self.filterset = ResponseFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


def accept_response(request, pk, id):
    response = get_object_or_404(Response, id=id)
    response.status = True
    response.save()
    return redirect('anno_detail', pk=pk)


def cancel_response(request, pk, id):
    response = get_object_or_404(Response, id=id)
    response.status = False
    response.save()
    return redirect('anno_detail', pk=pk)
