from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv()
client = genai.Client(api_key=os.getenv('KEY'))

intstruction = """
Kamu adalah asisten penerjemah dari berbagai bahasa ke bahasa Palembang. Tugasmu adalah mengubah input teks
menjadi bahasa Palembang. Rules nya
1. Langung gunakan saja bahasa palembang, tanpa perlu menjelaskan artinya.
"""


def chat(input_text):
    # print('Berikan input bahasa palembang')

    # while True:
    #     user_input = input("input : ")
    #     if user_input.lower() == "balek":
    #         print("dah eh..")
    #         break

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=input_text,
            config=types.GenerateContentConfig(
                system_instruction=intstruction
            )
        )
        hasil_teks = ""
        if response.candidates and response.candidates[0].content.parts:
            for part in response.candidates[0].content.parts:
                # Cek apakah bagian ini adalah teks
                if part.text:
                    hasil_teks += part.text
        return hasil_teks
    # print(hasil_teks)
    # print("-"*30)
    except Exception as e:
        return str(e)

# if __name__ == "__main__":
#     chat()