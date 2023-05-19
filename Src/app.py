from flask import Flask, render_template, request, redirect, url_for
from Admin import Admin

app = Flask(__name__)
admin = Admin()

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Sign Up Page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        admin.signUp(name, email, password)
        return redirect(url_for('signin'))
    return render_template('signup.html')

# Sign In Page
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if admin.signIn(email, password):
            return redirect(url_for('user_profile'))
        else:
            # Handle invalid credentials
            return render_template('signin.html', error='Invalid email or password')
    return render_template('signin.html')

# User Profile Page
@app.route('/user_profile')
def user_profile():
    # Fetch user details from the admin object and pass them to the template
    name = admin.get_name()
    email = admin.get_email()
    return render_template('userprofile.html', name=name, email=email)

# Add Trip Page
@app.route('/add_trip', methods=['GET', 'POST'])
def add_trip():
    if request.method == 'POST':
        src = request.form['src']
        dist = request.form['dist']
        departs = request.form['departs']
        arrives = request.form['arrives']
        price = request.form['price']
        admin.add_trip(src, dist, departs, arrives, price)
        return redirect(url_for('home'))
    return render_template('addtrip.html')

# Edit Trip Page
@app.route('/edit_trip', methods=['GET', 'POST'])
def edit_trip():
    if request.method == 'POST':
        trip_id = request.form['trip_id']
        src = request.form['src']
        dist = request.form['dist']
        departs = request.form['departs']
        arrives = request.form['arrives']
        price = request.form['price']
        admin.update_trip(trip_id, src, dist, departs, arrives, price)
        return redirect(url_for('home'))
    return render_template('edittrip.html')

# Booking Confirmation Page
@app.route('/booking_confirmation')
def booking_confirmation():
    # Implement logic to retrieve booking details and pass them to the template
    booking_details = admin.get_booking_details()
    return render_template('bookingconfirmation.html', booking_details=booking_details)

# Booking Cancellation Page
@app.route('/booking_cancellation')
def booking_cancellation():
    # Implement logic to retrieve booking details and pass them to the template
    booking_details = admin.get_booking_details()
    return render_template('bookingcancellation.html', booking_details=booking_details)

if __name__ == '__main__':
    app.run(debug=True)
