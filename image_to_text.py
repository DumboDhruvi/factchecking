import easyocr

def image_to_text(image_path):
    try:
        # Create an EasyOCR reader instance
        reader = easyocr.Reader(['en'])  # You can specify the language(s) you want to use

        # Read the text from the image
        results = reader.readtext(image_path)

        # Extract the detected text
        extracted_text = ""
        for result in results:
            text = result[1]  # The detected text is in the second element of each result tuple
            extracted_text += text + " "

        return extracted_text.strip()

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Allow the user to input the image path interactively
    image_path = input("Enter the path to the image: ")

    # Example: Convert an image to text using EasyOCR
    extracted_text = image_to_text(image_path)
    print("Extracted Text:")
    print(extracted_text)
