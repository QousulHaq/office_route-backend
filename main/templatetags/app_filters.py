# your_app/templatetags/currency_filters.py
from django import template

register = template.Library()

@register.filter
def currency_format(value):
    try:
        value = int(value)
        return f"{value:,}".replace(",", ".")
    except (ValueError, TypeError):
        return value
    
@register.filter
def star_rating(value):
    try:
        value = int(value)
        return "★" * value  # Menampilkan bintang sebanyak nilai rating
    except (ValueError, TypeError):
        return ""