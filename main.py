import streamlit as st
from datetime import datetime
import sqlite3

# Database setup
conn = sqlite3.connect('garage.db')
c = conn.cursor()

# Create tables for appointments and reviews
def create_tables():
    c.execute('''CREATE TABLE IF NOT EXISTS appointments 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, contact TEXT, car_model TEXT, problem TEXT, date TEXT, time TEXT, status TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS reviews 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rating INTEGER, review TEXT)''')

create_tables()

# App title and description
st.title("International Car AC Works")
st.subheader("Your trusted partner for all car AC needs!")

# --- Section 1: Business Introduction ---
st.write("""
### Welcome to International Car AC Works!
We provide expert AC diagnostics, repairs, and maintenance services to keep your car cool and comfortable.
Located at the heart of the city, we are your go-to solution for all car AC-related problems.
""")

# --- Section 2: Appointment Booking ---
st.header("Book an Appointment")

with st.form(key='appointment_form'):
    name = st.text_input("Name")
    contact = st.text_input("Contact Information")
    car_model = st.text_input("Car Make & Model")
    problem = st.text_area("Problem Description")
    date = st.date_input("Preferred Date", min_value=datetime.today())
    time = st.time_input("Preferred Time")
    submit_appointment = st.form_submit_button("Book Appointment")
    
    if submit_appointment:
        c.execute("INSERT INTO appointments (name, contact, car_model, problem, date, time, status) VALUES (?, ?, ?, ?, ?, ?, 'Pending')", 
                  (name, contact, car_model, problem, date.strftime('%Y-%m-%d'), time.strftime('%H:%M')))
        conn.commit()
        st.success(f"Appointment booked successfully for {date.strftime('%Y-%m-%d')} at {time.strftime('%H:%M')}!")

# --- Section 3: Service Packages ---
st.header("Service Packages")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("### Basic Package")
    st.write("Price: RS.1500")
    st.write("- AC Gas Refilling\n- Filter Replacement\n- Basic Diagnostics")

with col2:
    st.write("### Standard Package")
    st.write("Price: RS.2000")
    st.write("- AC Gas Refilling\n- Filter Replacement\n- Detailed Diagnostics\n- AC Compressor Check")

with col3:
    st.write("### Premium Package")
    st.write("Price: RS.3500")
    st.write("- AC Gas Refilling\n- Filter Replacement\n- Detailed Diagnostics\n- AC Compressor Replacement\n- Electrical Wiring Check")

# --- Section 4: Testimonials and Reviews ---
st.header("Customer Reviews")

with st.form(key='review_form'):
    reviewer_name = st.text_input("Your Name")
    rating = st.slider("Rating", 1, 5)
    review_text = st.text_area("Your Review")
    submit_review = st.form_submit_button("Submit Review")
    
    if submit_review:
        c.execute("INSERT INTO reviews (name, rating, review) VALUES (?, ?, ?)", (reviewer_name, rating, review_text))
        conn.commit()
        st.success("Thank you for your review!")

st.write("### What our customers are saying:")

reviews = c.execute("SELECT name, rating, review FROM reviews").fetchall()
if reviews:
    for review in reviews:
        st.write(f"**{review[0]}** - {review[1]} stars")
        st.write(f"{review[2]}")
        st.write("---")
else:
    st.write("No reviews yet. Be the first to leave a review!")

# --- Section 5: Real-time Status Updates ---
st.header("Check Your Appointment Status")

status_contact = st.text_input("Enter your contact number to check your appointment status:")
if st.button("Check Status"):
    status = c.execute("SELECT status FROM appointments WHERE contact = ?", (status_contact,)).fetchone()
    if status:
        st.write(f"Your appointment status is: **{status[0]}**")
    else:
        st.write("No appointments found with that contact number.")

# --- Section 6: Promotions and Offers ---
st.header("Promotions and Offers")
st.write("""
**Current Offers:**
- 10% off on all services for new customers.
- Free diagnostics with any repair service.
""")

# --- Section 7: Emergency Contact Button ---
st.header("Emergency Service")
st.write("Need urgent help? Call us now!")
if st.button("Call Now"):
    st.write("📞 Contact us at: +91 8790440317")

# --- Section 8: Live Chat (Simulated) ---
st.header("Live Chat (Coming Soon)")
st.write("This feature is under development. Please stay tuned.")

# Footer with location and contact
st.write("### Visit Us:")
st.write("**International Car AC Works**")
st.write("Chamu Kaluva, Nandyal")
st.write("📞 Phone: +91 8790440317")
st.write("⏰ Open from 9 AM to 10 PM, Monday to Saturday")

# Closing the database connection
conn.close()
