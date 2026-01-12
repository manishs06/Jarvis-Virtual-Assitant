# 🤖 Jarvis - AI Voice Assistant

A Python-based voice assistant that provides weather information, time, and answers questions using natural language processing powered by Hugging Face AI models.

## ✨ Features

- 🎤 **Voice Recognition** - Speak naturally to interact with Jarvis
- 🗣️ **Text-to-Speech** - Jarvis responds with natural voice
- 🌤️ **Real-time Weather** - Get weather information for 50+ Indian cities
- ⏰ **Time Information** - Ask for current time with natural responses
- 💬 **AI-Powered Conversations** - Chat with Jarvis using advanced AI models
- 🔄 **Robust Error Handling** - Automatic retries and fallback mechanisms

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Microphone for voice input
- Internet connection

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/manishs06/Jarvis-Virtual-Assitant.git
cd Jarvis-Virtual-Assitant
```

2. **Automated Setup (Windows)**
```bash
setup.bat
```
*(Or install manually: `pip install -r requirements.txt`)*

3. **Configure AI (Optional)**
- **Online (Fast)**: Get a free key from [Hugging Face](https://huggingface.co/settings/tokens) and add it to `.env`.
- **Offline (Private)**: No key needed! Jarvis will automatically use **GPT4All** (downloads ~2GB model on first run).

4. **Run Jarvis**
```bash
run.bat
```

## 🧠 AI Models

Jarvis uses a smart fallback system:

1. **Hugging Face API** (Primary):
   - Fast responses
   - Requires Internet & API Key
   - Lightweight

2. **GPT4All Local AI** (Fallback):
   - Works completely **Offline**
   - No API Key required
   - Private & Secure
   - Downloads a model (~2GB) on first use

## 🎯 Usage

Once Jarvis is running, you can use these commands:

### Weather Commands
- "What's the weather in Delhi?"
- "Tell me the weather in Lucknow"
- "How's the weather?" (will ask for city)

### Time Commands
- "What time is it?"
- "Tell me the time"

### General Commands
- "Hello" or "Hi" - Greet Jarvis
- "Help" - See all available commands
- Ask any question - Jarvis will use AI to answer
- "Goodbye" or "Exit" - Stop Jarvis

### Supported Cities

Delhi, Lucknow, Kanpur, Agra, Varanasi, Prayagraj, Noida, Greater Noida, Ghaziabad, Meerut, Gorakhpur, Aligarh, Bareilly, Moradabad, Saharanpur, Ayodhya, Mathura, Jhansi, and 30+ more Indian cities.

## 🛠️ Troubleshooting

### PyAudio Installation Issues

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Linux:**
```bash
sudo apt-get install python3-pyaudio portaudio19-dev
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

### Microphone Not Working

1. Check if your microphone is properly connected
2. Grant microphone permissions to your terminal/IDE
3. Test with: `python test_apis.py`

### API Errors

1. Verify your Hugging Face API key is correct in `.env`
2. Check your internet connection
3. Some models may take time to load (503 error) - wait and retry

## 📁 Project Structure

```
Jarvis-Virtual-Assistant/
├── Jarvis.py           # Main application
├── test_apis.py        # API and dependency testing
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment file
├── .env                # Your API keys (create this)
├── README.md           # This file
└── LICENSE             # MIT License
```

## 🔧 Technical Details

### APIs Used
- **Hugging Face Inference API** - For AI responses
  - Primary: Mistral-7B-Instruct-v0.2
  - Fallback: Google FLAN-T5-Base
- **Open-Meteo API** - For weather data (no API key required)

### Libraries
- `SpeechRecognition` - Voice input
- `pyttsx3` - Text-to-speech output
- `requests` - API calls
- `python-dotenv` - Environment variable management
- `PyAudio` - Microphone access

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Hugging Face for providing free AI model inference
- Open-Meteo for free weather API
- All the open-source libraries that make this possible

## 📧 Contact

For issues and questions, please open an issue on GitHub.

---

Made with ❤️ by [manishs06](https://github.com/manishs06)