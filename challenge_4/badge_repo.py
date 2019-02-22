
import badge

badges = {'Jj': 'A1', 'Bk': 'A1, A2, A3', 'Ok': 'A2'}

def add_badge(badge_id, doors, more_doors):
	b = badge.Badge(badge_id, doors, more_doors)
	badges.__repr__(b)

def update_badge():#TODO
	pass


def get_badges():
	return badges

	