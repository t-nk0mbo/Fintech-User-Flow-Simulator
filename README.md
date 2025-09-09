🔗 **Live Demo:** [Fintech User Flow Simulator](https://fintech-user-flow.streamlit.app/)

---

## 📌 Overview

The **Fintech User Flow Simulator** is a lightweight prototype that simulates the digital experience of small business banking customers.  
It focuses on **onboarding, KYC checks, credit qualification, and loan workflows**, showcasing how real fintech platforms handle key user journeys.

This project is **not connected to real financial systems**.  
Instead, it uses mock logic, CSV data, and UI flows to create a realistic demonstration.

---

## 🚀 Features

### 1. **Digital Onboarding with KYC**
- Collects user information (name, SIN, address, business details).
- Validates inputs (e.g., Canadian SIN checksum validation).
- Simulates ID upload step.
- Displays a **"Congratulations!"** screen with a credit product offer.
- To pass through the onboarding simulation use 046454286 as SIN or Business Numbers

### 2. **Account Dashboard (Business Banking)**
- Interactive dashboard for **chequings, savings, credit, and loans**.
- Visualizations include:
  - Spending over time (chequings + credit).
  - Top vendors by spend.
  - Monthly earnings and expenses summary.
- Data sourced from CSV files to simulate real transactions.
- Includes a mock **"Ask Mercury" AI Assistant** button.

### 3. **SME Loan Approval Workflow**
- Step-by-step loan application simulator.
- Collects loan details and business financials.
- Next steps:
  - Upload supporting documents **OR**
  - Connect via mock **3rd party partners** (simulated e-commerce integrations).
- Simulated decision page (approval/decline logic can be extended).

---

## 🛠️ Tech Stack

- **Python**  
- **Streamlit** (for UI & app flow)  
- **Pandas** (for CSV data handling)  
- **Plotly Express** (for interactive graphs)  
- **GitHub + Streamlit Cloud** (for deployment)  

---

## 📊 Example Dashboard Views

- **Spending Over Time** (line/dot plots)  
- **Top Vendors by Spend** (bar chart)  
- **Monthly Earned vs Spent Summary**  

---

## ⚠️ Disclaimer

This project is **for demonstration purposes only**.  
It does **not** perform real KYC, financial analysis, or partner integrations.  
Any data used here is **dummy/sample data**.  

---

## 👨🏽‍💻 Author

Created by **Thierry Nkombo**  
As part of a fintech technical + product portfolio.  

---

