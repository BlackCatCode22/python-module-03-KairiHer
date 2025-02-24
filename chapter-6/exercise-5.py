text = 'X-DSPAM-Confidence: 0.8475'

# Find the position of the colon
colon_pos = text.find(':')

# Extract the portion after the colon and strip any whitespace
number_str = text[colon_pos + 1:].strip()

# Convert to float
confidence_value = float(number_str)

print(confidence_value)  # Output: 0.8475
