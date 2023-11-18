import os
from flask import Flask, render_template, send_from_directory, redirect
from flask import request
from os import listdir
import os.path
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a+') as database:
        database.write('\n' + str(data))
    database.close()
    
def write_to_csv(data):
    file_exists = os.path.isfile('./database.csv')
    with open('database.csv', 'a', newline='\n') as database:
        headers = ['Contact Name', 'Contact Email', 'Contact Message']
        head_writer = csv.DictWriter(database, headers)
        writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        contact_name = data["contact_name"]
        contact_email = data["contact_email"]
        contact_message = data["contact_message"] 
        if not file_exists:
            head_writer.writeheader()
            
        writer.writerow([contact_name,contact_email,contact_message])
    database.close()
    
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect('./thankyou.html')
        except:
            return 'Did not save to database, contact administrator.'
        else:
            return 'Something went wrong try again.'

##TEMP SAVE OFF
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     if request.method == 'POST':
#         data = request.form.to_dict()
#         print(data)
#         return redirect('./thankyou.html')
#     else:
#         return 'Something went wrong try again.'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')











# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('./index.html', name=username, post_id=post_id)

# @app.route("/about_me.html")
# def about():
#     return render_template('./about_me.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'), 'bolt.ico', mimetype='image/vnd.microsoft.icon')
    
    
    
    