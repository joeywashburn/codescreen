#import needed modules
import flask, ipaddress, csv
from flask import request, jsonify

#create the app
app = flask.Flask(__name__)
app.config["DEBUG"] = True
servers = {}
reader = csv.DictReader(
    open('newservers.csv'),
    fieldnames=('hostname', 'serial', 'ip', 'netmask', 'gateway'),
)

#This skips the header row
next(reader)

#this strip the white space TBH I dont understand why, but it works. 
#I need to work on understanding this concept better
reader = (
    dict((k, v.strip()) for k, v in row.items() if v) for row in reader)

#run through the rows and 
for row  in reader:
    servers[row['hostname']] = row

#build the "URLs"
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Code Screen REST API</h1>
<p>A prototype API for the CodeScreen.</p>'''
@app.route('/api/v1/resources/servers/all', methods=['GET'])
def api_all():
    return jsonify(servers)

    # Create an empty list for our results
    results = []

    return jsonify(results)
app.run()