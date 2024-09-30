from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from forms.models import Form

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