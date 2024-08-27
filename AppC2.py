#   streamlit run Y:\0Python-Working\ExpenseTracker\ExTrackBing\AppC2.py
#   streamlit run C:\inetpub\wwwroot\image4.cf\b\AppC2.py

import streamlit as st
import sqlite3
from sqlite3 import Error
import pandas as pd
from datetime import datetime
# pip install streamlit-option-menu
from streamlit_option_menu import option_menu

import subprocess
import sys
import os

import plotly.express as px
import plotly.graph_objects as go
import plotly.express as px


path = '/Users/sarjak/Desktop/My_Projects/Projects_2024/expense_tracker/'

fileRunE = 'AppEmail4E.py'
fileRunI = 'AppEmail4I.py'


def create_connection():
    try:
        conn = sqlite3.connect('exp_track.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        return None
### Income  ####


def create_table(conn):
    try:
        c = conn.cursor()
        # Expenses
        c.execute('''CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date text NOT NULL, amount numeric(5,2) NOT NULL, payee text NOT NULL, category text, account text, note text)''')
        c.execute(
            '''CREATE TABLE IF NOT EXISTS payee (id INTEGER PRIMARY KEY,name text NOT NULL)''')
        c.execute(
            '''CREATE TABLE IF NOT EXISTS category (id INTEGER PRIMARY KEY,name text NOT NULL)''')
        c.execute(
            '''CREATE TABLE IF NOT EXISTS account (id INTEGER PRIMARY KEY,name text NOT NULL)''')
        # Income
        c.execute('''CREATE TABLE IF NOT EXISTS income (id INTEGER PRIMARY KEY,date text NOT NULL, amount numeric(5,2) NOT NULL, payer text NOT NULL, categoryI text, account text, note text)''')
        c.execute(
            '''CREATE TABLE IF NOT EXISTS payer (id INTEGER PRIMARY KEY,name text NOT NULL)''')
        c.execute(
            '''CREATE TABLE IF NOT EXISTS categoryI (id INTEGER PRIMARY KEY,name text NOT NULL)''')
        conn.commit()
    except Error as e:
        print(e)

# -------Expenses ----------


def add_expense(conn, date, amount, payee, category, account, note):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO expenses (date, amount, payee, category, account, note) VALUES (?, ?, ?, ?, ?, ?)",
                  (date, amount, payee, category, account, note))
        conn.commit()
    except Error as e:
        print(e)


