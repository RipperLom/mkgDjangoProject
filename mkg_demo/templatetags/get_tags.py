from django import template

register = template.Library()

# 自定义过滤器:获取余数，
@register.filter
def get_remainder(arg1, arg2):
    return int(arg1) % int(arg2)
