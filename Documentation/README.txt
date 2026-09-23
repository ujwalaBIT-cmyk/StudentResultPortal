# Student Result Portal

## 1. Project Title

**Student Result Portal**

A web-based student result management system developed using **Python and Django** with **MySQL** as the database. The system provides separate access and functionality for **Admin, Teacher, and Student** users.

---

## 2. Project Description

The Student Result Portal is designed to simplify the management and viewing of student academic results.

The application provides role-based access to different users:

* **Admin** can manage users and application data.
* **Teacher** can enter, view, and update student results.
* **Student** can securely view their own academic results.

The system uses Django for backend development, Django templates with HTML/CSS/JavaScript for the frontend, and MySQL for persistent data storage.

---

## 3. Objectives

The main objectives of the project are:

* Provide a centralized system for student result management.
* Reduce manual result-management work.
* Provide secure user authentication.
* Implement role-based access control.
* Allow teachers to manage student results.
* Allow students to view their own results.
* Calculate result-related information such as total, percentage, grade, and pass/fail status.
* Maintain academic data in a MySQL database.
* Provide database scripts for project deployment and evaluation.
* Provide API documentation and Postman collection for API testing.
* Maintain the project source code using Git and GitHub.

---

## 4. Key Features

### Authentication

* User login
* Logout
* Role-based access
* Protected dashboard pages
* Unauthorized users cannot access restricted functionality

### Admin

The Admin role is responsible for managing the application and its data through the Django administration interface.

Admin functionality includes:

* User management
* Student management
* Teacher management
* Class management
* Subject management
* Result-related data management

### Teacher

Teachers can:

* Login securely
* Access the Teacher Dashboard
* View students
* Add student results
* View results
* Update results
* Manage marks according to their authorized functionality

### Student

Students can:

* Login securely
* Access the Student Dashboard
* View their own academic results
* View result details such as marks, total, percentage, grade, and result status

Students are restricted from accessing other students' result information.

---

## 5. Technology Stack

| Technology         | Purpose                    |
| ------------------ | -------------------------- |
| Python             | Programming language       |
| Django             | Backend web framework      |
| MySQL              | Relational database        |
| MySQL Workbench    | Database management        |
| HTML5              | Page structure             |
| CSS3               | Styling                    |
| JavaScript         | Client-side functionality  |
| Django Templates   | Dynamic frontend rendering |
| Bootstrap          | UI styling, where used     |
| Git                | Version control            |
| GitHub             | Source-code repository     |
| Postman            | API testing                |
| Visual Studio Code | Development environment    |
| Windows            | Development platform       |

---

## 6. User Roles

The application contains three main roles.

| Role    | Main Responsibility               |
| ------- | --------------------------------- |
| Admin   | Manage application data and users |
| Teacher | Manage and update student results |
| Student | View own academic results         |

### Role-based Dashboard URLs

After successful login, users are directed according to their role.

```text
Admin:
 /admin/

Teacher:
 /accounts/teacher-dashboard/

Student:
 /accounts/student-dashboard/
```

---

## 7. Project Structure

The project is organized into separate Django applications according to functionality.

```text
StudentResultPortal/
│
├── studentresult/
│   ├── manage.py
│   ├── studentresult/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── accounts/
│   ├── classes/
│   ├── students/
│   ├── teachers/
│   ├── subjects/
│   ├── results/
│   │
│   ├── templates/
│   ├── static/
│   └── media/
│
├── 02_Database/
│   ├── schema.sql
│   └── seed.sql
│
├── 03_Documentation/
│   ├── README.md
│   ├── API_Documentation.md
│   ├── Postman_Collection.json
│   ├── ER_Diagram.png
│   └── GitHub_Repo_Link.txt
│
├── requirements.txt
├── .env.example
└── .gitignore
```

> The exact files and folders may increase as additional functionality is developed.

---

# 8. Prerequisites

Before running the project, install the following:

* Python 3.x
* Django
* MySQL Server
* MySQL Workbench
* Git
* A code editor such as Visual Studio Code

Make sure MySQL Server is running before starting the Django application.

---

