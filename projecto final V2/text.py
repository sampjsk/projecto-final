import pyttsx3
import time
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text, delay=0.6):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()
    time.sleep(delay)

def get_user_choice(prompt, options):
    speak(prompt)
    for i, option in enumerate(options, start=1):
        speak(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Your choice: ").strip())
            if 1 <= choice <= len(options):
                return choice
            else:
                speak("That’s not a valid number. Try again.")
        except ValueError:
            speak("Please enter a number.")

def main():
    speak("Hi! I'm your virtual assistant, and today we're going to talk about something really important: climate change.")
    speak("Before we start, may I ask your name?")
    name = input("Your name: ").strip()
    speak(f"Great to meet you, {name}!")

    speak("Climate change is one of the biggest challenges facing our world.")
    speak("It's caused by greenhouse gases like carbon dioxide trapping heat in our atmosphere, which leads to rising temperatures, melting ice caps, and more extreme weather.")

    awareness = get_user_choice(
        "How much do you already know about climate change?",
        [
            "Not much. I’m here to learn.",
            "I know the basics.",
            "I follow it closely."
        ]
    )

    if awareness == 1:
        speak("No problem! We all start somewhere. You're doing the right thing by learning.")
    elif awareness == 2:
        speak("That’s great! A solid understanding helps us make better choices.")
    else:
        speak("Awesome! Then you’ll probably recognize the urgency of taking action.")

    action = get_user_choice(
        "Which of these effects of climate change concerns you the most?",
        [
            "Rising sea levels",
            "More wildfires and hurricanes",
            "Loss of biodiversity",
            "Impact on future generations"
        ]
    )

    effects = {
        1: "Rising seas could displace millions of people who live in coastal areas.",
        2: "Extreme weather events are becoming stronger and more frequent.",
        3: "Species are disappearing at an alarming rate due to habitat loss and temperature shifts.",
        4: "Our choices today shape the world our children will inherit."
    }

    speak(effects[action])

    speak("But here's the good news: we can still make a difference.")

    solutions = [
        "Use renewable energy like solar and wind instead of fossil fuels.",
        "Reduce, reuse, and recycle to cut down on waste.",
        "Use public transport, bike, or walk whenever possible.",
        "Plant trees and protect green spaces.",
        "Support leaders and policies that protect the environment."
    ]

    speak("Let me share a few actions we can take:")

    for solution in solutions:
        speak(f"• {solution}")

    inspire_quotes = [
        "The Earth is what we all have in common. – Wendell Berry",
        "The greatest threat to our planet is the belief that someone else will save it. – Robert Swan",
        "We do not inherit the Earth from our ancestors, we borrow it from our children. – Native American Proverb"
    ]
    
    speak("And here's something to inspire you before we finish.")
    speak(random.choice(inspire_quotes))

    speak(f"Thanks for taking the time to talk about this, {name}. The planet needs more people like you.")
    speak("Would you like to learn more about what you can do at home or school in another session?")
    speak("Until next time!")

if __name__ == "__main__":
    main()