import re

print("==============================")
print("   AI DOCUMENT SUMMARIZER")
print("==============================")

# Read document
with open("document.txt", "r", encoding="utf-8") as f:
    document = f.read()

# Clean text
document = re.sub(r"\s+", " ", document).strip()

# Split into sentences
sentences = re.split(r"(?<=[.!?])\s+", document)

# Summary length
print("\nChoose summary length:")
print("1 - Short")
print("2 - Medium")
print("3 - Long")

choice = input("Enter choice: ")

if choice == "1":
    ratio = 3
elif choice == "3":
    ratio = 1
else:
    ratio = 2

# Healthcare keywords
keywords = [
    "patient", "diagnosis", "treatment", "disease",
    "medical", "hospital", "healthcare", "privacy",
    "medication", "doctor", "clinical", "data"
]

stop_words = {
    "the", "a", "an", "is", "are", "and", "or",
    "of", "to", "in", "on", "for", "with", "that",
    "this", "by", "as", "it"
}

# Score sentences
scored = []

for index, sentence in enumerate(sentences):
    words = re.findall(r"\b\w+\b", sentence.lower())

    score = sum(
        1 for word in words
        if word not in stop_words
    )

    for keyword in keywords:
        if keyword in sentence.lower():
            score += 5

    scored.append((score, index, sentence))

# Select important sentences
number_to_select = max(1, len(sentences) // ratio)

selected = sorted(
    scored,
    reverse=True
)[:number_to_select]

# Restore original order
selected = sorted(
    selected,
    key=lambda x: x[1]
)

summary = " ".join(
    item[2] for item in selected
)

# Statistics
characters = len(document)
words = len(document.split())
sentence_count = len(sentences)

# Display results
print("\n===== DOCUMENT STATISTICS =====")
print("Characters:", characters)
print("Words:", words)
print("Sentences:", sentence_count)

print("\n===== SUMMARY =====")
print(summary)

print("\n==============================")
print("Project completed successfully.")
