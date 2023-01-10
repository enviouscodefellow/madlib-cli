print("Welcome to the Madlib!  You will be prompted to select words to complete a story.  Have fun!")

def read_template(path="assets/make_me_a_video_game_template.txt"):
  try:
    with open(path, 'r') as file:
      return file.read()
  except FileNotFoundError:
    raise FileNotFoundError("Invalid filepath.  The file could not be found.")

  # text = read_template()
  # print(text)


def parse_template(text):
  actual_parts = []
  actual_stripped = ""
  start = 0
  while True:
    start = text.find("{", start)
    if start == -1:
      actual_stripped += text[start:]
      break
    actual_stripped += text[start:]
    end = text.find("}", start)
    actual_parts.append(text[start+1:end])
    start = end + 1
  actual_stripped = text
  for each in actual_parts:
    actual_stripped = actual_stripped.replace(each,"")
    print(actual_parts)
    print(actual_stripped)
  return actual_stripped, tuple(actual_parts)


def user_inputs(text):
  user_inputs = []

  for placeholder in parse_template(read_template(text)):
    user_input = input(f"Enter a {placeholder}: ")
    user_inputs.append(user_input)
  return user_inputs


def merge(actual_stripped, user_inputs):
  completed_madlib = actual_stripped
  for i, input in enumerate(user_inputs):
    completed_madlib = completed_madlib.replace("{}", user_inputs[i], 1)

  print(completed_madlib)

  with open("completed_madlib.txt", "w") as file:
    file.write(completed_madlib)
  return completed_madlib


# merge(parse_template(read_template()),user_inputs(parse_template(read_template())))



