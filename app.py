from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, World!"
@app.route('/about')
def about():
    return "This is the About Page!"


# Run the app on port 5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

