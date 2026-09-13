import re # For Regular Expressions

import time as t # For time based elements to help the user read edited text

import os # For searching directories and file handling

from random import randint # For random generation

import matplotlib.pyplot as plt # for statistical analysis

import polars as pl # For transcript creation and csv making

# AI Word list

ai_words = [
    'journey', 'multitude', 'plethora', 'testament', 'accordingly', 'actionable',
    'insights', 'adept', 'adoption', 'rate', 'aforementioned', 'agile',
    'ai-powered', 'aligns', 'ample', 'opportunities', 'amplify', 'arduous',
    'result', 'augment', 'bandwidth', 'based', 'information', 'provided',
    'best', 'practices', 'blockchain-enabled', 'brand', 'awareness', 'broadly',
    'speaking', 'burgeoning', 'cannot', 'overstated', 'capacity', 'building',
    'captivating', 'certainly', 'here’s', 'change', 'management', 'cloud-based',
    'cognizant', 'collaborative', 'commendable', 'competitive', 'complexity',
    'conceptualize', 'conducting', 'consequently', 'considerable', 'continuous',
    'improvement', 'corporate', 'social', 'responsibility', 'cost', 'optimization',
    'craft', 'critical', 'crucial', 'customer', 'loyalty', 'satisfaction',
    'customer-centric', 'cutting-edge', 'data-driven', 'deep', 'dive',
    'understanding', 'deliverables', 'delve', 'delved', 'delving', 'intricacies',
    'demonstrates', 'significant', 'deployment', 'digital', 'transformation',
    'disruptive', 'innovation', 'expertise', 'downtime', 'drive', 'driven',
    'driving', 'dynamic', 'efficiency', 'elevate', 'embark', 'voyage',
    'embarked', 'emerging', 'technologies', 'empower', 'enable', 'encountered',
    'hurdles', 'enhance', 'enhancing', 'enlightening', 'enriches', 'entails',
    'entrenched', 'epicenter', 'essential', 'essentially', 'esteemed', 'ethical',
    'considerations', 'ever-evolving', 'excels', 'exciting', 'exemplary',
    'explore', 'facilitate', 'flourishing', 'foray', 'foster', 'fostering',
    'fresh', 'perspectives', 'inception', 'execution', 'fundamental',
    'fundamentally', 'furthermore', 'future-proof', 'game', 'changer',
    'game-changer', 'generally', 'given', 'glean', 'going', 'forward',
    'golden', 'governance', 'granular', 'granularly', 'grasp', 'groundbreaking',
    'growing', 'recognition', 'hence', 'herein', 'heretofore', 'high-level',
    'hinder', 'holistic', 'holistically', 'however', 'impactful', 'implementation',
    'implications', 'important', 'particular', 'today’s', 'rapidly', 'evolving',
    'industry', 'innovative', 'invaluable', 'issue', 'resolution', 'worth',
    'noting', 'iteration', 'kaleidoscope', 'key', 'takeaways', 'knowledge',
    'transfer', 'kpis', 'performance', 'indicators', 'latency', 'leverage',
    'linchpin', 'low-level', 'manifold', 'penetration', 'share', 'trends',
    'maximize', 'milestone', 'mission-critical', 'moreover', 'moving',
    'multifaceted', 'mvp', 'minimum', 'viable', 'product', 'namely', 'navigating',
    'complexities', 'nevertheless', 'new', 'next-generation', 'notable',
    'notwithstanding', 'nuanced', 'numerous', 'offboarding', 'offer',
    'comprehensive', 'offerings', 'edge', 'onboarding', 'operational',
    'excellence', 'optimize', 'pain', 'point', 'paradigm', 'shift',
    'paramount', 'particularly', 'areas', 'pervasive', 'pivotal', 'poc',
    'proof', 'concept', 'preemptively', 'problem', 'solving', 'process',
    'profitability', 'profound', 'promote', 'pronged', 'quality', 'assurance',
    'control', 'reaching', 'recognize', 'regulatory', 'compliance',
    'relentless', 'remarkable', 'resonate', 'resource', 'allocation',
    'revenue', 'growth', 'risk', 'mitigation', 'roadmap', 'robust',
    'roi', 'return', 'investment', 'root', 'cause', 'analysis', 'scalable',
    'scrum', 'seamless', 'shed', 'showcasing', 'significantly', 'contributes',
    'simply', 'put', 'sla', 'service', 'level', 'agreement', 'solution',
    'development', 'specifically', 'sprint', 'state-of-the-art', 'strategic',
    'alignment', 'streamline', 'strive', 'strong', 'substantial', 'substantially',
    'sustainability', 'synergistically', 'synergy', 'systemic', 'tailor',
    'tapestry', 'tco', 'total', 'cost', 'ownership', 'thereby', 'therefore',
    'therein', 'thereof', 'thought', 'thought-provoking', 'thrive', 'thriving',
    'throughput', 'thus', 'time', 'clarify', 'demonstrate', 'elucidate',
    'emphasize', 'exemplify', 'furnish', 'highlight', 'illustrate', 'provide',
    'reiterate', 'showcase', 'underscore', 'unleash', 'unlock', 'touchpoint',
    'transformative', 'transforming', 'ultimately', 'uncharted', 'undeniable',
    'underscores', 'unique', 'undoubtedly', 'unparalleled', 'uptime',
    'user', 'engagement', 'experience', 'feedback', 'interface', 'utilize',
    'utmost', 'valuable', 'value', 'proposition', 'value-added', 'various',
    'vast', 'vibrant', 'vital', 'well-crafted', 'whilst', 'true', 'widely',
    'recognized', 'keen']

