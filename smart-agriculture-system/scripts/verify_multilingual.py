import os
import sys
import io

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# pyrefly: ignore [missing-import]
import ai_edge_litert.interpreter as tflite
# pyrefly: ignore [missing-import]
from PIL import Image
# pyrefly: ignore [missing-import]
import utils

utils.load_models(tflite)

langs = ['en', 'hi', 'hinglish']

print("MULTILINGUAL MODEL PREDICTION REPORT:")
print("=" * 60)

for lang in langs:
    print(f"\n--- LANGUAGE: {lang.upper()} ---")
    fert_res, fert_msg = utils.recommend_fertilizer(50, 40, 30, 'Wheat', lang=lang)
    print(f"Fertilizer: {fert_res} | Advice: {fert_msg}")
    
    yield_res, yield_msg = utils.predict_yield('Rice', 3.0, 1200, 30, lang=lang)
    print(f"Yield: {yield_res} tons | Note: {yield_msg}")
    
    soil_res, soil_msg = utils.predict_soil(80, 60, 70, 6.8, lang=lang)
    print(f"Soil: {soil_res} | Note: {soil_msg}")
    
    weather_res, weather_msg = utils.predict_weather_crop(28, 85, 200, lang=lang)
    print(f"Weather: {weather_res} | Note: {weather_msg}")
    
    dummy_img = Image.new('RGB', (224, 224), color=(34, 139, 34))
    buf = io.BytesIO()
    dummy_img.save(buf, format='JPEG')
    buf.seek(0)
    dis_res, dis_msg = utils.predict_disease(buf, lang=lang)
    print(f"Disease: {dis_res} | Tip: {dis_msg}")

print("\n" + "=" * 60)
print("ALL MULTILINGUAL TESTS PASSED!")
