import pyttsx3 # text-to-speech library
import datetime # datetime library to get the current time
import speech_recognition as sr # speech recognition library
import wikipedia # wikipedia library for searching
import webbrowser # webbrowser library to open web pages
import os # os library for interacting with the operating system
import smtplib # smtplib library for sending emails
import requests # requests library for making HTTP requests
from googleapiclient.discovery import build # Google API client library


# CONFIGURATION
VOICE_PASSWORD = "beautiful"  # Change this to your desired password
API_KEY = ''  # Your Google Custom Search API key
SEARCH_ENGINE_ID = ''  # Your Custom Search Engine ID
EMAIL_ADDRESS = 'youremail@gmail.com' # Your email address for sending emails
EMAIL_PASSWORD = 'your-password-here' # Your email password
MUSIC_DIR = "C:\\Users\\dixit\\Music\\my music" # Directory path for music files
VS_CODE_PATH = "C:\\Users\\dixit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # Path to VS Code executable

# TEXT-TO-SPEECH SETUP 
engine = pyttsx3.init('sapi5')           # Initialize the pyttsx3 engine with SAPI5 driver (Windows TTS API)
voices = engine.getProperty('voices')    # Get a list of available voices installed on the system
engine.setProperty('voice', voices[0].id)  # Set the voice to the first available one (default system voice)

# Function to convert the given text string into spoken audio
def speak(audio):
    engine.say(audio)       # Load the text into the speech engine
    engine.runAndWait()     # Speak the loaded text aloud

# Function to greet the user based on current time
def wishMe():
    hour = int(datetime.datetime.now().hour)  # Get the current hour (0–23)

    if hour >= 0 and hour < 12:
        speak("Hey...Good Morning!")         
    elif hour >= 12 and hour < 18:
        speak("Hey...Good Afternoon!")        
    else:
        speak("Hey...Good Evening!")           

    speak("I am Drogon, How May I Assist You?")   


# Captures voice input from the user and returns it as text
def takeCommand():
    r = sr.Recognizer()  # Create a Recognizer object for speech recognition
    with sr.Microphone() as source:  # Use the default microphone as input source
        print("Listening...")  
        r.pause_threshold = 1  # Wait for 1 second of silence before ending recording
        audio = r.listen(source)  # Capture the audio from the microphone

    try:
        print("Recognizing...")  
        query = r.recognize_google(audio, language='en-in')  # Convert audio to text using Google's API
        print(f"User said: {query}\n")  # Display the recognized text

    except Exception as e:
        print("Say that again please...")  # If recognition fails, prompt user to repeat
        return "None"  # Return "None" if there's an error

    return query  # Return the recognized text


# Fetches a random joke from JokeAPI and returns it
def get_joke():
    response = requests.get("https://v2.jokeapi.dev/joke/Any?type=single")  # Request a single-part joke
    joke_data = response.json()  # Parse the JSON response

    if joke_data.get("joke"):  # If a joke is present in the response
        return joke_data["joke"]  # Return the joke text

    return "Apologies, I'm out of jokes for now. Try again later."  # Fallback if no joke received


# Performs a Google Custom Search using the provided query
def google_search(query):
    service = build("customsearch", "v1", developerKey=API_KEY)  # Initialize the custom search service with API key
    res = service.cse().list(q=query, cx=SEARCH_ENGINE_ID).execute()  # Execute search with query and search engine ID
    return res  # Return the search results


# Sends an email using the SMTP protocol
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to Gmail's SMTP server on port 587
    server.ehlo()  # Identify the client to the server
    server.starttls()  # Start TLS encryption for the connection
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in using the sender's email credentials
    server.sendmail(EMAIL_ADDRESS, to, content)  # Send the email from sender to recipient with content
    server.close()  # Terminate the SMTP session


# MAIN PROGRAM 

