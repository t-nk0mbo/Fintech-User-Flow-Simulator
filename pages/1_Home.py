# onboarding_kyc_app.py

import streamlit as st
import re

# ------------------------------
# Validation Functions
# ------------------------------

def validate_sin(sin):
    """Validate Canadian SIN using length and Luhn checksum. (Use 046454286 for simulation)"""
    if not re.fullmatch(r"\d{9}", sin):
        return False
    
    # Luhn algorithm implementation for SIN
    total = 0
    for i, digit in enumerate(sin):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def validate_business_number(bn):
    """Validate Canadian Business Number (9 digits)."""
    return bool(re.fullmatch(r"\d{9}", bn))

def validate_email(email):
    """Basic email pattern validation."""
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email))

def validate_phone(phone):
    """Validate North American phone number (10 digits)."""
    phone_digits = re.sub(r"\D", "", phone)
    return len(phone_digits) == 10

def validate_address(address):
    """Basic validation to check if address field is not empty."""
    return bool(address.strip())

# ------------------------------
# Simulated Existing SINs
# ------------------------------
existing_sins = {"123456782", "987654321", "111222333"}

# ------------------------------
# Streamlit App Setup
# ------------------------------

st.title("🪙 Sublime for Business")

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'form'

# ------------------------------
# Page 1 – Onboarding Form
# ------------------------------
if st.session_state.page == 'form':

    st.write("Fill out the form below to sign up for Sublime for Business chequings account:")

    with st.form("onboarding_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        home_address = st.text_input("Home Address")
        business_name = st.text_input("Business Name")
        business_address = st.text_input("Business Address")
        business_number = st.text_input("Business Number (9 digits)")
        sin = st.text_input("Social Insurance Number (SIN) (9 digits)")
        
        submit = st.form_submit_button("Continue")

    if submit:
        # Perform validations
        errors = []
        
        if not validate_email(email):
            errors.append("Invalid email format.")
        if not validate_phone(phone):
            errors.append("Invalid phone number format. Enter 10 digits.")
        if not validate_business_number(business_number):
            errors.append("Invalid business number format. Must be 9 digits.")
        if not validate_sin(sin):
            errors.append("Invalid SIN. Must be 9 digits and pass checksum. (*Use 046454286 to advance*)")
        if not validate_address(home_address):
            errors.append("Home address is required.")
        if not validate_address(business_address):
            errors.append("Business address is required.")
        
        # Simulate duplicate SIN check
        if sin in existing_sins:
            errors.append("SIN already exists in the system (duplicate detected).")
        
        # Display results
        if errors:
            st.error("❌ Unable to continue due to the followign errors:")
            for err in errors:
                st.write(f"- {err}")
        else:
            st.success("✅ Sign up complete!")
            st.write("Your application has passed initial KYC checks and will proceed to government ID verification.")
            # Move to ID upload page
            st.session_state.page = 'id_upload'
            st.rerun()

# ------------------------------
# Page 2 – Government ID Upload
# ------------------------------
elif st.session_state.page == 'id_upload':
    st.subheader("🪪 Government ID Upload (Simulation)")

    st.write("""
    As part of our KYC process, please upload a photo of your government-issued ID.  
    **Note:** For simulation purposes, you can continue without uploading.
    """)

    uploaded_id = st.file_uploader("Upload your government ID", type=["jpg", "jpeg", "png", "pdf"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Submit ID"):
            st.success("✅ ID uploaded successfully (simulated).")
            st.session_state.page = 'offer'
            st.rerun()

    with col2:
        if st.button("Skip and Continue"):
            st.warning("⚠️ You skipped ID upload. For this simulation, onboarding continues.")
            st.session_state.page = 'offer'
            st.rerun()


# ------------------------------
# Page 3 – Credit Card Application
# ------------------------------

elif st.session_state.page == 'offer':
    st.subheader("🎉 Congratulations!")

    st.write("Your business qualifies for the **Sublime Mastercard for Business!**")

    # Layout for image + details
    col1, col2 = st.columns([1,2])

    with col1:
        st.image("C:/Users/thien/OneDrive/Documents/EBB_onbarding/sublime_card.png", caption="Sublime Mastercard for Business", use_container_width=True)  # Replace path later

    with col2:
        st.markdown("""
        **Card Details:**  
        - **Type:** Business Credit Card  
        - **Annual Fee:** $99 (waived first year)  
        - **Interest Rate:** 19.99% purchases / 22.99% cash advances  
        - **Credit Limit:** Up to $50,000
        """)

    st.write("""
    The Sublime Mastercard for Business helps you manage cash flow with ease, provides employee card controls, and earns competitive cashback on business expenses.  
    Enjoy **insurance protections**, **extended warranty**, and **access to exclusive business offers**.
    """)

    if st.button("Continue"):
        st.info("🔧 Continue button pressed. No further navigation implemented in this simulation.")