from django.test import TestCase

from catalog.models import Breeder

class BreederModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Breeder.objects.create(name='Good Doggies', address='33 Hilbilly, Pleasantville 6754')

    def test_name_max_length(self):
        breeder = Breeder.objects.get(id=1)
        max_length = breeder._meta.get_field('name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_name(self):
        breeder = Breeder.objects.get(id=1)
        expected_object_name = breeder.name
        self.assertEquals(expected_object_name, str(breeder))

    def test_get_absolute_url(self):
        breeder = Breeder.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(breeder.get_absolute_url(), '/catalog/breeder/1')
