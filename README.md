# 🏦 Banking Management System (Python OOP Project)

A terminal-based banking system developed using **Object-Oriented Programming (OOP) in Python**.

This project simulates real-world banking operations such as:

- Account creation
- Secure transactions
- Fund transfers
- Financial tracking
- Admin management

---

# 📌 Features

## 👤 Account Management

- Create **Current** and **Savings** accounts
- Secure **4-digit PIN authentication**
- Change PIN functionality
- Admin-controlled account updates
- Delete and restore accounts

---

## 💰 Banking Operations

- Deposit money
- Withdraw money
- Transfer funds between accounts
- Prevent self-transfers
- Balance inquiry system
- Input validation for invalid transactions

---

## 📊 Financial Tracking

- Transaction history with timestamps
- Monthly transaction analysis
- Deposit and expense tracking
- Largest expense analysis
- Total transaction count

---

## 🧾 File Handling

- Save account details to text files
- Automatically generate transaction receipts
- Store transaction history permanently

### Generated Files

```text
account_<account_number>.txt
receipt_<account_number>_<timestamp>.txt
```

---

# 🛡️ Security Features

- PIN-based authentication system
- Encapsulation using private variables
- Admin authentication system
- Validation for invalid PINs
- Duplicate account prevention
- Insufficient balance protection

---

# 🏦 Admin Panel Features

## 🔐 Admin Login

### Default Admin Credentials

```text
Admin ID : admin
Password : 1234
```

---

## ⚙️ Admin Operations

- View all registered accounts
- Update user information
- Reset user PINs
- Change account types
- Delete accounts
- Restore deleted accounts
- View bank statistics

---

# 🧠 OOP Concepts Used

## 🔒 Encapsulation

Private attributes protect sensitive data like balance and PIN.

```python
self.__balance
self.__pin
```

---

## 🧬 Inheritance

`SavingsAccount` inherits features from `BankAccount`.

```python
class SavingsAccount(BankAccount):
```

---

## 🔄 Polymorphism

Savings accounts support additional interest functionality.

```python
apply_interest()
```

---

## 📦 Class Variables

Used for tracking total bank accounts.

```python
total_accounts = 0
```

---

# 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Language | Python 3 |
| Library Used | datetime |
| Concepts | OOP, File Handling, Validation |

---

# 📂 Project Structure

```text
banking_system.py
│
├── account_<account_number>.txt
├── receipt_<account_number>_<timestamp>.txt
```

---

# 📋 Main Menu

```text
1. Create Account
2. User Login
3. Admin Login
4. Total Accounts
0. Exit
```

---

# 👤 User Menu

```text
1. Deposit
2. Withdraw
3. Check Balance
4. Transfer Money
5. Transaction History
6. Monthly Analysis
7. Change PIN
8. Save Account Data
9. Apply Interest (Savings Only)
0. Logout
```

---

# 📈 Example Output

## 💵 Deposit Example

```text
✔ ₹5000.00 deposited successfully.
Current Balance: ₹5000.00
```

---

## 🧾 Receipt Example

```text
🧾 Receipt saved: receipt_1001_10-05-2026_18-45-22.txt
```

---

# ▶️ How to Run the Project

## Step 1 — Install Python

Download Python from the official website:

https://www.python.org/

---

## Step 2 — Save the File

Save the program as:

```text
banking_system.py
```

---

## Step 3 — Run the Program

Open terminal or command prompt:

```bash
python banking_system.py
```

---

# ✅ Advantages of the Project

- Beginner-friendly Python project
- Real-world banking simulation
- Strong OOP implementation
- Interactive menu-driven interface
- Demonstrates file handling concepts
- Includes admin management system

---

# 🚀 Future Improvements

Possible future upgrades:

- SQLite/MySQL database integration
- GUI using Tkinter or PyQt
- Password encryption/hashing
- ATM simulation
- Mobile banking features
- Email/SMS transaction alerts
- Online transaction support

---

# 📌 Conclusion

The **Banking Management System** demonstrates practical implementation of:

- Object-Oriented Programming
- Encapsulation
- Inheritance
- File Handling
- Data Validation
- Menu-Driven Programming

It provides a complete terminal-based banking simulation while maintaining clean code structure and modular design.
