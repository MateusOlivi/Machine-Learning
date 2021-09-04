from pacman import runGames,loadAgent
from pacman import Directions
from pacmanAgents import GreedyAgent
from util import Queue
import textDisplay
import game
import layout
import random
import graphicsDisplay

import numpy as np


from pympler.tracker import SummaryTracker
tracker = SummaryTracker()

props={}
pacman = GreedyAgent()
ghostType = loadAgent('RandomGhost', True)
textDisplay.SLEEP_TIME = 0
props['layout'] = layout.getLayout( 'mediumClassic' )
props['pacman'] = pacman
props['ghosts'] = [ghostType( i+1 ) for i in range( 2 )]
props['display'] = textDisplay.NullGraphics()
props['numGames'] = 20
props['record'] = False
props['catchExceptions'] = False
props['timeout'] = 0.6
    
res = runGames(**props)

tracker.print_diff()