# Entry point for the program when run directly
if __name__ == "__main__":
    wishMe()  # Greet the user according to current time
    i = 0      # Counter for authentication failures
    task = 0   # Flag to indicate if a task was successfully completed

    # Loop to allow up to 3 authentication attempts if no task has been executed yet        
    while i < 3 and task == 0:
        speak("Please speak the password to activate Drogon.")
        password_input = takeCommand().lower()  # Capture spoken password

        if VOICE_PASSWORD in password_input:
            speak("Authentication successful. Drogon is now active. How can I assist you today?")# Confirm authentication
 
            # Start infinite loop to process further user commands
            while True:
                query = takeCommand().lower()  # Capture the next voice command

                # ===== WIKIPEDIA SEARCH =====
                if 'wikipedia' in query:
                    speak('Searching Wikipedia...')   
                    query = query.replace("wikipedia", "")  # Remove the keyword 'wikipedia' from the query
                    try:
                        results = wikipedia.summary(query, sentences=2)  # Get 2-line summary from Wikipedia
                        speak("So, According to Wikipedia")  
                        print(results)   
                        speak(results)   
                    except:
                        speak("Couldn't find info on Wikipedia.")  # If any error occurs (e.g., no results)
                    task = 1  # Set task completion flag
                    break  # Exit the inner command-processing loop

                # ===== GOOGLE SEARCH VIA BROWSER =====
                elif 'search on google' in query:
                    speak('What I can search for you...')  # Prompt user for a search query
                    query = takeCommand().lower()  # Take the actual search term from user
                    if query != 'none':  # Check if valid command received
                        audio = f"Searching '{query}' on browser..."  
                        print(audio)  
                        speak(audio)  
                        webbrowser.open(f"https://www.bing.com/search?q={query}")  # Open search in browser
                        task = 1  
                        break       # Exit the current loop


                # ===== TELL A RANDOM JOKE =====
                elif 'tell me a joke' in query:
                    joke = get_joke()       # Fetch a random joke using JokeAPI
                    print(joke)             
                    speak(joke)             
                    task = 1               
                    break                   

                # ===== YOUTUBE SEARCH =====
                elif 'search on youtube' in query:
                    speak('What I can search for you on youtube')  # Ask user for the search term
                    query = takeCommand().lower()                 # Take user voice input and convert to lowercase
                    if query != 'none':                           # Proceed only if user provided a valid input
                        audio = f"Searching '{query}' on YouTube..."
                        print(audio)                              
                        speak(audio)                              
                        webbrowser.open(f"https://www.youtube.com/results?sp=mAEB&search_query={query}")  # Open YouTube search results
                        task = 1                                  
                        break                                     

                # ===== SPOTIFY SEARCH =====
                elif 'search on spotify' in query:
                    speak('What I can search for you on Spotify')  # Ask user what to search for on Spotify
                    query = takeCommand().lower()                 # Capture the user's response
                    if query != 'none':                           
                        audio = f"Searching '{query}' on Spotify..."  # Construct response
                        print(audio)                               
                        speak(audio)                               
                        webbrowser.open(f"https://open.spotify.com/search/{query}")  # Open Spotify search page
                        task = 1                                   
                        break                                  

                # ===== PLAY MUSIC ON SPOTIFY  =====
                elif 'play music on spotify' in query:
                    webbrowser.open("Update with spotify link or any playlist list")  # Open a predefined Spotify playlist or track
                    task = 1   
                    break      

                # ===== PLAY MUSIC ON YOUTUBE =====
                elif 'play music on youtube' in query:
                    webbrowser.open("https://www.youtube.com/watch?v=w402dXxAO3c&list=PLummYxZcETxcVoFlS5q38HZm0Eg2g8D-P&pp=gAQBiAQB8AUB")  # Open a predefined YouTube music playlist
                    task = 1
                    break

                # ===== PLAY MUSIC FROM LOCAL COMPUTER DIRECTORY =====
                elif 'play music on computer' in query:
                    songs = os.listdir(MUSIC_DIR)  # List all files in the specified music directory
                    print(songs)  # Output the list of music files to the console
                    os.startfile(os.path.join(MUSIC_DIR, songs[0]))  # Play the first song in the directory
                    task = 1
                    break

                # ===== PERFORM A GOOGLE CUSTOM SEARCH =====
                elif 'search' in query:
                    query = query.replace('search', '').strip()  # Clean the query by removing the word "search"
                    speak(f"Searching for {query}")  # Speak the search query
                    results = google_search(query)  # Perform Google Custom Search
                    if 'items' in results:
                        for item in results['items'][:2]:  # Read out the first two search results
                            speak(f"Title: {item['title']}. {item['snippet']}")
                    else:
                        speak("No results found.")  
                    task = 1
                    break

                # ===== SEND EMAIL TO A PREDEFINED RECIPIENT =====
                elif 'email to yash' in query:
                    try:
                        speak("What should I say?")   
                        content = takeCommand()  # Capture message via voice input
                        to = "ReceiverEmail"  # Replace with the recipient's actual email address
                        sendEmail(to, content)  
                        speak("Email has been sent!")  
                    except Exception as e:
                        speak("Sorry Sir, not able to send this email")  
                    task = 1
                    break

                # ===== OPEN TIME TABLE LINK IN BROWSER =====
                elif 'open time table' in query:
                    webbrowser.open("Update with your time table link")  # Opens the user’s timetable in the browser 
                    task = 1  # Mark task as completed
                    break  # Exit the command loop

                # ===== GENERAL OPEN COMMAND FOR WEBSITES AND LOCATIONS =====
                elif 'open' in query:
                    if 'youtube' in query:
                        speak("Sure Sir...I am opening YouTube for you.")  # Voice confirmation
                        webbrowser.open("youtube.com")  # Open YouTube

                    elif 'google' in query:
                        speak("Sure Sir...I am opening Google for you.")
                        webbrowser.open("google.com")  # Open Google homepage

                    elif 'lead code' in query:
                        speak("Sure Sir...I am opening LeetCode for you.")
                        webbrowser.open("leetcode.com")  # Open LeetCode

                    elif 'games' in query:
                        speak("Sure Sir...I am opening Games for you.")
                        webbrowser.open("poki.com")  # Open Poki - free online games

                    elif 'amazon' in query:
                        speak("Sure Sir...I am opening Amazon for you.")
                        webbrowser.open("https://amazon.in")  # Open Amazon India

                    elif 'flipkart' in query:
                        speak("Sure Sir...I am opening Flipkart for you.")
                        webbrowser.open("https://flipkart.com")  # Open Flipkart

                    elif 'drive' in query:
                        speak("Sure Sir...I am opening drive for you.")
                        os.startfile("D:\\")  # Open D: drive on local machine

                    else:
                        speak("I looked everywhere, but couldn't find that site.")  # Fallback if no match found

                    task = 1  # Mark task as completed
                    break  

                # ===== OPEN VISUAL STUDIO CODE =====
                elif 'open vs code' in query:
                    os.startfile(VS_CODE_PATH)  # Launch Visual Studio Code using its path
                    task = 1
                    break

                # ===== SHUT DOWN SYSTEM =====
                elif 'shutdown' in query:
                    speak("Shutting Down the System in 3 seconds")  # Voice notification before shutdown
                    os.system("shutdown /s /t 3")  # Execute system shutdown with a delay of 3 seconds
                    task = 1
                    break

                # ===== REPORT CURRENT TIME =====
                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Get the current system time
                    speak(f"Sir, the time is {strTime}")  # Speak out the current time

                # ===== EXIT THE ASSISTANT =====
                elif 'exit' in query or 'quit drogon' in query:
                    speak("Goodbye Sir, power down initiated. See you next time!")  # Farewell voice message
                    exit()  # Exit the entire assistant program

                # ===== UNKNOWN COMMAND HANDLER =====
                else:
                    speak("Hmm... I'm smart, but not that smart yet. Try asking something else!")  # Fallback for unrecognized commands


        # ===== HANDLE FAILED ACTIVATION/LOGIN ATTEMPTS =====
        else:
            if i == 0:
                # First failed attempt
                speak("Warning! Incorrect password. You have two attempts left.")
            elif i == 1:
                # Second failed attempt
                speak("Second failed attempt. One final try remaining.")
            else:
                # Third failed attempt - lockout triggered
                speak("Access denied.Goodbye.")
            i += 1  # Increment the failed attempts counter

