from django import forms
from .models import ReportField


class DailyReportForm(forms.ModelForm):

	class Meta:
		model = ReportField
		fields = ('calls', 'meetings', 'contracts', 'prepayment', 'standart_shop', )
