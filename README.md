# 🎓 College Event Registration System

A full-stack web application that allows students to register for college events. Built with **Python Flask**, **SQLite**, and a clean responsive frontend using **HTML, CSS, and JavaScript**.

---

## 📸 Overview

Students fill out a simple registration form with their details and select an event. The data is saved to a local SQLite database, and a success message is displayed instantly — no page reload required.

---

## ✨ Features

- 📝 Student registration form with full validation
- 🗄️ Data stored persistently in a local SQLite database
- ✅ Success and error messages shown without page reload
- 📋 Admin page to view all registered students in a table
- 🎨 Clean, responsive UI that works on desktop and mobile
- 🔒 Server-side validation to prevent empty or malformed submissions

---

## 🛠️ Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Frontend   | HTML5, CSS3, JavaScript |
| Backend    | Python 3, Flask         |
| Database   | SQLite (via Python's built-in `sqlite3` module) |

> **Why SQLite?** It is a lightweight, file-based SQL database — no installation or configuration needed. It behaves exactly like MySQL for this use case and is perfect for local development.

---

## 📁 Project Structure

```
college_event_registration/
│
├── app.py                  # Flask backend — routes, DB logic
│
├── templates/
│   ├── index.html          # Student registration form
│   └── admin.html          # Admin view of all registrations
│
├── static/
│   └── style.css           # Styling for the frontend
│
├── registrations.db        # SQLite database (auto-created on first run)
│
└── README.md               # You are here
```

---

## ⚙️ Prerequisites

Make sure you have the following installed on your machine:

- **Python 3.x** — [Download here](https://www.python.org/downloads/)
  - During installation, check **"Add Python to PATH"**
- **pip** — comes bundled with Python 3

To verify your installation, open a terminal and run:

```bash
python --version
```

You should see something like `Python 3.12.x`.

---

## 🚀 Installation & Setup

Follow these steps exactly to get the project running on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/college-event-registration.git
cd college-event-registration
```

> Replace `YOUR_USERNAME` with your actual GitHub username.

### 2. Install Flask

Flask is the only external dependency. Install it using pip:

```bash
pip install flask
```

### 3. Run the application

```bash
python app.py
```

You should see output like this:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 4. Open in your browser

Visit: **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

The registration form will load. The SQLite database (`registrations.db`) is created automatically on first run — no setup needed.

---

## 📖 How to Use

### Student Registration

1. Open **http://127.0.0.1:5000** in your browser
2. Fill in the form:
   - **Full Name** — e.g. Arjun Sharma
   - **Student ID** — e.g. CS2024001
   - **Course** — e.g. B.Tech Computer Science
   - **Event Name** — select from the dropdown
3. Click **Register Now**
4. A green success message will appear confirming your registration

### Admin — View All Registrations

To see all registered students, open:

**[http://127.0.0.1:5000/admin](http://127.0.0.1:5000/admin)**

This displays a table with every registration including the timestamp.

---

## 🗄️ Database

The database file `registrations.db` is created automatically in the project folder when you first run the app. It contains one table:

### `registrations` table

| Column          | Type      | Description                        |
|-----------------|-----------|------------------------------------|
| `id`            | INTEGER   | Auto-incrementing primary key      |
| `full_name`     | TEXT      | Student's full name                |
| `student_id`    | TEXT      | College-issued student ID          |
| `course`        | TEXT      | Student's course/program           |
| `event_name`    | TEXT      | Name of the event registered for   |
| `registered_at` | TIMESTAMP | Date and time of registration      |

### Viewing the database directly (optional)

You can inspect the raw database using **DB Browser for SQLite**:

1. Download from [https://sqlitebrowser.org](https://sqlitebrowser.org)
2. Open `registrations.db` from your project folder
3. Go to the **Browse Data** tab → select the `registrations` table

---

## 🎪 Available Events

The following events are available in the registration form:

- 🖥️ Tech Fest 2025
- 🎭 Cultural Night
- 🌐 Web Development Workshop
- 🤖 AI & ML Workshop
- 🏅 Sports Day

---

## 🔧 Troubleshooting

| Problem | Solution |
|--------|----------|
| `python: command not found` | Make sure Python is installed and added to PATH |
| `ModuleNotFoundError: flask` | Run `pip install flask` again |
| Port already in use | Change the port: `app.run(debug=True, port=5001)` in `app.py` |
| Database not created | Make sure you run `python app.py` from inside the project folder |
| Page not loading | Confirm the server is running and visit `http://127.0.0.1:5000` |

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---
