from datetime import datetime


# ─────────────────────────────────────────────────
#  BASE CLASS: BankAccount
# ─────────────────────────────────────────────────
class BankAccount:

    total_accounts = 0

    def __init__(self, name, account_number, pin):

        self.__pin = pin
        self.__balance = 0.0

        self.name = name
        self.account_number = account_number
        self.account_type = "Current"

        self.transaction_history = []

        BankAccount.total_accounts += 1

    # ── PIN METHODS ─────────────────────────────
    def verify_pin(self, pin):
        return self.__pin == pin

    def change_pin(self, old_pin, new_pin):

        if self.verify_pin(old_pin):
            self.__pin = new_pin
            print("  ✔ PIN changed successfully.")
        else:
            print("  ✘ Incorrect old PIN.")

    # ── BALANCE METHODS ─────────────────────────
    def get_balance(self):
        return self.__balance

    def _set_balance(self, amount):
        self.__balance = amount

    # ── DEPOSIT ─────────────────────────────────
    def deposit(self, amount):

        if amount <= 0:
            print("  ✘ Invalid deposit amount.")
            return False

        self.__balance += amount

        self._log_transaction("DEPOSIT", amount)

        print(f"  ✔ ₹{amount:.2f} deposited successfully.")
        print(f"  Current Balance: ₹{self.__balance:.2f}")

        return True

    # ── WITHDRAW ────────────────────────────────
    def withdraw(self, amount):

        if amount <= 0:
            print("  ✘ Invalid withdrawal amount.")
            return False

        if amount > self.__balance:
            print("  ✘ Insufficient balance.")
            return False

        self.__balance -= amount

        self._log_transaction("WITHDRAWAL", amount)

        print(f"  ✔ ₹{amount:.2f} withdrawn successfully.")
        print(f"  Current Balance: ₹{self.__balance:.2f}")

        return True

    # ── TRANSFER ────────────────────────────────
    def transfer(self, target_account, amount):

        if amount <= 0:
            print("  ✘ Invalid transfer amount.")
            return False

        if amount > self.__balance:
            print("  ✘ Insufficient balance.")
            return False

        self.__balance -= amount

        target_account._BankAccount__balance += amount

        self._log_transaction(
            f"TRANSFER TO {target_account.account_number}",
            amount
        )

        target_account._log_transaction(
            f"TRANSFER FROM {self.account_number}",
            amount
        )

        print(f"  ✔ ₹{amount:.2f} transferred successfully.")
        print(f"  Current Balance: ₹{self.__balance:.2f}")

        self._save_receipt(
            "TRANSFER",
            amount,
            target_account.name
        )

        return True

    # ── TRANSACTION HISTORY ─────────────────────
    def _log_transaction(self, txn_type, amount):

        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        entry = (
            f"[{timestamp}] "
            f"{txn_type:<30} ₹{amount:.2f}"
        )

        self.transaction_history.append(entry)

    def show_history(self):

        print(f"\n  {'─' * 60}")
        print(f"  Transaction History - {self.name}")
        print(f"  {'─' * 60}")

        if not self.transaction_history:
            print("  No transactions found.")
        else:
            for txn in self.transaction_history:
                print(f"  {txn}")

        print(f"  {'─' * 60}")

    # ── MONTHLY ANALYSIS ────────────────────────
    def monthly_analysis(self):

        current_month = datetime.now().strftime("%m-%Y")

        deposits = []
        withdrawals = []

        for txn in self.transaction_history:

            if current_month in txn:

                if "DEPOSIT" in txn or "TRANSFER FROM" in txn:
                    amount = float(txn.split("₹")[-1])
                    deposits.append(amount)

                elif "WITHDRAWAL" in txn or "TRANSFER TO" in txn:
                    amount = float(txn.split("₹")[-1])
                    withdrawals.append(amount)

        print(f"\n  📊 Monthly Analysis - {current_month}")
        print(f"  {'─' * 45}")

        print(f"  Total Deposits : ₹{sum(deposits):.2f}")
        print(f"  Total Expenses : ₹{sum(withdrawals):.2f}")
        print(f"  Total Transactions: {len(self.transaction_history)}")

        if withdrawals:
            print(f"  Largest Expense : ₹{max(withdrawals):.2f}")

        print(f"  {'─' * 45}")

    # ── RECEIPT ─────────────────────────────────
    def _save_receipt(self, txn_type, amount, extra=""):

        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        filename = (
            f"receipt_{self.account_number}_{timestamp}.txt"
        )

        receipt = (
            f"==============================\n"
            f"       BANK RECEIPT\n"
            f"==============================\n"
            f"Date     : "
            f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
            f"Account  : {self.account_number}\n"
            f"Name     : {self.name}\n"
            f"Type     : {txn_type}\n"
            f"Amount   : ₹{amount:.2f}\n"
        )

        if extra:
            receipt += f"To/From  : {extra}\n"

        receipt += (
            f"Balance  : ₹{self.get_balance():.2f}\n"
            f"==============================\n"
        )

        with open(filename, "w", encoding="utf-8") as f:
            f.write(receipt)

        print(f"  🧾 Receipt saved: {filename}")

    # ── DISPLAY ACCOUNT INFO ────────────────────
    def display_info(self):

        print(f"\n  {'─' * 45}")
        print(f"  Account Holder : {self.name}")
        print(f"  Account Number : {self.account_number}")
        print(f"  Account Type   : {self.account_type}")
        print(f"  Balance        : ₹{self.get_balance():.2f}")
        print(f"  {'─' * 45}")

    # ── SAVE TO FILE ────────────────────────────
    def save_to_file(self):

        filename = f"account_{self.account_number}.txt"

        with open(filename, "w", encoding="utf-8") as f:

            f.write(f"Name: {self.name}\n")
            f.write(f"Account Number: {self.account_number}\n")
            f.write(f"Account Type: {self.account_type}\n")
            f.write(f"Balance: ₹{self.get_balance():.2f}\n")

            f.write(
                f"Saved On: "
                f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n"
            )

            f.write("\n--- Transaction History ---\n")

            for txn in self.transaction_history:
                f.write(f"{txn}\n")

        print(f"  ✔ Account data saved to {filename}")


