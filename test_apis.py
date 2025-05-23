import os
from dotenv import load_dotenv
import requests
from openai import OpenAI

# Load environment variables
load_dotenv()
WEATHER_KEY = os.getenv("WEATHER_API_KEY")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def test_weather_api():
    print("\nTesting Weather API...")
    if not WEATHER_KEY:
        print("❌ Weather API key not found in .env file")
        return
    
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q=London&appid={WEATHER_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Weather API is working!")
            print(f"Temperature in London: {data['main']['temp']}°C")
        else:
            print(f"❌ Weather API error: {response.status_code}")
    except Exception as e:
        print(f"❌ Weather API error: {str(e)}")

def test_openai_api():
    print("\nTesting OpenAI API...")
    if not OPENAI_KEY:
        print("❌ OpenAI API key not found in .env file")
        return
    
    try:
        client = OpenAI(api_key=OPENAI_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Say hello!"}]
        )
        print("✅ OpenAI API is working!")
        print(f"Response: {response.choices[0].message.content}")
    except Exception as e:
        print(f"❌ OpenAI API error: {str(e)}")

if __name__ == "__main__":
    print("Testing APIs...")
    test_weather_api()
    test_openai_api() 