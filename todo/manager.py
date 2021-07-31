from django.db import models
from django.utils import timezone
from django.db.models.aggregates import Count


class TaskManager(models.Manager):
    """
    تسک هایی را که زمان سررسید آنها گذشته برمیگرداند
    """
    def task_is_expired(self):
        return super().get_queryset().filter(deadline__lte=timezone.now())


class CategoryManager(models.Manager):
    def category_no_task(self):
        """
        گروه هایی را که در آنها تسکی وجود ندارد برمیگرداند
        """
        return self.annotate(num_tasks=Count('categorise')).filter(num_tasks=0)

    def category_with_task(self):
        """
        گروه هایی را که در آنها تسکی وجود دارد برمیگرداند
        """
        return self.annotate(num_tasks=Count('categorise')).filter(num_tasks__gt=0)

    



