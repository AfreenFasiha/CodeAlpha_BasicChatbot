# ============================================================
# CodeAlpha Internship — Task 4: Basic Chatbot
# Author  : AFREEN FASIHA | ID: CA/DF1/86093
# Domain  : Python Programming
# ============================================================

import random
import datetime

# ── Response rules: keyword → list of possible replies ─────
RESPONSES = {
    # Greetings
    ("hello", "hi", "hey", "howdy", "hiya"): [
        "Hello! 👋 How can I help you today?",
        "Hey there! Great to see you!",
        "Hi! I'm your CodeAlpha chatbot. What's up?",
    ],
    # How are you
    ("how are you", "how r u", "how are u", "how do you do", "you good"): [
        "I'm doing great, thanks for asking! 😊",
        "Feeling fantastic! Ready to chat.",
        "All systems running perfectly! How about you?",
    ],
    # Name
    ("your name", "who are you", "what are you", "what's your name"): [
        "I'm CodeBot 🤖 — your CodeAlpha internship chatbot!",
        "Call me CodeBot! Built with ❤ using Python.",
    ],
    # Time / Date
    ("time", "what time", "current time"): [],   # handled dynamically
    ("date", "today", "what day"): [],            # handled dynamically
    # Help
    ("help", "assist", "support", "what can you do"): [
        "I can chat with you, tell you the time/date, share jokes, and more. Just ask!",
    ],
    # Jokes
    ("joke", "funny", "laugh", "tell me a joke"): [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why did the Python developer go broke? Because he used up all his cache! 💸",
        "What do you call a fish without eyes? A fsh. 🐟",
    ],
    # Compliments
    ("good bot", "nice", "great", "awesome", "well done", "thanks", "thank you"): [
        "Aww, thank you! 😊 You're pretty awesome yourself.",
        "That means a lot! I'm just doing my best. 🤖",
    ],
    # Farewell
    ("bye", "goodbye", "see you", "exit", "quit", "later"): [
        "Goodbye! 👋 Have a wonderful day!",
        "See you later! Stay curious and keep coding! 🐍",
        "Bye! It was nice chatting with you. 😊",
    ],
    # About Python / CodeAlpha
    ("python", "coding", "programming"): [
        "Python is amazing! 🐍 It's beginner-friendly yet super powerful.",
        "Love Python! Great choice for your CodeAlpha internship.",
    ],
    ("codealpha",): [
        "CodeAlpha is a great platform to build real-world skills! 🚀",
        "Keep working hard on your CodeAlpha tasks — you've got this! 💪",
    ],
}

# Flat map: each keyword → its reply list (for fast lookup)
KEYWORD_MAP = {}
for keywords, replies in RESPONSES.items():
    for kw in keywords:
        KEYWORD_MAP[kw] = replies

FALLBACK_REPLIES = [
    "Hmm, I didn't quite catch that. Could you rephrase?",
    "Interesting! Tell me more. 🤔",
    "I'm still learning. Try asking me something else!",
    "Not sure I understand, but I'm here to chat!",
]


def get_reply(user_input: str) -> str:
    """Return a reply based on keywords found in user_input."""
    text = user_input.lower().strip()

    # ── Dynamic replies ────────────────────────────────────
    if any(w in text for w in ("time", "what time", "current time")):
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now} ⏰"

    if any(w in text for w in ("date", "today", "what day")):
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"Today is {today} 📅"

    # ── Keyword matching ───────────────────────────────────
    for keyword, replies in KEYWORD_MAP.items():
        if keyword in text and replies:
            return random.choice(replies)

    # ── Fallback ───────────────────────────────────────────
    return random.choice(FALLBACK_REPLIES)


def chat():
    """Main chatbot loop."""
    print("\n" + "=" * 45)
    print("   🤖  CodeBot — CodeAlpha Basic Chatbot")
    print("=" * 45)
    print("  Type 'bye' to exit.\n")

    while True:
        user_input = input("  You: ").strip()

        if not user_input:
            print("  Bot: Please say something! 😅\n")
            continue

        reply = get_reply(user_input)
        print(f"  Bot: {reply}\n")

        # Exit if the reply is a farewell
        if any(word in user_input.lower() for word in ("bye", "goodbye", "exit", "quit")):
            break


if __name__ == "__main__":
    chat()