def add_payee(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO payee (name) VALUES (?)", (name,))
        conn.commit()
    except Error as e:
        print(e)


def add_category(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO category (name) VALUES (?)", (name,))
        conn.commit()
    except Error as e:
        print(e)


def add_account(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO account (name) VALUES (?)", (name,))
        conn.commit()
    except Error as e:
        print(e)


def get_payees_L4D(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM payee")
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)


def get_payees(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM payee")
        rows = c.fetchall()
        names = [row[0] for row in rows]
        return names
    except Error as e:
        print(e)


def get_categories_L4D(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM category")
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)


def get_categories(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM category")
        rows = c.fetchall()
        names = [row[0] for row in rows]
        return names
    except Error as e:
        print(e)


def get_accounts_L4D(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM account")
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)


def get_accounts(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM account")
        rows = c.fetchall()
        names = [row[0] for row in rows]
        return names
    except Error as e:
        print(e)


def get_expenses_by_month(conn, month):
    try:
        c = conn.cursor()
        query = "SELECT * FROM expenses WHERE strftime('%m', date) = ?"
        c.execute(query, (month,))

        rows = c.fetchall()

        df = pd.DataFrame(
            rows, columns=['ID', 'Date', 'Amount', 'Payee', 'Category', 'Account', 'Note'])

        return df
    except Error as e:
        print(e)


def delete_expense(conn, id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM expenses WHERE id=?", (id,))
        conn.commit()
    except Error as e:
        print(e)


def delete_payee(conn, id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM payee WHERE id=?", (id,))
        conn.commit()
    except Error as e:
        print(e)


def delete_category(conn, id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM category WHERE id=?", (id,))
        conn.commit()
    except Error as e:
        print(e)


def delete_account(conn, id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM account WHERE id=?", (id,))
        conn.commit()
    except Error as e:
        print(e)


def export_expenses_to_csv(conn):
    try:
        df = pd.read_sql_query("SELECT * FROM expenses", conn)
        df.to_csv(path+'expenses.csv', index=False)

    except Error as e:
        print(e)

# -------INcome ----------# some repetition in functions


def add_income(conn, date, amount, payer, categoryI, account, note):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO income (date, amount, payer, categoryI, account, note) VALUES (?, ?, ?, ?, ?, ?)",
                  (date, amount, payer, categoryI, account, note))
        conn.commit()
    except Error as e:
        print(e)


def add_payer(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO payer (name) VALUES (?)", (name,))
        conn.commit()
    except Error as e:
        print(e)


def add_categoryI(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO categoryI (name) VALUES (?)", (name,))
        conn.commit()
    except Error as e:
        print(e)


def get_payers_L4D(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM payer")
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)


def get_payers(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM payer")
        rows = c.fetchall()
        names = [row[0] for row in rows]
        return names
    except Error as e:
        print(e)


def get_categoryI_L4D(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM categoryI")
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)


def get_categoryI(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM categoryI")
        rows = c.fetchall()
        names = [row[0] for row in rows]
        return names
    except Error as e:
        print(e)


def get_income_by_month(conn, month):
    try:
        c = conn.cursor()
        query = "SELECT * FROM income WHERE strftime('%m', date) = ?"
        c.execute(query, (month,))

        rows = c.fetchall()

        df = pd.DataFrame(rows, columns=[
                          'ID', 'Date', 'Amount', 'Payer', 'Cat_Income', 'Account', 'Note'], index=None)

        return df
    except Error as e:
        print(e)


def delete_income(conn, id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM income WHERE id=?", (id,))
        conn.commit()
    except Error as e:
        print(e)


def delete_payer(conn, id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM payer WHERE id=?", (id,))
        conn.commit()
    except Error as e:
        print(e)


def delete_categoryI(conn, id):
    try:
        c = conn.cursor()
        c.execute("DELETE FROM categoryI WHERE id=?", (id,))
        conn.commit()
    except Error as e:
        print(e)


def export_income_to_csv(conn):
    try:
        df = pd.read_sql_query("SELECT * FROM income", conn)
        df.to_csv(path+'income.csv', index=False)

    except Error as e:
        print(e)


def plot_category_wise(df_expenses, df_income):
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
    # Aggregate expenses and income data
    expense_sum = df_expenses.groupby('category')['total'].sum()
    # Note - for income, column name is categoryI
    income_sum = df_income.groupby('categoryI')['total'].sum()

    # Generate colors dynamically
    num_expense_colors = len(expense_sum)
    num_income_colors = len(income_sum)

    expense_colors = px.colors.qualitative.Plotly[:num_expense_colors]
    income_colors = px.colors.qualitative.Plotly[:num_income_colors]

    # Create Pie chart for Expenses
    fig = go.Figure()
    fig.add_trace(go.Pie(
        labels=expense_sum.index,
        values=expense_sum.values,
        name='Expenses',
        marker=dict(colors=expense_colors)
    ))

    # Create Pie chart for Income
    fig.add_trace(go.Pie(
        labels=income_sum.index,
        values=income_sum.values,
        name='Income',
        marker=dict(colors=income_colors)
    ))

    # Update layout
    fig.update_layout(
        title_text='Expense and Income Distribution',
        grid=dict(rows=1, columns=2),
        annotations=[dict(text='Expenses', x=0.18, y=0.5, font_size=20, showarrow=False),
                     dict(text='Income', x=0.82, y=0.5, font_size=20, showarrow=False)]
    )

    return fig


conn = create_connection()
create_table(conn)

# Config streamlit page
st.set_page_config(page_title='Finance Tracker',
                   page_icon=':coin:', layout='wide')

# Menu Tabs
menu_tabs = ['Expense', 'Income', 'Summary']
selected_tab = option_menu(
    menu_title=None,
    options=menu_tabs,
    icons=['pencil-fill', 'pencil-fill', 'bar-chart-fill'],
    orientation='horizontal'
)

#  Fill colouring for buttons
html_code = """
    <style>
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
    }
    
    </style>
"""
st.markdown(html_code, unsafe_allow_html=True)


st.markdown("""
    <style>
            .streamlit-expanderHeader > div:nth-child(1) > p:nth-child(1) > strong:nth-child(1) {
         font-size: 24px;
        color: red;
            }
    </style>
""", unsafe_allow_html=True)

# Expense Tab

if selected_tab == "Expense":
    date = st.date_input('Date', value=None)
    amount = st.number_input('Amount ($)', value=0.00)
    payee = st.selectbox('Payee', get_payees(conn))
    category = st.selectbox('Category', get_categories(conn))
    account = st.selectbox('Account', get_accounts(conn))
    note = st.text_area('Note', max_chars=150)

    if st.button('Submit Expense'):
        if payee:  # Check if payee is not empty
            add_expense(conn, date.strftime('%Y-%m-%d'),
                        amount, payee, category, account, note)
            st.success('Expense added!')
        else:
            st.error('Payee cannot be empty!')

    # Remove or fix the incorrect Streamlit function call
    # st.experimental_user()

    st.subheader('View Expenses by Month')
    month_options = ['01', '02', '03', '04', '05',
                     '06', '07', '08', '09', '10', '11', '12']
    current_month = datetime.now().strftime('%m')
    selected_month = st.selectbox(
        'Month', month_options, index=month_options.index(current_month))

    if st.button('View Expenses'):
        df = get_expenses_by_month(conn, selected_month)
        st.dataframe(df)
        st.write('Total: $', df['Amount'].sum())


## _____HIDDEN in expander_____##

    with st.expander("**EXPENSE FUNCTIONS** - *Add New Payee, Category, Account & to CSV*"):
        # st.markdown("**This text is bold and red.**", unsafe_allow_html=True)

        st.subheader('Delete Expense')

        id = st.number_input('Expense ID to delete', value=0)
        if st.button('Delete Expense'):
            delete_expense(conn, int(id))
            st.success('Expense deleted!')
            st.experimental_rerun()

        st.subheader('Add Payee')

        new_payee = st.text_input('New Payee')
        if st.button('Add Payee'):
            if new_payee != '':
                add_payee(conn, new_payee)
                st.success('Payee added!')
                # st.experimental_rerun()

        if st.button('List IDs & Payees'):
            getIt = get_payees_L4D(conn)
            st.dataframe(getIt)

        id = st.number_input('Payee ID to delete', value=0)
        if st.button('Delete Payee'):
            delete_payee(conn, int(id))
            st.success('Payee deleted!')
            st.experimental_rerun()

        st.subheader('Add Category')
        new_category = st.text_input('New Category')

        if st.button('Add Category'):
            add_category(conn, new_category)
            st.success('Category added!')

        if st.button('List IDs & Categories'):
            getIt = get_categories_L4D(conn)
            st.dataframe(getIt)

        id = st.number_input('Category ID to delete', value=0)
        if st.button('Delete Category'):
            delete_category(conn, int(id))
            st.success('Category deleted!')
            st.experimental_rerun()

        st.subheader('Add Account')
        new_account = st.text_input('New Account')

        if st.button('Add Account'):
            add_account(conn, new_account)
            st.success('Account added!')

        if st.button('List IDs & Accounts'):
            getIt = get_accounts_L4D(conn)
            st.dataframe(getIt)

        id = st.number_input('Account ID to delete', value=0)
        if st.button('Delete Account'):
            delete_account(conn, int(id))
            st.success('Account deleted!')
            st.experimental_rerun()

        if st.button('Export Expenses to CSV'):
            export_expenses_to_csv(conn)
            subprocess.run([f"{sys.executable}", path+fileRunE])
            st.success('Expense data exported to '+path + 'Expenses.csv')
        #     if os.path.exists(path + fileIn):
        #         os.remove(path + fileIn)
        #         os.remove(path + fileIn2)
        #         st.success(f"The file {fileIn} was deleted from the {path} directory.")
        #    else:
        #         st.warning(f"The file {fileIn} was not found in the {path} directory.")


elif selected_tab == 'Income':
    #   st.title('Income Tracker')

    date = st.date_input('Date', value=None)
    amount = st.number_input('Amount ($)', value=0.0)
    payer = st.selectbox('Payer', get_payers(conn))
    categoryI = st.selectbox('Income Category', get_categoryI(conn))
    account = st.selectbox('Account', get_accounts(conn))
    note = st.text_area('Note', max_chars=150)

    if st.button('Submit'):
        add_income(conn, date.strftime('%Y-%m-%d'),
                   amount, payer, categoryI, account, note)
        st.success('Income added!')
        # st.experimental_rerun()

    st.subheader('View Income by Month')
    month_options = ['01', '02', '03', '04', '05',
                     '06', '07', '08', '09', '10', '11', '12']
    current_month = datetime.now().strftime('%m')
    selected_month = st.selectbox(
        'Month', month_options, index=month_options.index(current_month))

    if st.button('View Income'):
        df = get_income_by_month(conn, selected_month)
        st.dataframe(df)
        st.write('Total: $', df['Amount'].sum())


## _____HIDDEN in expander_____##
    with st.expander("**INCOME FUNCTIONS** - *Add New payer, Category, Account & to CSV*"):

        st.subheader('Delete Income Row')
        id = st.number_input('Income ID to delete', value=0)
        if st.button('Delete Income'):
            delete_income(conn, int(id))
            st.success('Income deleted!')
            st.experimental_rerun()

        st.subheader('Add Payer')
        new_payer = st.text_input('New Payer')

        if st.button('Add Payer'):
            add_payer(conn, new_payer)
            st.success('Payer added!')
            # st.experimental_rerun()

        if st.button('List IDs & Payers'):
            getIt = get_payers_L4D(conn)
            st.dataframe(getIt)

        id = st.number_input('Payer ID to delete', value=0)
        if st.button('Delete Payer'):
            delete_payer(conn, int(id))
            st.success('Payer deleted!')
            st.experimental_rerun()

        st.subheader('Add Income Category')
        new_categoryI = st.text_input('New Income Category')

        if st.button('Add Income Category'):
            add_categoryI(conn, new_categoryI)
            st.success('Income Category added!')
            st.experimental_rerun()

        if st.button('List IDs & Income Categories'):
            getIt = get_categoryI_L4D(conn)
            st.dataframe(getIt)

        id = st.number_input('Income Category ID to delete', value=0)
        if st.button('Delete Income Category'):
            delete_categoryI(conn, int(id))
            st.success('Income Category deleted!')
            st.experimental_rerun()

        st.subheader('Add Account')
        new_account = st.text_input('New Account')

        if st.button('Add Account'):
            add_account(conn, new_account)
            st.success('Account added!')

        if st.button('List IDs & Accounts'):
            getIt = get_accounts_L4D(conn)
            st.dataframe(getIt)

        id = st.number_input('Account ID to delete', value=0)
        if st.button('Delete Account'):
            delete_account(conn, int(id))
            st.success('Account deleted!')
            st.experimental_rerun()

        if st.button('Export Income to CSV'):
            export_income_to_csv(conn)
            subprocess.run([f"{sys.executable}", path+fileRunI])
            st.success('Income data exported to '+path + 'income.csv')
            # if os.path.exists(path + fileIn):
            #     os.remove(path + fileIn)
            #     os.remove(path + fileIn2)
            #     st.success(f"The file {fileIn} was deleted from the {path} directory.")
            # else:
            #     st.warning(f"The file {fileIn} was not found in the {path} directory.")

else:
    # st.write("Summary content goes here.")
    st.title('Summary Dashboard')

    # Retrieve data for expenses and income
    df_expenses = pd.read_sql_query(
        "SELECT category, SUM(amount) as total FROM expenses GROUP BY category", conn)
    df_income = pd.read_sql_query(
        "SELECT categoryI, SUM(amount) as total FROM income GROUP BY categoryI", conn)

    # Plot Expense and Income Distribution
    if not df_expenses.empty and not df_income.empty:
        fig_pie = plot_expense_income_distribution(df_expenses, df_income)
        st.plotly_chart(fig_pie)
    else:
        st.write("No data available for Expense and Income Distribution chart.")

    # Plot Category-wise Expenses and Income
    if not df_expenses.empty and not df_income.empty:
        fig_bar = plot_category_wise(df_expenses, df_income)
        st.plotly_chart(fig_bar)
    else:
        st.write("No data available for Category-wise Expenses and Income chart.")
