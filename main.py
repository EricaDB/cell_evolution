"""
Erica Johnson
29 Dec 2014
"""

import cell
import random

alleleA = {'lifespan': 11, 'BMR': 1, 'dominant_over': ['alleleC']}
alleleB = {'lifespan': 12, 'BMR': 2, 'dominant_over': ['alleleD']}
alleleC = {'lifespan': 13, 'BMR': 3, 'dominant_over': []}
alleleD = {'lifespan': 14, 'BMR': 4, 'dominant_over': []}

def main():
    cell_1 = cell.Cell(alleleA, alleleD)
    cell_2 = cell.Cell(alleleA, alleleC)
    print(cell_1.BMR)
    
main()