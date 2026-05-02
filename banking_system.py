"""
====================================================
  Banking System - CA 2 Mini Project
  OOP Python | Terminal Based
  Library Used: datetime
====================================================
"""

from datetime import datetime


# ─────────────────────────────────────────────────
#  BASE CLASS: BankAccount
# ─────────────────────────────────────────────────
class BankAccount:
    total_accounts = 0  # Class variable

    def __init__(self, name, account_number, pin):
        self.__pin = pin                   # Encapsulation - private PIN
        self.__balance = 0.0              # Encapsulation - private balance
        self.name = name
        self.account_number = account_number
        self.account_type = "Current"
        self.transaction_history = []
        BankAccount.total_accounts += 1

    # ── PIN ──────────────────────────────────────
    def verify_pin(self, pin):
        return self.__pin == pin

    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.__pin = new_pin
            print("  ✔ PIN changed successfully.")
        else:
            print("  ✘ Incorrect old PIN.")

    # ── BALANCE ──────────────────────────────────
    def get_balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount

    # ── DEPOSIT ──────────────────────────────────
    def deposit(self, amount):
        if amount <= 0:
            print("  ✘ Invalid deposit amount.")
            return False
        self.__balance += amount
        self._log_transaction("DEPOSIT", amount)
        print(f"  ✔ ₹{amount:.2f} deposited. New Balance: ₹{self.__balance:.2f}")
        return True

    # ── WITHDRAW ─────────────────────────────────
    def withdraw(self, amount):
        if amount <= 0:
            print("  ✘ Invalid withdrawal amount.")
            return False
        if amount > self.__balance:
            print("  ✘ Insufficient balance.")
            return False
        # Fraud detection
        if amount > 50000:
            print("  ⚠  FRAUD ALERT: Large transaction detected (₹{:.2f})".format(amount))
            confirm = input("  Confirm this transaction? (yes/no): ").strip().lower()
            if confirm != "yes":
                print("  Transaction cancelled.")
                return False
        self.__balance -= amount
        self._log_transaction("WITHDRAWAL", amount)
        print(f"  ✔ ₹{amount:.2f} withdrawn. New Balance: ₹{self.__balance:.2f}")
        return True

    # ── TRANSFER ─────────────────────────────────
    def transfer(self, target_account, amount):
        print(f"\n  Transferring ₹{amount:.2f} to {target_account.name}...")
        # Validate and deduct manually to avoid logging a generic WITHDRAWAL
        if amount <= 0:
            print("  ✘ Invalid transfer amount.")
            return False
        if amount > self._BankAccount__balance:
            print("  ✘ Insufficient balance.")
            return False
        if amount > 50000:
            print("  ⚠  FRAUD ALERT: Large transaction detected (₹{:.2f})".format(amount))
            confirm = input("  Confirm this transaction? (yes/no): ").strip().lower()
            if confirm != "yes":
                print("  Transaction cancelled.")
                return False
        # Deduct & credit directly — log as TRANSFER (not WITHDRAWAL/DEPOSIT)
        self._BankAccount__balance -= amount
        target_account._BankAccount__balance += amount
        self._log_transaction(f"TRANSFER TO   {target_account.account_number}", amount)
        target_account._log_transaction(f"TRANSFER FROM {self.account_number}", amount)
        print(f"  ✔ ₹{amount:.2f} transferred to {target_account.name}.")
        print(f"  Your Balance: ₹{self._BankAccount__balance:.2f}")
        self._save_receipt("TRANSFER", amount, target_account.name)
        return True

    # ── TRANSACTION LOG ──────────────────────────
    def _log_transaction(self, txn_type, amount):
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        entry = f"[{timestamp}] {txn_type:<30} ₹{amount:.2f}"
        self.transaction_history.append(entry)

    def show_history(self):
        print(f"\n  {'─'*55}")
        print(f"  Transaction History for {self.name} ({self.account_number})")
        print(f"  {'─'*55}")
        if not self.transaction_history:
            print("  No transactions yet.")
        else:
            for txn in self.transaction_history:
                print(f"  {txn}")
        print(f"  {'─'*55}")

    # ── MONTHLY SPENDING ANALYSIS ─────────────────
    def monthly_analysis(self):
        current_month = datetime.now().strftime("%m-%Y")
        withdrawals = []
        deposits = []
        for txn in self.transaction_history:
            if current_month in txn:
                if "WITHDRAWAL" in txn or "TRANSFER TO" in txn:
                    amount = float(txn.split("₹")[-1])
                    withdrawals.append(amount)
                elif "DEPOSIT" in txn or "TRANSFER FROM" in txn:
                    amount = float(txn.split("₹")[-1])
                    deposits.append(amount)

        print(f"\n  📊 Monthly Analysis - {current_month}")
        print(f"  {'─'*40}")
        print(f"  Total Deposits  : ₹{sum(deposits):.2f}")
        print(f"  Total Spent     : ₹{sum(withdrawals):.2f}")
        print(f"  Transactions    : {len(self.transaction_history)}")
        if withdrawals:
            print(f"  Largest Expense : ₹{max(withdrawals):.2f}")
        print(f"  {'─'*40}")

    # ── RECEIPT ──────────────────────────────────
    def _save_receipt(self, txn_type, amount, extra=""):
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        filename = f"receipt_{self.account_number}_{timestamp}.txt"
        receipt = (
            f"==============================\n"
            f"   BANK RECEIPT\n"
            f"==============================\n"
            f"Date     : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
            f"Account  : {self.account_number}\n"
            f"Name     : {self.name}\n"
            f"Type     : {txn_type}\n"
            f"Amount   : Rs.{amount:.2f}\n"
        )
        if extra:
            receipt += f"To/From  : {extra}\n"
        receipt += (
            f"Balance  : Rs.{self.get_balance():.2f}\n"
            f"==============================\n"
        )
        with open(filename, "w") as f:
            f.write(receipt)
        print(f"  🧾 Receipt saved: {filename}")

    # ── DISPLAY ──────────────────────────────────
    def display_info(self):
        print(f"\n  {'─'*40}")
        print(f"  Account Holder : {self.name}")
        print(f"  Account Number : {self.account_number}")
        print(f"  Account Type   : {self.account_type}")
        print(f"  Balance        : ₹{self.__balance:.2f}")
        print(f"  {'─'*40}")

    # ── FILE HANDLING ─────────────────────────────
    def save_to_file(self):
        filename = f"account_{self.account_number}.txt"
        with open(filename, "w") as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Account Number: {self.account_number}\n")
            f.write(f"Account Type: {self.account_type}\n")
            f.write(f"Balance: {self.get_balance():.2f}\n")
            f.write(f"Saved On: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
            f.write("\n--- Transaction History ---\n")
            for txn in self.transaction_history:
                f.write(f"{txn}\n")
        print(f"  ✔ Account data saved to {filename}")


# ─────────────────────────────────────────────────
#  CHILD CLASS: SavingsAccount (Inheritance)
# ─────────────────────────────────────────────────
class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.04  # 4% per year

    def __init__(self, name, account_number, pin):
        super().__init__(name, account_number, pin)
        self.account_type = "Savings"

    def apply_interest(self):
        interest = self.get_balance() * self.INTEREST_RATE
        self._set_balance(self.get_balance() + interest)
        self._log_transaction("INTEREST CREDITED", interest)
        print(f"  ✔ Interest of ₹{interest:.2f} (4% p.a.) credited.")
        print(f"  New Balance: ₹{self.get_balance():.2f}")


# ─────────────────────────────────────────────────
#  CONTROLLER CLASS: BankSystem
# ─────────────────────────────────────────────────
class BankSystem:
    def __init__(self):
        self.accounts = {}   # account_number -> BankAccount object

    # ── CREATE ACCOUNT ────────────────────────────
    def create_account(self):
        print("\n  ── Create New Account ──")
        name = input("  Enter Name          : ").strip()
        acc_no = input("  Enter Account Number: ").strip()

        if acc_no in self.accounts:
            print("  ✘ Account number already exists.")
            return

        pin = input("  Set 4-digit PIN     : ").strip()
        if len(pin) != 4 or not pin.isdigit():
            print("  ✘ PIN must be exactly 4 digits.")
            return

        acc_type = input("  Account Type (1-Current / 2-Savings): ").strip()
        if acc_type == "2":
            account = SavingsAccount(name, acc_no, pin)
        else:
            account = BankAccount(name, acc_no, pin)

        self.accounts[acc_no] = account
        print(f"  ✔ Account created for {name} ({account.account_type}).")

    # ── LOGIN ─────────────────────────────────────
    def login(self):
        print("\n  ── Login ──")
        acc_no = input("  Account Number: ").strip()
        if acc_no not in self.accounts:
            print("  ✘ Account not found.")
            return None
        pin = input("  Enter PIN     : ").strip()
        account = self.accounts[acc_no]
        if account.verify_pin(pin):
            print(f"  ✔ Welcome, {account.name}!")
            return account
        else:
            print("  ✘ Incorrect PIN.")
            return None

    # ── ACCOUNT MENU ──────────────────────────────
    def account_menu(self, account):
        while True:
            print(f"\n  ╔══════════════════════════════════╗")
            print(f"  ║  {account.name:<32}║")
            print(f"  ╠══════════════════════════════════╣")
            print(f"  ║  1. Deposit                      ║")
            print(f"  ║  2. Withdraw                     ║")
            print(f"  ║  3. Check Balance                ║")
            print(f"  ║  4. Transfer Money               ║")
            print(f"  ║  5. Transaction History          ║")
            print(f"  ║  6. Monthly Analysis             ║")
            print(f"  ║  7. Change PIN                   ║")
            print(f"  ║  8. Save Account Data            ║")
            if account.account_type == "Savings":
                print(f"  ║  9. Apply Interest               ║")
            print(f"  ║  0. Logout                       ║")
            print(f"  ╚══════════════════════════════════╝")

            choice = input("  Choice: ").strip()

            if choice == "1":
                try:
                    amt = float(input("  Amount to deposit  : ₹"))
                    account.deposit(amt)
                    account._save_receipt("DEPOSIT", amt)
                except ValueError:
                    print("  ✘ Invalid amount.")

            elif choice == "2":
                try:
                    amt = float(input("  Amount to withdraw : ₹"))
                    if account.withdraw(amt):
                        account._save_receipt("WITHDRAWAL", amt)
                except ValueError:
                    print("  ✘ Invalid amount.")

            elif choice == "3":
                account.display_info()

            elif choice == "4":
                target_no = input("  Target Account Number: ").strip()
                if target_no not in self.accounts:
                    print("  ✘ Target account not found.")
                elif target_no == account.account_number:
                    print("  ✘ Cannot transfer to same account.")
                else:
                    try:
                        amt = float(input("  Amount to transfer : ₹"))
                        account.transfer(self.accounts[target_no], amt)
                    except ValueError:
                        print("  ✘ Invalid amount.")

            elif choice == "5":
                account.show_history()

            elif choice == "6":
                account.monthly_analysis()

            elif choice == "7":
                old = input("  Old PIN: ").strip()
                new = input("  New PIN: ").strip()
                if len(new) != 4 or not new.isdigit():
                    print("  ✘ New PIN must be 4 digits.")
                else:
                    account.change_pin(old, new)

            elif choice == "8":
                account.save_to_file()

            elif choice == "9" and account.account_type == "Savings":
                account.apply_interest()

            elif choice == "0":
                print(f"  Logging out {account.name}. Goodbye!")
                break

            else:
                print("  ✘ Invalid choice.")

    # ── MAIN MENU ─────────────────────────────────
    def run(self):
        print("\n  ╔══════════════════════════════════════╗")
        print("  ║       BANKING MANAGEMENT SYSTEM      ║")
        print("  ║      CA 2 Mini Project | Python      ║")
        print("  ╚══════════════════════════════════════╝")

        while True:
            print("\n  ┌──────────────────────────────┐")
            print("  │         MAIN MENU            │")
            print("  ├──────────────────────────────┤")
            print("  │  1. Create Account           │")
            print("  │  2. Login                    │")
            print("  │  3. Total Accounts           │")
            print("  │  0. Exit                     │")
            print("  └──────────────────────────────┘")

            choice = input("  Choice: ").strip()

            if choice == "1":
                self.create_account()
            elif choice == "2":
                account = self.login()
                if account:
                    self.account_menu(account)
            elif choice == "3":
                print(f"  Total accounts registered: {BankAccount.total_accounts}")
            elif choice == "0":
                print("\n  Thank you for using the Banking System. Goodbye!\n")
                break
            else:
                print("  ✘ Invalid choice.")


# ─────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    system = BankSystem()
    system.run()