# 🐾 PurrPCScanAdvisor

A beautifully crafted, minimalist hardware diagnostic companion that translates raw machine telemetry into clear, human-readable advice with a touch of whimsy.

## 📡 Live Deployment Note (Recruiter Review)
Because browser sandboxing securely blocks websites from executing low-level kernel queries (`psutil`, system hardware registries) on a remote client's machine, the live-hosted application utilizes automated mock fallback telemetry modules. This allows seamless inspection of UI state handling, live animations, historical telemetry databases, and custom AI chat modules instantly.

---

## 🖥️ Local Architecture Setup (Run with Live Hardware Telemetry)

To hook the application up to your actual computer core registries and capture live machine data, you can run the local Python agent.

### 1. Fire up the Backend Engine
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload