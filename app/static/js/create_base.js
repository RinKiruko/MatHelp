$("#saveAndAddAnotherButton").click(function (e) {
    this.form.action = saveAndAddAnotherUrl;
    this.form.submit();
});

$("#saveButton").click(function (e) {
    this.form.action = saveUrl;
    this.form.submit();
});