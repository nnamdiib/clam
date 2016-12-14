from django import forms


from studentable.models import Course

MAX = 15

class CourseCodesForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(CourseCodesForm, self).__init__(*args, **kwargs)
		for i in range(MAX):
			self.fields["code %d"%i] = forms.CharField(label="Course code:")
			self.fields["code %d"%i].required = False
	