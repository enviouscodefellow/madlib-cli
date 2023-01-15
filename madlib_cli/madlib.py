import re

def read_template(path="assets/dark_and_stormy_night_template.txt"):
    try:
        with open(path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Invalid filepath.  The file {path} could not be found.")

def parse_template(text):
    placeholders = re.findall(r"\{(.*?)\}", text)
    stripped_text = re.sub(r"\{(.*?)\}", "{}", text)
    # print(stripped_text,placeholders)
    return stripped_text, tuple(placeholders)

def user_inputs(placeholders):
    user_inputs = []
    for placeholder in placeholders:
        user_input = input(f"Enter a {placeholder}: ")
        user_inputs.append(user_input)
    return user_inputs

def merge(stripped_text, user_inputs):
    completed_madlib = stripped_text.format(*user_inputs)
    with open("completed_madlib.txt", "w") as file:
        file.write(completed_madlib)
    return print(completed_madlib)

class FileNotFoundError(Exception):
  pass

# stripped_text, placeholders = parse_template(read_template("assets/make_me_a_video_game_template.txt"))
stripped_text, placeholders = parse_template(read_template())
merge(stripped_text, user_inputs(placeholders))
