import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Import DB functions
from db_functions import (
    create_connection,
    create_table,
    get_expenses_by_month,
    get_income_by_month,
    delete_expense,
    delete_payee,
    get_payees_L4D,
    delete_category,
    get_categories_L4D,
    delete_account,
    get_accounts_L4D,
    export_expenses_to_csv,
    export_income_to_csv,
    delete_income,
    add_payer,
    get_payers_L4D,
    delete_payer,
    add_categoryI,
    get_categoryI_L4D,
    delete_categoryI,
    add_account
    # ... any other functions you need
)

# Import the form UIs
from forms import expense_form_ui, income_form_ui


# Import your custom email function
from AppEmail import send_email_with_csv

# ----------------------------------
# Create DB connection & table setup
# ----------------------------------
conn = create_connection()
create_table(conn)

# ----------------------------------
# Set Page Config
# ----------------------------------
st.set_page_config(page_title='Finance Tracker',
                   page_icon=':coin:', layout='wide')


# 🔹 ADD THE TITLE AT THE TOP
st.markdown(
    "<h1 style='text-align: center;'>Expense Tracker Web App</h1>",
    unsafe_allow_html=True
)


# ----------------------------------
# Navigation Tabs
# ----------------------------------
menu_tabs = ['Expense', 'Income', 'Summary']
selected_tab = option_menu(
    menu_title=None,
    options=menu_tabs,
    icons=['pencil-fill', 'pencil-fill', 'bar-chart-fill'],
    orientation='horizontal'
)

# ----------------------------------
# Custom CSS for button coloring
# ----------------------------------
html_code = """
    <style>
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
    }
    </style>
"""
st.markdown(html_code, unsafe_allow_html=True)


# ----------------------------------
# Plotting Helpers (Summary Tab)
# ----------------------------------


def plot_category_wise(df_expenses, df_income):
    """Bar chart comparing expense categories vs. income categories."""
    df_expenses['type'] = 'Expense'
    df_income['type'] = 'Income'

    df_expenses = df_expenses.rename(
        columns={'category': 'category', 'total': 'total'})
    df_income = df_income.rename(
        columns={'categoryI': 'category', 'total': 'total'})

    df_combined = pd.concat([df_expenses, df_income])

    fig = px.bar(
        df_combined,
        x='category',
        y='total',
        color='type',
        title='Category-wise Expenses and Income',
        labels={'total': 'Amount', 'category': 'Category'}
    )
    fig.update_layout(xaxis_title='Category', yaxis_title='Amount')
    return fig


def plot_expense_income_distribution(df_expenses, df_income):
    expense_sum = df_expenses.groupby('category')['total'].sum()
    income_sum = df_income.groupby('categoryI')['total'].sum()

    expense_colors = px.colors.qualitative.Plotly[:len(expense_sum)]
    income_colors = px.colors.qualitative.Plotly[:len(income_sum)]

    fig = go.Figure()

    # Pie for Expenses (show only percentages, in white)
    fig.add_trace(go.Pie(
        labels=expense_sum.index,
        values=expense_sum.values,
        name='Expenses',
        marker=dict(colors=expense_colors),
        domain=dict(x=[0, 0.45]),
        textinfo='percent',  # show only the % inside the slices
        insidetextfont=dict(color='white')  # make those % white
    ))

    # Pie for Income (show only percentages, in white)
    fig.add_trace(go.Pie(
        labels=income_sum.index,
        values=income_sum.values,
        name='Income',
        marker=dict(colors=income_colors),
        domain=dict(x=[0.55, 1.0]),
        textinfo='percent',
        insidetextfont=dict(color='white')
    ))

    # Keep your "Expenses" and "Income" annotations in black
    fig.update_layout(
        title_text='Expense and Income Distribution',
        annotations=[
            dict(
                text='Expenses',
                x=0.18,
                y=0.5,
                font_size=16,
                font=dict(color='black'),  # black annotation
                showarrow=False
            ),
            dict(
                text='Income',
                x=0.82,
                y=0.5,
                font_size=16,
                font=dict(color='black'),  # black annotation
                showarrow=False
            )
        ]
    )

    return fig


