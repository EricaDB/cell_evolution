"""
	-- Cell Evolution --

    A cell evolution web application
    
    Erica Johnson
    7 Jan 2015
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')
    
if __name__ == '__main__':
    app.run(debug = True)