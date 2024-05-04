# Cleric Project

## Overview
The Cleric Project is a web application designed to process and analyze call logs to extract actionable insights and present them in an easily digestible format. It uses FastAPI for the backend to handle API requests and React for the frontend to provide a dynamic user interface.

## Features
- **Submit Queries**: Users can submit specific questions they want answered from the call logs.
- **Upload Documents**: Users can upload or link to call log documents which are then processed by the application.
- **Extract Insights**: The application processes the uploaded call logs and extracts relevant facts that answer the user-submitted questions.
- **Interactive UI**: A simple, user-friendly interface that allows easy interaction with the application's features.

## Technologies Used
- **Backend**: FastAPI
- **Frontend**: React (Optional mention of state management like Redux, Context API)
- **Database**: SQLite for session management and storing processed results (if applicable)
- **Deployment**: Docker, AWS/GCP (if applicable)

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14.x+ (if using React for the frontend)
- npm or yarn
- pipenv or virtualenv (for Python dependency management)

### Installation

#### Backend Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/ravitheja990/cleric_project.git
   cd cleric_project/backend
   ```

2. **Set up a Python virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Unix/macOS
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server**
   ```bash
   uvicorn app.main:app --reload
   ```

#### Frontend Setup (if applicable)
1. **Navigate to the frontend directory**
   ```bash
   cd ../frontend
   ```

2. **Install JavaScript dependencies**
   ```bash
   npm install
   ```

3. **Start the frontend development server**
   ```bash
   npm start
   ```

### Usage
- Access the web application via `http://localhost:3000` (frontend) and manage APIs via `http://localhost:8000/docs` (backend).
Also, this web application is deployed at: 130.211.239.95 at the same respective ports for reference. 
