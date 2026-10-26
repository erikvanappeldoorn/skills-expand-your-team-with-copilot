import unittest

from src.backend.database import initial_activities


class ActivitySeedTests(unittest.TestCase):
    def test_manga_maniacs_activity_is_present(self):
        activity = initial_activities["Manga Maniacs"]

        self.assertEqual(
            activity["description"],
            "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).",
        )
        self.assertEqual(activity["schedule_details"]["days"], ["Tuesday"])
        self.assertEqual(activity["schedule_details"]["start_time"], "19:00")
        self.assertEqual(activity["schedule_details"]["end_time"], "20:30")
        self.assertEqual(activity["max_participants"], 15)
        self.assertEqual(activity["participants"], [])


if __name__ == "__main__":
    unittest.main()
