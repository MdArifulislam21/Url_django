from django import forms

from .validators import validate_url, validate_dot_com



class SubmitUrlForm(forms.Form):
	url = forms.CharField(
		label='Submit URL',
		validators= [validate_url],
		widget  = forms.TextInput(
				attrs = {"placeholder": "long url",
				'class': 'form-control'
			}
		)
	)

	# def clean(self):
	# 	cleaned_data =super(SubmitUrlForm, self).clean()
	# 	url = cleaned_data.get('url')
	# 	url_validator = URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError('Invalid URL')
	# 	return url


	# def clean_url(self):
	# 	url = self.cleaned_data['url']
	# 	if 'http' in url:
	# 		return url
	# 	else:
	# 		'http://' + url
	# 