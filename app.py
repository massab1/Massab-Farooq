from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
