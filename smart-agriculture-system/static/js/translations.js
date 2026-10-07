/**
 * Smart Agriculture System - Multilingual Translations
 * Languages Supported: English (en), Hindi (hi), Hinglish (hinglish)
 */

const translations = {
    en: {
        // Brand & Navigation
        "nav_brand": "Agri-Smart",
        "nav_home": "Home",
        "nav_yield": "Crop Yield",
        "nav_soil": "Soil Quality",
        "nav_fertilizer": "Fertilizer",
        "nav_disease": "Disease",
        "nav_weather": "Weather",
        "lang_name": "English",

        // Hero Section
        "hero_title": "Smart Agriculture Analytic System",
        "hero_subtitle": "Empowering Farmers with Machine Learning & AI",

        // Home Cards
        "card_yield_title": "Crop Yield Prediction",
        "card_yield_desc": "Predict your harvest yield based on soil, weather, and area.",
        "card_yield_btn": "Predict Yield",

        "card_soil_title": "Soil Analysis",
        "card_soil_desc": "Classify soil quality (Poor, Medium, Fertile) using NPK values.",
        "card_soil_btn": "Check Soil",

        "card_fert_title": "Fertilizer Recommender",
        "card_fert_desc": "Get the best fertilizer suggestions based on nutrient deficiencies.",
        "card_fert_btn": "Get Advice",

        "card_disease_title": "Disease Detection",
        "card_disease_desc": "Upload a leaf image to detect diseases using Deep Learning (CNN).",
        "card_disease_btn": "Scan Plant",

        "card_weather_title": "Best Crop Suggestion",
        "card_weather_desc": "Find the best crop to grow for your current weather conditions.",
        "card_weather_btn": "Suggest Crop",

        // Common Form Labels
        "lbl_nitrogen": "Nitrogen (N)",
        "lbl_phosphorus": "Phosphorus (P)",
        "lbl_potassium": "Potassium (K)",
        "lbl_ph": "pH Level (0-14)",
        "lbl_crop_type": "Crop Type",
        "lbl_crop_name": "Crop Name",
        "lbl_area": "Area (Hectares)",
        "lbl_rainfall": "Average Rainfall (mm)",
        "lbl_temperature": "Temperature (°C)",
        "lbl_humidity": "Humidity (%)",
        "lbl_date": "Date (Reference)",
        "lbl_choose_image": "Choose Leaf Image",

        // Placeholders
        "ph_n": "Example: 50",
        "ph_p": "Example: 50",
        "ph_k": "Example: 50",
        "ph_ph": "Example: 6.5",
        "ph_area": "Example: 5.5",
        "ph_rain": "Example: 1200",
        "ph_temp": "Example: 28",
        "ph_humidity": "Example: 80",

        // Page Titles & Headers
        "title_yield": "Crop Yield Prediction",
        "title_soil": "Soil Quality Analysis",
        "title_fertilizer": "Fertilizer Recommendation",
        "title_disease": "Leaf Disease Detection",
        "title_weather": "Weather-based Crop Suggestion",

        // Alerts & Instructions
        "disease_upload_notice": "Upload a clear image of the crop leaf to detect diseases.",

        // Buttons
        "btn_predict_yield": "Predict Yield",
        "btn_analyze_soil": "Analyze Soil",
        "btn_get_fert": "Get Recommendation",
        "btn_scan_leaf": "Scan Leaf",
        "btn_suggest_crop": "Suggest Best Crop",

        // Result Headings
        "res_yield_head": "Predicted Yield",
        "res_soil_head": "Soil Classification",
        "res_fert_head": "Recommended Fertilizer",
        "res_disease_head": "Disease Detected",
        "res_weather_head": "Best Crop to Grow",

        // Footer
        "footer_text": "© Smart Agriculture System | Made for Farmers ❤️",

        // Crops in dropdowns
        "crop_barley": "Barley",
        "crop_cotton": "Cotton",
        "crop_groundnuts": "Ground Nuts",
        "crop_maize": "Maize",
        "crop_millets": "Millets",
        "crop_oilseeds": "Oil seeds",
        "crop_paddy": "Paddy / Rice",
        "crop_pulses": "Pulses",
        "crop_sugarcane": "Sugarcane",
        "crop_tobacco": "Tobacco",
        "crop_wheat": "Wheat",
        "crop_rice": "Rice",
        "crop_soybean": "Soybean"
    },

    hi: {
        // Brand & Navigation
        "nav_brand": "एग्री-स्मार्ट",
        "nav_home": "होम",
        "nav_yield": "फसल उत्पादन",
        "nav_soil": "मिट्टी की गुणवत्ता",
        "nav_fertilizer": "उर्वरक (खाद)",
        "nav_disease": "रोग पहचान",
        "nav_weather": "मौसम सलाह",
        "lang_name": "हिंदी",

        // Hero Section
        "hero_title": "स्मार्ट कृषि विश्लेषणात्मक प्रणाली",
        "hero_subtitle": "मशीन लर्निंग और AI के साथ किसानों का सशक्तिकरण",

        // Home Cards
        "card_yield_title": "फसल उत्पादन अनुमान",
        "card_yield_desc": "मिट्टी, मौसम और क्षेत्रफल के आधार पर फसल पैदावार का अनुमान लगाएं।",
        "card_yield_btn": "पैदावार जानें",

        "card_soil_title": "मिट्टी परीक्षण व विश्लेषण",
        "card_soil_desc": "NPK और pH मानों के आधार पर मिट्टी (उपजाऊ, मध्यम, कमजोर) की जांच करें।",
        "card_soil_btn": "मिट्टी जांचें",

        "card_fert_title": "उर्वरक (खाद) सिफारिश",
        "card_fert_desc": "पोषक तत्वों की कमी के अनुसार अपनी फसल के लिए सर्वोत्तम खाद की सलाह पाएं।",
        "card_fert_btn": "खाद सलाह लें",

        "card_disease_title": "पत्ती रोग पहचान",
        "card_disease_desc": "पत्ती की तस्वीर अपलोड करें और AI डीप लर्निंग से रोग व उपचार तुरंत जानें।",
        "card_disease_btn": "पौधा स्कैन करें",

        "card_weather_title": "मौसम अनुसार फसल सलाह",
        "card_weather_desc": "अपने क्षेत्र के तापमान और वर्षा के अनुसार उगाने के लिए सबसे सही फसल जानें।",
        "card_weather_btn": "फसल सुझाव पाएं",

        // Common Form Labels
        "lbl_nitrogen": "नाइट्रोजन (N)",
        "lbl_phosphorus": "फास्फोरस (P)",
        "lbl_potassium": "पोटेशियम (K)",
        "lbl_ph": "पीएच स्तर (0-14)",
        "lbl_crop_type": "फसल का प्रकार",
        "lbl_crop_name": "फसल का नाम",
        "lbl_area": "क्षेत्रफल (हेक्टेयर में)",
        "lbl_rainfall": "औसत वर्षा (मिमी में)",
        "lbl_temperature": "तापमान (°C)",
        "lbl_humidity": "नमी / आर्द्रता (%)",
        "lbl_date": "तारीख (संदर्भ हेतु)",
        "lbl_choose_image": "पत्ती की तस्वीर चुनें",

        // Placeholders
        "ph_n": "उदाहरण: 50",
        "ph_p": "उदाहरण: 50",
        "ph_k": "उदाहरण: 50",
        "ph_ph": "उदाहरण: 6.5",
        "ph_area": "उदाहरण: 5.5",
        "ph_rain": "उदाहरण: 1200",
        "ph_temp": "उदाहरण: 28",
        "ph_humidity": "उदाहरण: 80",

        // Page Titles & Headers
        "title_yield": "फसल उत्पादन पूर्वानुमान",
        "title_soil": "मिट्टी गुणवत्ता विश्लेषण",
        "title_fertilizer": "उर्वरक (खाद) सिफारिश",
        "title_disease": "पत्ती रोग पहचान व निदान",
        "title_weather": "मौसम अनुसार फसल सुझाव",

        // Alerts & Instructions
        "disease_upload_notice": "रोग पहचानने के लिए पौधे की पत्ती की साफ तस्वीर अपलोड करें।",

        // Buttons
        "btn_predict_yield": "पैदावार का अनुमान लगाएं",
        "btn_analyze_soil": "मिट्टी का विश्लेषण करें",
        "btn_get_fert": "उर्वरक सलाह प्राप्त करें",
        "btn_scan_leaf": "पत्ती स्कैन करें",
        "btn_suggest_crop": "सर्वोत्तम फसल जानें",

        // Result Headings
        "res_yield_head": "अनुमानित कुल पैदावार",
        "res_soil_head": "मिट्टी की श्रेणी व स्थिति",
        "res_fert_head": "सर्वोत्तम अनुशंसित उर्वरक",
        "res_disease_head": "पाया गया रोग",
        "res_weather_head": "उगाने के लिए सर्वश्रेष्ठ फसल",

        // Footer
        "footer_text": "© स्मार्ट कृषि प्रणाली | किसानों के लिए समर्पित ❤️",

        // Crops in dropdowns
        "crop_barley": "जौ (Barley)",
        "crop_cotton": "कपास (Cotton)",
        "crop_groundnuts": "मूंगफली (Ground Nuts)",
        "crop_maize": "मक्का (Maize)",
        "crop_millets": "बाजरा / मोटा अनाज (Millets)",
        "crop_oilseeds": "तिलहन (Oil seeds)",
        "crop_paddy": "धान / चावल (Paddy / Rice)",
        "crop_pulses": "दालें (Pulses)",
        "crop_sugarcane": "गन्ना (Sugarcane)",
        "crop_tobacco": "तंबाकू (Tobacco)",
        "crop_wheat": "गेहूं (Wheat)",
        "crop_rice": "चावल (Rice)",
        "crop_soybean": "सोयाबीन (Soybean)"
    },

    hinglish: {
        // Brand & Navigation
        "nav_brand": "Agri-Smart",
        "nav_home": "Home",
        "nav_yield": "Crop Yield",
        "nav_soil": "Soil Quality",
        "nav_fertilizer": "Fertilizer (Khad)",
        "nav_disease": "Rog Pehchan",
        "nav_weather": "Mausam Salah",
        "lang_name": "Hinglish",

        // Hero Section
        "hero_title": "Smart Agriculture Analytic System",
        "hero_subtitle": "Machine Learning aur AI se Kisan Bhaiyo ki Madad",

        // Home Cards
        "card_yield_title": "Crop Yield Prediction",
        "card_yield_desc": "Mitti, mausam aur zameen ke area ke hisaab se fasal ki paidawar jaanein.",
        "card_yield_btn": "Yield Predict Karein",

        "card_soil_title": "Soil Quality Analysis",
        "card_soil_desc": "NPK aur pH value se mitti ki quality (Fertile, Medium, Poor) check karein.",
        "card_soil_btn": "Mitti Check Karein",

        "card_fert_title": "Fertilizer Recommender",
        "card_fert_desc": "Fasal aur mitti me kami ke mutabiq sabse best khad ki advice lein.",
        "card_fert_btn": "Khad Ki Salah Lein",

        "card_disease_title": "Leaf Disease Detection",
        "card_disease_desc": "Patte ki photo upload karein aur AI se bimari aur ilaj turant jaanein.",
        "card_disease_btn": "Plant Scan Karein",

        "card_weather_title": "Weather Crop Suggestion",
        "card_weather_desc": "Apne ilaqe ke mausam aur barish ke hisaab se best fasal jaanein.",
        "card_weather_btn": "Fasal Suggestion Lein",

        // Common Form Labels
        "lbl_nitrogen": "Nitrogen (N)",
        "lbl_phosphorus": "Phosphorus (P)",
        "lbl_potassium": "Potassium (K)",
        "lbl_ph": "pH Level (0-14)",
        "lbl_crop_type": "Fasal Ka Type",
        "lbl_crop_name": "Fasal Ka Naam",
        "lbl_area": "Zameen Ka Area (Hectares)",
        "lbl_rainfall": "Average Barish (Rainfall mm)",
        "lbl_temperature": "Tapman (Temperature °C)",
        "lbl_humidity": "Nami (Humidity %)",
        "lbl_date": "Date (Tarikh)",
        "lbl_choose_image": "Patte (Leaf) Ki Photo Choose Karein",

        // Placeholders
        "ph_n": "Example: 50",
        "ph_p": "Example: 50",
        "ph_k": "Example: 50",
        "ph_ph": "Example: 6.5",
        "ph_area": "Example: 5.5",
        "ph_rain": "Example: 1200",
        "ph_temp": "Example: 28",
        "ph_humidity": "Example: 80",

        // Page Titles & Headers
        "title_yield": "Crop Yield Prediction (Paidawar)",
        "title_soil": "Soil Quality Analysis (Mitti Ki Jaanch)",
        "title_fertilizer": "Fertilizer Recommendation (Khad Salah)",
        "title_disease": "Leaf Disease Detection (Patte Ki Bimari)",
        "title_weather": "Weather-based Crop Suggestion",

        // Alerts & Instructions
        "disease_upload_notice": "Bimari pehchanne ke liye paudhe ke patte ki saaf photo upload karein.",

        // Buttons
        "btn_predict_yield": "Yield Predict Karein",
        "btn_analyze_soil": "Soil Analyze Karein",
        "btn_get_fert": "Khad Suggestion Lein",
        "btn_scan_leaf": "Patta Scan Karein",
        "btn_suggest_crop": "Best Fasal Jaanein",

        // Result Headings
        "res_yield_head": "Estimated Yield (Paidawar)",
        "res_soil_head": "Soil Condition (Mitti Ki Sthiti)",
        "res_fert_head": "Best Recommended Khad",
        "res_disease_head": "Detected Disease (Bimari)",
        "res_weather_head": "Sabse Best Fasal",

        // Footer
        "footer_text": "© Smart Agriculture System | Kisan Bhaiyo Ke Liye ❤️",

        // Crops in dropdowns
        "crop_barley": "Barley (Jau)",
        "crop_cotton": "Cotton (Kapas)",
        "crop_groundnuts": "Ground Nuts (Mungfali)",
        "crop_maize": "Maize (Makka)",
        "crop_millets": "Millets (Bajra)",
        "crop_oilseeds": "Oil seeds (Tilhan)",
        "crop_paddy": "Paddy / Rice (Chawal)",
        "crop_pulses": "Pulses (Daalein)",
        "crop_sugarcane": "Sugarcane (Ganna)",
        "crop_tobacco": "Tobacco (Tambaku)",
        "crop_wheat": "Wheat (Gehun)",
        "crop_rice": "Rice (Chawal)",
        "crop_soybean": "Soybean"
    }
};

