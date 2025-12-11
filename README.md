# 🏦 Secure CLI Banking System

A robust, command-line interface (CLI) banking application built with Python. This project simulates core banking features including user registration, secure authentication, and transaction management, with a focus on data security and persistence.

## 🚀 Features

* **Secure Authentication:** User passwords are hashed and salted using **Bcrypt**, ensuring that plain-text passwords are never stored.
* **Persistent Storage:** All user data and account balances are stored in a local JSON database, allowing data to persist between sessions.
* **Dynamic Path Handling:** The system automatically detects the operating system and file paths, making it runnable on any machine without configuration.
* **Core Banking Operations:**
    * Account Registration (with duplicate user detection)
    * Secure Login
    * Deposit & Withdrawal
    * Balance Inquiry
    * Password Management

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Libraries:**
    * `bcrypt`: For enterprise-grade password hashing.
    * `json`: For lightweight database management.
    * `os`: For cross-platform file path handling.
    * `time`: For UI flow control.

## ⚙️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/banking-system.git](https://github.com/yourusername/banking-system.git)
    cd banking-system
    ```

2.  **Install dependencies:**
    This project requires the `bcrypt` library.
    ```bash
    pip install bcrypt
    ```

3.  **Run the application:**
    ```bash
    python banking_sys.py
    ```

## 📂 Project Structure

```text
banking-system/
├── banking_sys.py       # Main source code
├── customer_data.txt    # JSON database (auto-generated on first run)
└── README.md            # Project documentation
```
## 🔒 Security Implementation
Unlike basic banking scripts, this project prioritizes security.

**Hashing**: Passwords are converted to bytes, combined with a unique random salt, and hashed using the bcrypt algorithm.

**Verification**: Login attempts are verified using bcrypt.checkpw(), ensuring timing attacks are mitigated and original passwords cannot be reverse-engineered.

## 🤝 Contributing
This is a personal learning project, but suggestions are welcome! Feel free to open an issue or submit a pull request if you find bugs or want to suggest new features.
