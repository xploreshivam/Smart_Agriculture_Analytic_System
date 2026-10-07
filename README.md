# 🌾 Smart Agriculture Analytic System

A machine learning & deep learning powered agriculture management system with an ultra-modern **Glassmorphism UI** and **Multilingual support** (English, Hindi, Hinglish).

---

## 📂 Project Structure

```text
smart-agriculture-system/
│
├── app.py                      # Flask Application entry point & route controllers
├── utils.py                    # ML model loading, predictions & multilingual responses
├── run_server.bat              # One-click Windows batch launcher for Flask
│
├── models/                     # Trained Machine Learning & TFLite models
│   ├── crop_encoder.pkl        # Label encoder for fertilizer crops
│   ├── disease_classes.pkl     # Disease classification class labels
│   ├── disease_model.tflite    # TFLite CNN model for plant leaf disease detection
│   ├── fertilizer_model.pkl    # Random Forest model for fertilizer recommendations
│   ├── soil_model.pkl          # Soil quality classification model (Fertile/Medium/Poor)
│   ├── weather_crop_model.pkl  # Climate-based crop recommendation model
│   ├── yield_crop_encoder.pkl  # Label encoder for crop yield
│   └── yield_model.pkl         # Regression model for harvest yield estimation
│
├── templates/                  # Frontend HTML templates (Glassmorphism + Jinja2)
│   ├── index.html              # Base layout with navbar, language selector & hero
│   ├── crop_yield.html         # Harvest yield prediction interface
│   ├── soil_quality.html       # Soil health testing interface
│   ├── fertilizer.html         # Fertilizer recommendation interface
│   ├── disease.html            # Plant disease image scanning interface
│   ├── weather.html            # Weather-based crop suggestion interface
│   ├── error.html              # Error page template
│   └── module_placeholder.html # Modular placeholder template
│
├── static/                     # Frontend static assets
│   ├── css/
│   │   └── style.css           # Premium Glassmorphism design system & mesh animations
│   └── js/
│       ├── translations.js     # Multilingual engine (English, Hindi, Hinglish)
│       └── script.js           # UI interactive scripts
│
└── scripts/                    # Maintenance, training & verification scripts
    ├── create_disease_model.py # Script to generate TFLite disease CNN model
    ├── train_missing_models.py # Script to train and export missing ML models
    ├── test_all_models.py      # Health check script for all 5 models
    └── verify_multilingual.py  # Validation script for multilingual outputs
```

---

## 🚀 How to Run

### Method 1: One-Click Batch File (Windows)
Double-click [`smart-agriculture-system/run_server.bat`](smart-agriculture-system/run_server.bat).

### Method 2: Command Line
```bash
cd smart-agriculture-system
py app.py
```
Open your browser at: **http://127.0.0.1:5001**

### Method 3: VS Code / IDE Debugger
Press **F5** in VS Code (select `Python: Flask App`).

---

## ✨ Features
1. **🧪 Fertilizer Recommendation**: Predicts best fertilizer based on N, P, K & crop type.
2. **📈 Crop Yield Prediction**: Estimates harvest yield (in tons) from area, rain & temperature.
3. **🌍 Soil Quality Analysis**: Classifies soil into Fertile, Medium, or Poor with actionable tips.
4. **🔍 Leaf Disease Detection**: Deep Learning CNN model (`.tflite`) classifies leaf diseases and suggests treatments.
5. **⛅ Weather-based Crop Suggestion**: Recommends the ideal crop to sow based on weather parameters.
6. **🌐 Multilingual Support**: Instant toggle between **English**, **हिंदी**, and **Hinglish**.
7. **💎 Glassmorphism UI**: Frosted glass cards, ambient floating glow, and responsive micro-interactions.
