# 🛍️ Simple E-Commerce Backend with Django & DRF

A production-ready backend API for a simple e-commerce platform built using **Django** and **Django REST Framework**, featuring authentication, product management, cart system, and order checkout.

---

## 🚀 Features

- 🔐 JWT Authentication (Login/Register)
- 🛒 Cart System (user-specific)
- 📦 Product Management (admin-only CRUD)
- 💳 Checkout System (convert cart → order)
- 🔍 Product Search & Filtering
- 📘 Swagger API Docs

---

## 📁 Project Structure

```

ecommerce-backend/
├── ecommerce/         # Project settings
├── store/             # Core app (models, views, serializers)
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md

````

---

## 🛠 Tech Stack

- **Backend:** Django, Django REST Framework
- **Auth:** JWT (using `djangorestframework-simplejwt`)
- **Database:** SQLite (easy dev) or PostgreSQL (production-ready)
- **Docs:** Swagger (via `drf-yasg`)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo
```bash
git clone https://github.com/itsahnafarafat/-Simple-E-Commerce-Backend-with-Django-DRF-.git
cd ecommerce-backend
````

### 2️⃣ Create & activate virtual environment

```bash
python -m venv env
source env/bin/activate     # On Windows: env\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py migrate
```

### 5️⃣ Create superuser (admin)

```bash
python manage.py createsuperuser
```

### 6️⃣ Start the development server

```bash
python manage.py runserver
```

---

## 🔑 API Authentication

This project uses **JWT Authentication**.

* **Login:**
  `POST /api/token/`
  → returns `access` and `refresh` tokens

* **Refresh:**
  `POST /api/token/refresh/`

Add token to headers:

```
Authorization: Bearer <access_token>
```

---

## 📬 API Endpoints Overview

| Resource     | Endpoint         | Methods           | Auth Required      |
| ------------ | ---------------- | ----------------- | ------------------ |
| Products     | `/api/products/` | GET, POST, PUT    | Admin only (write) |
| Cart         | `/api/cart/`     | GET, POST, DELETE | ✅ Yes              |
| Orders       | `/api/orders/`   | GET, POST         | ✅ Yes              |
| Auth (JWT)   | `/api/token/`    | POST              | ❌ No               |
| Swagger Docs | `/swagger/`      | GET               | ❌ No               |

---

## 🧪 Sample API Request (Using curl)

```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "adminpassword"}'
```

---

## 📘 API Documentation

Visit:

```
http://localhost:8000/swagger/
```

---

## 🧹 To-Do / Possible Improvements

* [ ] Add Stripe/PayPal integration
* [ ] Add product images/media
* [ ] Add user profile and address model
* [ ] Add pagination to cart/orders
* [ ] Deploy to Render or Railway

---

## 🧑‍💻 Author

**Ahanf Arafat**
Backend Developer | Python & Django Specialist
[GitHub](https://github.com/itsahnafarafat) | [LinkedIn](https://www.linkedin.com/in/ahnaf-arafat-30189a357/)

---

## 📝 License

MIT License – do whatever you want, just give credit :)

````

---

### ✅ Next Step:

1. Save this as `README.md` in the root of your project.
2. Replace `itsahnafarafat` and `Ahnaf Arafat` with your GitHub and LinkedIn.
3. Commit it:

```bash
git add README.md
git commit -m "📘 Add professional README with features, setup, and docs"
git push
````


