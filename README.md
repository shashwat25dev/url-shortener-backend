🔗 URL Shortener – Backend

This is the backend service for the URL Shortener application, built using FastAPI, PostgreSQL, and Redis.
It handles URL shortening, redirection, analytics, caching, and security.

🌐 Frontend Repository

The frontend for this project is available here:
👉 https://github.com/shashwat25dev/url-shortener-frontend

✨ Features

🔐 Generate unique short URLs

⚡ Redis caching for ultra-fast redirects

📊 Click tracking and analytics

🗑 Delete short URLs

⏳ Rate limiting

🔄 HTTP redirects

🧩 RESTful API

🛠 Tech Stack

FastAPI

PostgreSQL

Redis

SQLAlchemy

Docker

📌 API Endpoints
Method	Endpoint	Description
POST	/shorten	Create short URL
GET	/{shortCode}	Redirect to original URL
GET	/stats/{shortCode}	Get URL analytics
DELETE	/delete/{shortCode}	Delete short URL

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/shashwat25dev/url-shortener-backend.git
cd url-shortener-backend

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Environment Variables

Create .env file:

DATABASE_URL=postgresql://username:password@localhost:5432/urlshortener
REDIS_URL=redis://localhost:6379

5️⃣ Run the server
uvicorn main:app --reload


Backend runs at:
http://localhost:8000

🐳 Docker Support
docker-compose up --build

🔗 Connecting Backend to Frontend

Follow these steps to connect the React frontend with this FastAPI backend.

1️⃣ Run the Backend

Start the backend server:

uvicorn main:app --reload

It will run at:

http://localhost:8000

2️⃣ Configure Frontend API URL

In the frontend project, create or edit the .env file:

VITE_API_BASE_URL=http://localhost:8000

Restart the frontend after saving.



Starts:

FastAPI

PostgreSQL

Redis

📈 Redis Caching Flow

Client requests a short URL

Redis is checked first

If cache miss → PostgreSQL is queried

URL is cached in Redis

Next request is served from cache

🔒 Security

Input validation

SQL injection protection

Environment-based secrets

👤 Author

Shashwat Dwivedi
Full-Stack Developer
