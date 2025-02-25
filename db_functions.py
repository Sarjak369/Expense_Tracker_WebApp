from sqlite3 import Connection
import streamlit as st
import os
import sqlite3
from sqlite3 import Error

import pandas as pd
import streamlit as st  # For download buttons in export functions


def create_connection():
    """Create a SQLite database connection."""
    try:
        conn = sqlite3.connect('exp_track.db')  # using relative path
        return conn
    except sqlite3.Error as e:
        print(f"Error occurred: {e}")
        return None


def create_table(conn):
    """Create tables if they do not exist."""
    try:
        c = conn.cursor()
        # Expenses
        c.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                amount NUMERIC(5,2) NOT NULL,
                payee TEXT NOT NULL,
                category TEXT,
                account TEXT,
                note TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS payee (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS category (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS account (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        # Income
        c.execute('''
            CREATE TABLE IF NOT EXISTS income (
                id INTEGER PRIMARY KEY,
                date TEXT NOT NULL,
                amount NUMERIC(5,2) NOT NULL,
                payer TEXT NOT NULL,
                categoryI TEXT,
                account TEXT,
                note TEXT
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS payer (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        c.execute('''
            CREATE TABLE IF NOT EXISTS categoryI (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        conn.commit()
    except Error as e:
        print(e)


# -----------------------
# Expense-Related
# -----------------------
def add_expense(conn, date, amount, payee, category, account, note):
    try:
        c = conn.cursor()
        c.execute("""
            INSERT INTO expenses (date, amount, payee, category, account, note)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (date, amount, payee, category, account, note))
        conn.commit()
    except Error as e:
        print(e)


def get_expenses_by_month(conn, month):
    try:
        c = conn.cursor()
        query = "SELECT * FROM expenses WHERE strftime('%m', date) = ?"
        c.execute(query, (month,))
        rows = c.fetchall()
        df = pd.DataFrame(
            rows,
            columns=['ID', 'Date', 'Amount', 'Payee',
                     'Category', 'Account', 'Note']
        )
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


def export_expenses_to_csv(conn: Connection):
    """Export all expenses to a CSV in the 'Files' directory and provide a download button."""
    try:
        # 1. Create 'Files' folder if it doesn't exist
        folder_path = 'Files'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # 2. Write CSV to 'Files/expenses.csv'
        df = pd.read_sql_query("SELECT * FROM expenses", conn)
        csv_file_path = os.path.join(folder_path, 'expenses.csv')
        df.to_csv(csv_file_path, index=False)

        # 3. Provide a download button for the exported file
        with open(csv_file_path, 'rb') as f:
            st.download_button(
                label="Download Expenses CSV",
                data=f,
                file_name="expenses.csv",
                mime="text/csv"
            )

        st.success("Expense data exported successfully.")
        return csv_file_path  # Return the file path for further use

    except Exception as e:
        st.error(f"Error exporting data: {e}")
        return None


# -----------------------
# Payee
# -----------------------
def add_payee(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO payee (name) VALUES (?)", (name,))
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


def get_payees(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM payee")
        rows = c.fetchall()
        names = [row[0] for row in rows]
        return names
    except Error as e:
        print(e)


def get_payees_L4D(conn):
    """Get payees for listing ID and Name."""
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM payee")
        rows = c.fetchall()
        return rows
    except Error as e:
        print(e)


# -----------------------
# Category
# -----------------------
def add_category(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO category (name) VALUES (?)", (name,))
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


def get_categories(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM category")
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


# -----------------------
# Account
# -----------------------
def add_account(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO account (name) VALUES (?)", (name,))
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


def get_accounts(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM account")
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


# --------------------
# Income-Related
# --------------------
def add_income(conn, date, amount, payer, categoryI, account, note):
    try:
        c = conn.cursor()
        c.execute("""
            INSERT INTO income (date, amount, payer, categoryI, account, note)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (date, amount, payer, categoryI, account, note))
        conn.commit()
    except Error as e:
        print(e)


def get_income_by_month(conn, month):
    try:
        c = conn.cursor()
        query = "SELECT * FROM income WHERE strftime('%m', date) = ?"
        c.execute(query, (month,))
        rows = c.fetchall()
        df = pd.DataFrame(
            rows,
            columns=['ID', 'Date', 'Amount', 'Payer',
                     'Cat_Income', 'Account', 'Note']
        )
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


def export_income_to_csv(conn: Connection):
    """Export all income to a CSV in the 'Files' directory and provide a download button."""
    try:
        # 1. Ensure 'Files' folder exists
        folder_path = 'Files'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # 2. Write CSV to 'Files/income.csv'
        df = pd.read_sql_query("SELECT * FROM income", conn)
        csv_file_path = os.path.join(folder_path, 'income.csv')
        df.to_csv(csv_file_path, index=False)

        # 3. Provide a download button for the exported file
        with open(csv_file_path, 'rb') as f:
            st.download_button(
                label="Download Income CSV",
                data=f,
                file_name="income.csv",
                mime="text/csv"
            )

        st.success("Income data exported successfully.")
        return csv_file_path  # Return the file path for further use

    except Exception as e:
        st.error(f"Error exporting data: {e}")
        return None


# -----------------------
# Payer
# -----------------------
def add_payer(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO payer (name) VALUES (?)", (name,))
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


def get_payers(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM payer")
        rows = c.fetchall()
        names = [row[0] for row in rows]
        return names
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


# -----------------------
# CategoryI (Income)
# -----------------------
def add_categoryI(conn, name):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO categoryI (name) VALUES (?)", (name,))
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


def get_categoryI(conn):
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM categoryI")
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
