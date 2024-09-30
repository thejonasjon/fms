from django.test import TestCase
from forms.models import Form, Field, Response

class FormModelTest(TestCase):
    """Test Forms model."""

    def setUp(self):
        # Setup a form instance with fields.
        self.field1 = Field(name="Test Field 1", type="text")
        self.field2 = Field(name="Test Field 2", type="checkbox")
        self.form = Form(
            title="Test Form",
            description="Form Description",
            fields=[self.field1, self.field2]
        )
        self.form.save()

    def test_form_creation(self):
        """Test creating a form is successful."""

        form = Form.objects.filter(title="Test Form").first()
        self.assertEqual(form.title, "Test Form")
        self.assertEqual(form.description, "Form Description")
        self.assertEqual(len(form.fields), 2)
        self.assertEqual(form.fields[0].name, "Test Field 1")

    def test_form_fields_uniqueness(self):
        duplicate_field = Field(name="Test Field 1", type="text")
        with self.assertRaises(Exception):
            Form.objects.create(
                title="Duplicate Test",
                description="Duplicate Form",
                field=[duplicate_field]
            )

class ResponseModelTest(TestCase):
    """Test Repsonse model."""

    def setUp(self):
        # Create a form instance.
        self.field = Field(name="Name", type="text")
        self.form = Form(
            title="Test Response Form",
            description="Form for testing responses",
            fields=[self.field]
        )
        self.form.save()

        # Create a response for that form.
        self.response = Response(
            form=self.form,
            responses={"name": "Test Response"}
        )
        self.response.save()

    def test_response_creation(self):
        """Test creating a response is successful."""

        response = Response.objects.get(form=self.form)
        self.assertEqual(response.responses["name"], "Test Response")
        self.assertEqual(response.form.title, "Test Response Form")