# ----------------------------------
# EXPENSE TAB
# ----------------------------------
if selected_tab == "Expense":
    st.title("Expenses")

    # 1. Add Expense (session-state form)
    expense_form_ui(conn)

    # 2. View Expenses by Month
    st.subheader("View Expenses by Month")
    month_options = [f"{i:02d}" for i in range(1, 13)]
    current_month = datetime.now().strftime('%m')
    selected_month = st.selectbox(
        'Month', month_options, index=month_options.index(current_month)
    )

    if st.button('View Expenses'):
        df = get_expenses_by_month(conn, selected_month)
        st.dataframe(df)
        if not df.empty:
            st.write(f"Total: ${df['Amount'].sum():.2f}")
        else:
            st.write("No expenses found for this month.")

    # 3. Manage Expense Data
    st.subheader("Manage Expense Data")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Delete an Expense**")
        expense_id_to_delete = st.number_input(
            'Expense ID to delete', value=0, key="expense_id_delete"
        )
        if st.button('Delete Expense', key="delete_expense_button"):
            if expense_id_to_delete > 0:
                delete_expense(conn, int(expense_id_to_delete))
                st.success(f"Expense with ID {expense_id_to_delete} deleted!")

    with col2:
        st.markdown("**Add a Payee**")
        new_payee = st.text_input('New Payee', key="new_payee_input")
        if st.button('Add Payee', key="add_payee_button"):
            if new_payee.strip():
                # Or add_payee if you prefer
                add_payer(conn, new_payee.strip())
                st.success(f'Payee "{new_payee}" added!')

        if st.button('List Payees', key="list_payees_button"):
            data = get_payees_L4D(conn)
            st.dataframe(data)

        payee_id_to_delete = st.number_input(
            'Payee ID to delete', value=0, key="payee_id_delete"
        )
        if st.button('Delete Payee', key="delete_payee_button"):
            if payee_id_to_delete > 0:
                delete_payee(conn, int(payee_id_to_delete))
                st.success(f'Payee with ID {payee_id_to_delete} deleted!')

    st.markdown("---")
    st.subheader("Add / Delete Category")

    col3, col4 = st.columns(2)
    with col3:
        new_category = st.text_input('New Category', key="new_category_input")
        if st.button('Add Category', key="add_category_button"):
            if new_category.strip():
                add_categoryI(conn, new_category.strip())
                st.success(f'Category "{new_category}" added!')

        if st.button('List Categories', key="list_categories_button"):
            data = get_categories_L4D(conn)
            st.dataframe(data)

    with col4:
        category_id_to_delete = st.number_input(
            'Category ID to delete', value=0, key="category_id_delete"
        )
        if st.button('Delete Category', key="delete_category_button"):
            if category_id_to_delete > 0:
                delete_category(conn, int(category_id_to_delete))
                st.success(
                    f'Category with ID {category_id_to_delete} deleted!')

    st.markdown("---")
    st.subheader("Add / Delete Account")

    col5, col6 = st.columns(2)
    with col5:
        new_account = st.text_input('New Account', key="new_account_input")
        if st.button('Add Account', key="add_account_button"):
            if new_account.strip():
                add_account(conn, new_account.strip())
                st.success(f'Account "{new_account}" added!')

        if st.button('List Accounts', key="list_accounts_button"):
            data = get_accounts_L4D(conn)
            st.dataframe(data)

    with col6:
        account_id_to_delete = st.number_input(
            'Account ID to delete', value=0, key="account_id_delete"
        )
        if st.button('Delete Account', key="delete_account_button"):
            if account_id_to_delete > 0:
                delete_account(conn, int(account_id_to_delete))
                st.success(f'Account with ID {account_id_to_delete} deleted!')

    st.markdown("---")
    st.subheader("Export & Email Expenses CSV")

    if st.button('Export Expenses to CSV', key="export_expenses_button"):
        csv_file_path = export_expenses_to_csv(conn)
        if csv_file_path:
            st.success("Expenses CSV exported successfully.")

    recipient_email_exp = st.text_input(
        "Enter recipient's email address:", key="recipient_email_expenses"
    )
    if st.button("Send Expense CSV via Email", key="send_email_expenses_button"):
        if not recipient_email_exp.strip():
            st.warning("Please enter a valid email address.")
        else:
            csv_file_path = os.path.join('Files', 'expenses.csv')
            if os.path.exists(csv_file_path):
                try:
                    send_email_with_csv(
                        csv_file_path, "expenses.csv", recipient_email_exp
                    )
                    st.success("Email sent successfully!")
                except Exception as e:
                    st.error(f"Failed to send email: {e}")
            else:
                st.error("CSV file not found. Please export again.")

