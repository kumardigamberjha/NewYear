from django.forms import ModelForm
from red.models import FormModel, SaveImage


class FormForm(ModelForm):
    class Meta:
        model = FormModel
        fields = "__all__"


class SaveImageForm(ModelForm):
    class Meta:
        model = SaveImage
        fields = "__all__"
