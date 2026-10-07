import os
import pickle
# pyrefly: ignore [missing-import]
import numpy as np
# pyrefly: ignore [missing-import]
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
os.makedirs(MODELS_DIR, exist_ok=True)

np.random.seed(42)

# ==========================================
# 1. YIELD MODEL (yield_model.pkl)
# Input features: [encoded_crop, area, rain, temp]
# Target: yield in tonnes
# ==========================================
print("Training Yield Model...")

# Classes in yield_crop_encoder.pkl:
# 0: Cotton, 1: Maize, 2: Rice, 3: Soybean, 4: Sugarcane, 5: Wheat
# Typical yield rates per hectare:
# Cotton: ~1.5 - 3.5 tons/ha
# Maize: ~4.0 - 8.0 tons/ha
# Rice: ~3.5 - 6.5 tons/ha
# Soybean: ~2.0 - 4.0 tons/ha
# Sugarcane: ~50.0 - 90.0 tons/ha
# Wheat: ~3.0 - 5.5 tons/ha

base_yield_per_ha = {
    0: 2.2,   # Cotton
    1: 5.5,   # Maize
    2: 4.5,   # Rice
    3: 2.8,   # Soybean
    4: 68.0,  # Sugarcane
    5: 4.0    # Wheat
}

X_yield = []
y_yield = []

N_SAMPLES_PER_CROP = 400
for crop_code, base_rate in base_yield_per_ha.items():
    for _ in range(N_SAMPLES_PER_CROP):
        area = np.random.uniform(0.5, 50.0)          # hectares
        rain = np.random.uniform(300.0, 2500.0)      # mm
        temp = np.random.uniform(15.0, 42.0)         # Celsius
        
        # Weather factor: optimum rain and temp boosts yield
        rain_factor = 1.0 - abs(rain - 1000.0) / 4000.0
        temp_factor = 1.0 - abs(temp - 27.0) / 60.0
        weather_multiplier = np.clip(rain_factor * temp_factor, 0.6, 1.4)
        noise = np.random.normal(1.0, 0.08)
        
        total_yield = area * base_rate * weather_multiplier * noise
        total_yield = max(0.5, round(total_yield, 2))
        
        X_yield.append([crop_code, area, rain, temp])
        y_yield.append(total_yield)

yield_model = RandomForestRegressor(n_estimators=100, max_depth=12, random_state=42)
yield_model.fit(X_yield, y_yield)

yield_path = os.path.join(MODELS_DIR, 'yield_model.pkl')
with open(yield_path, 'wb') as f:
    pickle.dump(yield_model, f)
print(f"-> Saved: {yield_path} (Size: {os.path.getsize(yield_path)} bytes)")


# ==========================================
# 2. SOIL HEALTH MODEL (soil_model.pkl)
# Input features: [N, P, K, pH]
# Target classes: 'Fertile', 'Medium', 'Poor'
# ==========================================
print("Training Soil Health Model...")

X_soil = []
y_soil = []

# Class 1: Fertile (Optimal N: 60-140, P: 40-90, K: 40-90, pH: 6.0-7.8)
for _ in range(700):
    n = np.random.uniform(60, 140)
    p = np.random.uniform(40, 90)
    k = np.random.uniform(40, 90)
    ph = np.random.uniform(6.0, 7.8)
    X_soil.append([n, p, k, ph])
    y_soil.append("Fertile")

# Class 2: Medium (Moderate nutrients or slightly sub-optimal pH)
for _ in range(700):
    n = np.random.uniform(30, 70)
    p = np.random.uniform(20, 45)
    k = np.random.uniform(20, 45)
    ph = np.random.choice([np.random.uniform(5.5, 6.2), np.random.uniform(7.6, 8.3)])
    X_soil.append([n, p, k, ph])
    y_soil.append("Medium")

# Class 3: Poor (Deficient nutrients or acidic/alkaline pH)
for _ in range(700):
    n = np.random.uniform(5, 35)
    p = np.random.uniform(5, 20)
    k = np.random.uniform(5, 20)
    ph = np.random.choice([np.random.uniform(3.5, 5.5), np.random.uniform(8.3, 10.5)])
    X_soil.append([n, p, k, ph])
    y_soil.append("Poor")

soil_model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
soil_model.fit(X_soil, y_soil)

soil_path = os.path.join(MODELS_DIR, 'soil_model.pkl')
with open(soil_path, 'wb') as f:
    pickle.dump(soil_model, f)
print(f"-> Saved: {soil_path} (Size: {os.path.getsize(soil_path)} bytes)")


# ==========================================
# 3. WEATHER CROP MODEL (weather_crop_model.pkl)
# Input features: [temp, humid, rain]
# Target: Crop Name
# ==========================================
print("Training Weather-Based Crop Suggestion Model...")

crops_weather = {
    "Rice":       {"temp": (21, 35), "humid": (75, 95), "rain": (150, 300)},
    "Wheat":      {"temp": (12, 25), "humid": (45, 70), "rain": (40, 100)},
    "Maize":      {"temp": (18, 32), "humid": (55, 80), "rain": (60, 150)},
    "Cotton":     {"temp": (24, 38), "humid": (50, 75), "rain": (50, 120)},
    "Sugarcane":  {"temp": (22, 36), "humid": (70, 92), "rain": (120, 250)},
    "Soybean":    {"temp": (20, 32), "humid": (60, 85), "rain": (70, 180)},
    "Chickpea":   {"temp": (14, 26), "humid": (35, 60), "rain": (30, 80)},
    "Jute":       {"temp": (24, 38), "humid": (75, 95), "rain": (140, 280)},
    "Coffee":     {"temp": (17, 28), "humid": (65, 90), "rain": (110, 220)}
}

X_weather = []
y_weather = []

for crop_name, conditions in crops_weather.items():
    t_min, t_max = conditions["temp"]
    h_min, h_max = conditions["humid"]
    r_min, r_max = conditions["rain"]
    for _ in range(300):
        t = np.random.uniform(t_min, t_max) + np.random.normal(0, 1.0)
        h = np.random.uniform(h_min, h_max) + np.random.normal(0, 2.0)
        r = np.random.uniform(r_min, r_max) + np.random.normal(0, 5.0)
        X_weather.append([t, h, r])
        y_weather.append(crop_name)

weather_model = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42)
weather_model.fit(X_weather, y_weather)

weather_path = os.path.join(MODELS_DIR, 'weather_crop_model.pkl')
with open(weather_path, 'wb') as f:
    pickle.dump(weather_model, f)
print(f"-> Saved: {weather_path} (Size: {os.path.getsize(weather_path)} bytes)")

print("\nAll 3 missing models trained and saved successfully!")
