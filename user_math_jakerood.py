"""
Jake Rood
September 3, 2023

Project 2, Task #4
Purpose: Highlight ability to create custom functions relating to my domain of choice, baseball.

"""

import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

# Get Size of Scoreboard at Baseball Stadium
def get_area_scoreboard(height, width):
    try:
        area = height * width
        logger.info(f"The area of the scoreboard is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None

# Use the defensive math examples to call the permutations and combinations as shown
if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")

# Call the method created with several different arguments
logger.info("TRY: Call get_area_scoreboard() function with different values.")
get_area_scoreboard(40, 60)
get_area_scoreboard(30, 50)
get_area_scoreboard(20, 40)
logger.info("")

# Add three more functions useful to domain

# Get A Player's Batting Average
def get_batting_average(hits, at_bats):
    try:
        batting_average = hits / at_bats
        logger.info(f"The player's batting average is {batting_average: .3f}")
        return batting_average
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
# Get a Team's Runs Per Game
def get_team_runs_per_game(runs):
    try:
        runs_per_game = math.fsum(runs) / len(runs)
        logger.info(f"The team's average runs per game is {runs_per_game: .2f}")
        return runs_per_game
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None
    
# Get a Pitcher's Earned Run Average
def get_pitcher_era(earned_runs, innings):
    try:
        pitcher_era = earned_runs * 9 / innings
        logger.info(f"The pitcher's earned run average is {pitcher_era: .2f}")
        return pitcher_era
    except Exception as ex:
        logger.error (f"Error: {ex}")
        return None
    
# Call the new methods created
logger.info("TRY: Call get_batting_average() function with different values.")
get_batting_average(25, 81)
get_batting_average(126, 504)
get_batting_average(174, 581)
logger.info("")

logger.info("TRY: Call get_team_runs_per_game() function with a list of runs scored.")
runs_list = [3, 7, 0, 4, 3, 6, 8, 2, 5, 6, 3, 4]
get_team_runs_per_game(runs_list)
logger.info("")

logger.info("TRY: Call get_pitcher_era function with different values.")
get_pitcher_era(27, 85)
get_pitcher_era(55, 200)
logger.info("")