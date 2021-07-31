from django.urls import path
from .views import *


urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'), # لیست تسک ها <----
    path('category/', CategoryListView.as_view(), name='category_list'), # لیست گرو ها <----
    path(r'^category/(?P<ctg_id>[0-9]+)/$', RelatedTaskView.as_view(), name='related_task'), # تسک هایی که در یک گروه قرار دارند <---
    path('<int:pk>/', TaskDetailView.as_view(), name='task_detail'), # جزئیات هر تسک <----
    path('<int:pk>/done/', TaskDoneView.as_view(), name='task_done'), # اعلام به اتمام رساندن تسک <----
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),# حذف تسک <----
    path('new/', TaskCreateView.as_view(), name='new_task'), # ایجاد تسک جدید <----
]