ai_words = set(ai_words)

# Functions

# adding text

def add_text(text, added_text):

    text = text + added_text
    print(f'\n{text}')

    t.sleep(2)

    return text

# deleting text

def delete_text(text, text_to_delete, amt_of_deletions):

    text = re.sub(text_to_delete, "", text, count=int(amt_of_deletions), flags=re.I)

    print(f'\n{text}')

    t.sleep(2)

    return text

# replacing text

def replace_text(text_to_replace, text, replacement, amt_of_replacements):

    text = re.sub(text_to_replace, replacement, text, count=int(amt_of_replacements), flags=re.I)

    print(f'\n{text}')

    t.sleep(2)

    return text

# searching text

def search_text(text, search):

    
    text = text.lower()

    search = search.lower()

    result_amt = 0

    for i in text.splitlines():

      if re.search(search, i, re.I):

        result_amt += 1

        print(f"\n{i}")

    if not result_amt:

      print(f'\n0 results found for {search}.')

    else :

      print(f'\nThere has been {result_amt} results found for {search}.')

# flipping text

def flip_text(text):

  flipped = list(text)
  print("\nFlipped Text:")
  text = "".join(flipped[::-1])
  print(f'\n{text}')
  t.sleep(2)

  return text

def cipher_flow(cipher_choice, encode_decode, text): # Higher order function

    match cipher_choice.lower(), encode_decode.lower(): # Switch statement for function organization

        case "numeric", "encode":

            text = numeric_encode(text)

            return text

        case "numeric","decode":

            text = numeric_decode(text)

            return text

        case "caesar", "encode":

            try:

              user_amt = int(input("\nBy how much forward?: ")) # Encoding for Caesar Cipher
              text = caesar_encode(text, user_amt)
              return text

            except ValueError:

              print("\nNot a number, please enter a number.")

        case "caesar", "decode":

            try:

                user_amt = int(input("\nBy how much back?: ")) # Decoding for Caesar Cipher
                text = caesar_decode(text, user_amt)
                return text

            except ValueError:

                print("\nNot a number, please enter a number.")

        case _:

          print("Unsupported Cipher")


def numeric_encode(text): # Encoding for Numeric Cipher

    if re.search(r'[A-Za-z]', text):

        cipher_txt = ""

        for letter in list(text):

           if letter.isalpha():

              cipher_txt += letter_number[letter.upper()] + " "

           else:

              cipher_txt += letter

        text = cipher_txt

        print("\nHere is the encoded text!")

        print(f'\n{text}')

        t.sleep(2)

    else:

        print("\n🔠 There has been no letters in the text to encode 🔠.")

    return text

def numeric_decode(text): # Decoding for Numeric Cipher

    if re.search(r'[0-9]', text):

        cipher_txt = ""

        for num in text.split(" "):

            if num.isdigit():

                cipher_txt += number_letter[num]

            else:
                cipher_txt += num

        text = cipher_txt

        print("\nHere is the decoded text!")

        print(f'\n{text}')

        t.sleep(2)

    else:

      print("\n🔢 There has been no numbers in the text to decode 🔢.")

    return text



