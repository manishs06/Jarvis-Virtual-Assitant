import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

def test_gpt4all():
    """Test GPT4All local AI setup"""
    print("\nTesting Local AI (GPT4All)...")
    try:
        from gpt4all import GPT4All
        print("✅ gpt4all library is installed")
        
        # Check if model exists without downloading
        model_name = "orca-mini-3b-gguf2-q4_0.gguf"
        cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "gpt4all")
        model_path = os.path.join(cache_dir, model_name)
        
        if os.path.exists(model_path):
            print(f"✅ Model '{model_name}' found in cache!")
        else:
            print(f"⚠️  Model '{model_name}' not found locally.")
            print("   It will download automatically on first run (approx 2GB).")
            
    except ImportError:
        print("❌ gpt4all library is not installed")
        print("   Run: pip install gpt4all")
    except Exception as e:
        print(f"❌ GPT4All error: {e}")

def test_weather_api():
    """Test the Open-Meteo weather API (no API key required)"""
    print("\nTesting Weather API (Open-Meteo)...")
    try:
        # Test with Delhi coordinates
        url = "https://api.open-meteo.com/v1/forecast?latitude=28.6139&longitude=77.2090&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=auto"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            temp = data['current']['temperature_2m']
            print(f"✅ Weather API is working!")
            print(f"Temperature in Delhi: {temp}°C")
        else:
            print(f"❌ Weather API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Weather API error: {str(e)}")

def test_huggingface_api():
    """Test the Hugging Face API"""
    print("\nTesting Hugging Face API...")
    
    if not HF_API_KEY or HF_API_KEY == "your_huggingface_api_key_here":
        print("⚠️  Hugging Face API key not configured (Skipping)")
        print("   Using GPT4All as fallback.")
        return
    
    try:
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}
        payload = {"inputs": "Hi"}
        response = requests.post(
            "https://api-inference.huggingface.co/models/google/flan-t5-base",
            headers=headers,
            json=payload,
            timeout=5
        )
        if response.status_code == 200:
            print("✅ Hugging Face API is working!")
        else:
            print(f"❌ Hugging Face API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Hugging Face API error: {str(e)}")

def test_voice():
    """Test Voice capabilities"""
    print("\nTesting Voice Setup...")
    try:
        import speech_recognition as sr
        print(f"✅ SpeechRecognition installed (version {sr.__version__})")
        import pyttsx3
        print(f"✅ pyttsx3 installed")
    except ImportError as e:
        print(f"❌ Voice libraries missing: {e}")

if __name__ == "__main__":
    print("=" * 60)
    print("JARVIS - Setup & Alternatives Test")
    print("=" * 60)
    
    test_weather_api()
    test_huggingface_api()
    test_gpt4all()
    test_voice()
    
    print("\n" + "=" * 60)