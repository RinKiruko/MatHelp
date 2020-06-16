from django import forms


class BaseBoostrapForm(forms.Form):
    def __init__(self, **kwargs):
        super().__init__(kwargs)

        for _, field in self.fields.items():
            field_widget = field.widget
            field_widget.attrs.update({'tabindex': 1})

            if field_widget.input_type != 'checkbox':
                field_widget.attrs.update({'class': 'form-control'})

    def _post_clean(self):
        super()._post_clean()
        for error in self.errors:
            if 'class' in self.fields[error].widget.attrs:
                self.fields[error].widget.attrs['class'] += ' is-invalid'
            else:
                self.fields[error].widget.attrs['class'] = 'is-invalid'
