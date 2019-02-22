
import outing_repository


outings = []


def get_outings():
	return outings


def add_outing(outing_type, attending, date, cost_per_person, total_cost):
	o = outing_repository.Outing(outing_type, attending, date, cost_per_person, total_cost)
	outings.append(o)


def calc_outings():
		'''o = outing_repository.Outing(total_cost):'''
	#ADD COSTS OF OUTINGS
def calcbytype_outings():
	pass

