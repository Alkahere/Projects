# Create a Flask web application
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()


