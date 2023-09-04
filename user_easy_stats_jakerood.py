"""

Purpose: Illustrate the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpreter
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys

# Here's some bivariant baseball data for a team over eight games (two series of data)

arrayHits = [4, 7, 3, 8, 11, 6, 13, 9]
arrayRuns = [2, 4, 2, 4, 6, 3, 5, 4]

# Descriptive: Averages and measures of central tendency

mean = statistics.mean(arrayRuns)
median = statistics.median(arrayRuns)
mode = statistics.mode(arrayRuns)

# log use variable colon formatting to avoid unnecessary digits (e.g. .2f)

logger.info(f"mean   = {mean:.2f}")
logger.info(f"median = {median:.2f}")
logger.info(f"mode   = {mode:.2f}")

# Descriptive: Measures of spread

var = statistics.variance(arrayRuns)
stdev = statistics.stdev(arrayRuns)
lowest = min(arrayRuns)
highest = max(arrayRuns)

# Change to f-strings and display 2 decimal places (like we did above)
logger.info(f"var    = {var:.2f}")
logger.info(f"stdev  = {stdev:.2f}")
logger.info(f"lowest = {lowest:.2f}")
logger.info(f"highest= {highest:.2f}")

# Call linear_regression() function -
# and get back 2 values: slope and intercept
# describing the 'best fit' line through the data
slope, intercept = statistics.linear_regression(arrayHits, arrayRuns)

# Choose a hits value off in the future (future hits)
future_hits = 6

# Extend the line out into the unknown future
# and read the value (of future runs)
future_runs = round(slope * future_hits + intercept)

logger.info("Here's some bivariant data (2 variables, together):")
logger.info(f"Hits:{arrayHits}")
logger.info(f"Runs:{arrayRuns}")
logger.info("Calculate the slope and intercept of a best fit straight line:")
logger.info(f"   slope = {slope:.2f}")
logger.info(f"   intercept = { intercept:.2f}")
logger.info("Let's use our best fit line to PREDICT a future value.")
logger.info(f"   At future x = {future_hits:d},")
logger.info(f"   we predict the value of y will be { future_runs:d}.")
logger.info("How'd we do? Does this make sense given the data?")
