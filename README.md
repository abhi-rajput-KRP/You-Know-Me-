<h1>You Know Me ? </h1>
<h4>An anonymous Confession platform</h4>

<h3>🔗 Live Demo: </h3>
[Visit Application](https://foodshare-donation.onrender.com)

<h2>FEATURES</h2>

<h3>Tech stack</h3>

  * Backend: Flask (Python)

  * Database & Authentication: Supabase

  * Frontend: HTML, CSS

  * Deployment: Render

<h3>PROJECT STRUCTURE</h3>

```
You-Know-Me-/
├── .gitignore
├── README.md
├── app.py
├── requirements.txt
├── templates/
│   ├── create_posts.html
│   ├── login_fail.html
│   ├── login.html
│   ├── posts.html
│   ├── register.html
└── .env
```
<h3>SETUP</h3>

### 1. Create a Virtual Environment</h4>

#### 🪟 Windows (CMD or PowerShell)
```
python -m venv venv 
venv\Scripts\activate
```

#### 🍎 macOS / 🐧 Linux
```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies
`pip install -r requirements.txt`

### 3. Configure Supabase

Create .env file and add credentials

SUPABASE_URL = Your-Supabase-project-url<br>
SUPABASE_KEY = Your-project-api-key


### 4. Run the Application
`python app.py`