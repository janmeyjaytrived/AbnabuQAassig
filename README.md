# AdNabu QA Engineer Assignment

This repository contains the test design and automated test scripts for the **AdNabuTestStore** web application. The project is part of the Quality Assurance Engineer assignment for AdNabu.

> **Note:** If prompted during testing, the Store Password is `AdNabuQA`.

---

## 📝 Task 1: Test Design

The manual test cases covering positive, negative, and edge cases for the **Product Search** and **Add to Cart** functionalities are documented in the `Test_Cases.md` file.

---

## 🤖 Task 2: Test Automation

The automation script covers a single end-to-end scenario: **Searching for a product and successfully adding it to the cart.**

### Tech Stack Used

| Component      | Technology                          |
|----------------|-------------------------------------|
| Language       | Python                              |
| Framework      | Selenium WebDriver                  |
| Test Runner    | Pytest *(Recommended for modularity)* |

> **Note:** The framework uses explicit and implicit waits (no hardcoded sleeps) to ensure reliability and modularity. Cross-browser support and full framework setup were intentionally excluded as per the assignment instructions.

---

## ⚙️ Setup and Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 2. Set Up a Virtual Environment *(Optional but Recommended)*

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

> Dependencies include `selenium`, `pytest`, and `pytest-html` for reporting.

---

## 🚀 How to Run the Tests

To execute the automated test script, run the following command in your terminal:

```bash
pytest test_script_name.py -v
```

> Replace `test_script_name.py` with the actual name of your Python file.

---

## 📊 Test Reports

To generate an HTML test report during execution, run:

```bash
pytest test_script_name.py --html=report.html --self-contained-html
```

Upon completion, a `report.html` file will be generated in the root directory. Open this file in any web browser to view the detailed test execution report.
