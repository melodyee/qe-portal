from django import forms
from django.contrib.admin import widgets
#from django.forms.extras import widgets

from automation.models import CaseModel
from automation.models import SuiteModel
from automation.models import SchedulerModel

from markdownx.fields import MarkdownxFormField
from automation.models import RequirementModel


class CaseForm(forms.ModelForm):
    class Meta:
        model = CaseModel
        fields = '__all__'
        #fields = [ ]
        #exclude = [ ]
       #labels = { }
        #help_texts = { }
        #error_messages = { }

from django.forms.widgets import CheckboxSelectMultiple

class SuiteForm(forms.ModelForm):
    class Meta:
        model = SuiteModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SuiteForm, self).__init__(*args, **kwargs)

        self.fields["cases"].widget = CheckboxSelectMultiple()
        self.fields["cases"].queryset = CaseModel.objects.all()


class SchedulerForm(forms.ModelForm):
    # appoint_at = forms.TimeField(widget=widgets.AdminTimeWidget())
    # start_day = forms.DateField(widget=widgets.AdminSplitDateTime())
    # end_day = forms.DateField(widget=widgets.AdminDateWidget())

    # start_day = forms.DateField(widget=widgets.SelectDateWidget())
    # end_day = forms.DateField(widget=widgets.SelectDateWidget())

    def __init__(self, *args, **kwargs):
        super(SchedulerForm, self).__init__(*args, **kwargs)
        self.fields['start_day'].widget = widgets.AdminDateWidget()
        self.fields['end_day'].widget = widgets.AdminDateWidget()
        self.fields['appoint_at'].widget = widgets.AdminTimeWidget()

    class Meta:
        model = SchedulerModel
        #fields = '__all__'
        exclude = ['create_time', ]

        # widgets = {
        #    'start_time': DateInput(attrs={'class': 'datepicker'}),
        #    'end_time': DateInput(attrs={'class': 'datepicker'}),
        #}

        #widgets = {
        #    'start_time': widgets.AdminDateWidget(),
        #    'end_time': widgets.AdminDateWidget(),
        #}


class RequirementForm(forms.Form):
        ReqField = MarkdownxFormField()


