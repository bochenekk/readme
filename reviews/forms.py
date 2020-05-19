from django import forms

from .models import Grade, Review


class GradeForm(forms.ModelForm):
    grade = forms.IntegerField(max_value=10, min_value=1)

    class Meta:
        model = Grade
        fields = [
            'grade',
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self._fields['grade'].widget = forms.NumberInput(
    #         attrs=('min': 1, 'max': 10)
    #     )
