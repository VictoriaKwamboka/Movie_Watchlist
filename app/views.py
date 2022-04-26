from flask import render_template
from app import app

# Views

@app.route('/')
def index():
    '''
    view that returns the index page and its data
    '''
    return render_template('index.html')

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    view that returns movie details
    '''
    
    return render_template('movie.html', id = movie_id)