# ─────────────────────────────────────────────────
#  CHILD CLASS: SavingsAccount
# ─────────────────────────────────────────────────
class SavingsAccount(BankAccount):

    INTEREST_RATE = 0.04

    def __init__(self, name, account_number, pin):

        super().__init__(name, account_number, pin)

        self.account_type = "Savings"

    def apply_interest(self):

        interest = self.get_balance() * self.INTEREST_RATE

        self._set_balance(self.get_balance() + interest)

        self._log_transaction("INTEREST CREDITED", interest)

        print(f"  ✔ Interest of ₹{interest:.2f} credited.")
        print(f"  New Balance: ₹{self.get_balance():.2f}")


# ─────────────────────────────────────────────────
#  CONTROLLER CLASS: BankSystem
# ─────────────────────────────────────────────────
class BankSystem:

    ADMIN_ID = "admin"
    ADMIN_PASS = "1234"

    def __init__(self):

        self.accounts = {}
        self.deleted_accounts = {}

    # ── CREATE ACCOUNT ──────────────────────────
    def create_account(self):

        print("\n  ── Create New Account ──")

        name = input("  Enter Name          : ").strip()

        acc_no = input("  Enter Account Number: ").strip()

        if acc_no in self.accounts:
            print("  ✘ Account already exists.")
            return

        pin = input("  Set 4-digit PIN     : ").strip()

        if len(pin) != 4 or not pin.isdigit():
            print("  ✘ PIN must be exactly 4 digits.")
            return

        acc_type = input(
            "  Account Type (1-Current / 2-Savings): "
        ).strip()

        if acc_type == "2":
            account = SavingsAccount(name, acc_no, pin)
        else:
            account = BankAccount(name, acc_no, pin)

        self.accounts[acc_no] = account

        print(
            f"  ✔ Account created successfully "
            f"for {name}."
        )

    # ── USER LOGIN ──────────────────────────────
    def login(self):

        print("\n  ── User Login ──")

        acc_no = input("  Account Number: ").strip()

        if acc_no not in self.accounts:
            print("  ✘ Account not found.")
            return None

        pin = input("  Enter PIN     : ").strip()

        account = self.accounts[acc_no]

        if account.verify_pin(pin):
            print(f"  ✔ Welcome, {account.name}!")
            return account

        print("  ✘ Incorrect PIN.")
        return None

    # ── ADMIN LOGIN ─────────────────────────────
    def admin_login(self):

        print("\n  ── Admin Login ──")

        admin_id = input("  Admin ID : ").strip()
        admin_pass = input("  Password : ").strip()

        if (
            admin_id == self.ADMIN_ID
            and admin_pass == self.ADMIN_PASS
        ):
            print("  ✔ Admin login successful.")
            self.admin_menu()
        else:
            print("  ✘ Invalid admin credentials.")

    # ── VIEW ALL ACCOUNTS ───────────────────────
    def view_all_accounts(self):

        print(f"\n  {'─' * 60}")
        print("  ALL REGISTERED ACCOUNTS")
        print(f"  {'─' * 60}")

        if not self.accounts:
            print("  No accounts found.")
            return

        for acc_no, account in self.accounts.items():

            print(f"""
  Name    : {account.name}
  Acc No  : {account.account_number}
  Type    : {account.account_type}
  Balance : ₹{account.get_balance():.2f}
            """)

        print(f"  {'─' * 60}")

    # ── UPDATE ACCOUNT ──────────────────────────
    def update_account(self):

        print("\n  ── Update Account ──")

        acc_no = input("  Enter Account Number: ").strip()

        if acc_no not in self.accounts:
            print("  ✘ Account not found.")
            return

        account = self.accounts[acc_no]

        print("\n  1. Change Name")
        print("  2. Reset PIN")
        print("  3. Change Account Type")

        choice = input("  Choice: ").strip()

        # Change Name
        if choice == "1":

            new_name = input("  Enter New Name: ").strip()

            account.name = new_name

            print("  ✔ Name updated successfully.")

        # Reset PIN
        elif choice == "2":

            new_pin = input("  Enter New 4-digit PIN: ").strip()

            if len(new_pin) != 4 or not new_pin.isdigit():
                print("  ✘ Invalid PIN format.")
            else:
                account._BankAccount__pin = new_pin
                print("  ✔ PIN reset successfully.")

        # Change Account Type
        elif choice == "3":

            print("\n  1. Current")
            print("  2. Savings")

            acc_type = input("  Select Type: ").strip()

            if acc_type == "1":
                account.account_type = "Current"
                print("  ✔ Account changed to Current.")

            elif acc_type == "2":
                account.account_type = "Savings"
                print("  ✔ Account changed to Savings.")

            else:
                print("  ✘ Invalid choice.")

        else:
            print("  ✘ Invalid choice.")

    # ── DELETE ACCOUNT ──────────────────────────
    def delete_account(self):

        print("\n  ── Delete Account ──")

        acc_no = input("  Enter Account Number: ").strip()

        if acc_no not in self.accounts:
            print("  ✘ Account not found.")
            return

        account = self.accounts[acc_no]

        if account.get_balance() != 0:
            print("  ✘ Account balance must be zero.")
            return

        self.deleted_accounts[acc_no] = account

        del self.accounts[acc_no]

        BankAccount.total_accounts -= 1

        print("  ✔ Account moved to deleted records.")

    # ── RESTORE ACCOUNT ─────────────────────────
    def restore_account(self):

        print("\n  ── Restore Deleted Account ──")

        acc_no = input("  Enter Account Number: ").strip()

        if acc_no not in self.deleted_accounts:
            print("  ✘ Deleted account not found.")
            return

        self.accounts[acc_no] = self.deleted_accounts[acc_no]

        del self.deleted_accounts[acc_no]

        BankAccount.total_accounts += 1

        print("  ✔ Account restored successfully.")

    # ── BANK STATISTICS ─────────────────────────
    def bank_statistics(self):

        total_money = sum(
            acc.get_balance()
            for acc in self.accounts.values()
        )

        savings_count = sum(
            1
            for acc in self.accounts.values()
            if acc.account_type == "Savings"
        )

        current_count = sum(
            1
            for acc in self.accounts.values()
            if acc.account_type == "Current"
        )

        print(f"\n  {'─' * 45}")
        print("  BANK STATISTICS")
        print(f"  {'─' * 45}")

        print(f"  Total Accounts  : {BankAccount.total_accounts}")
        print(f"  Savings Accounts: {savings_count}")
        print(f"  Current Accounts: {current_count}")
        print(f"  Total Bank Funds: ₹{total_money:.2f}")

        print(f"  {'─' * 45}")

    # ── ADMIN MENU ──────────────────────────────
    def admin_menu(self):

        while True:

            print("\n  ╔══════════════════════════════════╗")
            print("  ║           ADMIN PANEL           ║")
            print("  ╠══════════════════════════════════╣")
            print("  ║  1. View All Accounts           ║")
            print("  ║  2. Update Account              ║")
            print("  ║  3. Delete Account              ║")
            print("  ║  4. Restore Deleted Account     ║")
            print("  ║  5. Bank Statistics             ║")
            print("  ║  0. Logout                      ║")
            print("  ╚══════════════════════════════════╝")

            choice = input("  Choice: ").strip()

            if choice == "1":
                self.view_all_accounts()

            elif choice == "2":
                self.update_account()

            elif choice == "3":
                self.delete_account()

            elif choice == "4":
                self.restore_account()

            elif choice == "5":
                self.bank_statistics()

            elif choice == "0":
                print("  Logging out admin...")
                break

            else:
                print("  ✘ Invalid choice.")

    # ── USER ACCOUNT MENU ───────────────────────
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

            # Deposit
            if choice == "1":

                try:
                    amt = float(input("  Amount to deposit : ₹"))

                    if account.deposit(amt):
                        account._save_receipt("DEPOSIT", amt)

                except ValueError:
                    print("  ✘ Invalid amount.")

            # Withdraw
            elif choice == "2":

                try:
                    amt = float(input("  Amount to withdraw: ₹"))

                    if account.withdraw(amt):
                        account._save_receipt("WITHDRAWAL", amt)

                except ValueError:
                    print("  ✘ Invalid amount.")

            # Balance
            elif choice == "3":
                account.display_info()

            # Transfer
            elif choice == "4":

                target_no = input(
                    "  Target Account Number: "
                ).strip()

                if target_no not in self.accounts:
                    print("  ✘ Target account not found.")

                elif target_no == account.account_number:
                    print("  ✘ Cannot transfer to same account.")

                else:

                    try:
                        amt = float(
                            input("  Amount to transfer: ₹")
                        )

                        account.transfer(
                            self.accounts[target_no],
                            amt
                        )

                    except ValueError:
                        print("  ✘ Invalid amount.")

            # History
            elif choice == "5":
                account.show_history()

            # Analysis
            elif choice == "6":
                account.monthly_analysis()

            # Change PIN
            elif choice == "7":

                old = input("  Old PIN: ").strip()
                new = input("  New PIN: ").strip()

                if len(new) != 4 or not new.isdigit():
                    print("  ✘ PIN must be exactly 4 digits.")
                else:
                    account.change_pin(old, new)

            # Save Account
            elif choice == "8":
                account.save_to_file()

            # Interest
            elif choice == "9" and account.account_type == "Savings":
                account.apply_interest()

            # Logout
            elif choice == "0":
                print(f"  Logging out {account.name}...")
                break

            else:
                print("  ✘ Invalid choice.")

    # ── MAIN SYSTEM ─────────────────────────────
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
            print("  │  2. User Login               │")
            print("  │  3. Admin Login              │")
            print("  │  4. Total Accounts           │")
            print("  │  0. Exit                     │")
            print("  └──────────────────────────────┘")

            choice = input("  Choice: ").strip()

            # Create Account
            if choice == "1":
                self.create_account()

            # User Login
            elif choice == "2":

                account = self.login()

                if account:
                    self.account_menu(account)

            # Admin Login
            elif choice == "3":
                self.admin_login()

            # Total Accounts
            elif choice == "4":

                print(
                    f"  Total accounts registered: "
                    f"{BankAccount.total_accounts}"
                )

            # Exit
            elif choice == "0":

                print("\n  Thank you for using the Banking System.\n")
                break

            else:
                print("  ✘ Invalid choice.")


# ─────────────────────────────────────────────────
#  OBJECT CREATION & METHOD CALL
# ─────────────────────────────────────────────────

system = BankSystem()
system.run()
