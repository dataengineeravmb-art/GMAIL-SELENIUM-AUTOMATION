# 📧 Gmail Selenium Automation using Python

## 📌 Overview

This project automates Gmail using **Python** and **Selenium WebDriver**. It automatically logs into a Gmail account, composes an email, fills the recipient details, subject, and message body, and sends the email.

The project is built as a reusable function, allowing users to send emails by simply passing the required parameters such as email address, password, recipients, subject, and message.

---

## 🚀 Features

- ✅ Gmail Login Automation
- ✅ Automatic Email Composition
- ✅ Send Email to Multiple Recipients
- ✅ Add CC Recipients
- ✅ Enter Subject Automatically
- ✅ Write Email Body Automatically
- ✅ Send Email Automatically
- ✅ Chrome Profile Support (Avoids Repeated Login)
- ✅ Explicit Waits for Stable Automation
- ✅ Function-Based Design for Reusability
- ✅ Easy Integration with Other Python Projects

---

## 🛠 Technologies Used

- Python 3
- Selenium WebDriver
- ChromeDriver
- ActionChains
- WebDriverWait
- Expected Conditions

---

## 📂 Project Structure

```
GMAIL-SELENIUM-AUTOMATION
│
├── GMAIL.py
├── README.md
├── requirements.txt
├── .gitignore
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/dataengineeravmb-art/GMAIL-SELENIUM-AUTOMATION.git
```

Go to the project folder

```bash
cd GMAIL-SELENIUM-AUTOMATION
```

Install dependencies



## 📖 Function

```python
Gmail_Login(
    Mail_Directory,
    Email,
    Password,
    Send_TO,
    Send_CC,
    Subject,
    Description
)
```

---

## 📥 Parameters

| Parameter | Description |
|------------|-------------|
| Mail_Directory | Chrome user profile directory |
| Email | Gmail Email Address |
| Password | Gmail Password |
| Send_TO | Recipient Email Address |
| Send_CC | CC Email Address |
| Subject | Email Subject |
| Description | Email Message |

---

## 💻 Example Usage

```python
from GMAIL import Gmail_Login

Gmail_Login(
    Mail_Directory="C:/SELENIUM/GMAIL",
    Email="yourmail@gmail.com",
    Password="yourpassword",
    Send_TO="receiver@gmail.com",
    Send_CC="manager@gmail.com",
    Subject="Automation Test",
    Description="This email was sent automatically using Python Selenium."
)
```

---

## 📌 Workflow

1. Launch Chrome Browser
2. Open Gmail
3. Login using Gmail Credentials
4. Open Compose Window
5. Enter TO Recipient
6. Add CC Recipient
7. Enter Subject
8. Write Email Body
9. Send Email
10. Close Browser

---

## 🎯 Applications

- Daily Business Reports
- Automated Notifications
- Email Testing
- Office Automation
- Personal Productivity
- Workflow Automation

---


## 📌 Future Enhancements

- Support Multiple Attachments
- HTML Email Support
- BCC Recipients
- Email Scheduling
- Reading Excel File for Bulk Email
- Logging System
- Error Handling Improvements

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Fork the repository, make your changes, and submit a Pull Request.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Azhar Basha**

Senior Data Analyst | Python | SQL | Power BI | Selenium | Automation

GitHub:
https://github.com/dataengineeravmb-art

---
