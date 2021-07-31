from django.shortcuts import render, HttpResponse, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import *


class TaskListView(ListView):
    """
    نمایش لیست تسک ها و جدا کردن تسک های منقضی شده از تسک های دارای مهلت انجام
    model: جدول تسک ها
    templated_name: صفحه نمایش لیست تسک ها
    """
    model = Task
    template_name = 'tasks/task_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['expired_task'] = Task.task_manager.task_is_expired()
        context['continuous_task'] = Task.objects.exclude(deadline__lt=timezone.now()) # تسک هایی که هنوز مهلت انجام دارند<---
        return context


class TaskDetailView(DetailView):
    """
    نمایش جزئیات هر تسک
    """
    model = Task
    template_name = 'tasks/task_detail.html'


class TaskDoneView(DeleteView):
    """
    اعلام اینکه تسک مورد نظر انجام شده است و حذف آن از لیست تسک ها
    """
    model = Task
    template_name = 'tasks/task_done.html'
    success_url = reverse_lazy('task_list') # جهت بازگشت به صفحه لیست تسک ها<----


class TaskDeleteView(DeleteView):
    """
    حذف تسک مورد نظر
    """
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('task_list')


class TaskCreateView(CreateView):
    """
    جهت ایجاد تسک جدید
    fields:فیلدهایی که قصد داریم در صفحه ایجاد تسک نمایش داده شوند و از طریق آنها داده دریافت شود
    """
    model = Task
    template_name = 'tasks/new_task.html'
    fields = ('title', 'description', 'category', 'priority', 'deadline')

    def form_valid(self, form):
        return super().form_valid(form)


class CategoryListView(ListView):
    """
    نمایش لیست گروه ها
    """
    model = Category
    template_name = 'tasks/category_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['full_category'] = Category.category_manager.category_with_task() # گروه های با تسک <----
        context['empty_category'] = Category.category_manager.category_no_task() # گروه های بیدون تسک <----
        return context


class RelatedTaskView(ListView):
    """
    نمایش تسک های مربوط به یک گروه
    """
    model = Task
    template_name = 'tasks/related_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['task_in_ctg'] = Task.objects.filter(category=self.kwargs['ctg_id']) # تسک هایی که متعلق به یک گروه هستند <----
        except Task.DoesNotExist:
            context['task_in_ctg'] = None
        return context

