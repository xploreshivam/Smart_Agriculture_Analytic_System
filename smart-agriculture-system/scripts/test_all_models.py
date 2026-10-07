import os
import sys
import io
import warnings
warnings.filterwarnings('ignore')

# Add parent directory to path so utils can be imported
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    # pyrefly: ignore [missing-import]
    import ai_edge_litert.interpreter as tflite
except ImportError:
    try:
        # pyrefly: ignore [missing-import]
        import tensorflow.lite as tflite
    except ImportError:
        tflite = None

# pyrefly: ignore [missing-import]
from PIL import Image
# pyrefly: ignore [missing-import]
import utils

print("=" * 60)
print("SMART AGRICULTURE SYSTEM - ONE-BY-ONE MODEL HEALTH CHECK")
print("=" * 60)

# Load all models
utils.load_models(tflite)

print("-" * 60)

# 1. FERTILIZER MODEL TEST
print("[TEST 1/5] Fertilizer Recommendation Model:")
if utils.models['fertilizer'] is not None and utils.models['crop_encoder'] is not None:
    try:
        classes = list(utils.models['crop_encoder'].classes_)
        sample_crop = classes[0]
        res, msg = utils.recommend_fertilizer(40, 50, 60, sample_crop)
        print(f"  -> STATUS: WORKING (SUCCESS)")
        print(f"  -> Sample Crop: {sample_crop}")
        print(f"  -> Input: N=40, P=50, K=60")
        print(f"  -> Result: {res}")
        print(f"  -> Message: {msg}")
    except Exception as e:
        print(f"  -> STATUS: FAILED ({e})")
else:
    print("  -> STATUS: NOT LOADED (Model or Crop Encoder missing)")

print("-" * 60)

# 2. CROP YIELD MODEL TEST
print("[TEST 2/5] Crop Yield Prediction Model:")
if utils.models['yield'] is not None and utils.models['yield_crop_encoder'] is not None:
    try:
        classes = list(utils.models['yield_crop_encoder'].classes_)
        sample_crop = classes[0]
        res, msg = utils.predict_yield(sample_crop, 2.5, 120, 28)
        print(f"  -> STATUS: WORKING (SUCCESS)")
        print(f"  -> Sample Crop: {sample_crop}")
        print(f"  -> Input: Area=2.5 ha, Rain=120 mm, Temp=28 C")
        print(f"  -> Result: {res} tons")
        print(f"  -> Message: {msg}")
    except Exception as e:
        print(f"  -> STATUS: FAILED ({e})")
else:
    print("  -> STATUS: NOT LOADED (yield_model.pkl missing from models folder)")

print("-" * 60)

# 3. SOIL HEALTH MODEL TEST
print("[TEST 3/5] Soil Health Prediction Model:")
if utils.models['soil'] is not None:
    try:
        res, msg = utils.predict_soil(60, 45, 50, 6.8)
        print(f"  -> STATUS: WORKING (SUCCESS)")
        print(f"  -> Input: N=60, P=45, K=50, pH=6.8")
        print(f"  -> Result: {res}")
        print(f"  -> Message: {msg}")
    except Exception as e:
        print(f"  -> STATUS: FAILED ({e})")
else:
    print("  -> STATUS: NOT LOADED (soil_model.pkl missing from models folder)")

print("-" * 60)

# 4. WEATHER CROP MODEL TEST
print("[TEST 4/5] Weather-Based Crop Suggestion Model:")
if utils.models['weather'] is not None:
    try:
        res, msg = utils.predict_weather_crop(26, 75, 150)
        print(f"  -> STATUS: WORKING (SUCCESS)")
        print(f"  -> Input: Temp=26 C, Humidity=75%, Rain=150 mm")
        print(f"  -> Result: {res}")
        print(f"  -> Message: {msg}")
    except Exception as e:
        print(f"  -> STATUS: FAILED ({e})")
else:
    print("  -> STATUS: NOT LOADED (weather_crop_model.pkl missing from models folder)")

print("-" * 60)

# 5. DISEASE MODEL TEST
print("[TEST 5/5] Leaf Disease Detection Model (TFLite):")
if utils.models['disease_interpreter'] is not None and utils.models['disease_classes'] is not None:
    try:
        dummy_img = Image.new('RGB', (224, 224), color=(34, 139, 34))
        buf = io.BytesIO()
        dummy_img.save(buf, format='JPEG')
        buf.seek(0)
        res, msg = utils.predict_disease(buf)
        print(f"  -> STATUS: WORKING (SUCCESS)")
        print(f"  -> Input: 224x224 RGB Leaf Image")
        print(f"  -> Available Classes: {utils.models['disease_classes']}")
        print(f"  -> Predicted Result: {res}")
        print(f"  -> Tip: {msg}")
    except Exception as e:
        print(f"  -> STATUS: FAILED ({e})")
else:
    print("  -> STATUS: NOT LOADED (disease_model.tflite or disease_classes.pkl missing)")

print("=" * 60)