def caesar_encode(text, shift): # Encoding for Caesar Cipher

    if re.search(r'[A-Za-z]', text):

        list_txt = list(text)

        shift_txt = []

        for character in list_txt: # Iteration

          if character.isalpha(): # Checks if character is in alphabet

            index_var = letters.index(character.upper())

            if character.islower():

                # preserving lowercase letters

                shift_txt.append(letters[(index_var + int(shift)) % 26].lower())

            else:
                shift_txt.append(letters[(index_var + int(shift)) % 26])

          else:

            shift_txt.append(character)

        text = "".join(shift_txt)

        print("\nHere is the encoded text!")

        print(f'\n{text}')

        t.sleep(2)

    else:

        print("\n🔠 There has been no letters in the text to encode 🔠.")

    return text


def caesar_decode(text, shift): # Decoding for Caesar Cipher

    if re.search(r'[A-Za-z]', text):

        list_txt = list(text)

        shift_txt = []

        for character in list_txt: # Iteration

          if character.isalpha(): # Checks if character is in alphabet
            index_var = letters.index(character.upper())

            if character.islower():

                # preserving lowercase letters

                shift_txt.append(letters[(index_var - int(shift)) % 26].lower())

            else:

                shift_txt.append(letters[(index_var - int(shift)) % 26])

          else:
            shift_txt.append(character)

        text = "".join(shift_txt)

        print("\nHere is the decoded text!")

        print(f'\n{text}')

        t.sleep(2)

    else:

        print("\n🔠 There has been no letters in the text to decode 🔠.")

    return text

def random_text(text, length, entropy): # random text generation function

    rng_txt = ""

    for i in range(0, length):
      try:
          rng_txt += chr(randint(0, entropy))
      except ValueError:
          rng_txt += chr(randint(0, 1114111))

    text = text + rng_txt

    print(f"\n{text}")

    print("\nNote: Some Text may not show due to the environment this code is running in.")

    return text

# AI Scanning Function

def is_it_ai(text: str):

  text = text.lower()

  text = re.split(r'[^A-Za-z0-9—]+', text) # Generates lexical tokens/lexer

  ai_amt = 0

  for word in text:
    if word in ai_words: # AI detection
      ai_amt += 1

  # Percentage Calculations
  try:

    ai_percent = (ai_amt/len(text)) * 100

  except ZeroDivisionError: # Graceful error handling for certain inputs

    ai_percent = 0

  human_percent = 100 - ai_percent

  return [ai_percent, human_percent], ai_amt

def character_analysis(text):

  word_amt, number_amt, special_character_amt = 0, 0, 0

  for char in text.split(" "):
    if char.isalpha():
      word_amt += 1
    elif char.isdigit():
      number_amt += 1
    else:
      special_character_amt += 1

  return [word_amt, number_amt, special_character_amt], word_amt


# Ciphering

letter_number = {
    'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5',
    'F': '6', 'G': '7', 'H': '8', 'I': '9', 'J': '10',
    'K': '11', 'L': '12', 'M': '13', 'N': '14', 'O': '15',
    'P': '16', 'Q': '17', 'R': '18', 'S': '19', 'T': '20',
    'U': '21', 'V': '22', 'W': '23', 'X': '24', 'Y': '25',
    'Z': '26'
}

number_letter = {values: keys for keys, values in letter_number.items()}

 # Associative Array for Numeric Cipher

letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
] # Associative Array for Caesar Cipher

# Instructions

user_txt = None

split_pattern = r'["\'.]' # Regular Expression Pattern

