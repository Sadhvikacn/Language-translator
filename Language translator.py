import tkinter as tk  
from translate import Translator  
from langdetect import detect  
  
def translate_text():  
    text = english_text.get("1.0", "end-1c")  
    target_language = target_code.get()  
  
    # Detect the source language  
    source_language = detect(text)  
  
    # Call the translation function  
    translator = Translator(from_lang=source_language, to_lang=target_language)  
    translation = translator.translate(text)  
  
    # Set the translated text in the GUI  
    translated_text.delete("1.0", "end")  
    translated_text.insert("1.0", translation)  
  
# Set up the GUI  
root = tk.Tk()  
root.title("Text Translator")  
  
# Text input  
text_label = tk.Label(root, text="Enter text:")  
text_label.pack()  
  
english_text = tk.Text(root, height=5, width=50)  
english_text.pack()  
  
# Target language input  
target_label = tk.Label(root, text="Enter target language code:")  
target_label.pack()  
  
target_code = tk.Entry(root)  
target_code.pack()  
  
# Translation button  
translate_button = tk.Button(root, text="Translate", command=translate_text)  
translate_button.pack()  
  
# Translated text output  
translated_label = tk.Label(root, text="Translated text:")  
translated_label.pack()  
  
translated_text = tk.Text(root, height=5, width=50)  
translated_text.pack()  
  
root.mainloop() 