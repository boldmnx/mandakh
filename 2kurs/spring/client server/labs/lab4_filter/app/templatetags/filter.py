from django import template
from datetime import datetime


register = template.Library()


@register.filter()
def tom(value):
    return value.upper()


@register.filter()
def jijig(value):
    return value.lower()


@register.filter(name='a')
def ognooTaoDate(value):

    date_object = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
    given_datetime = datetime(date_object.year, date_object.month, date_object.day,
                              date_object.hour, date_object.minute, date_object.second)

    current_datetime = datetime.now()

    # зөрүү
    time_difference = current_datetime - given_datetime

    # Цагийн зөрүүнээс жил, сар, өдөр, цаг, минут, секундийг гаргав
    years = time_difference.days // 365
    months = (time_difference.days % 365) // 30
    days = (time_difference.days % 365) % 30
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    result = ''
    if years > 0:
        result += f'{years} жил'
    if months > 0:
        result += f' {months} сар'
    if days > 0:
        result += f' {days} өдөр'
    if hours > 0:
        result += f' {hours} цаг'
    if minutes > 0:
        result += f' {minutes} минутын'
    result += ' өмнө'
    return result
