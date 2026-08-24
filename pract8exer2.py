# Text Moderation Filter

text = input("Enter your feedback: ")

# Words to be filtered
target_words = ["bad", "stupid", "hate"]

# Replace target words with ***
for word in target_words:
    text = text.replace(word, "***")

print("Filtered Feedback:", text)