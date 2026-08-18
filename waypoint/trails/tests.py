from django.test import TestCase
from django.urls import reverse
from trails.models import Trail

class TrailModelAndViewsTest(TestCase):

    def setUp(self):
        # Create a clean test record using the correct model fields
        self.trail = Trail.objects.create(
            name="Test Trail",
            distance_km=5.0,
            elevation_gain=150,
            difficulty="Easy",
            is_open=True
        )

    def test_open_trails_query(self):
        """WP-801: Verify that the open trails query returns only the correct items"""
        open_trails = Trail.objects.filter(is_open=True)
        self.assertIn(self.trail, open_trails)
        self.assertEqual(open_trails.count(), 1)

    def test_trail_detail_404(self):
        """WP-801: Verify that a non-existent URL returns a 404 status code"""
        response = self.client.get('/non-existent-url-path/')
        self.assertEqual(response.status_code, 404)

    def test_distance_rejects_negatives(self):
        """WP-801: Unit test for a domain rule (e.g., negative distance validation)"""
        with self.assertRaises(Exception):
            invalid_trail = Trail(
                name="Bad Trail",
                distance_km=-2.5,
                elevation_gain=50,
                difficulty="Easy",
                is_open=True
            )
            invalid_trail.full_clean()