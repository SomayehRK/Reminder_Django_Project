from django import template
from todo.models import *
from datetime import datetime
from django.utils.timesince import timeuntil

register = template.Library()


@register.simple_tag
def remaining_time(time):
    return timeuntil(time)


@register.filter
def up_first_letter(word):
    return word.title()
