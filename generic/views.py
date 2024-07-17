from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy


class CustomListView(ListView):
    paginate_by = 15
    template_name = "generics/list.html"
    filter_class = None 
    partial_template_name = None
    sidebar = None

    def get_sidebar_label(self):
        sidebar = self.sidebar
        if not sidebar:
            sidebar = self.model._meta.model_name
        return sidebar
    
    def get_filterset(self):
        if self.filter_class:
            filterset = self.filterset
        else:
            filterset = None 
        return filterset

    def get_partial_template_name(self):
        template_name = self.partial_template_name
        if not template_name:
            app_name = self.model._meta.app_label
            model_name = self.model._meta.model_name
            template_name = f"{app_name}/{model_name}_list_partial.html"
        return template_name

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.filter_class:
            self.filterset = self.filter_class(self.request.GET, queryset=queryset)
            return self.filterset.qs
        else:
            return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        model_name = self.model._meta.model_name
        context["verbose_name"] = self.model._meta.verbose_name
        context["verbose_name_plural"] = self.model._meta.verbose_name_plural
        context["sidebar"] = self.get_sidebar_label()
        context["list_url"] = f"{model_name}-list"
        context["create_url"] = f"{model_name}-create"
        context["partial_template"] = self.get_partial_template_name()
        context['total_count'] = self.model.objects.count()
        context['filterset'] = self.get_filterset()
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.htmx:
            self.template_name = context["partial_template"]
        return super().render_to_response(context, **response_kwargs)


class CustomDetailView(DetailView):
    template_name = "generics/detail.html"
    fields = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = self.fields
        context["verbose_name"] = self.object._meta.verbose_name
        return context


class CustomCreateView(CreateView):
    template_name = "generics/form.html"
    child_param = "default_param"

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(status=204, headers={'HX-Trigger': 'listChanged'})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["verbose_name"] = self.model._meta.verbose_name
        return context
    
    def get_success_url(self):
        model_name = self.model._meta.model_name
        return reverse_lazy(f'{model_name}-list')
    
    def get_initial(self):
        initial = super().get_initial()
        my_param = self.request.GET.get(self.child_param)
        if my_param:
            initial[self.child_param] = my_param
        return initial


class CustomUpdateView(UpdateView):
    template_name = "generics/form.html"

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponse(status=204, headers={'HX-Trigger': 'listChanged'})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["verbose_name"] = self.model._meta.verbose_name
        return context
    
    def get_success_url(self):
        model_name = self.model._meta.model_name
        return reverse_lazy(f'{model_name}-list')


class CustomDeleteView(DeleteView):
    template_name = "generics/confirm_delete.html"

    def form_valid(self, form):
        self.object.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'listChanged'})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = self.object._meta.verbose_name
        return context
    
    def get_success_url(self):
        model_name = self.model._meta.model_name
        return reverse_lazy(f'{model_name}-list')
