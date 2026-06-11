'''
Test para la función fun_total_goals del ejercicio 6
'''
import unittest
import os
import sys
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from exercises.ex6 import fun_total_goals

class TestFunTotalGoals(unittest.TestCase):
    '''
    Test para la función fun_total_goals
    '''

    # Creamos un dataframe ficticio
    def setUp(self):
        self.data = pd.DataFrame({'FTHG' : [1,2,3], 'FTAG' : [0,1,2]})
    
    # Probamos el dataframe ficticio
    def test_fun_total_goals(self):
        home_goals, away_goals, total_goals = fun_total_goals(self.data)
        self.assertEqual(home_goals, 6)
        self.assertEqual(away_goals, 3)
        self.assertEqual(total_goals, 9)

if __name__ == '__main__':
    unittest.main()