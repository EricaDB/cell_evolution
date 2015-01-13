"""
    freeze.py
    To create a build directory with the application's 
    content turned into static files.
    
    Erica Johnson
    7 Jan 2015
"""

from flask_frozen import Freezer
from cell_evolution import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()