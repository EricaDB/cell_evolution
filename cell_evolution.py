"""
	-- Cell Evolution --

    A cell evolution web application
    
    Erica Johnson
    7 Jan 2015
"""

from flask import Flask, render_template, jsonify
import json
from cell import Cell
import random

cell_list = []

alleleA = {'dominant_over': [], 'BMR': 20, 'lifespan': 20}
alleleB = {'dominant_over': [alleleA], 'BMR': 30, 'lifespan': 30}
alleleC = {'dominant_over': [alleleB], 'BMR': 10, 'lifespan': 10}
alleleD = {'dominant_over': [alleleC], 'BMR': 15, 'lifespan': 15}

cell1 = Cell(alleleA, alleleB)
cell2 = Cell(alleleC, alleleB)
cell3 = Cell(alleleD, alleleD)

cells = [cell1, cell2, cell3]

# for cell in cells:
#     color = "%06x" % random.randint(0,0xFFFFFF)
#     for i in range(random.randint(1, 5)):
#         cell_list.append({
#             "color" : "#" + color
#             })

for cell in cells:
    color = "%06x" % random.randint(0,0xFFFFFF)
    for i in range(random.randint(1, 5)):
        cell_list.append("#" + color)
            
print(cell_list)

out_file = open("cells.json", "w")
json.dump(cell_list, out_file, indent=4)

app = Flask(__name__)

@app.route('/')
def index():
    #data = jsonify(results=cell_list)
    data = cell_list
    return render_template('layout.html', data = data)
    
if __name__ == '__main__':
    app.run(debug = True)