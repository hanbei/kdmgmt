from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class TestCsvExport(TestCase):

    def test_export_csv_no_data(self):
        response = self.client.get(reverse('member:csv_export'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="kader.csv"')
        self.assertEqual(response.content, b'Name, First Name, Birth date, Gender, Grade, Email, Club, Zekken, Jacket, Joined\n')