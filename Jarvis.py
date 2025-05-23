import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import requests
import os
from dotenv import load_dotenv
import difflib
import time
import json

# Load environment variables
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

# Initialize text-to-speech
try:
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # Try to set a male voice, fall back to default if not available
    for voice in voices:
        if "male" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    # Set properties for better voice
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
except Exception as e:
    print(f"Error initializing text-to-speech: {e}")
    engine = None

def speak(text):
    """Speak the given text with error handling and retry logic"""
    if not text:
        return
        
    if engine:
        try:
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"Error in text-to-speech: {e}")
            # Fallback to print if speech fails
            print(f"JARVIS: {text}")
    else:
        print(f"JARVIS: {text}")

def listen(retry_count=3):
    """Listen for user input with retry logic and better error handling"""
    recognizer = sr.Recognizer()
    
    for attempt in range(retry_count):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                # Adjust for ambient noise
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                # Set timeout and phrase time limit
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                
                try:
                    command = recognizer.recognize_google(audio).lower()
                    print(f"You said: {command}")
                    return command
                except sr.UnknownValueError:
                    if attempt < retry_count - 1:
                        speak("I didn't catch that. Could you please repeat?")
                        continue
                    else:
                        speak("Sorry, I couldn't understand. Please try again.")
                        return ""
                except sr.RequestError:
                    speak("Network error. Please check your internet connection.")
                    return ""
                    
        except Exception as e:
            print(f"Error accessing microphone: {e}")
            if attempt < retry_count - 1:
                speak("Having trouble with the microphone. Trying again...")
                time.sleep(1)
                continue
            else:
                speak("I'm having trouble accessing the microphone. Please check your microphone settings.")
                return ""
    
    return ""

