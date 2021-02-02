import os.path
import sqlite3

from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


def get_db_connection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "clients.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')


address_offer = []
adr1 = ['свободный', 'высотная', 'дачная', 'Свободный', 'Высотная', 'Дачная']
adr2 = ['мира', 'ленина', 'робеспьера']


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        surname = request.form['surname']
        city = request.form.get('city')
        address = request.form['address']
        address_offer.clear()
        address_offer.append(address)
        phone1 = request.form.get('phone1')
        phone2 = request.form.get('phone2')
        reason = request.form.get('reason')
        comment = request.form.get('comment')
        conn = get_db_connection()
        conn.execute(
            "INSERT INTO clients(first_name, last_name, surname, city, address, phone1, phone2, reason, comment) "
            "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (first_name, last_name, surname, city, address, phone1, phone2, reason, comment))
        conn.commit()
        conn.close()
        return redirect(url_for('offers'))
    return render_template('create.html')


@app.route('/create/offers', methods=('GET', 'POST'))
def offers():
    flg = 1
    if len(address_offer) != 0:
        for i in adr1:
            if i in address_offer[0]:
                if request.method == 'POST':
                    offer = request.form.get('offer')
                    conn = get_db_connection()
                    conn.execute(
                        "INSERT INTO offers(offer) "
                        "VALUES(?)",
                        (offer,))
                    conn.commit()
                    conn.close()
                    flg = 0
                    return redirect(url_for('information'))
                return render_template('offers1.html')
        for i in adr2:
            if i in address_offer[0]:
                if request.method == 'POST':
                    offer = request.form.get('offer')
                    conn = get_db_connection()
                    conn.execute(
                        "INSERT INTO offers(offer) "
                        "VALUES(?)",
                        (offer,))
                    conn.commit()
                    conn.close()
                    flg = 0
                    return redirect(url_for('information'))
                return render_template('offers2.html')
        if flg == 1:
            if request.method == 'POST':
                offer = request.form.get('offer')
                conn = get_db_connection()
                conn.execute(
                    "INSERT INTO offers(offer) "
                    "VALUES(?)",
                    (offer,))
                conn.commit()
                conn.close()
                return redirect(url_for('information'))
            return render_template('offers3.html')
    else:
        if request.method == 'POST':
            offer = request.form.get('offer')
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO offers(offer) "
                "VALUES(?)",
                (offer,))
            conn.commit()
            conn.close()
            return redirect(url_for('information'))
        return render_template('offers1.html')


@app.route('/create/offers/information')
def information():
    conn = get_db_connection()
    clients = conn.execute('SELECT * FROM clients').fetchall()[-1]
    offers = conn.execute('SELECT * FROM offers').fetchall()[-1]
    conn.close()
    return render_template('information.html', clients=clients, offers=offers)


@app.route('/create/offers/information/finish')
def finish():
    return render_template('finish.html')


@app.route('/close')
def close():
    return render_template('close.html')
