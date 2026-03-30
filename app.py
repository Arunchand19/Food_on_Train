import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, render_template, request, redirect, url_for, session, flash, send_from_directory
from flask_mail import Mail, Message
from random import randint
from database import init_db,get_restaurants_by_station, get_menu_by_restaurant, trains_db, restaurants_db



app = Flask(__name__)
app.secret_key = 'your_secret_key'


app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'arunchandmallarapu@gmail.com'
app.config['MAIL_PASSWORD'] = 'xklr zmvj ytkg ntem'
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


init_db() 

@app.route('/stations/<train_number>', methods=['GET'])
def get_stations(train_number):
    stations = get_stations_by_train(train_number)
    if stations:
        return {'success': True, 'stations': stations}
    return {'success': False, 'message': 'Invalid train number. Please try again.'}



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        train_number = request.form.get('train_number').strip()
        train_details = trains_db.get(train_number)

        if not train_details:
            flash("Invalid train number. Please try again.", "error")
            return redirect(url_for('index'))

        session['train_number'] = train_number
        session['train_details'] = train_details

        return render_template(
            'index.html',
            train_number=train_number,
            train_details=train_details
        )

    return render_template('index.html', train_number=None, train_details=None)


@app.route('/stations/<train_number>', methods=['POST'])
def stations(train_number):
    station_name = request.form.get('station_name')

    if not station_name:
        flash("Please select a valid station.", "error")
        return redirect(url_for('index'))

    session['station_name'] = station_name
    return redirect(url_for('restaurants', station_code=station_name))




@app.route('/restaurants/<station_code>', methods=['GET'])
def restaurants(station_code):
    
    restaurants = get_restaurants_by_station(station_code)

    
    restaurant_names = [restaurant[1] for restaurant in restaurants]
    order_counts = [randint(3, 5) for _ in restaurants] 

    fig, ax = plt.subplots()
    ax.bar(restaurant_names, order_counts)
    ax.set_xlabel('RESTAURANTS')
    ax.set_ylabel('RATING')
    ax.set_title('FOOD REVIEW')

    img_io = io.BytesIO()
    fig.savefig(img_io, format='png')
    img_io.seek(0)
    graph_url = base64.b64encode(img_io.getvalue()).decode('utf-8')

    return render_template('restaurants.html', restaurants=restaurants, graph_url=graph_url)

@app.route('/menu/<int:restaurant_id>', methods=['GET'])
def menu(restaurant_id):
    menu_items = get_menu_by_restaurant(restaurant_id)
    return render_template('menu.html', menu_items=menu_items, restaurant_id=restaurant_id)

@app.route('/images/<path:filename>')
def images(filename):
    return send_from_directory('static/images', filename)


@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_id = request.form.get('item_id')
    item_name = request.form.get('item_name')
    item_price = float(request.form.get('item_price', 0))
    quantity = int(request.form.get('quantity', 1)) 
    if 'cart' not in session:
        session['cart'] = []

    
    for item in session['cart']:
        if item['id'] == item_id:
            item['quantity'] += quantity 
            break
    else:
      
        session['cart'].append({
            'id': item_id,
            'name': item_name,
            'price': item_price,
            'quantity': quantity  
        })
    
    session.modified = True  
    return redirect(url_for('cart'))

@app.route('/cart', methods=['GET'])
def cart():
    cart_items = session.get('cart', [])
    total_bill = sum(item['price'] * item['quantity'] for item in cart_items) 
    return render_template('cart.html', cart_items=cart_items, total_bill=total_bill)

@app.route('/delete_from_cart', methods=['POST'])
def delete_from_cart():
    item_id = request.form.get('item_id')
    delete_quantity = int(request.form.get('delete_quantity', 1))
    cart = session.get('cart', [])

    for item in cart:
        if item['id'] == item_id:
            if item['quantity'] > delete_quantity:
                item['quantity'] -= delete_quantity
            else:
                cart.remove(item)
            break

    session['cart'] = cart
    session.modified = True
    return redirect(url_for('cart'))

@app.route('/payment', methods=['GET'])
def payment():
    total_bill = sum(item['price'] * item['quantity'] for item in session.get('cart', []))
    return render_template('payment.html', total_bill=total_bill)

@app.route('/upi_payment', methods=['GET', 'POST'])
def upi_payment():
    if request.method == 'POST':
        upi_id = request.form.get('upi_id')
        email = request.form.get('email')  
        send_otp(email)
        session['payment_method'] = 'UPI'  
        return redirect(url_for('verify_email'))
    return render_template('upi_payment.html')

@app.route('/card_payment', methods=['GET', 'POST'])
def card_payment():
    if request.method == 'POST':
        card_number = request.form.get('card_number')
        expiry_date = request.form.get('expiry_date')
        cvv = request.form.get('cvv')
        email = request.form.get('email')  
        send_otp(email)
        session['payment_method'] = 'Card'  
        return redirect(url_for('verify_email'))
    return render_template('card_payment.html')



@app.route('/verify_email', methods=['GET', 'POST'])
def verify_email():
    remaining_time = session.get('remaining_time', 30)  
    
    if request.method == 'POST':
        user_otp = request.form.get('otp')
        if session.get('otp') and int(user_otp) == session['otp']:
            flash('Email verification successful', 'success')
            session.pop('otp', None)  
            session.pop('remaining_time', None)  
            return redirect(url_for('index'))
        else:
            remaining_time -= 5  
            session['remaining_time'] = remaining_time 
    
    return render_template('verify.html', time_left=remaining_time)


def send_otp(email):
    global otp
    otp = randint(000000, 999999)  
    msg = Message(subject='OTP Verification', sender='arunchandmallarapu@gmail.com', recipients=[email])
    msg.body = f'Your OTP for Food On Train is: {otp}'
    mail.send(msg)

@app.route('/validate', methods=['POST'])
def validate():
    user_otp = request.form['otp']
    if otp == int(user_otp):
        message = 'OTP verified successfully! Food will deliver to your seat.'
    else:
        message = 'Invalid OTP. Please try again.'

    return render_template('verify.html', message=message)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)