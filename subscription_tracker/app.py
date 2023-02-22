from flask import Flask, request, render_template
from subscription_tracker.notion_api import retreive_databse, add_entry
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
DATABSE_LINK = app.config['DATABSE_LINK']
# get NOTION_KEY from config.py
NOTION_KEY = app.config['NOTION_KEY']
# get NOTION_DATABASE_ID from config.py
NOTION_DATABASE_ID = app.config['NOTION_DATABASE_ID']

@app.route('/')
def hello_world():
    return render_template('index.html', data_base_link=DATABSE_LINK)

# validate the request
def validate_request(request):
    # name is not empty and string
    if not isinstance(request['name'], str) or request['name'] == "":
        return False
    # tag is not empty and string
    if not isinstance(request['tag'], str) or request['tag'] == "":
        return False
  # date is not empty and string
    if not isinstance(request['date'], str) or request['date'] == "":
        return False
    # try convert price to float
    try:
        float(request['price'])
    except ValueError:
        return False
    return True

# Add the new entry to the database
@app.route('/add', methods=['POST'])
def add():
    # get request and parse json
    response = request.get_json()
    # validate request
    if not validate_request(response):
        return "400"
    else:
        # add entry to database
        add_entry(response['name'], response['tag'],
                  response['date'], float(response['price']))
    # return response 200
    return "200"
# Get the database
@app.route('/get')
def get():
    return retreive_databse()