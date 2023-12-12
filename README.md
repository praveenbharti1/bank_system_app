## Open Account 

This Python code creates a simple bank account system using SQLite3. It allows users to create new accounts, deposit and withdraw funds, and check their balance.

**Features:**

* Create new accounts with account name, number, and balance.
* Deposit funds into an account.
* Withdraw funds from an account.
* Check the balance of an account.

**Here's a breakdown of the code:**

1. **Class definition:**

   * `Bank` class connects to an SQLite3 database named `Bank.db`.
   * `createAccount()` method creates the `Bank` table if it doesn't exist.
   * `OpenAccount()` method allows users to interact with their accounts.

2. **`createAccount()` method:**

   * Creates table with columns for name, account number, and balance.
   * Takes user input for name and checks for valid format.
   * Generates a random account number.
   * Inserts new account information into the table.
   * Prints confirmation message and account details.

3. **`OpenAccount()` method:**

   * Takes user input for account number.
   * Checks if the account exists.
   * If valid, displays account options (deposit, withdraw, check balance).
   * Based on user choice, performs the operation and updates the balance.

4. **Output:**

   * User interaction prompts and informative messages.
   * Account details after creation and balance updates.

