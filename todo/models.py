from django.db import models
from django.urls import reverse
from django.utils import timezone
from .manager import *


class Category(models.Model):
    """
    name: نام گروه
    object:منیجر اصلی مدل
    category_manager:منیجیری که گروه های شامل تسک و بدون تسک را برمگیرداند
    """
    name = models.CharField(max_length=20)
    objects = models.Manager()
    category_manager = CategoryManager()

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    title:عنوان تسک
    description:توضیحات مربوط به تسک
    category:گروهی که تسک مربوط به آن است
    priority:میزان اهمیت تسک
    created_at:زمان ایجاد تسک در دیتابیس
    deadline:زمان سررسید تسک
    object:منیجر اصلی مدل
    task_manager:منیجری که تسکهای منقضی شده را برمیگرداند
    """

    PRIORITY = [
        (0, 'unimportant'),
        (1, 'important'),
        (3, 'urgent'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categorise', null=True)
    priority = models.IntegerField(choices=PRIORITY, default=4)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    objects = models.Manager()
    task_manager = TaskManager()

    class Meta:
        """
        تسکها را براساس زمان ایجاد آنها بصورت نزولی مرتب میکند
        """
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])