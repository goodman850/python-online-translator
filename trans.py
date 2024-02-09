from googletrans import Translator

def translate_file(input_file, output_file):
    # Create a translator object
    translator = Translator()

    # Read content from the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Detect the language of the text
    detected_lang = translator.detect(text).lang

    # Translate the text to English
    if detected_lang == 'zh-cn' or detected_lang == 'zh-tw':
        translated_text = translator.translate(text, src=detected_lang, dest='en').text
    else:
        print("The input file does not contain Chinese text. No translation performed.")
        translated_text = text

    # Write the translated text to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(translated_text)

if __name__ == "__main__":
    input_file = input("Enter the input file path: ")
    output_file = input("Enter the output file path: ")

    translate_file(input_file, output_file)
    print("Translation complete.")
