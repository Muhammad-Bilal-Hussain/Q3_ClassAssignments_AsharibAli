import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import uuid
import plotly.express as px

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Budget Manager", layout="centered")

# === Login Section (basic) ===
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Simple Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "M@1234":
            st.session_state.logged_in = True
            try:
                st.experimental_rerun()
            except AttributeError:
                st.stop()
        else:
            st.error("Invalid credentials")
    st.stop()

if st.button("🚪 Logout"):
    st.session_state.logged_in = False
    try:
        st.experimental_rerun()
    except AttributeError:
        st.stop()

st.title("💸 Personal Budget Manager")

# === Add Transaction Tab ===
tab1, tab2 = st.tabs(["➕ Add Transaction", "📊 Summary & History"])

with tab1:
    st.subheader("Add New Transaction")

    t_type = st.selectbox("Type", ["Income", "Expense"])
    amount = st.number_input("Amount (Rs)", min_value=0, step=1)

    income_categories = ["Salary", "Freelance", "Bonus", "Investment", "Gift", "Other"]
    expense_categories = ["Food", "Transport", "Rent", "Utilities", "Shopping", "Other"]

    selected_category = st.selectbox(
        "Select Category",
        income_categories if t_type == "Income" else expense_categories
    )

    if st.checkbox("Want to add custom category?"):
        custom_category = st.text_input("Enter custom category")
        if custom_category:
            selected_category = custom_category

    description = st.text_input("Description")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if st.button("Add Transaction"):
        transaction = {
            "id": str(uuid.uuid4()),
            "type": t_type,
            "amount": amount,
            "category": selected_category,
            "description": description,
            "date": date
        }
        res = requests.post(f"{API_URL}/transactions", json=transaction)
        if res.status_code == 200:
            st.success("Transaction added successfully!")
            try:
                st.experimental_rerun()
            except AttributeError:
                st.stop()
        else:
            st.error("Failed to add transaction.")

# === Summary and History ===
with tab2:
    st.subheader("📊 Budget Summary")

    res = requests.get(f"{API_URL}/transactions")
    if res.status_code != 200:
        st.error("Failed to fetch transactions.")
        st.stop()

    data = res.json()
    df = pd.DataFrame(data)

    if not df.empty:
        income = df[df["type"] == "Income"]["amount"].sum()
        expense = df[df["type"] == "Expense"]["amount"].sum()
        balance = income - expense

        st.metric("Total Income", f"Rs. {income}")
        st.metric("Total Expense", f"Rs. {expense}")
        st.metric("Net Savings", f"Rs. {balance}")

        st.subheader("📋 Transaction History")
        st.dataframe(df, use_container_width=True)

        # === Delete Option ===
        delete_id = st.selectbox("Select Transaction to Delete", df["id"])
        if st.button("Delete Selected"):
            res = requests.delete(f"{API_URL}/transactions/{delete_id}")
            if res.status_code == 200:
                st.success("Deleted successfully!")
                try:
                    st.experimental_rerun()
                except AttributeError:
                    st.stop()
            else:
                st.error("Failed to delete.")

        # === Chart ===
        st.subheader("📊 Category Distribution Chart")
        chart_data = df.groupby(["type", "category"])["amount"].sum().reset_index()
        fig = px.bar(chart_data, x="category", y="amount", color="type", barmode="group")
        st.plotly_chart(fig, use_container_width=True)

        # === Export ===
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", data=csv, file_name="transactions.csv", mime="text/csv")
    else:
        st.info("No transactions found.")
