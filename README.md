# 📚 ManageBooks - User Management & Email Scheduler

A Django-based project to:

- 👤 Register and log in users  
- 📖 Manage books & scheduled emails  
- 📬 Send scheduled emails via dashboard  
- ⚙️ Handle tasks asynchronously with Celery & RabbitMQ  

---

## 🚀 Features

- ✅ User registration & authentication  
- ✅ Book & scheduled email management  
- 🕒 Email scheduling with delay or repetition  
- 🖥️ Admin dashboard for scheduled emails  
- 🧵 Background task processing via Celery + RabbitMQ  
- 🎨 Fully templated HTML frontend (Django templates)  

---

## 🛠️ Tech Stack

- 🐍 **Backend**: Django, Celery  
- 🐇 **Task Queue**: RabbitMQ  
- 🗄️ **Database**: SQLite *(can be swapped with PostgreSQL)*  
- 🖼️ **Frontend**: Django Templates  
- 🔧 **Other Tools**: Redis *(optional)*, Python 3.11+, HTML  

---

## 🔑 How It Works

### 👥 User Registration & Login

- Built using Django’s auth system in `accounts/`  
- Custom login & signup forms via Django templates  

### 📨 Email Scheduling

- Users create emails and schedule delivery  
- Emails can repeat daily/weekly/etc.  

### 🔄 Celery Background Task

- `tasks.py` defines email-sending jobs  
- Celery + RabbitMQ handles tasks asynchronously  

### 🧭 Admin Dashboard

- Custom dashboard to view, edit, or delete scheduled emails  

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AmirRezaiyan/managebooks-send-email-manage-users.git
cd managebooks-send-email-manage-users

2️⃣ Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies

pip install -r requirements.txt
If requirements.txt is missing:


pip install django celery django-celery-beat
4️⃣ Run Migrations

python manage.py migrate
5️⃣ Run Redis or RabbitMQ Server (Example via Docker)

docker run -d --hostname my-rabbit --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
6️⃣ Start Celery Worker

celery -A gmail worker -l info
(Optional: Start celery beat if using periodic tasks)

7️⃣ Run Django Server

python manage.py runserver
✅ Example User Flow
Go to /accounts/signup/ → Create an account

Log in → Redirect to home

Create a scheduled email → Add subject, message, time

Visit dashboard → View/edit/delete tasks

Email sent automatically via Celery 🎯

📌 Notes
⚠️ pyvenv.cfg is part of virtualenv – do not push it to production repositories

🛢️ Default DB is SQLite → Consider PostgreSQL for production