/**
 * Get current language (stored in localStorage or cookie, defaults to 'en')
 */
function getCurrentLanguage() {
    const saved = localStorage.getItem('app_lang');
    if (saved && (saved === 'en' || saved === 'hi' || saved === 'hinglish')) {
        return saved;
    }
    // Check cookie
    const match = document.cookie.match(/(?:^|; )lang=([^;]*)/);
    if (match && (match[1] === 'en' || match[1] === 'hi' || match[1] === 'hinglish')) {
        return match[1];
    }
    return 'en';
}

/**
 * Apply language to DOM
 */
function setLanguage(lang) {
    if (!translations[lang]) lang = 'en';

    // Save preferences
    localStorage.setItem('app_lang', lang);
    document.cookie = `lang=${lang}; path=/; max-age=31536000; SameSite=Lax`;

    const dict = translations[lang];

    // Update all text elements with data-i18n
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (dict[key]) {
            el.textContent = dict[key];
        }
    });

    // Update all placeholder elements with data-i18n-ph
    document.querySelectorAll('[data-i18n-ph]').forEach(el => {
        const key = el.getAttribute('data-i18n-ph');
        if (dict[key]) {
            el.setAttribute('placeholder', dict[key]);
        }
    });

    // Update hidden lang inputs in all forms
    document.querySelectorAll('input[name="lang"], .lang-input').forEach(input => {
        input.value = lang;
    });

    // Update language selector dropdown label
    const labelEl = document.getElementById('current-lang-label');
    const flagEl = document.getElementById('current-lang-flag');
    if (labelEl) {
        if (lang === 'hi') {
            labelEl.textContent = 'हिंदी';
            if (flagEl) flagEl.textContent = '🇮🇳';
        } else if (lang === 'hinglish') {
            labelEl.textContent = 'Hinglish';
            if (flagEl) flagEl.textContent = '🌾';
        } else {
            labelEl.textContent = 'English';
            if (flagEl) flagEl.textContent = '🇬🇧';
        }
    }

    // Set html lang attribute
    document.documentElement.lang = (lang === 'hi') ? 'hi' : 'en';

    // Dispatch event
    document.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
}

/**
 * Helper called when user clicks on language in dropdown
 */
function changeLanguage(lang) {
    setLanguage(lang);
}

// Auto-run on page load
document.addEventListener('DOMContentLoaded', () => {
    const initialLang = getCurrentLanguage();
    setLanguage(initialLang);

    // Ensure dynamically submitted forms have lang input
    document.querySelectorAll('form').forEach(form => {
        if (!form.querySelector('input[name="lang"]')) {
            const hidden = document.createElement('input');
            hidden.type = 'hidden';
            hidden.name = 'lang';
            hidden.className = 'lang-input';
            hidden.value = getCurrentLanguage();
            form.appendChild(hidden);
        }
    });
});
