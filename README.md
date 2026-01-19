---
# TruthScan Frontend

TruthScan is an interactive web application that visualizes credibility analysis results for **text claims and images**.

This frontend consumes the TruthScan backend API and presents results using **animated gauges**, clear verdicts, and human-readable explanations.

---

## ✨ Features

- Text claim analysis
- Image verification
- Animated circular confidence & risk gauges
- Verdict badges with clear color coding
- Explanation of why content was flagged
- Clean, dark-mode UI

---

## 🖥️ Built With

- **Streamlit** – frontend framework
- **SVG + CSS animations** – gauge visualizations
- **Requests** – backend communication
- **Custom UI components** – modern, minimal design

---

## 🔗 Backend Dependency

This app requires a running TruthScan backend.

Set the API base URL inside `app.py`:

```python
API_BASE = "https://truthscan-backend-production.up.railway.app/verify"


🚀 Running Locally

git clone https://github.com/your-username/truthscan-streamlit.git
cd truthscan-streamlit
pip install -r requirements.txt
streamlit run app.py

App runs at:

http://localhost:8501

🌍 Deployment
	•	Deployed on Streamlit Cloud
	•	Connected to live Railway backend
	•	Fully public demo

⸻

🧠 Design Philosophy

TruthScan does not say “this is true”.

It says:
	•	How confident the system is
	•	How risky the claim or image appears
	•	Why it raised concern

This keeps humans in control of final judgment.

⸻

📸 Example Use Cases
	•	Checking viral headlines
	•	Screening screenshots and images
	•	Teaching media literacy
	•	Demonstrating AI risk analysis


# TruthScan Frontend

🔗 **Live Demo:** https://your-app-name.streamlit.app
🔗 **Backend API:** https://truthscan-backend-production.up.railway.app


⸻


⚠️ Disclaimer

This tool is for decision support only.
It does not replace expert verification or fact-checking.


