# Basic Banking System 🏦

A Command Line Interface (CLI) based banking application written in Python. This system simulates basic banking operations including user authentication, transaction management, and data persistence using file handling.

## 🚀 Features

* **User Authentication:** Secure Login and Logout functionality.
* **New User Registration:** Create a new account with a username, password, and initial deposit.
* **Account Management:**
    * Check Current Balance.
    * Deposit Money.
    * Withdraw Money.
* **Security:** Change Password functionality.
* **Data Persistence:** All user data (credentials and balances) is stored permanently in a text file (`customer_data.txt`).

## 🛠️ Tech Stack

* **Language:** Python 3.10+ (Required for `match-case` syntax)
* **Libraries:** `time` (Standard Library)
* **Concepts Used:** OOP (Classes & Objects), File Handling, Exception Handling, Control Flow.

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/sajjanaaru-ops/simple-banking-system.git](https://github.com/sajjanaaru-ops/simple-banking-system.git)
    ```

2.  **Navigate to the directory:**
    ```bash
    cd simple-banking-system
    ```

3.  **⚠️ Important Configuration (File Path):**
    Before running the code, you must update the file path to match your local machine.\
    note: while programming this file, i tailored my code for my local device.You must change it so that you canrun the code on your laptop. 
    * Open `banking_sys.py`.
    * Locate the line: `file_path='C:/Users/sajja/OneDrive/Desktop/python/basic banking system/customer_data.txt'`
    * Change it to the path where your `customer_data.txt` is located. 
    * *Tip:* You can simply use `file_path = 'customer_data.txt'` if the text file is in the same folder as the python script.

4.  **The code has been modified in a way to initialize the database of the customer_data.txt file.**
5.  **Soon the repository will be updated with secured hashmaps and will use an .csv file instead of an .txt file for better secuirty**

## 🏃 Usage

Run the program using Python:

```bash
python banking_sys.py
