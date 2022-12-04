import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

def main():
  while True:
      try:
        prompt = input(">: ")
        print("Loading...")
        completions = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        for choice in completions.choices:
            print(choice.text)
      except KeyboardInterrupt:
          print("\nKeyboard Interrupt was caught. Exiting program.")
          break
      except openai.error.OpenAIError as e:
          print(f"An error occurred: {e}")
