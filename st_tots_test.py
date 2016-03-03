import unittest
import st_tots

class ST_TOTSTESTS(unittest.TestCase):
	@classmethod
	def setUpClass(ST_TOTSTESTS):
		ST_TOTSTESTS.url = 'http://www.premierleague.com/en-gb/matchday/league-table.html'
		ST_TOTSTESTS.tag = 'td'
		ST_TOTSTESTS.team = 'Arsenal'
		ST_TOTSTESTS.points_per_win = 3
		ST_TOTSTESTS.games_per_season = 38
		ST_TOTSTESTS.max_points = ST_TOTSTESTS.games_per_season * ST_TOTSTESTS.points_per_win
		ST_TOTSTESTS.min_points = 0
		ST_TOTSTESTS.soup = st_tots.Soup(ST_TOTSTESTS.url).page


	def test_init_Soup(self):
		class_name = str(type(ST_TOTSTESTS.soup))
		self.assertEqual("<class 'bs4.BeautifulSoup'>", class_name)

	def test_Team__init__games_played(self):
		arsenal = st_tots.Team(ST_TOTSTESTS.team, ST_TOTSTESTS.soup)
		self.assertTrue(0 < arsenal.games_played < ST_TOTSTESTS.games_per_season)


	def test_Team__init__team_points(self):
		arsenal = st_tots.Team(ST_TOTSTESTS.team, ST_TOTSTESTS.soup)
		self.assertTrue(0 < arsenal.team_points < ST_TOTSTESTS.max_points)


	def test_Team_init_available_points(self):
		arsenal = st_tots.Team(ST_TOTSTESTS.team, ST_TOTSTESTS.soup)
		self.assertTrue(0 < arsenal.available_points < ST_TOTSTESTS.max_points)


if __name__ == '__main__':
	unittest.main()