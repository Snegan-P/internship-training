from decimal import Decimal


# 1. A list of ten message dictionaries.
messages = [
    {"role": "user",      "content": "Hello!",                  "token_count": 101},
    {"role": "assistant", "content": "Hi! How can I help?",      "token_count": 202},
    {"role": "user",      "content": "Explain Python lists.",    "token_count": 303},
    {"role": "assistant", "content": "Lists are mutable.",       "token_count": 404},
    {"role": "user",      "content": "What is a dictionary?",   "token_count": 505},
    {"role": "assistant", "content": "A key-value data type.",   "token_count": 606},
    {"role": "user",      "content": "Show me a loop.",          "token_count": 707},
    {"role": "assistant", "content": "Use for item in items.",   "token_count": 808},
    {"role": "user",      "content": "What is a lambda?",       "token_count": 909},
    {"role": "assistant", "content": "A small anonymous function.", "token_count": 1010},
]

# Cost per token. Using 0.1 makes floating-point representation
# errors easy to see in the final totals.
COST_PER_TOKEN = 0.1


# 2. Print each message with its position and cost to six decimals.
print("MESSAGES")
for position, message in enumerate(messages, start=1):
    cost = message["token_count"] * COST_PER_TOKEN
    print(
        f"{position}: {message['role']:9} "
        f"{message['token_count']:4} tokens | "
        f"cost = ${cost:.6f} | "
        f"{message['content']}"
    )


# 3. Filter the list two ways.
# Keep messages with at least 500 tokens.

filtered_loop = []
for message in messages:
    if message["token_count"] >= 500:
        filtered_loop.append(message)

filtered_comprehension = [
    message for message in messages
    if message["token_count"] >= 500
]

print("\nFILTER RESULTS")
print("For-loop result:       ", len(filtered_loop), "messages")
print("Comprehension result:  ", len(filtered_comprehension), "messages")

# Confirm that both methods produced the same messages.
assert filtered_loop == filtered_comprehension
print("Both filters agree:", filtered_loop == filtered_comprehension)


# 4. Sort by token count, descending, using lambda.
sorted_messages = sorted(
    messages,
    key=lambda message: message["token_count"],
    reverse=True
)

print("\nSORTED BY TOKEN COUNT (DESCENDING)")
for message in sorted_messages:
    print(message["token_count"], message["role"], message["content"])


# 5. Read token counts from a text file.
#
# Example token_counts.txt:
#
# 111
# 222
# 333
# 444
# 555
# 666
# 777
# 888
# 999
# 1110
# not-a-number
#
# The invalid value is deliberately included to demonstrate error handling.

print("\nREADING TOKEN COUNTS FROM FILE")

try:
    with open("token_counts.txt", "r", encoding="utf-8") as file:
        file_counts = []

        for line_number, line in enumerate(file, start=1):
            value = line.strip()

            if not value:
                continue

            try:
                token_count = int(value)
                file_counts.append(token_count)
            except ValueError:
                print(
                    f"Line {line_number}: {value!r} is not a number; "
                    "skipping it."
                )

except FileNotFoundError:
    print("token_counts.txt was not found.")
    file_counts = []


# Use the valid values to update the ten messages.
for message, token_count in zip(messages, file_counts):
    message["token_count"] = token_count

print("Valid token counts read:", file_counts)


# 6. Total the cost twice: float and Decimal.

# Float calculation.
float_total = sum(
    message["token_count"] * COST_PER_TOKEN
    for message in messages
)

# Decimal calculation.
decimal_rate = Decimal("0.1")
decimal_total = sum(
    Decimal(message["token_count"]) * decimal_rate
    for message in messages
)

print("\nTOTAL COST")
print(f"Float total:   {float_total:.17f}")
print(f"Decimal total: {decimal_total}")
print(f"Difference:    {abs(Decimal(str(float_total)) - decimal_total)}")

print(
    "\nThe totals can differ because float uses binary floating-point "
    "representation, while Decimal represents the decimal value exactly."
)


# 7. Unicode: Tamil string.
text = "வணக்கம் உலகம்"

character_length = len(text)
byte_length = len(text.encode("utf-8"))

print("\nUNICODE")
print("Text:", text)
print("Length in characters:", character_length)
print("Length in UTF-8 bytes:", byte_length)

print(
    "UTF-8 bytes are not the same thing as tokens: a Tamil string can use "
    "more bytes per character, but the token bill depends on the tokenizer."
)


# 8. Deliberate list aliasing.
first_name = ["apple", "banana", "cherry"]
second_name = first_name

first_name.append("orange")

print("\nLIST ALIASING")
print("first_name: ", first_name)
print("second_name:", second_name)

print(
    "Both names refer to the same list object, so changing the list through "
    "first_name also changes what second_name sees."
)