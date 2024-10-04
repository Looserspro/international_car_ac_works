import streamlit as st
from datetime import datetime
import urllib.parse

# WhatsApp owner's number (replace with actual number)
OWNER_WHATSAPP_NUMBER = "+918790440317"

# Helper function to generate WhatsApp message URL
def generate_whatsapp_url(message):
    base_url = "https://wa.me/"
    full_url = f"{base_url}{OWNER_WHATSAPP_NUMBER}?text={urllib.parse.quote(message)}"
    return full_url

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
        # Prepare WhatsApp message content
        appointment_message = (f"New Appointment Request:\n"
                               f"Name: {name}\n"
                               f"Contact: {contact}\n"
                               f"Car Model: {car_model}\n"
                               f"Problem: {problem}\n"
                               f"Preferred Date: {date.strftime('%Y-%m-%d')}\n"
                               f"Preferred Time: {time.strftime('%H:%M')}")
        
        whatsapp_url = generate_whatsapp_url(appointment_message)
        st.markdown(f"[Send Appointment Request on WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

# --- Section 3: Service Packages ---
st.header("Service Packages")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("### Basic Package")
    st.write("Price: RS.1500")
    st.write("- AC Gas Refilling\n- Filter Replacement\n- Basic Diagnostics")

with col2:
    st.write("### Standard Package")
    st.write("Price: RS.2500-3500")
    st.write("- AC Gas Refilling\n- Filter Replacement\n- Detailed Diagnostics\n- AC Compressor Check")

with col3:
    st.write("### Premium Package")
    st.write("Price: RS.4000-5000")
    st.write("- AC Gas Refilling\n- Filter Replacement\n- Detailed Diagnostics\n- AC Compressor Replacement\n- Electrical Wiring Check")

# --- Section 4: Testimonials and Reviews ---
st.header("Customer Reviews")

with st.form(key='review_form'):
    reviewer_name = st.text_input("Your Name")
    rating = st.slider("Rating", 1, 5)
    review_text = st.text_area("Your Review")
    submit_review = st.form_submit_button("Submit Review")
    
    if submit_review:
        # Prepare WhatsApp message content
        review_message = (f"New Customer Review:\n"
                          f"Name: {reviewer_name}\n"
                          f"Rating: {rating} stars\n"
                          f"Review: {review_text}")
        
        whatsapp_url = generate_whatsapp_url(review_message)
        st.markdown(f"[Send Review on WhatsApp]({whatsapp_url})", unsafe_allow_html=True)

st.write("### What our customers are saying:")
st.write("No reviews yet. Be the first to leave a review!")

# --- Section 5: Real-time Status Updates ---
st.header("Check Your Appointment Status")
st.write("This feature is under development.")

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
    st.write("📞 Contact us at: +918790440317")

# --- Section 8: Live Chat (Simulated) ---
st.header("Live Chat (Coming Soon)")
st.write("This feature is under development. Please stay tuned.")

# Footer with location and contact
st.write("### Visit Us:")
st.write("**International Car AC Works**")
st.write("Chamu Kaluva, Nandyal")
st.write("📞 Phone: +918790440317")
st.write("⏰ Open from 9 AM to 6 PM, Monday to Saturday")
