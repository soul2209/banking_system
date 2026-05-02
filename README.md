# 🏦 Banking Management System (Python OOP Project)

A terminal-based banking system built using **Object-Oriented Programming (OOP) in Python**.  
This project simulates real-world banking operations like account creation, transactions, and financial analysis.

---

## 📌 Features

### 👤 Account Management
- Create **Current** and **Savings** accounts  
- Secure **4-digit PIN authentication**  
- Change PIN functionality  

### 💰 Transactions
- Deposit money  
- Withdraw money  
- Transfer funds between accounts  
- Fraud detection for large transactions (> ₹50,000)  

### 📊 Financial Tracking
- Transaction history with timestamps  
- Monthly spending analysis  
- Largest expense tracking  

### 🧾 File Handling
- Save account data to file  
- Auto-generate transaction receipts  

### 🏦 OOP Concepts Used
- **Encapsulation** → Private balance & PIN  
- **Inheritance** → `SavingsAccount` extends `BankAccount`  
- **Polymorphism** → Different account behaviors  
- **Class Variables** → Track total accounts  

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Library Used:** `datetime`  
- **Concepts:** OOP, File Handling  

---

## 📂 Project Structure
bank.py # Main program file
account_.txt # Saved account data
receipt_.txt # Generated transaction receipts

---
MAIN MENU
1. Create Account
2. Login
3. Total Accounts
0. Exit
---
##🔐 Security Features
1.PIN-based login system
2.Private attributes using encapsulation
3.Fraud alert for high-value transactions
---
##📈 Example Output
✔ ₹5000.00 deposited. New Balance: ₹5000.00
🧾 Receipt saved: receipt_1234_02-05-2026.txt

