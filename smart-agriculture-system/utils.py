import os
import pickle
import warnings
warnings.filterwarnings('ignore')
# pyrefly: ignore [missing-import]
import numpy as np
# pyrefly: ignore [missing-import]
import pandas as pd
# pyrefly: ignore [missing-import]
from PIL import Image

# Setup Model Paths for student project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# Yeh dictionaries hamare models ko store karengi
models = {
    'fertilizer': None,
    'crop_encoder': None,
    'yield': None,
    'yield_crop_encoder': None,
    'soil': None,
    'weather': None,
    'disease_interpreter': None,
    'disease_input_details': None,
    'disease_output_details': None,
    'disease_classes': None
}

def load_models(tflite_module):
    """Sare machine learning models ko load karta hai server start hone par."""
    print("Models load ho rahe hain...")
    try:
        def load_pkl(filename):
            path = os.path.join(MODELS_DIR, filename)
            if not os.path.exists(path):
                print(f"File nahi mili: {filename}")
                return None
            with open(path, 'rb') as f:
                return pickle.load(f)

        # 1. Fertilizer Models
        models['fertilizer'] = load_pkl('fertilizer_model.pkl')
        models['crop_encoder'] = load_pkl('crop_encoder.pkl')
        
        # 2. Yield Models
        models['yield'] = load_pkl('yield_model.pkl')
        models['yield_crop_encoder'] = load_pkl('yield_crop_encoder.pkl')
        
        # 3. Soil Model
        models['soil'] = load_pkl('soil_model.pkl')
        
        # 4. Weather Model
        models['weather'] = load_pkl('weather_crop_model.pkl')
        
        # 5. Disease Model (Image Processing)
        if not tflite_module:
            try:
                # pyrefly: ignore [missing-import]
                import tflite_runtime.interpreter as tflite_module
            except ImportError:
                try:
                    # pyrefly: ignore [missing-import]
                    import ai_edge_litert.interpreter as tflite_module
                except ImportError:
                    try:
                        # pyrefly: ignore [missing-import]
                        import tensorflow.lite as tflite_module
                    except ImportError:
                        tflite_module = None

        if tflite_module:
            tflite_path = os.path.join(MODELS_DIR, 'disease_model.tflite')
            if os.path.exists(tflite_path):
                interpreter = tflite_module.Interpreter(model_path=tflite_path)
                interpreter.allocate_tensors()
                models['disease_interpreter'] = interpreter
                models['disease_input_details'] = interpreter.get_input_details()
                models['disease_output_details'] = interpreter.get_output_details()
                models['disease_classes'] = load_pkl('disease_classes.pkl')
            else:
                print("Warning: disease_model.tflite nahi mili.")
        else:
            print("Warning: TFLite module import nahi ho paya.")
                
        print("Sare models successfully load ho gaye!")
    except Exception as e:
        print(f"Error aagaya model loading me: {e}")

def validate_numeric(*args):
    """Check karta hai ki user ne numbers hi daale hain na."""
    try:
        nums = [float(arg) for arg in args]
        if any(n < 0 for n in nums):
            return False, "Negative values allowed nahi hain."
        return True, nums
    except (ValueError, TypeError):
        return False, "Kripya sirf numbers daalein."


# --- CORE LOGIC FUNCTIONS WITH MULTILINGUAL SUPPORT ---

def recommend_fertilizer(n, p, k, crop, lang='en'):
    valid, values = validate_numeric(n, p, k)
    if not valid:
        return "Validation Error", values

    if models['fertilizer'] is None:
        err_msg = {
            "en": "Fertilizer model is not loaded.",
            "hi": "उर्वरक मॉडल लोड नहीं हुआ।",
            "hinglish": "Fertilizer model load nahi hua."
        }
        return "Model Error", err_msg.get(lang, err_msg["en"])
    
    try:
        encoded_crop = models['crop_encoder'].transform([crop])[0]
        prediction = models['fertilizer'].predict([[n, p, k, encoded_crop]])
        
        advice_msgs = {
            "en": "This fertilizer is optimal for your crop health.",
            "hi": "यह उर्वरक आपकी फसल के लिए सबसे उपयुक्त रहेगा।",
            "hinglish": "Ye fertilizer aapke crop ke liye best rahega."
        }
        return prediction[0], advice_msgs.get(lang, advice_msgs["en"])
    except Exception as e:
        return "Error", str(e)


def predict_yield(crop, area, rain, temp, lang='en'):
    valid, values = validate_numeric(area, rain, temp)
    if not valid:
        return "Validation Error", values

    if models['yield'] is None:
        err_msg = {
            "en": "Yield model is not loaded.",
            "hi": "उत्पादन मॉडल लोड नहीं हुआ।",
            "hinglish": "Yield model load nahi hua."
        }
        return "Model Error", err_msg.get(lang, err_msg["en"])
        
    try:
        encoded_crop = models['yield_crop_encoder'].transform([crop])[0]
        prediction = models['yield'].predict([[encoded_crop, float(area), float(rain), float(temp)]])
        
        yield_msgs = {
            "en": f"Estimated yield for {area} hectares.",
            "hi": f"{area} हेक्टेयर के लिए अनुमानित उत्पादन।",
            "hinglish": f"{area} hectare ke liye estimated yield."
        }
        return round(prediction[0], 2), yield_msgs.get(lang, yield_msgs["en"])
    except Exception as e:
        return "Error", str(e)


