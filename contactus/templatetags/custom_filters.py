from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Add a CSS class to Django form fields."""
    return field.as_widget(attrs={"class": css_class})
