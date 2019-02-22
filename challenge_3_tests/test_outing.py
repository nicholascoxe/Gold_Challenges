
import unittest
import outing


class TestOuting(unittest.TestCase):

    def test_outing_get_outings_should_be_equal(self):
        actual = len(outing.get_outings())
        expected = 1
        self.assertEqual(actual, expected)

    
    def test_outing_add_outings_should_add(self):
        self.outing_type = 'outing_type'
        self.attending = 'attending'
        self.date = 'date'
        self.cost_per_person = 'cost_per_person'
        self.total_cost = 'total_cost'
        outing.add_outing(self.outing_type, self.attending, self.date, self.cost_per_person, self.total_cost)
        
        actual = len(outing.outings)
        expected = 1