# 9. Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/ujwalaBIT-cmyk/StudentResultPortal.git
```

Move into the project directory:

```bash
cd StudentResultPortal
```

The Django project is located inside:

```text
studentresult
```

Therefore:

```bash
cd studentresult
```

---

# 10. Virtual Environment

Create and activate a Python virtual environment.

### Create virtual environment

```bash
python -m venv venv
```

### Windows activation

```bash
venv\Scripts\activate
```

If your virtual environment is maintained outside the project folder, activate that existing environment before running the Django commands.

After activation, the terminal should show:

```text
(venv)
```

---

# 11. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

If the project uses MySQL through `mysqlclient`, make sure the required MySQL client dependencies are installed correctly.

Verify Django:

```bash
python -m django --version
```

---

# 12. MySQL Database Setup

The project uses MySQL database:

```text
student_result_portal
```

Open **MySQL Workbench** and create the database:

```sql
CREATE DATABASE student_result_portal;
```

Select the database:

```sql
USE student_result_portal;
```

---

# 13. Environment Variables

The project uses environment variables for configuration.

A sample configuration is provided in:

```text
.env.example
```

Create your local `.env` file from the example.

Example:

```env
DB_NAME=student_result_portal
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
```

Replace:

```text
your_mysql_password
```

with the password configured for your local MySQL installation.

### Security

The actual `.env` file should **not be committed to GitHub**.

Only:

```text
.env.example
```

should be included in the repository.

---

# 14. Database Scripts

The project provides database scripts in:

```text
02_Database/
```

### schema.sql

`schema.sql` contains the database structure/schema generated from the project's MySQL database.

It contains the tables and relationships required by the application.

### seed.sql

`seed.sql` contains meaningful sample/test data required for demonstrating the application.

The seed data can include:

* Admin/test user data
* Teacher data
* Student data
* Classes
* Subjects
* Results
* Other application-specific records

Django's internal/system tables do not need to be populated with application sample data unless required by the project setup.

---

# 15. Django Migrations

After configuring the database, run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

To check the migration status:

```bash
python manage.py showmigrations
```

---

# 16. Create Django Superuser

To create an administrator account:

```bash
python manage.py createsuperuser
```

Enter:

```text
Username
Email
Password
```

The superuser can then access:

```text
/admin/
```

---

# 17. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will normally be available at:

```text
http://127.0.0.1:8000/
```

If a different port is configured, use the configured port.

For example:

```bash
python manage.py runserver 8080
```

---

# 18. Login and Role-Based Access

The application supports role-based authentication.

### Admin

Admin users can access:

```text
/admin/
```

### Teacher

Teacher users are redirected to:

```text
/accounts/teacher-dashboard/
```

### Student

Student users are redirected to:

```text
/accounts/student-dashboard/
```

The application checks the user's role before allowing access to protected functionality.

---

# 19. Test Login Credentials

For evaluation/demo purposes, test accounts should be provided.

### Admin

```text
Username: <admin-test-username>
Password: <admin-test-password>
```

### Teacher

```text
Username: <teacher-test-username>
Password: <teacher-test-password>
```

### Student

```text
Username: <student-test-username>
Password: <student-test-password>
```

> Replace the placeholders above with the actual test credentials used in the project. Do not publish production passwords or sensitive credentials.

---

# 20. Result Management

The result module manages student academic results.

The general result workflow is:

```text
Teacher Login
      ↓
Teacher Dashboard
      ↓
Select Student
      ↓
Enter Marks
      ↓
Save Result
      ↓
Calculate Result Information
      ↓
Student Login
      ↓
Student Dashboard
      ↓
