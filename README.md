# 🌾 **Agri-Smart Assistant**

### *AI + Agronomy for Smarter Indian Farming*

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit"/>
  <img src="https://img.shields.io/badge/Google%20Gemini%20AI-8E75B2?style=for-the-badge&logo=google"/>
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
</p>

> **Agri-Smart Assistant** is a next-gen **Hybrid Farming Intelligence System**.
> It blends **Machine Learning**, **Real-time Weather**, **Satellite Data**, and **Traditional Farmer Wisdom** to provide ultra-accurate crop recommendations for diverse Indian agro-climatic regions.

---

# 🚀 **Why This Project Stands Out**

Unlike standard ML crop tools, this system uses **two brains**:

### 🧠 **1. Machine Learning Engine**

Predicts crops using scientific parameters:

* N-P-K levels
* Soil chemistry
* Weather factors

### 🌱 **2. Farmer Logic Engine (Rule-Based Layer)**

A strict post-ML filter that applies real agronomy rules:

* Stops **Rice** recommendation in low rainfall districts
* Penalizes **Winter crops** in **Zaid/Summer**
* Boosts heat-tolerant crops in hot regions
* Ensures only *seasonally and geographically correct crops* appear

**This dual-system approach removes bias and makes predictions trustworthy.**

---

# 🌤️ **Live Weather + Climate Intelligence**

Integrated using **Open-Meteo API**

* Temperature
* Humidity
* Wind Speed
* Solar Radiation
* Annual rainfall (auto-estimated if API fails)

If weather data is missing → **Gemini AI predicts typical climatic values** for that location & season.

---

# 🌐 **Multilingual Support**

Because agriculture is regional ❤️
UI is fully available in:

* 🇬🇧 English
* 🇮🇳 हिंदी
* 🇮🇳 తెలుగు

Crop names are also localized.

---

# 🤖 **AI-Powered Agronomy Guidance**

Once the best crop is chosen, Gemini generates:

* Irrigation Plan
* Soil-enrichment tips
* Fertilizer strategy
* Season-based warnings
* Pest/disease precautions

Every output is crop & district specific.

---

# 🏆 **Smart Crop Ranking (Top 3 System)**

We don’t show wrong predictions.
The system filters out:

* Season-mismatched crops
* High-water crops in drought areas
* Temperature-incompatible crops

Only **valid**, **agronomically correct** top 3 crops are displayed.

---

# 🔍 **How the Intelligence Works**

```
User Input → Weather Fetch → ML Model → Farmer Logic Filter → 
Rescoring → Top 3 Valid Crops → Gemini AI Agronomy Tips
```

### ✔ Ensures correctness

### ✔ Avoids bias

### ✔ Farmer-friendly outputs

---

# 🖼️ **Screenshots**

<img width="1880" height="957" alt="image" src="https://github.com/user-attachments/assets/f003f873-e380-4a4d-8fbe-611e5f341b5f" />
<img width="1868" height="986" alt="image" src="https://github.com/user-attachments/assets/981f0140-a0c9-441f-a9e0-1feea3efaa07" />
<img width="1871" height="848" alt="image" src="https://github.com/user-attachments/assets/70b0de49-bbe2-4972-babd-4efe1110b8ea" />




---

# 🛠️ **Installation & Setup**

### **Prerequisites**

* Python 3.8 or above
* Gemini API key
* Streamlit installed

---

## 🔧 **1. Clone the Repository**

```bash
git clone https://github.com/your-username/agri-smart-assistant.git
cd agri-smart-assistant
```

---

## 📦 **2. Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 🔑 **3. Add Gemini API Key**

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ **4. Run the Application**

```bash
streamlit run app.py
```

---

# 🙌 **Made for Farmers. Powered by AI.**

If you like this project, ⭐ star the repository and contribute!

---
