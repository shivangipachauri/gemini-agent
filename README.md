## **Gemini Agent: Fullstack Prompt-Based Action App**



A simple fullstack application using Django REST (backend) and Nuxt 3 (frontend) that takes a text prompt, sends it to the Gemini API, and performs two types of actions based on the response (e.g., joke generation or weather info retrieval).



### Features



\- Frontend: Nuxt 3 + TailwindCSS + Pinia (with persisted store)

\- Backend: Django + Django REST Framework

\- Gemini API: Integrates with Gemini (Google's LLM API) to process prompts and decide actions

\- Two Actions Implemented: (Example) Generate a joke and fetch weather



### 🔧 Setup Instructions



#### Prerequisites



\- Python 3.10+

\- Node.js 18+

\- Google Gemini API Key



##### 1\. Clone the Repo



git clone https://github.com/shivangipachauri/gemini-agent.git



cd gemini-agent



##### 2\. Backend Setup (Django)



cd backend

python -m venv venv

source venv/bin/activate   (or venv\\Scripts\\activate on Windows)

pip install -r requirements.txt



Create a .env file in the backend folder:



GEMINI\_API\_KEY=your\_gemini\_api\_key\_here



Run the server:



python manage.py runserver



##### 3\. Frontend Setup (Nuxt 3)



cd ../frontend

npm install

npm run dev



*Update apiBaseUrl in your Nuxt code if needed (default is http://localhost:8000/ for backend).*



#### 📂 Folder Structure



gemini-agent/

├── backend/   # Django backend (Gemini API, REST endpoint)

├── frontend/  # Nuxt 3 frontend (Tailwind, Pinia)

└── README.md



#### Example Prompt



“Tell me a joke about AI”



Response: {"action": "joke", "result": "Why did the AI go to therapy? Because it had deep learning issues!"}



#### Author



Shivangi Pachauri — feel free to raise issues or feature requests!

