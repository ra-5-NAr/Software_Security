# Run-Length Encoding (RLE)

def rle_encode(data):
    encoded = ""
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            count += 1
        else:
            encoded += str(count) + data[i-1]
            count = 1

    encoded += str(count) + data[-1]
    return encoded


def rle_decode(data):
    decoded = ""
    count = ""

    for char in data:
        if char.isdigit():
            count += char
        else:
            if count == "":
                print("ERROR: Text is not valid RLE encoded data.")
                return ""
            decoded += char * int(count)
            count = ""

    return decoded


# User input
text = input("Enter text: ")
choice = input("Do you want to Encode or Decode? (e/d): ").lower()

if choice == "e":
    print("Encoded text:", rle_encode(text))

elif choice == "d":
    result = rle_decode(text)
    if result != "":
        print("Decoded text:", result)

else:
    print("Invalid choice. Enter 'e' or 'd'.")