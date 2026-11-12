# Red's Cyber Nook 💻🛡️

⚠️ Notice: This project has been redesigned and split into two distinct sites.

Check out the redthemadhacker and allnyteallbyte repositories to view the updated personal portfolio and terminal-inspired showcase for Amari James (SE, CySA, LA). The new sites highlight current engineering credentials, security background, enterprise systems experience, live active projects, and direct contact avenues.

---

## 🌐 Live Production

* **URL:** [https://reds-cyber-nook-8c6f2fdd415e.herokuapp.com/](https://reds-cyber-nook-8c6f2fdd415e.herokuapp.com/)

---

## 🛠️ Stack & Dependencies

* **Host Environment:** Linux (Ubuntu 24.10), VS Code, GitHub, Heroku
* **Runtime & Web Framework:** Python, Flask, Gunicorn
* **Frontend:** HTML5, Modern CSS styling, dynamic responsive layouts

---

## ⚙️ Architecture & Deployment Notes

* **Static-to-WSGI Wrapper:** Heroku natively looks for Node.js buildpacks when encountering certain frontend project setups. To maintain an ultra-lean runtime without unnecessary Node overhead, the static site is served through a lightweight Python/Flask WSGI layer orchestrated by `gunicorn`.
* **Deployment Assets:**
  * `app.py`: Flask static file and route handler.
  * `Procfile`: Declarative process runner targeting Gunicorn (`web: gunicorn app:app`).
  * `requirements.txt`: Minimal WSGI dependencies (`Flask`, `gunicorn`).

## Acknowledgements 
* Copilot, Gemini

### Version History
* 1.0
    - Initial release 
* 2.0
    - Version 2.0 release. Legibility fixes and page updates. 
* 2.1
    - Version 2.1 release. Resume and page updates.  

---

## 🚀 Local Development Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/redthemadhacker/reds-cyber-nook.git](https://github.com/redthemadhacker/reds-cyber-nook.git)
   cd reds-cyber-nook

   ### Help
* Deploy: Issues deploying with Heroku due to site being written in HTML while Heroku automatically looks for Node.js. Added app.py, requirements.txt and Procfile with Python, Flask, and Gunicorn. 

### Authors
* Amari James
* [@redthemadhacker](https://github.com/redthemadhacker)
