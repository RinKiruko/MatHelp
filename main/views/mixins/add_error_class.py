class AddErrorClassMixin:
    def form_invalid(self, form):
        for error in form.errors:
            form.fields[error].widget.attrs['class'] += ' is-invalid'

        return super().form_invalid(form)
