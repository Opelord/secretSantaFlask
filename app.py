import csv

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

with open('connections.csv', mode='r') as infile:
    reader = csv.reader(infile)
    connections = {rows[0]: rows[1] for rows in reader}


@app.route('/', methods=['GET', 'POST'])
def main_page():
    error = ""
    if request.method == 'POST':
        name = request.form['name']
        if len(name) == 0:
            # Form data failed validation; try again
            error = "Prosze wpisać imię!"
        else:
            # Form data is valid; move along
            return redirect(url_for('gift_page'), code=307)
    return render_template('index.html', names=connections, message=error)


@app.route('/gift', methods=['POST'])
def gift_page():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('gift.html', names=connections, gifter=name)


if __name__ == '__main__':
    app.run(debug=True)
