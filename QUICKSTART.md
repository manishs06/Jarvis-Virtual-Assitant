# 🚀 Quick Start Guide

Get Jarvis up and running in 5 minutes!

## Step 1: Install Python (if not already installed)

Download and install Python 3.8 or higher from [python.org](https://www.python.org/downloads/)

**Important**: Check "Add Python to PATH" during installation!

## Step 2: Get Your API Key

1. Go to [Hugging Face](https://huggingface.co/join) and create a free account
2. Go to [Settings > Access Tokens](https://huggingface.co/settings/tokens)
3. Click "New token" and create a token with "read" permissions
4. Copy your token - you'll need it in Step 4

## Step 3: Run Setup (Automated)

### Windows Users:
Double-click `setup.bat` or run in terminal:
```bash
setup.bat
```

### Linux/Mac Users:
```bash
# Install dependencies
pip install -r requirements.txt

# For PyAudio on Linux:
sudo apt-get install python3-pyaudio portaudio19-dev

# For PyAudio on Mac:
brew install portaudio
pip install pyaudio

# Create .env file
cp .env.example .env
```

## Step 4: Configure Your API Key

1. Open the `.env` file in a text editor
2. Replace `your_huggingface_api_key_here` with your actual API key from Step 2
3. Save the file

Example:
```
HF_API_KEY=hf_abcdefghijklmnopqrstuvwxyz123456789
```

## Step 5: Test Your Setup

```bash
python test_apis.py
```

You should see ✅ checkmarks for all tests. If you see ❌, check the error messages.

## Step 6: Run Jarvis!

### Windows:
Double-click `run.bat` or:
```bash
python Jarvis.py
```

### Linux/Mac:
```bash
python Jarvis.py
```

## 🎤 Try These Commands

Once Jarvis is running:

1. **Say**: "Hello"
   - Jarvis will greet you back

2. **Say**: "What's the weather in Delhi?"
   - Jarvis will tell you the current weather

3. **Say**: "What time is it?"
   - Jarvis will tell you the current time

4. **Say**: "Help"
   - Jarvis will list all available commands

5. **Say**: "Goodbye"
   - Jarvis will exit

## 🐛 Troubleshooting

### "Microphone not found" error
- Make sure your microphone is plugged in
- Grant microphone permissions to your terminal/command prompt
- Try running as administrator (Windows)

### "PyAudio installation failed"
**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Linux:**
```bash
sudo apt-get install python3-pyaudio portaudio19-dev
pip install pyaudio
```

**Mac:**
```bash
brew install portaudio
pip install pyaudio
```

### "API key not configured"
- Make sure you created the `.env` file
- Make sure you replaced the placeholder with your actual API key
- Make sure there are no extra spaces or quotes

### "Model is loading" (503 error)
- This is normal for the first request to a model
- Wait 30 seconds and try again
- The model will stay loaded for future requests

### "I didn't catch that"
- Speak clearly and at a normal pace
- Make sure you're in a quiet environment
- Check your microphone volume settings

## 📚 Need More Help?

- Read the full [README.md](README.md)
- Check the [CHANGELOG.md](CHANGELOG.md) for recent fixes
- Open an issue on GitHub

## 🎉 You're All Set!

Enjoy using Jarvis! Try asking it questions, checking the weather, or just having a conversation.

---

**Pro Tips:**
- Use a good quality microphone for best results
- Speak naturally - Jarvis understands conversational language
- If Jarvis doesn't understand, try rephrasing your question
- The first AI response might be slow as the model loads
