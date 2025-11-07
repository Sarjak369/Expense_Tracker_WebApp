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

## UI Snapshots

<img width="1905" height="900" alt="1" src="https://github.com/user-attachments/assets/ff671e6a-aeb8-40f7-bd3c-f8b563ee8cff" />

<img width="1909" height="855" alt="2" src="https://github.com/user-attachments/assets/89ba4554-fc1d-4a37-a822-81c268286950" />

<img width="1897" height="877" alt="3" src="https://github.com/user-attachments/assets/40ff8bf2-2c3a-4bd6-af46-6567209ebef5" />

<img width="1904" height="914" alt="4" src="https://github.com/user-attachments/assets/9f863e47-7ee7-4cca-9268-cb9a07f4008c" />

<img width="1889" height="898" alt="5" src="https://github.com/user-attachments/assets/5c4cedf4-5b0a-476d-882e-6a049f59ae3d" />

<img width="1908" height="915" alt="6" src="https://github.com/user-attachments/assets/7e56629b-9169-44d6-87ff-2da57d93ffac" />

<img width="1902" height="791" alt="7" src="https://github.com/user-attachments/assets/502d99d6-644d-400d-8892-d1c5e80b4035" />

<img width="1890" height="563" alt="8" src="https://github.com/user-attachments/assets/0a915818-e1a7-4d42-9dc6-750b317ae473" />

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

