from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Contact




class ContactTests(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.data = {'fname': 'TestCase','lname':'TestCase','phone':'09123456789','home':'021456789','email':'test@case.test'}


    def test_get_contact(self):
        """
        Ensure we can get objects.
        """
        url = reverse('api:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_contact(self):
        """
        Ensure we can create a new contact object.
        """
        url = reverse('api:list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().fname, 'TestCase')

    def test_update_contact(self):
        """
        Ensure we can update a  contact object.
        """
		
        res = self.client.post(reverse('api:list'), self.data, format='json').json()
        url = reverse('api:detail',args=[res['id']])
        response = self.client.put(url , data=res, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contact.objects.get().fname, 'TestCase')


    def test_delete_contact(self):
        """
        Ensure we can delete a  contact object.
        """
		
        res = self.client.post(reverse('api:list'), self.data, format='json').json()
        url = reverse('api:detail',args=[res['id']])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)