
class Outing:
    def __init__(self, outing_type, attending, date, cost_per_person, total_cost ):
        self.outing_type = outing_type
        self.attending = attending
        self.date = date
        self.cost_per_person = cost_per_person
        self.total_cost = total_cost
    def __repr__(self):
        return f'{self.outing_type} {self.attending} {self.date} {self.cost_per_person} {self.total_cost}'

class Outings:
    def __init__(self):
        self.outings_list = []
    
    def get_outings(self):
        return self.outings_list

    def combine_outings(self):
        pass

    """def add_outing(self, outing_type, attending, date, cost_per_person, total_cost ):
        outing = Outing( outing_type, attending, date, cost_per_person, total_cost)
        self.outings_list.append(outing)
        return self.outings_list"""


