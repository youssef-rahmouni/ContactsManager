# 📇 ContactsManager

**ContactsManager** is a beginner-friendly Python application for storing, viewing, and searching personal contacts. It supports saving names, phone numbers, and email addresses, and writing them to a `.txt` file automatically.

---

## 🚀 Why I Created It

Managing contact lists manually with text files is time-consuming and error-prone. This script was built as a small project to:

- Practice Python fundamentals
- Create a real-world CLI tool
- Save contact data easily in text format
- Learn file manipulation, loops, and validation

---

## ⚙️ Key Features

- ✅ Add contacts (name, surname, phone, email)
- 🔍 Search by name, surname, or phone number
- 🧾 Display all saved contacts in a table format
- 🗂️ Save data in a `.txt` file (auto-generated)
- 🛠️ Change the output path of the contact file
- 🧪 Comes with unit tests using `unittest`

---

## 📦 Project Structure

```
ContactsManager/
│
├── ContactsManager.py           # Main program logic (menu + contact system)
├── contacts_output_file.txt     # Auto-generated contact storage file
├── test/
│   └── test_ContactsManager.py # Unit test for contact saving
```

---

## ▶️ How to Use

### Requirements

- Python 3.x

### Run the program

```bash
python ContactsManager.py
```

### Run the tests

```bash
python -m unittest discover -s test
```

---

## 🧪 What the Test Does

* Inserts a sample contact
* Triggers saving to the `.txt` file
* Verifies the file exists and contains the expected values

---

## 📌 Notes

* Contact phone numbers must be 10 digits.
* Supported emails: `@gmail.com`, `@e-mail.com`, `@outlook.fr`
* The file is saved in the current working directory by default, but can be changed via menu option 6.

---

## ⚠️ Disclaimer

This project is not a production-grade application. It’s a learning tool for exploring Python programming concepts like input validation, file handling, and unit testing.