try:

  user_command = input("Do you want to insert a file? 🗂 (y/n): ") # Command Line Interface/User Input

  if re.match(r'\A[Yy]$', user_command):

    user_txt = input("\nInsert file: ") ## File Insertion

    file_var = re.split(split_pattern, user_txt)

    found_path = ""

    for path, dirs, files in os.walk(os.getcwd()): ## Finds File
          if user_txt in files:
              found_path = os.path.join(path, user_txt)
              print(f"\n{found_path} is the file you inserted")

    if "txt" in file_var : # If file is .txt

      try:

        with open(found_path) as f:

          user_txt = f.read()
          print(f'\n{user_txt}')

      except FileNotFoundError:

          print("No file found 🗂")

    else:

          print("Unsupported File Type.")

  else:

    user_txt = input("\nWrite ✏️: ")

    print(f'\n{user_txt}')


  while True:

    print("\nControls ⚙️:")

    print("\nA - Add ➕")

    print("\nD - Delete ➖")

    print("\nR - Replace 🔄")

    print("\nS - Search 🔎")

    print("\nF - Flip 🔄")

    print("\nC - Cipher 🕵️‍♀️")

    print("\nRNG - Random ❓")

    print("\nStats - Statistics on Text 📊")

    print("\nE - Erase All 🗑️")

    print("\nQ - Quit Application 🛑")

  # Commands

    user_command = input("\nCommand: ")

    match user_command.lower():

      case "a": # Adding Text

        user_add = input("\nAdd: ")

        user_txt = add_text(user_txt, user_add)

      case "d": # Deleting Text

        user_delete = input("\nDelete: ")

        try:

          replace_count = input(f"\nHow many {user_delete}s do you want to delete? (0 for all) : ")

        except ValueError:

          replace_count = 0

        user_txt = delete_text(user_txt, user_delete, replace_count)

      case "r": # Replacing Text

        user_replaced = input("\nWhich text to Replace?: ")
        user_replacement = input("\nReplace with: ")

        try: 
          replace_count = input(f"\nHow many {user_replaced}s to replace? (0 for all): ")
        except ValueError:
          replace_count = 0

        user_txt = replace_text(user_replaced, user_txt, user_replacement, replace_count)

      case "s": # Searching Software

        user_search = input("\nSearch: ")

        search_text(user_txt, user_search)

      case "f":  # Flipping Text

        user_txt = flip_text(user_txt)

      case "c": # Cryptographic Algorithms

        user_cipher = input("\nPick Cipher (Numeric/Caesar): ")

        user_command = input("\nEncode or Decode?: ")

        user_txt = cipher_flow(user_cipher, user_command, user_txt)

      case "rng": # Random Text Generator

        try:

          user_length = int(input("\nHow many characters long should the text be?: "))
          user_range = int(input("\nHow random? (Type 100, for 1%, Type 100000 for 0.001%): "))
          user_txt = random_text(user_txt, user_length, user_range)

        except ValueError:

          print("\nNot a number, please type a number.")

      case "stats": # Stats on Text

        if len(user_txt.split(" ")) > 250: # Feature used for accuracy

          # AI Scanning

          scanner_percentages, ai_generated_words = is_it_ai(user_txt)

          scanner_labels = ["A.I", "Human"]

          scanner_colours = ["red", "blue"]

          myexplode = [0.2, 0]

          plt.pie(scanner_percentages, labels = scanner_labels, explode = myexplode, colors = scanner_colours)

          print(f"\nYour text is {round(scanner_percentages[0], 1)}% AI-generated and {round(scanner_percentages[1], 1)}% human.")

          print(f"\n{ai_generated_words} words in your text have been detected as AI.")

          plt.show()

          t.sleep(1.0)

        # Character Statistics (amt of words, numbers, special characters)

        [char_words, char_numbers, char_special], words = character_analysis(user_txt)

        char_labels = ["Words", "Numbers", "Special Characters"]

        char_colours = ["blue", "green", "yellow"]

        plt.pie([char_words, char_numbers, char_special], labels = char_labels, colors = char_colours)

        plt.show()

        print(f"\nThere are {words} words in your text")

        user_transcript = input("Do you want a transcript for your text (y/n)?: ")

        if re.match(r'\A[Yy]$', user_transcript): # Creating Dataframe (Text Transcript)

             print("\nText Transcript")

             transcript_df = pl.DataFrame({

                "Transcript": user_txt.split(" "),
                "Index": [i for i in range(0, len(user_txt.split(" ")))]

             })

             print(f"\n{transcript_df}")

             user_csv = input("\nDo you want a .csv file to save the transcript? (y/n)?: ")

             if re.match(r'\A[Yy]$', user_csv): # Saving transcript as .csv

                  user_csv = input("\nMake a name for the file (Don't worry the .csv is automatically done for you!): ")

                  transcript_df.write_csv(os.path.abspath(f'{user_csv}.csv'))

                  print("\nDone!")

      case "e": # Erasing Text

         user_txt = ""

      case "q": # Quitting Text


        user_create = input("Do you want a saved file for your text (y/n)?: ") #Saving file as .txt

        if re.match(r'\A[Yy]$', user_create):

            user_filename = input("Write name for file (Don't worry the .txt is automatically done for you!): ")

            try:

              with open(f'{user_filename}.txt', 'x') as f:

                f.write(user_txt)

            except FileExistsError:

              print("File already exists")

        print("\nClosing Application...")

        t.sleep(2)

        print("\nApplication CLosed")

        break

except KeyboardInterrupt:

      user_create = input("Do you want a saved file for your text (y/n)?: ") #Saving file as .txt

      if re.match(r'\A[Yy]$', user_create):

          user_filename = input("Write name for file (Don't worry the .txt is automatically done for you!): ")

          with open(f'{user_filename}.txt', 'x') as f:

            f.write(user_txt)

      print("\nClosing Application...")

      t.sleep(2)

      print("\nApplication Closed")
