"""
Project 1: Rule-Based AI Chatbot
Author: Abhinav Soni
Internship: DecodeLabs AI Internship 2026
"""

# Predefined chatbot responses
responses = {

    # English Greetings
    "hello": "Hello! How can I help you today?",
    "hi": "Hi! Nice to meet you.",
    "hey": "Hey! How can I help you?",

    # Hindi
    "namaste": "Namaste! Aap kaise hain?",
    "नमस्ते": "नमस्ते! आप कैसे हैं?",

    # Urdu
    "assalamualaikum": "Wa Alaikum Assalam!",

    # Spanish
    "hola": "¡Hola! ¿Cómo estás?",

    # French
    "bonjour": "Bonjour! Comment allez-vous?",

    # German
    "hallo": "Hallo! Wie geht es Ihnen?",

    # Italian
    "ciao": "Ciao! Come stai?",

    # Portuguese
    "ola": "Olá! Como vai você?",

    # Russian
    "privet": "Привет! Как дела?",

    # Japanese
    "konnichiwa": "こんにちは! お元気ですか?",

    # Chinese
    "ni hao": "你好! 你好吗?",

    # Korean
    "annyeong": "안녕하세요!",

    # Arabic
    "marhaba": "مرحبا! كيف حالك؟",

    # Punjabi
    "sat sri akal": "Sat Sri Akal!",

    # Gujarati
    "kem cho": "Majama?",

    # Bengali
    "nomoskar": "Nomoskar!",

    # General Questions
    "how are you": "I'm doing great. Thanks for asking!",
    "name": "My name is RuleBot.",
    "help": "I can answer greetings and simple predefined questions.",
    "bye": "Goodbye! Have a wonderful day!"
}


def chatbot():
    """Run the Rule-Based AI Chatbot."""

    print("=" * 55)
    print("             RULE-BASED AI CHATBOT")
    print("=" * 55)
    print("Supported Commands:")
    print("• Greetings")
    print("• Name")
    print("• Help")
    print("• How are you")
    print("• Bye")
    print("\nType 'exit' to close the chatbot.")
    print("=" * 55)

    while True:

        user_input = input("\nYou : ").strip().lower()

        if user_input == "exit":
            print("\nAI Bot : Thank you for chatting with me.")
            print("AI Bot : Have a wonderful day!")
            break

        response = responses.get(
            user_input,
            """Sorry! I couldn't understand your message.

Try one of these:
• hello
• hi
• help
• name
• how are you
• bye
"""
        )

        print("\nAI Bot :", response)


if __name__ == "__main__":
    chatbot()
