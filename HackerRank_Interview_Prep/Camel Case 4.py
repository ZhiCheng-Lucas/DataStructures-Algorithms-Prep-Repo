import sys

lines = sys.stdin.readlines()
for line in lines:
    # Parse input
    parts = line.strip().split(";")
    operation = parts[0]  # S or C
    string_type = parts[1]  # M, C, or V
    text = parts[2]  # The actual text to process

    # Split operation
    if operation == "S":
        # Remove () for methods
        text = text.replace("()", "")

        # Process the string
        tmp = []
        tmp_string = ""

        for i, char in enumerate(text):
            if i == 0:  # First character should always be lowercase in output
                tmp_string = char.lower()
            elif char.isupper():
                if tmp_string:  # Store previous word
                    tmp.append(tmp_string)
                tmp_string = char.lower()
            else:
                tmp_string += char

        # Add the last word if it exists
        if tmp_string:
            tmp.append(tmp_string)

        # Print result
        print(" ".join(tmp))

    # Combine operation
    else:
        words = text.strip().split()
        result = ""

        if string_type == "C":  # Class
            # Capitalize first letter of each word
            result = "".join(word.capitalize() for word in words)

        elif string_type == "V":  # Variable
            # First word lowercase, rest capitalized
            result = words[0].lower() + "".join(word.capitalize() for word in words[1:])

        elif string_type == "M":  # Method
            # First word lowercase, rest capitalized, add ()
            result = words[0].lower() + "".join(word.capitalize() for word in words[1:]) + "()"

        print(result)
