import streamlit as st
from datetime import datetime

# Import your DB functions
from db_functions import (
    add_expense,
    get_payees,
    get_categories,
    get_accounts,
    add_income,
    get_payers,
    get_categoryI
)


def expense_form_ui(conn):
    """
    Displays a form for adding new expense entries with session state.
    Uses placeholder options for Payee, Category, and Account to force the user to pick one.
    """

    # 1. Initialize session state defaults (if not already set)
    if "expense_date" not in st.session_state:
        st.session_state["expense_date"] = datetime.now()
    if "expense_amount" not in st.session_state:
        st.session_state["expense_amount"] = 0.0
    if "expense_payee" not in st.session_state:
        st.session_state["expense_payee"] = "--Select Payee--"
    if "expense_category" not in st.session_state:
        st.session_state["expense_category"] = "--Select Category--"
    if "expense_account" not in st.session_state:
        st.session_state["expense_account"] = "--Select Account--"
    if "expense_note" not in st.session_state:
        st.session_state["expense_note"] = ""

    # 2. Retrieve data from DB
    payees_list = get_payees(conn)
    categories_list = get_categories(conn)
    accounts_list = get_accounts(conn)

    # 3. Build placeholder-based options
    placeholder_payee = "--Select Payee--"
    placeholder_category = "--Select Category--"
    placeholder_account = "--Select Account--"

    payee_options = [placeholder_payee] + payees_list
    category_options = [placeholder_category] + categories_list
    account_options = [placeholder_account] + accounts_list

    # Ensure session state defaults are valid options in the lists
    if st.session_state["expense_payee"] not in payee_options:
        st.session_state["expense_payee"] = placeholder_payee
    if st.session_state["expense_category"] not in category_options:
        st.session_state["expense_category"] = placeholder_category
    if st.session_state["expense_account"] not in account_options:
        st.session_state["expense_account"] = placeholder_account

    # 4. Display the form
    st.subheader("Add New Expense")

    # Date and Amount fields
    st.date_input("Date", key="expense_date")
    st.number_input("Amount ($)", key="expense_amount")

    # Payee, Category, and Account with placeholders
    st.selectbox("Payee", payee_options, key="expense_payee")
    st.selectbox("Category", category_options, key="expense_category")
    st.selectbox("Account", account_options, key="expense_account")

    # Note
    st.text_area("Note", max_chars=150, key="expense_note")

    # 5. Handle Submit
    if st.button("Submit Expense"):
        # Check if user actually selected valid options
        if st.session_state["expense_payee"] == placeholder_payee:
            st.error("Please select a Payee.")
        elif st.session_state["expense_category"] == placeholder_category:
            st.error("Please select a Category.")
        elif st.session_state["expense_account"] == placeholder_account:
            st.error("Please select an Account.")
        else:
            # All placeholders are replaced, so proceed
            add_expense(
                conn,
                st.session_state["expense_date"].strftime('%Y-%m-%d'),
                st.session_state["expense_amount"],
                st.session_state["expense_payee"],
                st.session_state["expense_category"],
                st.session_state["expense_account"],
                st.session_state["expense_note"]
            )
            st.success("Expense added successfully!")

            # Reset only the fields that won't cause an error.

            # st.session_state["expense_amount"] = 0.0
            # st.session_state["expense_payee"] = placeholder_payee
            # st.session_state["expense_category"] = placeholder_category
            # st.session_state["expense_account"] = placeholder_account
            # st.session_state["expense_note"] = ""


def income_form_ui(conn):
    """Displays a form for adding new income entries with session state and placeholders."""
    # Initialize session state defaults with placeholders for payer, income category, and account.
    if "income_date" not in st.session_state:
        st.session_state["income_date"] = datetime.now()
    if "income_amount" not in st.session_state:
        st.session_state["income_amount"] = 0.0
    if "income_payer" not in st.session_state:
        st.session_state["income_payer"] = "--Select Payer--"
    if "income_categoryI" not in st.session_state:
        st.session_state["income_categoryI"] = "--Select Income Category--"
    if "income_account" not in st.session_state:
        st.session_state["income_account"] = "--Select Account--"
    if "income_note" not in st.session_state:
        st.session_state["income_note"] = ""

    st.subheader("Add New Income")

    # Retrieve options from DB.
    payers_list = get_payers(conn)
    categories_i_list = get_categoryI(conn)
    accounts_list = get_accounts(conn)

    # Define placeholder strings.
    placeholder_payer = "--Select Payer--"
    placeholder_category = "--Select Income Category--"
    placeholder_account = "--Select Account--"

    # Build options lists with placeholders.
    payer_options = [placeholder_payer] + payers_list
    category_options = [placeholder_category] + categories_i_list
    account_options = [placeholder_account] + accounts_list

    # Ensure session state defaults are valid.
    if st.session_state["income_payer"] not in payer_options:
        st.session_state["income_payer"] = placeholder_payer
    if st.session_state["income_categoryI"] not in category_options:
        st.session_state["income_categoryI"] = placeholder_category
    if st.session_state["income_account"] not in account_options:
        st.session_state["income_account"] = placeholder_account

    # Create the form fields.
    st.date_input("Date", key="income_date")
    st.number_input("Amount ($)", key="income_amount")
    st.selectbox("Payer", payer_options, key="income_payer")
    st.selectbox("Income Category", category_options, key="income_categoryI")
    st.selectbox("Account", account_options, key="income_account")
    st.text_area("Note", max_chars=150, key="income_note")

    # Handle submission.
    if st.button("Submit Income"):
        if st.session_state["income_payer"] == placeholder_payer:
            st.error("Please select a Payer.")
        elif st.session_state["income_categoryI"] == placeholder_category:
            st.error("Please select an Income Category.")
        elif st.session_state["income_account"] == placeholder_account:
            st.error("Please select an Account.")
        else:
            add_income(
                conn,
                st.session_state["income_date"].strftime('%Y-%m-%d'),
                st.session_state["income_amount"],
                st.session_state["income_payer"],
                st.session_state["income_categoryI"],
                st.session_state["income_account"],
                st.session_state["income_note"]
            )
            st.success("Income added successfully!")

            # Do NOT reset 'income_date' to datetime.now(). That triggers the Streamlit error.
            # st.session_state["income_amount"] = 0.0
            # st.session_state["income_payer"] = placeholder_payer
            # st.session_state["income_categoryI"] = placeholder_category
            # st.session_state["income_account"] = placeholder_account
            # st.session_state["income_note"] = ""
