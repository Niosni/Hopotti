def generate_weirdness(prompt):
    return """Answer the following question with just a weird answer like the following:
    Question: What is 2+2?
    Answer: Not over 10
    Question: What is the capital of Finland?
    Answer: Turku, or some other finnish city.
    Question: What is water?
    Answer: It's a combination of some stuff. Not dry.
    Question: {}?
    Answer:""".format(prompt)

def generate_haiku(prompt):
    return """Answer the following question with a haiku
    Question: {}?
    Answer:""".format(prompt)

def generate_story(prompt):
    return """Generate a very short story about {}""".format(prompt)

def generate_howitsmade(prompt):
    return """Question: Can you tell me about the production and how {} is made? Answer:""".format(prompt)