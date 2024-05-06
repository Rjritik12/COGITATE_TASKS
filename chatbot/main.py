import nltk
from nltk.chat.util import Chat, reflections

# Define the pairs of patterns and responses
pairs = [
    [
        r"My name is (.*)",
        ["Hello %1, How can I help you today?",]
    ],
    [
        r"What is your name?",
        ["I'm a simple chatbot, I don't have a name.",]
    ],
    [
        r"How are you?",
        ["I'm a program, so I don't have feelings, but I'm here to help you.",]
    ],
    [
        r"I need help (.*)",
        ["Sure, I'd be happy to help with %1",]
    ],
    [
        r"Quit",
        ["Goodbye!", "Farewell!", "So long!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand what you mean.",]
    ]
]

# Create the chatbot
chat = Chat(pairs, reflections)

# Start the conversation
chat.converse()