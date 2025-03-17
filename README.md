# Secure File Upload System

This project is **Secure File Upload System** built with **Django REST Framework** (backend) and **Svelte** (frontend). It allows users to upload, encrypt, download, and manage files securely.

## Features

- User authentication (JWT-based login/logout)
- Secure file uploads with encrypted filenames
- File listing with download functionality
- Role-based access control (admin/user)
- Responsive and clean UI with Svelte

## Tech Stack

- **Backend:** Django, Django REST Framework, JWT Authentication
- **Frontend:** Svelte
- **Database:** SQLite

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/MohibShaikh/Secure-File-API.git
```

### 2. Backend Setup (Django)

```sh
source venv/bin/activate  # Activate virtual environment (Linux/macOS)
venv\Scripts\activate # Activate virtual environment (Windows)
```
```sh
pip install -r requirements.txt
python manage.py runserver
```

*Backend will run at* **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

### 3. Frontend Setup (Svelte)

```sh
cd frontend  # Navigate to the frontend folder
npm install  # Install dependencies
npm run dev  # Start the development server
```

*Frontend will run at* **[http://localhost:5173/](http://localhost:5173/)**


## Features of Secure File Storage System
- 🔐 **Authentication:** JWT-based login with role-based access.
- 📂 **Secure File Management:** Upload, list, and download encrypted files.
- 🔒 **Encrypted Filenames:** SHA-256 hashing for file name protection.
- 🚀 **Lightweight & Fast:** Built with Django REST Framework & Svelte.
- 🛠  **Deployment-Ready:** Works with SQLite & will be deployed on cloud platforms.

## API Endpoints

- **Login:** `POST /api/token/`
- **Refresh Token:** `POST /api/token/refresh/`
- **Upload File:** `POST /api/files/upload_file/`
- **List Files:** `GET /api/files/`
- **Download File:** `GET /api/files/{id}/`

## Usage

1. **Login** on the frontend.
2. **Upload files** via the UI.
3. **View and download files** from the file list.

## License

This project is open-source. Modify and use as needed!

---
