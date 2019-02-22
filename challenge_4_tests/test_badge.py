
import unittest
import badge

class TestCafe(unittest.TestCase):

    def test_badge_repo_add_badge_should_add(self:)
        self.badge_id = 'badge_id'
        self.door = 'door'
        self.more_doors = 'doors'
        badge.add_badge(badge_id, door, more doors)

        actual = len(badge.badges)
        expected = 1 

    def test_list_badges_should_list_badges(self:)
        actual = len(badge.get_badges())
        expected = 1
        self.assertEqual(actual, expected)