def get_ai_response(prompt):
    """Get AI response with better error handling and fallback"""
    if not HF_API_KEY:
        return "AI API key not configured. Please add your Hugging Face API key to the .env file."
    
    try:
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 250,
                "temperature": 0.7,
                "top_p": 0.95,
                "do_sample": True
            }
        }
        
        # Try primary model first
        try:
            response = requests.post(
                "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
                headers=headers,
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json()[0]['generated_text']
        except Exception as e:
            print(f"Primary model failed: {e}")
        
        # Fallback to simpler model
        response = requests.post(
            "https://api-inference.huggingface.co/models/google/flan-t5-base",
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()[0]['generated_text']
        else:
            return f"Error getting AI response: {response.status_code}"
            
    except Exception as e:
        return f"Error with AI service: {str(e)}"

# List of supported cities with their coordinates
SUPPORTED_CITIES = {
    "delhi": {"lat": 28.6139, "lon": 77.2090},
    "new delhi": {"lat": 28.6139, "lon": 77.2090},
    "lucknow": {"lat": 26.8467, "lon": 80.9462},
    "kanpur": {"lat": 26.4499, "lon": 80.3319},
    "agra": {"lat": 27.1767, "lon": 78.0081},
    "varanasi": {"lat": 25.3176, "lon": 82.9739},
    "prayagraj": {"lat": 25.4358, "lon": 81.8463},
    "ghaziabad": {"lat": 28.6692, "lon": 77.4538},
    "meerut": {"lat": 28.9845, "lon": 77.7064},
    "gorakhpur": {"lat": 26.7606, "lon": 83.3732},
    "aligarh": {"lat": 27.8974, "lon": 78.0880},
    "bareilly": {"lat": 28.3670, "lon": 79.4304},
    "moradabad": {"lat": 28.8388, "lon": 78.7768},
    "saharanpur": {"lat": 29.9640, "lon": 77.5461},
    "noida": {"lat": 28.5355, "lon": 77.3910},
    "greater noida": {"lat": 28.4744, "lon": 77.5040},
    "ayodhya": {"lat": 26.7924, "lon": 82.1948},
    "mathura": {"lat": 27.4924, "lon": 77.6737},
    "jhansi": {"lat": 25.4484, "lon": 78.5685},
    "shahjahanpur": {"lat": 27.8830, "lon": 79.9120},
    "firozabad": {"lat": 27.1591, "lon": 78.3958},
    "rampur": {"lat": 28.8103, "lon": 79.0268},
    "muzaffarnagar": {"lat": 29.4709, "lon": 77.7033},
    "shamli": {"lat": 29.4497, "lon": 77.3096},
    "hapur": {"lat": 28.7297, "lon": 77.7807},
    "amroha": {"lat": 28.9030, "lon": 78.4698},
    "etawah": {"lat": 26.7769, "lon": 79.0239},
    "mainpuri": {"lat": 27.2280, "lon": 79.0218},
    "sambhal": {"lat": 28.5841, "lon": 78.5699},
    "azamgarh": {"lat": 26.0674, "lon": 83.1836},
    "ballia": {"lat": 25.7615, "lon": 84.1471},
    "deoria": {"lat": 26.5047, "lon": 83.7873},
    "basti": {"lat": 27.1167, "lon": 82.7167},
    "sultanpur": {"lat": 26.2649, "lon": 82.0727},
    "lakhimpur": {"lat": 27.9483, "lon": 80.7795},
    "sitapur": {"lat": 27.5619, "lon": 80.6826},
    "hardoi": {"lat": 27.0943, "lon": 80.1311},
    "unnao": {"lat": 26.5471, "lon": 80.4878},
    "raebareli": {"lat": 26.2309, "lon": 81.2332},
    "fatehpur": {"lat": 25.9304, "lon": 80.8139},
    "pratapgarh": {"lat": 25.8969, "lon": 81.9436},
    "jaunpur": {"lat": 25.7539, "lon": 82.6868},
    "mirzapur": {"lat": 25.1449, "lon": 82.5653},
    "sonbhadra": {"lat": 24.4021, "lon": 83.0539},
    "chitrakoot": {"lat": 25.1605, "lon": 80.8906},
    "banda": {"lat": 25.4776, "lon": 80.3349},
    "hamirpur": {"lat": 25.9500, "lon": 80.1500},
    "mahoba": {"lat": 25.2833, "lon": 79.8667},
    "lalitpur": {"lat": 24.6877, "lon": 78.4127},
    "jalaun": {"lat": 26.1480, "lon": 79.3365},
    "orai": {"lat": 26.0114, "lon": 79.4533},
    "etah": {"lat": 27.6333, "lon": 78.6667},
    "kasganj": {"lat": 27.8167, "lon": 78.6500},
    "farrukhabad": {"lat": 27.3917, "lon": 79.5800}
}

def fuzzy_city_match(city):
    """Improved city matching with better fuzzy logic"""
    city = city.lower().strip()
    
    # Direct match
    if city in SUPPORTED_CITIES:
        return city
        
    # Try to match with common variations
    variations = {
        "new delhi": ["delhi", "noida"],
        "delhi": ["new delhi", "noida"],
        "noida": ["greater noida"],
        "greater noida": ["noida"],
        "prayagraj": ["allahabad"],
        "allahabad": ["prayagraj"]
    }
    
    for main_city, var_list in variations.items():
        if city in var_list or main_city in city:
            return main_city
    
    # Fuzzy match as last resort
    matches = difflib.get_close_matches(city, SUPPORTED_CITIES.keys(), n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return None

def get_weather(city="delhi"):
    """Get weather information with improved error handling and retry logic"""
    try:
        matched_city = fuzzy_city_match(city)
        if not matched_city:
            return f"Sorry, I couldn't find weather data for '{city}'. Please try a different city."
        
        coords = SUPPORTED_CITIES[matched_city]
        url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['lat']}&longitude={coords['lon']}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code&timezone=auto"
        
        print(f"DEBUG: Fetching weather for {matched_city}")
        
        # Try up to 3 times with increasing timeouts
        for attempt in range(3):
            try:
                response = requests.get(url, timeout=5 * (attempt + 1))
                print(f"DEBUG: Response status code: {response.status_code}")
                
                if response.status_code == 200:
                    data = response.json()
                    current = data['current']
                    
                    # Convert weather code to description
                    weather_codes = {
                        0: "clear sky",
                        1: "mainly clear",
                        2: "partly cloudy",
                        3: "overcast",
                        45: "foggy",
                        48: "depositing rime fog",
                        51: "light drizzle",
                        53: "moderate drizzle",
                        55: "dense drizzle",
                        61: "slight rain",
                        63: "moderate rain",
                        65: "heavy rain",
                        71: "slight snow",
                        73: "moderate snow",
                        75: "heavy snow",
                        77: "snow grains",
                        80: "slight rain showers",
                        81: "moderate rain showers",
                        82: "violent rain showers",
                        85: "slight snow showers",
                        86: "heavy snow showers",
                        95: "thunderstorm",
                        96: "thunderstorm with slight hail",
                        99: "thunderstorm with heavy hail"
                    }
                    
                    weather_desc = weather_codes.get(current['weather_code'], "unknown conditions")
                    temp = current['temperature_2m']
                    humidity = current['relative_humidity_2m']
                    wind_speed = current['wind_speed_10m']
                    
                    # Format the response based on conditions
                    if temp > 30:
                        temp_desc = "hot"
                    elif temp > 25:
                        temp_desc = "warm"
                    elif temp > 20:
                        temp_desc = "pleasant"
                    elif temp > 15:
                        temp_desc = "cool"
                    else:
                        temp_desc = "cold"
                    
                    return (f"The weather in {matched_city} is {temp}°C, which is {temp_desc}. "
                            f"Conditions are {weather_desc}. "
                            f"Humidity is {humidity}% and wind speed is {wind_speed} km/h.")
                            
                elif response.status_code == 429:  # Rate limit
                    if attempt < 2:
                        time.sleep(2 ** attempt)  # Exponential backoff
                        continue
                        
            except requests.exceptions.Timeout:
                if attempt < 2:
                    continue
                return "Sorry, the weather service is taking too long to respond. Please try again."
            except requests.exceptions.RequestException as e:
                if attempt < 2:
                    continue
                return f"Error connecting to weather service: {str(e)}"
                
        return "Sorry, I couldn't fetch the weather information. Please try again later."
        
    except Exception as e:
        print(f"DEBUG: Exception occurred: {str(e)}")
        return f"An error occurred: {str(e)}"

def get_time():
    """Get current time with a natural language response"""
    current_time = datetime.datetime.now()
    hour = current_time.hour
    
    # Determine time of day
    if 5 <= hour < 12:
        time_of_day = "morning"
    elif 12 <= hour < 17:
        time_of_day = "afternoon"
    elif 17 <= hour < 21:
        time_of_day = "evening"
    else:
        time_of_day = "night"
        
    return f"Good {time_of_day}! The current time is {current_time.strftime('%I:%M %p')}"

def process_command(command):
    """Process user commands with improved handling"""
    if not command:
        return
        
    try:
        command = command.lower().strip()
        
        # Weather commands
        if "weather" in command:
            if "in" in command:
                city = command.split("in", 1)[1].strip()
            else:
                speak("Which city's weather would you like to know?")
                city = listen()
                if not city:
                    return
            weather = get_weather(city)
            speak(weather)
            
        # Time commands
        elif any(word in command for word in ["time", "clock"]):
            time_info = get_time()
            speak(time_info)
            
        # Greeting commands
        elif any(word in command for word in ["hello", "hi", "hey"]):
            speak("Hello! How can I help you today?")
            
        # Exit commands
        elif any(word in command for word in ["bye", "goodbye", "exit", "quit"]):
            speak("Goodbye! Have a great day!")
            return "exit"
            
        # Help command
        elif "help" in command:
            help_text = (
                "I can help you with:\n"
                "1. Weather information - just ask 'what's the weather in [city]'\n"
                "2. Current time - ask 'what time is it'\n"
                "3. General questions - just ask anything else\n"
                "4. To exit, just say 'goodbye' or 'exit'"
            )
            speak(help_text)
            
        # Default to AI response for other queries
        else:
            response = get_ai_response(command)
            speak(response)
            
    except Exception as e:
        print(f"Error processing command: {e}")
        speak("I encountered an error. Please try again.")

def main():
    """Main function with improved error handling and graceful exit"""
    speak("Hello! I'm your AI assistant. How can I help you today?")
    
    while True:
        try:
            command = listen()
            if command:
                result = process_command(command)
                if result == "exit":
                    break
                    
        except KeyboardInterrupt:
            speak("Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("I encountered an error. Please try again.")
            time.sleep(1)  # Brief pause before continuing

if __name__ == "__main__":
    main()
