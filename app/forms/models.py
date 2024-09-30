from mongoengine import EmbeddedDocument, Document, fields, DateTimeField, CASCADE
from datetime import datetime


class Field(EmbeddedDocument):
    """Field Model"""

    FIELD_TYPES = (
        ('text', 'Text'),
        ('date', 'Date'),
        ('boolean', 'Boolean'),
        ('checkbox', 'Checkbox'),
        ('dropdown', 'Dropdown'),
        ('attachment', 'Attachment'),
        ('others', 'Others'),
    )

    name = fields.StringField(max_length=200, required=True) # remove uniquess validation for now, will check back
    type = fields.StringField(choices=FIELD_TYPES, required=True)
    required = fields.BooleanField(default=True)
    created_at = fields.DateTimeField(default=datetime.utcnow)
    updated_at = fields.DateTimeField(default=datetime.utcnow)

class Form(Document):
    """Form Model"""

    title = fields.StringField(max_length=200, required=True)
    description = fields.StringField()
    fields = fields.EmbeddedDocumentListField(Field)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    meta = {
        'ordering': ['-created_at']
    }

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(Form, self).save(*args, **kwargs)


class Response(Document):
    """Response Model"""

    form = fields.ReferenceField(Form, reverse_delete_rule=CASCADE)
    responses = fields.DictField()
    created_at = fields.DateTimeField(default=datetime.utcnow)
    updated_at = fields.DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(Response, self).save(*args, **kwargs)
