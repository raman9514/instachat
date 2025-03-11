# Instant Chat

## 🚀 A Lightweight, Real-Time Chat Room App
Instant Chat is a simple, real-time chat application built using **Django, Redis, and Django Channels**. It allows users to join or create chat rooms instantly without any data storage. Messages disappear upon refresh, ensuring a completely temporary and anonymous chat experience.

## 🔥 Features
- ✅ **Zero Data Storage** – No logs, no history, just pure conversations.
- ✅ **Real-Time Messaging** – Powered by **WebSockets** for instant communication.
- ✅ **Open-Source & Lightweight** – Built with Django, Redis, and Django Channels.
- ✅ **Temporary & Anonymous** – Refresh the page, and everything vanishes.
- ✅ **Create or Join Any Chat Room** – Connect with people worldwide.

## 🛠 Tech Stack
- **Backend:** Django, Django Channels
- **Real-Time Communication:** WebSockets, Redis
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Deployment:** Nginx, Daphne, Gunicorn (optional)

## 📦 Installation

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/raman9514/instachat.git
cd instachat
```

### 2️⃣ Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Redis (Required for WebSockets):
Ensure Redis is installed and running on your machine.
```bash
# Start Redis server
redis-server
```

### 5️⃣ Run Django migrations:
```bash
python manage.py migrate
```

### 6️⃣ Start the development server:
```bash
python manage.py runserver
```

Now, open **http://127.0.0.1:8000** in your browser and start chatting!

## ⚡ WebSocket Endpoint
WebSocket connections are established at:
```plaintext
ws://127.0.0.1:8000/ws/chat/<str:group_name>
```

## 🏗 Future Improvements
- [ ] User authentication for persistent usernames
- [ ] Improved UI/UX with chat bubbles
- [ ] Message encryption for security
- [ ] Deployment guides for cloud platforms

## 🤝 Contributing
Pull requests are welcome! Feel free to fork the project and submit improvements.

## 📜 License
This project is **open-source** under the MIT License.

---
### ⭐ Don't forget to star the repo if you like it! ⭐

