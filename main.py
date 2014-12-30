"""
Erica Johnson
29 Dec 2014
"""

import cell

alleleA = {'lifespan': 10, 'BMR': 2, 'dominant_over': ['alleleC']}
alleleB = {'lifespan': 10, 'BMR': 2, 'dominant_over': ['alleleD']}
alleleC = {'lifespan': 10, 'BMR': 2, 'dominant_over': []}
alleleD = {'lifespan': 10, 'BMR': 2, 'dominant_over': []}

def main():
    new_cell = cell.Cell(alleleA, alleleD)
    
main()