def predict_soil(n, p, k, ph, lang='en'):
    valid, values = validate_numeric(n, p, k, ph)
    if not valid:
        return "Validation Error", values
    
    if float(ph) < 0 or float(ph) > 14:
        ph_err = {
            "en": "pH level must be between 0 and 14.",
            "hi": "pH स्तर 0 से 14 के बीच होना चाहिए।",
            "hinglish": "pH level 0 se 14 ke beech hona chahiye."
        }
        return "Error", ph_err.get(lang, ph_err["en"])

    if models['soil'] is None:
        err_msg = {
            "en": "Soil model is not loaded.",
            "hi": "मिट्टी मॉडल लोड नहीं हुआ।",
            "hinglish": "Soil model load nahi hua."
        }
        return "Model Error", err_msg.get(lang, err_msg["en"])
        
    try:
        prediction = models['soil'].predict([[float(n), float(p), float(k), float(ph)]])
        predicted_class = prediction[0]
        
        soil_messages = {
            "en": {
                "Fertile": "Your soil is in excellent (Fertile) condition.",
                "Medium": "Soil condition is moderate. Organic compost or fertilizer recommended.",
                "Poor": "Soil fertility is poor. Soil conditioning and nutrient enrichment required."
            },
            "hi": {
                "Fertile": "आपकी मिट्टी बहुत अच्छी (उपजाऊ) स्थिति में है।",
                "Medium": "मिट्टी सामान्य है, थोड़ा जैविक खाद या उर्वरक डालने की जरूरत है।",
                "Poor": "मिट्टी की उर्वरता खराब है, विशेष उपचार और पोषण की आवश्यकता है।"
            },
            "hinglish": {
                "Fertile": "Aapki mitti bahut achi (Fertile) condition me hai.",
                "Medium": "Mitti theek hai, thoda khad (fertilizer) daalna padega.",
                "Poor": "Mitti ki condition kharab hai, treatment ki zaroorat hai."
            }
        }
        lang_dict = soil_messages.get(lang, soil_messages["en"])
        return predicted_class, lang_dict.get(predicted_class, "Check nutrients.")
    except Exception as e:
        return "Error", str(e)


def predict_weather_crop(temp, humid, rain, lang='en'):
    valid, values = validate_numeric(temp, humid, rain)
    if not valid:
        return "Validation Error", values

    if models['weather'] is None:
        err_msg = {
            "en": "Weather model is not loaded.",
            "hi": "मौसम मॉडल लोड नहीं हुआ।",
            "hinglish": "Weather model load nahi hua."
        }
        return "Model Error", err_msg.get(lang, err_msg["en"])
        
    try:
        prediction = models['weather'].predict([[float(temp), float(humid), float(rain)]])
        
        weather_msgs = {
            "en": "Based on current weather, this is the most suitable crop to grow.",
            "hi": "मौसम के अनुसार यह फसल उगाने के लिए सबसे उत्तम रहेगी।",
            "hinglish": "Mausam ke hisab se ye fasal sabse best rahegi."
        }
        return prediction[0], weather_msgs.get(lang, weather_msgs["en"])
    except Exception as e:
        return "Error", str(e)


def is_valid_leaf_image(pil_img):
    """
    Validates whether an uploaded image contains genuine plant leaf foliage 
    using Excess Green Index (ExG) and vegetation color spectrometry.
    Prevents random objects (cars, faces, buildings, blank screens) from being misclassified.
    """
    try:
        rgb = pil_img.convert('RGB')
        arr = np.array(rgb, dtype=np.float32)
        r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
        
        # Excess Green Index: 2*G - R - B (signature spectral index for plant chlorophyll)
        exg = 2.0 * g - r - b
        
        # 1. Healthy green foliage
        green_leaf = (exg > 8) & (g > 28) & (g > b * 1.05)
        
        # 2. Diseased / chlorotic / necrotic leaf lesions (yellowish, rust, blight spots on leaf)
        lesion_leaf = (r > b * 1.1) & (g > b * 1.05) & (r + g > 2.2 * b) & (r - g < 45) & (exg > -40) & (g > 35)
        
        plant_mask = green_leaf | lesion_leaf
        total_pixels = arr.shape[0] * arr.shape[1]
        plant_ratio = np.sum(plant_mask) / total_pixels
        green_ratio = np.sum(green_leaf) / total_pixels
        
        # Must have significant plant tissue and detectable chlorophyll/green foliage
        return (plant_ratio >= 0.12) and (green_ratio >= 0.02 or plant_ratio >= 0.22)
    except Exception:
        return False


