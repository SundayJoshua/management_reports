from django import forms
from .models import Calendar

class UploadFileForm(forms.Form):
	img = forms.ImageField()


class CalendarPlanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                }
        )
    class Meta:
        model = Calendar
        fields = '__all__'
