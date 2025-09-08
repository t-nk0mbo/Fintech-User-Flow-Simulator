import streamlit as st
import re


# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(page_title="Sublime Optima Loan Application", page_icon="💰", layout="centered")

# ------------------------------
# Initialize session state for navigation and data
# ------------------------------
if "page" not in st.session_state:
    st.session_state["page"] = 1

if "form_data" not in st.session_state:
    st.session_state["form_data"] = {}

# ------------------------------
# Decision Engine Logic
# ------------------------------
def decision_engine(loan_amount, annual_income, credit_score):
    min_credit_score = 650
    max_lti_ratio = 0.4

    if credit_score < min_credit_score:
        return "DECLINED", 0, "Credit score below minimum eligibility (650)."

    lti_ratio = loan_amount / annual_income

    if lti_ratio > max_lti_ratio:
        approved_amount = round(annual_income * max_lti_ratio, -2)
        return "Conditionally Approved", approved_amount, f"Requested amount exceeds allowable loan-to-income ratio (max 40%). Approved for ${approved_amount} instead."
    
    return "APPROVED", loan_amount, "Your income and credit score meet our lending criteria."

# ------------------------------
# Page 1: Application Details
# ------------------------------
if st.session_state["page"] == 1:
    st.title("Sublime Optima Loan Application")
    st.write("Step 1 of 3: Provide your business loan details below.")

    with st.form("loan_form"):
        full_name = st.text_input("Full Name")
        loan_amount = st.number_input("Requested Loan Amount ($)", min_value=1000, max_value=1000000, step=1000)
        loan_purpose = st.selectbox("Loan Purpose", ["Working Capital", "Equipment Purchase", "Inventory Purchase", "Business Expansion", "Other"])
        loan_term = st.number_input("Loan Term (years)", min_value=1, max_value=10, step=1)
        annual_income = st.number_input("Business Annual Income ($)", min_value=10000, max_value=10000000, step=1000)
        credit_score = st.number_input("Credit Score", min_value=625, max_value=900, step=1)

        continue_btn = st.form_submit_button("Continue")

    if continue_btn:
        st.session_state["form_data"] = {
            "full_name": full_name,
            "loan_amount": loan_amount,
            "loan_purpose": loan_purpose,
            "loan_term": loan_term,
            "annual_income": annual_income,
            "credit_score": credit_score
        }
        st.session_state["page"] = 2
        st.rerun()

# ------------------------------
# Page 2: Supporting Documents or Connect via Partner
# ------------------------------
elif st.session_state["page"] == 2:
    st.title("📄 Submit Supporting Documents")
    st.write("Step 2 of 3: To process your application, please provide your supporting documents attested by an accredited CPA or financial professional.")

    uploaded_files = st.file_uploader("Upload financial statements or tax documents", accept_multiple_files=True)

    st.write("### Or connect via partner platform to import your financial data directly:")

    # Placeholder logos for e-commerce partners (replace with actual logos later)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("C:/Users/thien/OneDrive/Documents/EBB_onbarding/shopify.png", caption="Shopify")
    with col2:
        st.image("C:/Users/thien/OneDrive/Documents/EBB_onbarding/amzn.png", caption="Amazon")
    with col3:
        st.image("C:/Users/thien/OneDrive/Documents/EBB_onbarding/39003.png", caption="Square")

    st.write("By choosing to connect your account via a third-party partner, you acknowledge and consent to the retrieval of your business financial information directly from the selected partner platform. This information may include transaction history, account balances, and other relevant data used to assess your application.")

    connect_partner = st.button("Sign in with Partner Platform")
    continue_docs = st.button("Continue with Uploaded Documents")

    if connect_partner or continue_docs:
        st.session_state["page"] = 3
        st.rerun()

# ------------------------------
# Page 3: Decision Result
# ------------------------------
elif st.session_state["page"] == 3:
    st.title("Loan Application Result")

    data = st.session_state["form_data"]
    result, approved_amount, reason = decision_engine(
        data["loan_amount"],
        data["annual_income"],
        data["credit_score"]
    )

    st.write(f"**Applicant:** {data['full_name']}")
    st.write(f"**Requested Amount:** ${data['loan_amount']:,.2f}")
    st.write(f"**Result:** {result}")

    if result != "Declined":
        st.write(f"**Approved Amount:** ${approved_amount:,.2f}")

    st.write(f"**Reason:** {reason}")

    if st.button("Submit Another Application"):
        st.session_state["page"] = 1
        st.session_state["form_data"] = {}
        st.rerun()

st.markdown("---")
st.subheader("🧠 Explore Deeper Insights with Mercury")
st.write("Gain tailored financial advice, identify opportunities, and optimize cash flow with Mercury, your interactive financial analysis AI.")

if st.button("Ask Mercury 💬"):
    st.write("🔧 Mercury is under development.")
