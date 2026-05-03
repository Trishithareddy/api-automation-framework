# 🚀 API Automation Framework

## 📌 Project Overview

This project is an **API Automation Framework** built using **Python, PyTest, and Requests**.
It is designed to automate testing of REST APIs including validation of responses, status codes, and data integrity.

---

## 🛠 Tech Stack

* Python
* PyTest
* Requests
* PyTest HTML Reports

---

## 📂 Project Structure

```
api-automation-framework/
│
├── tests/             # Test cases
├── utils/             # API client & logger
├── payloads/          # Test data (request payloads)
├── reports/           # Test reports & logs
├── pytest.ini         # PyTest configuration
├── requirements.txt   # Dependencies
└── README.md
```

---

## ✅ Features

* Automated API testing (GET, POST, PUT, DELETE)
* Data-driven testing using PyTest
* Response validation (status codes & JSON data)
* Reusable API client for scalability
* Logging for debugging (`reports/api_test.log`)
* HTML test report generation

---

## 🧪 Test Scenarios Covered

* Fetch user data (GET API)
* Create new user (POST API)
* Update user details (PUT API)
* Delete user (DELETE API)

---

## ▶️ How to Run

### 1. Clone repository

```
git clone https://github.com/Trishithareddy/api-automation-framework.git
cd api-automation-framework
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run tests

```
pytest -s
```

---

## 📊 Reports

After execution:

* HTML report → `reports/report.html`
* Logs → `reports/api_test.log`

---

## 🎯 Key Highlights

* Designed scalable API automation framework
* Implemented reusable components for easy maintenance
* Followed best practices for test automation

---

## 👩‍💻 Author

**Trishitha Reddy**