# ----------------------------------
# INCOME TAB
# ----------------------------------
elif selected_tab == "Income":
    st.title("Income")

    # 1. Add Income (session-state form)
    income_form_ui(conn)

    # 2. View Income by Month
    st.subheader("View Income by Month")
    month_options = [f"{i:02d}" for i in range(1, 13)]
    current_month = datetime.now().strftime('%m')
    selected_month = st.selectbox(
        'Month', month_options, index=month_options.index(current_month)
    )

    if st.button('View Income'):
        df = get_income_by_month(conn, selected_month)
        st.dataframe(df)
        if not df.empty:
            st.write(f"Total: ${df['Amount'].sum():.2f}")
        else:
            st.write("No income found for this month.")

    # 3. Manage Income Data
    st.subheader("Manage Income Data")

    col7, col8 = st.columns(2)
    with col7:
        st.markdown("**Delete an Income Entry**")
        income_id_to_delete = st.number_input(
            'Income ID to delete', value=0, key="income_id_delete"
        )
        if st.button('Delete Income', key="delete_income_button"):
            if income_id_to_delete > 0:
                delete_income(conn, int(income_id_to_delete))
                st.success(f"Income with ID {income_id_to_delete} deleted!")

    with col8:
        st.markdown("**Add a Payer**")
        new_payer = st.text_input('New Payer', key="new_payer_input")
        if st.button('Add Payer', key="add_payer_button"):
            if new_payer.strip():
                add_payer(conn, new_payer.strip())
                st.success(f'Payer "{new_payer}" added!')

        if st.button('List Payers', key="list_payers_button"):
            data = get_payers_L4D(conn)
            st.dataframe(data)

        payer_id_to_delete = st.number_input(
            'Payer ID to delete', value=0, key="payer_id_delete"
        )
        if st.button('Delete Payer', key="delete_payer_button"):
            if payer_id_to_delete > 0:
                delete_payer(conn, int(payer_id_to_delete))
                st.success(f'Payer with ID {payer_id_to_delete} deleted!')

    st.markdown("---")
    st.subheader("Add / Delete Income Category")

    col9, col10 = st.columns(2)
    with col9:
        new_categoryI = st.text_input(
            'New Income Category', key="new_categoryI_input"
        )
        if st.button('Add Income Category', key="add_categoryI_button"):
            if new_categoryI.strip():
                add_categoryI(conn, new_categoryI.strip())
                st.success(f'Income Category "{new_categoryI}" added!')

        if st.button('List Income Categories', key="list_categoriesI_button"):
            data = get_categoryI_L4D(conn)
            st.dataframe(data)

    with col10:
        categoryI_id_to_delete = st.number_input(
            'Income Category ID to delete', value=0, key="categoryI_id_delete"
        )
        if st.button('Delete Income Category', key="delete_categoryI_button"):
            if categoryI_id_to_delete > 0:
                delete_categoryI(conn, int(categoryI_id_to_delete))
                st.success(
                    f'Income Category with ID {categoryI_id_to_delete} deleted!'
                )

    st.markdown("---")
    st.subheader("Add / Delete Account")

    col11, col12 = st.columns(2)
    with col11:
        new_account_income = st.text_input(
            'New Account', key="new_account_income_input"
        )
        if st.button('Add Account (Income)', key="add_account_income_button"):
            if new_account_income.strip():
                add_account(conn, new_account_income.strip())
                st.success(f'Account "{new_account_income}" added!')

        if st.button('List Accounts (Income)', key="list_accounts_income_button"):
            data = get_accounts_L4D(conn)
            st.dataframe(data)

    with col12:
        account_id_to_delete_income = st.number_input(
            'Account ID to delete', value=0, key="account_id_delete_income"
        )
        if st.button('Delete Account (Income)', key="delete_account_income_button"):
            if account_id_to_delete_income > 0:
                delete_account(conn, int(account_id_to_delete_income))
                st.success(
                    f'Account with ID {account_id_to_delete_income} deleted!'
                )

    st.markdown("---")
    st.subheader("Export & Email Income CSV")

    if st.button('Export Income to CSV', key="export_income_button"):
        csv_file_path = export_income_to_csv(conn)
        if csv_file_path:
            st.success("Income CSV exported successfully.")

    recipient_email_inc = st.text_input(
        "Enter recipient's email address:", key="recipient_email_income"
    )
    if st.button("Send Income CSV via Email", key="send_email_income_button"):
        if not recipient_email_inc.strip():
            st.warning("Please enter a valid email address.")
        else:
            csv_file_path = os.path.join('Files', 'income.csv')
            if os.path.exists(csv_file_path):
                try:
                    send_email_with_csv(
                        csv_file_path, "income.csv", recipient_email_inc
                    )
                    st.success("Email sent successfully!")
                except Exception as e:
                    st.error(f"Failed to send email: {e}")
            else:
                st.error("CSV file not found. Please export again.")


