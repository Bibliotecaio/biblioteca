from django import forms
from django.utils.safestring import mark_safe
from django.utils.html import escape


class ReadonlyInput(forms.Widget):
    def __init__(self, value, attrs=None):
        self.value = value
        super(ReadonlyInput, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if self.value:
            return mark_safe(u'<p>%s</p>' % escape(self.value))
        else:
            return ''
