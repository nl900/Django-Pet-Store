from django.test import TestCase
from django.urls import reverse

from catalog.models import Breeder

class BreederListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_breeders = 3

        for breeder_id in range(number_of_breeders):
            Breeder.objects.create(
                name=f'Cats Forever Ltd {breeder_id}',
                address=f'Newman St, Pleasantville {breeder_id}',
            )
           
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/breeders/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('breeders'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('breeders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/breeder_list.html')
        
