# 🔊 Drogon – AI Voice Assistant

## 🔍 What is Drogon?

Drogon is not just another Python script — it’s your intelligent, voice-activated **desktop companion**, designed to simplify your digital life. From browsing the web to sending emails, from playing your favorite songs to telling you a joke when you’re bored — **Drogon listens, understands, and acts** on your spoken commands in real time.

Whether you're a developer looking for quick productivity hacks, a tech enthusiast, or someone who simply wants a smarter way to interact with their PC — **Drogon is built for you**.

---

## 🔐 Your Voice Is Your Key

Drogon stays inactive until you **unlock it using a spoken password**. With a smart, voice-based authentication system, your assistant remains secure even in a shared environment — ensuring that **only your voice activates Drogon**.

---

## 🔄 Working of the Project

### 🔁 Startup Phase
- Drogon greets the user and prompts for a voice password.
- If the correct password is spoken, Drogon is activated.
- Incorrect attempts are counted and capped at 3, after which access is denied.

### 🧠 Command Listening Loop
- After successful authentication, Drogon enters an infinite loop to listen for voice commands.

### 🧾 Command Handling
Based on keywords (like `"Wikipedia"`, `"search"`, `"joke"`, etc.), Drogon performs specific actions:
- Opens web pages  
- Plays media  
- Fetches search results  
- Sends emails  
- Tells time  
- Executes system commands like shutdown or exit  

### ✅ Task Completion
- Once a task is completed, Drogon ends the command loop for that session unless exited manually.

### 📴 Exit
- On commands like `"exit"` or `"quit Drogon"`, the assistant shuts down gracefully with a farewell message.

---

## 🧠 What Drogon Can Do (So Far!)

- ✅ Understand voice commands using Google’s Speech API  
- ✅ Speak back to you using human-like text-to-speech  
- ✅ Secure itself with a voice-based password system  
- ✅ Greet you based on the time of day  
- ✅ Search topics on Wikipedia and summarize them  
- ✅ Perform browser searches using Google or Bing  
- ✅ Fetch and read out custom search results using Google API  
- ✅ Tell you a joke when you need a laugh  
- ✅ Play music from YouTube, Spotify, or even your local PC  
- ✅ Send emails with your voice using SMTP  
- ✅ Tell you the current time  
- ✅ Open frequently used websites and applications  
- ✅ Even shut down your computer on command  

---

## 🛠️ Technologies Used

- **Python 3** - Core programming language  
- **pyttsx3** – Text-to-speech engine  
- **speech_recognition** – For capturing and converting voice commands to text  
- **Wikipedia API** – For information retrieval and summarization  
- **Webbrowser module** – To open URLs in the default browser  
- **Joke API (`jokeapi.dev`)** – To fetch random jokes  
- **smtplib** – For sending emails securely via SMTP  
- **OS module** – For file system interaction and launching applications  
- **Electron-based voice command flow** – (Optional/Future GUI integration for enhanced interactivity)

---

## 📂 Project Status

🚧 _Actively improving: More commands, AI enhancements, and smarter voice logic are under development._

---

## 👨‍💻 Developed by
**Yash Dixit** — _Turning everyday desktops into voice-powered machines._

