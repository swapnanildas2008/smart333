from flask import Flask, render_template, request, redirect, url_for
import firebase_admin
from firebase_admin import credentials, db

app = Flask(__name__)

cred = credentials.Certificate("./firebase.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-farming-and-contro-6c7be-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

db_ref = db.reference('Moisture')
db_ref1 = db.reference('MoistureValue')
db_ref2 = db.reference('Humidity')
db_ref3 = db.reference('Temperature')
db_ref4 = db.reference('relayState')

@app.route('/')
def index():
    data = db_ref.get()
    data1 = db_ref1.get()
    data2 = db_ref2.get()
    data3 = db_ref3.get()
    return render_template('index.html', data=data, data1=data1, data2=data2, data3=data3)

@app.route('/change_data', methods=['POST'])
def change_data():
    current_value = db_ref4.get()
    new_value = 0 if current_value == 1 else 1
    db_ref4.set(new_value)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)