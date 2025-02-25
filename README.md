# Expense Tracker Web App

## 🚀 Overview
The **Expense Tracker Web App** is a powerful and user-friendly financial management tool designed to help track my income and expenses efficiently. Built with **Streamlit**, the app provides an interactive interface to manage financial transactions, visualize spending patterns, and export data for analysis.

🔗 **Live Demo:** [Expense Tracker Web App](https://sarjakexpensetrackerwebapp.streamlit.app/)

## 🎯 Features
- **Add & Manage Expenses** – Log expenses with date, amount, category, and payee.
- **Add & Manage Income** – Record income transactions with payer details.
- **Category & Account Management** – Add, list, and delete custom expense/income categories and accounts.
- **Data Visualization** – Interactive pie charts and bar charts to analyze spending & income trends.
- **CSV Export & Email** – Export financial data to CSV files and send via email directly from the app.
- **Intuitive UI** – Responsive design with an easy-to-use navigation menu.
- **Deployment** – Hosted on **Streamlit Cloud** for seamless accessibility.

## 🛠️ Technologies Used
- **Python** – Backend logic and database operations.
- **Streamlit** – Web framework for UI & interactivity.
- **SQLite** – Lightweight database to store transactions.
- **Plotly** – For interactive data visualization.
- **Pandas** – Data manipulation and analysis.
- **SMTP (Email API)** – Send expense/income reports via email.

## 📌 Project Structure
```
Expense_Tracker_WebApp/
│── .venv/                 # Virtual environment
│── Files/                 # Stores exported CSV files
│── __pycache__/           # Cached Python files
│── app.py                 # Main Streamlit app
│── db_functions.py        # Database operations
│── forms.py               # UI form logic
│── AppEmail.py            # Email handling script
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

## 📊 How It Works
### **1️⃣ Adding Transactions**
- I can enter **income** and **expense** details via simple forms.
- Categories, payees, and accounts can be added dynamically.

### **2️⃣ Viewing Monthly Reports**
- I can select a **month** to view all transactions.
- A summary of total income and expenses is displayed.

### **3️⃣ Data Export & Email**
- I can export data as a **CSV file**.
- The CSV file can be sent via **email** from within the app.

### **4️⃣ Data Visualization**
- **Pie Charts**: Compare expense vs. income distribution.
- **Bar Charts**: Analyze category-wise spending patterns.

## 🔧 Setup & Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/Sarjak369/Expense_Tracker_WebApp.git
cd Expense_Tracker_WebApp
```
### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```
### **3️⃣ Run the App**
```sh
streamlit run app.py
```
### **4️⃣ Deploy on Streamlit Cloud**
- Push changes to GitHub.
- Streamlit Cloud will automatically detect and redeploy.

## 🌟 Future Enhancements
- **Multi-user authentication** for personalized tracking.
- **Budgeting & Alerts** for overspending categories.
- **Advanced analytics** for deeper financial insights.

## 🏆 Contributing
Contributions are welcome! Feel free to **fork**, **create a branch**, and submit a **pull request**.

## 📩 Contact
👨‍💻 **Sarjak Maniar**  
Email: [sarjkm369@gmail.com](mailto:sarjkm369@gmail.com)  
LinkedIn: [Sarjak369](https://www.linkedin.com/in/sarjak369/)  
GitHub: [Sarjak369](https://github.com/Sarjak369)