def predict_disease(image_file, lang='en'):
    if models['disease_interpreter'] is None:
        err_msg = {
            "en": "Disease detection model is not loaded.",
            "hi": "रोग पहचान मॉडल लोड नहीं हुआ।",
            "hinglish": "Disease model load nahi hua."
        }
        return "Model Error", err_msg.get(lang, err_msg["en"])
        
    try:
        # Image Load
        img = Image.open(image_file)
        
        # 1. Step 1: Image Validation - Is this actually a crop/leaf?
        if not is_valid_leaf_image(img):
            no_leaf_msgs = {
                "en": "No plant leaf detected in the image. Please upload a clear photo of a crop leaf.",
                "hi": "चित्र में पौधे की पत्ती नहीं मिली। कृपया फसल की पत्ती की स्पष्ट फोटो अपलोड करें।",
                "hinglish": "Photo me patti (leaf) detect nahi hui. Kripya kisi fasal ke patte ki saaf photo upload karein."
            }
            return "No Leaf Detected", no_leaf_msgs.get(lang, no_leaf_msgs["en"])

        input_details = models['disease_input_details'][0]
        req_height, req_width = input_details['shape'][1], input_details['shape'][2]

        # Step 2: Image Preprocessing for Model
        img_resized = img.convert('RGB').resize((req_width, req_height))
        img_array = np.array(img_resized, dtype=np.float32)
        
        # OpenCV BGR fix
        img_array = img_array[..., ::-1]
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Step 3: TFLite Inference
        interpreter = models['disease_interpreter']
        input_idx = input_details['index']
        output_idx = models['disease_output_details'][0]['index']
        
        interpreter.set_tensor(input_idx, img_array)
        interpreter.invoke()
        
        # Step 4: Output Analysis & Confidence Threshold
        preds = interpreter.get_tensor(output_idx)
        class_idx = np.argmax(preds[0])
        confidence = float(preds[0][class_idx])
        
        classes = models['disease_classes']
        result = classes[class_idx]
        
        # If model is uncertain (< 50% confidence), do not guess blindly
        if confidence < 0.50:
            uncertain_msgs = {
                "en": f"Image quality is too low or leaf symptom is unclear (Confidence: {confidence*100:.1f}%). Please upload a closer, well-lit leaf image.",
                "hi": f"छवि स्पष्ट नहीं है या लक्षण साफ नहीं दिख रहे (आत्मविश्वास: {confidence*100:.1f}%)। कृपया पत्ती की साफ और रोशनी वाली फोटो अपलोड करें।",
                "hinglish": f"Photo clear nahi hai ya disease saaf nahi dikh rahi ({confidence*100:.1f}% confidence). Kripya paas se saaf photo upload karein."
            }
            return "Uncertain Diagnosis", uncertain_msgs.get(lang, uncertain_msgs["en"])

        all_tips = {
            "en": {
                "Apple Scab": "Spray fungicide and remove infected foliage.",
                "Corn Common Rust": "Ensure proper airflow and drainage between crop rows.",
                "Potato Early Blight": "Prune affected leaves immediately and avoid excess moisture.",
                "Healthy Crop": "Crop is healthy and thriving. Maintain regular care."
            },
            "hi": {
                "Apple Scab": "फफूंदनाशक (Fungicide) का छिड़काव करें और खराब पत्तियों को हटा दें।",
                "Corn Common Rust": "फसल में हवा लगने की जगह बनाएं और जल निकासी ठीक रखें।",
                "Potato Early Blight": "संक्रमित पत्तियों को तुरंत काटें और ऊपर से पानी देने से बचें।",
                "Healthy Crop": "फसल बिल्कुल स्वस्थ है। ऐसे ही नियमित देखभाल जारी रखें।"
            },
            "hinglish": {
                "Apple Scab": "Fungicide ka spray karein aur kharab patton ko hata dein.",
                "Corn Common Rust": "Fasal me hawa lagne ki jagah banayein aur water drainage theek rakhein.",
                "Potato Early Blight": "Kharab patton ko turant kaat dein aur upar se pani dalne se bachein.",
                "Healthy Crop": "Sab kuch theek hai, aise hi regular dhyan rakhein."
            }
        }
        
        tips = all_tips.get(lang, all_tips["en"])
        tip_text = tips.get(result, "Maintain proper crop care.")
        msg = f"{tip_text} (Confidence: {confidence*100:.1f}%)"
            
        return result, msg
        
    except Exception as e:
        print(f"Image scan error: {e}")
        err_msg = {
            "en": "Scanning failed. Please check image.",
            "hi": "स्कैनिंग विफल रही। कृपया छवि जांचें।",
            "hinglish": "Scanning fail ho gayi. Photo check karein."
        }
        return "Error", err_msg.get(lang, err_msg["en"])

