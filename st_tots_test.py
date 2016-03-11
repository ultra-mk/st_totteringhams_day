import unittest
import st_tots

class ST_TOTSTESTS(unittest.TestCase):
	@classmethod
	def setUpClass(ST_TOTSTESTS):
		ST_TOTSTESTS.points_per_win = 3
		ST_TOTSTESTS.games_per_season = 38
		ST_TOTSTESTS.max_points = ST_TOTSTESTS.games_per_season * ST_TOTSTESTS.points_per_win
		ST_TOTSTESTS.soup = st_tots.Soup('http://www.premierleague.com/en-gb/matchday/league-table.html').page
		ST_TOTSTESTS.arsenal = st_tots.Team('Arsenal', ST_TOTSTESTS.soup)
		ST_TOTSTESTS.spurs = st_tots.Team('Tottenham Hotspur', ST_TOTSTESTS.soup)

	def test_init_Soup(self):
		class_name = str(type(ST_TOTSTESTS.soup))
		self.assertEqual("<class 'bs4.BeautifulSoup'>", class_name)

	def test_Team__init__games_played(self):
		self.assertTrue(0 < ST_TOTSTESTS.arsenal.games_played < ST_TOTSTESTS.games_per_season)


	def test_Team__init__team_points(self):
		self.assertTrue(0 < ST_TOTSTESTS.arsenal.points < ST_TOTSTESTS.max_points)

	# def test_Team_get_team_data(self):


	def test_Team_available_points(self):
		self.assertTrue(0 < ST_TOTSTESTS.arsenal.available_points(ST_TOTSTESTS.arsenal.games_played) < ST_TOTSTESTS.max_points)

	def test_check_for_st_tots_not_achieved(self):
		self.assertFalse(st_tots.st_tots(ST_TOTSTESTS.arsenal, ST_TOTSTESTS.spurs))

	def test_check_for_st_tots_achieved(self):
		#stubbing out attributes to trigger the else condition
		arsenal = st_tots.Team('Arsenal', ST_TOTSTESTS.soup)
		arsenal.points = 100
		spurs = st_tots.Team('Tottenham Hotspur', ST_TOTSTESTS.soup)
		spurs.points = 0
		self.assertTrue(st_tots.st_tots(arsenal, spurs))

	def test_end_of_season(self):
		self.assertFalse(st_tots.end_of_season(ST_TOTSTESTS.arsenal, ST_TOTSTESTS.spurs))

	def test_check_both_conditions(self):
		self.assertFalse(st_tots.check_both_conditions(ST_TOTSTESTS.arsenal, ST_TOTSTESTS.spurs))


if __name__ == '__main__':
	unittest.main()