View Own Result
```

Result information can include:

* Subject-wise marks
* Total marks
* Percentage
* Grade
* Pass/Fail status

---

# 21. Student Access Control

Students are allowed to view their own academic information.

The application should prevent a student from accessing another student's result by manually changing IDs or URLs.

Example:

```text
Student A → Student A's Result ✓
Student A → Student B's Result ✗
```

This provides an important role-based access restriction in the application.

---

# 22. API Documentation

API information is maintained separately in:

```text
03_Documentation/API_Documentation.md
```

The API documentation contains information such as:

* API endpoint
* HTTP method
* URL
* Authentication requirement
* Request parameters
* Request body
* Response
* Error responses

---

# 23. Postman Collection

The project includes:

```text
03_Documentation/Postman_Collection.json
```

The collection can be imported into **Postman** for API testing.

### Import steps

1. Open Postman.
2. Select **Import**.
3. Select:

```text
Postman_Collection.json
```

4. Import the collection.
5. Start the Django server.
6. Execute the required API requests.

---

# 24. ER Diagram

The database Entity Relationship Diagram is provided as:

```text
03_Documentation/ER_Diagram.png
```

The ER diagram represents the major entities in the Student Result Portal and their relationships.

The major application areas include:

```text
Users
  │
  ├── Admin
  ├── Teacher
  └── Student
        │
        ↓
      Class
        │
        ↓
     Subject
        │
        ↓
      Result
        │
        ↓
      Marks
```

The actual relationships should be referred to in `ER_Diagram.png`.

---

# 25. Testing

Django tests can be executed using:

```bash
python manage.py test
```

The testing process covers application functionality such as:

* Authentication
* Role-based access
* Student functionality
* Teacher functionality
* Result functionality
* URL access
* Form validation
* Restricted access

Test results and screenshots can be maintained in the project's testing/documentation folders.

---

# 26. Useful Django Commands

### Check project configuration

```bash
python manage.py check
```

### Create migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

### Run tests

```bash
python manage.py test
```

### Create superuser

```bash
python manage.py createsuperuser
```

### Start server

```bash
python manage.py runserver
```

### Show migrations

```bash
python manage.py showmigrations
```

---

# 27. Git and GitHub

The project source code is maintained using Git.

GitHub repository:

```text
https://github.com/ujwalaBIT-cmyk/StudentResultPortal.git
```

The project repository maintains incremental commits representing the development process.

The repository link is also available in:

```text
03_Documentation/GitHub_Repo_Link.txt
```

---

# 28. Project Documentation

The `03_Documentation` folder contains:

```text
03_Documentation/
│
├── README.md
├── API_Documentation.md
├── Postman_Collection.json
├── ER_Diagram.png
└── GitHub_Repo_Link.txt
```

### README.md

Contains:

* Project overview
* Features
* Technology stack
* Project structure
* Installation instructions
* Database setup
* Environment configuration
* Migration instructions
* Login information
* Testing instructions

### API_Documentation.md

Contains API endpoint documentation.

### Postman_Collection.json

Contains API requests for testing through Postman.

### ER_Diagram.png

Contains the database ER diagram.

### GitHub_Repo_Link.txt

Contains the GitHub repository URL.

---

# 29. Security Considerations

The project follows basic security practices including:

* Password-protected authentication
* Role-based authorization
* Protected dashboard URLs
* Student result access restrictions
* Environment variables for database credentials
* `.env` excluded from version control
* Django's built-in security mechanisms

Sensitive information such as actual database passwords should never be committed to GitHub.

---

# 30. Future Enhancements

Possible future enhancements include:

* PDF result generation
* Result report download
* Email notifications
* Advanced dashboard analytics
* Attendance management
* Parent login
* REST API expansion
* Result search and filtering
* Automated result publishing
* AI-assisted academic analytics

---

# 31. Project Deliverables

The project submission contains the following major components:

```text
01_Source_Code/
02_Database/
03_Documentation/
04_Screenshots/
05_Testing/
06_Project_Report/
```

Database scripts:

```text
02_Database/
├── schema.sql
└── seed.sql
```

Documentation:

```text
03_Documentation/
├── README.md
├── API_Documentation.md
├── Postman_Collection.json
├── ER_Diagram.png
└── GitHub_Repo_Link.txt
```

---

# 32. Conclusion

The Student Result Portal provides a structured web-based solution for managing student academic results.

By using Django, MySQL, authentication, and role-based authorization, the application provides separate functionality for Admin, Teacher, and Student users.

The project also includes database scripts, API documentation, Postman testing support, ER documentation, automated testing, and GitHub version control to support deployment, evaluation, maintenance, and future development.