# ----------------------------------
# SUMMARY TAB
# ----------------------------------
else:
    st.title("Summary Dashboard")

    # Retrieve aggregated data for summary
    df_expenses = pd.read_sql_query(
        "SELECT category, SUM(amount) as total FROM expenses GROUP BY category",
        conn
    )
    df_income = pd.read_sql_query(
        "SELECT categoryI, SUM(amount) as total FROM income GROUP BY categoryI",
        conn
    )

    # Pie charts
    if not df_expenses.empty and not df_income.empty:
        fig_pie = plot_expense_income_distribution(df_expenses, df_income)
        st.plotly_chart(fig_pie)
    else:
        st.write("No data available for Expense and Income Distribution chart.")

    # Bar chart
    if not df_expenses.empty and not df_income.empty:
        fig_bar = plot_category_wise(df_expenses, df_income)
        st.plotly_chart(fig_bar)
    else:
        st.write("No data available for Category-wise Expenses and Income chart.")


# 🔹 ADD THE FOOTER AT THE END

footer_html = """
<style>
.footer-container {
    width: 100%;
    background-color: #f8f9fa;
    text-align: center;
    padding: 10px 0;
    border-top: 1px solid #ddd;
    margin-top: 30px;  /* space above footer so it doesn't crowd content */
}

.footer-container p {
    margin: 0;
    font-weight: bold;
    color: #333;
    display: inline-block; /* keep text & links in one line */
}

.footer-container a {
    text-decoration: none;
    margin: 0 10px; /* spacing between links */
    color: #ff4b4b;
    font-weight: 600;
}

.footer-container img {
    width: 18px; 
    vertical-align: middle;
    margin-right: 5px; /* space between icon & text */
}
</style>

<div class="footer-container">
    <p>
        Made with ❤️ by Sarjak Maniar | 
        <a href="https://www.linkedin.com/in/sarjak369/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png"/> LinkedIn
        </a>
        <a href="https://github.com/Sarjak369" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png"/> GitHub
        </a>
        <a href="mailto:sarjkm369@gmail.com">
            <img src="https://cdn-icons-png.flaticon.com/512/732/732200.png"/> Email
        </a>
    </p>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
