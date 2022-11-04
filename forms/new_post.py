from wtforms import Form, StringField, DateTimeField, SubmitField, validators


class CreationForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=100)])
    content = StringField('Content', [validators.Length(min=1)])
    publish_date = DateTimeField('PublishDate')
    author = StringField('Author', [validators.Length(min=1, max=40)])
    submit = SubmitField('Create')
