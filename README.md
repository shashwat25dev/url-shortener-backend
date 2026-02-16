🔗 URL Shortener

A high-performance URL shortener built with FastAPI, PostgreSQL, Redis, and React.
It allows users to shorten long URLs, redirect instantly, view analytics, and delete short links — all with enterprise-grade performance and security.

✨ Features

🔐 Unique Short URLs

⚡ Redis-based Caching for ultra-fast redirects

📊 URL Analytics (click count & stats)

🗑 Delete Short URLs

⏳ Rate Limiting

🔄 Instant Redirects

🧩 RESTful API

🌐 Modern React Frontend

🏗️ System Architecture
React Frontend
     ↓
FastAPI Backend
     ↓
PostgreSQL (Persistent Storage)
     ↓
Redis (Cache Layer)


Redis is used to cache frequently accessed short URLs, drastically reducing database hits and improving response times.

🛠 Tech Stack
Backend

FastAPI

PostgreSQL

Redis

SQLAlchemy

Docker

Frontend

React

TypeScript

Tailwind CSS

📌 API Endpoints
Method	Endpoint	Description
POST	/shorten	Create short URL
GET	/{shortCode}	Redirect to original URL
GET	/stats/{shortCode}	Get analytics
DELETE	/delete/{shortCode}	Delete URL
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener

2️⃣ Backend Setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Create a .env file:

DATABASE_URL=postgresql://username:password@localhost:5432/urlshortener
REDIS_URL=redis://localhost:6379


Run:

uvicorn main:app --reload

3️⃣ Frontend Setup
cd frontend
npm install
npm run dev

🐳 Run using Docker
docker-compose up --build


This will start:

FastAPI

PostgreSQL

Redis

React Frontend

📈 Redis Caching Logic

When a user requests a short URL

Redis is checked first

If not found → PostgreSQL is queried

Result is cached in Redis

Next request hits Redis directly

This makes redirects blazing fast ⚡

🔒 Security

Input validation

Rate limiting

SQL Injection protection

Redis cache isolation

Environment-based secrets