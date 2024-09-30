from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from forms.models import Form, Response

class FormsApiTest(APITestCase):
    """Test Forms API request."""

    def test_create_form(self):
        """Test create form api"""

        url = reverse('form-list')
        data = {
            "title": "Form1",
            "description": "This is a test form.",
            "fields": [
                {
                    "type": "text",
                    "name": "Name1",
                    "required": "true"
                }
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)

    def test_get_form_by_id(self):
        """Test get a form by id"""

        form = Form.objects.create(
            title="Test Form",
            description="This is a sample form.",
            fields=[
                 {
                    "type": "text",
                    "name": "Name1",
                    "required": "true"
                }
            ]
        )
        url = reverse('form-detail', kwargs={'pk': form.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(str(response.data['id']), str(form.id))

    def test_update_form(self):
        """Test update form api"""

        form = Form.objects.create(
            title="Test Form",
            description="This is a sample form.",
            fields=[
                 {
                    "type": "text",
                    "name": "Name1",
                    "required": "true"
                }
            ]
        )
        url = reverse('form-detail', kwargs={'pk': form.id})
        data = {
            "title": "Form1",
            "description": "This is a test form.",
            "fields": [
                {
                    "type": "text",
                    "name": "Name1",
                    "required": "true"
                }
            ]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Form1")

    def test_delete_form(self):
        """Test delete form api"""

        form = Form.objects.create(
            title="Test Form",
            description="This is a sample form.",
            fields=[
                 {
                    "type": "text",
                    "name": "Name1",
                    "required": "true"
                }
            ]
        )
        url = reverse('form-detail', kwargs={'pk': form.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class ResponsesApiTestSuite(APITestCase):
    """Test Form Response API."""

    def test_submit_form_response(self):
        """Test create response api"""

        form = Form.objects.create(
            title="Test Form",
            description="This is a sample form.",
            fields=[
                 {
                    "type": "text",
                    "name": "Name1",
                    "required": "true"
                }
            ]
        )
        url = reverse('response-list')
        data = {
            "form": {
                "id": str(form.id),
                "title": "Test Form",
                "description": "Test Desc"
            },
            "responses": {
                "question1": "answer1",
                "question2": "answer2"
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)

    def test_get_responses_by_form_id(self):
        """Test get a response by id api"""

        form = Form.objects.create(
            title="Test Form",
            description="This is a sample form.",
            fields=[
                 {
                    "type": "text",
                    "name": "Name1",
                    "required": "true"
                }
            ]
        )
        Response.objects.create(
            form=form.id,
            responses={
                "field_one": "Test Field",
                "field_two": "Test Two"
            }
        )
        url = f"{reverse('response-list')}?form_id={form.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

