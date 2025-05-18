from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


def write_to_text(data):
    with open('data.txt', 'a') as file:
        file.write(f"{data['email']},{data['subject']},{data["message"]}\n")


def write_to_csv(data):
    with open('data.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['email'], data['subject'], data['message']])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:page_name>')
def page(page_name=None):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_text(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "Failed to save the data!!"
    else:
        return "Failed to submit the request!!"
