# Mad Libs Generator
# Import Modules
import random
import copy
# Create Story
story = (
    "My name is {} and I am {} years old. \n"+
    "If I were president, I would do a whole bunch of {} things. \n"+
    "1. I would drive the biggest {} car in the country. And that car would go faster than any other {} in the world. \n"+
    "2. Everyone would eat {} for dinner. \n"+
    "3. I would live in {} and build a {} there. \n"+
    "4. I would wear a {} on my head and every one would say I look {} like {}. \n"+
    "5. School would be open only {} days a year. \n"+
    "6. I would give my friends the best jobs. I would nominate {} for vice {}."
)
# Create Word Dictionary
word_dict = {
    'name':["Steve","Tony","Hulk","Hawk Eye"],
    'number':[25,38,55,41],
    'adjective':["cool","funny","big","beautiful"],
    'color':["blue","red","white","black"],
    'noun':["car","cycle","aeroplane","motor cycle"],
    'food':["burger","pizza","momo","biriyani"],
    'city':["London","New York","Toronto","New Delhi"],
    'structure':["statue","building","pool","bridge"],
    'clothing':["hat","shirt","trouser","t shirt"],
    'celebrity':["Chris Evans","Di Caprio","Shahrukh Khan","Brad Pitt"],
    'friend':["Mark","Elon","Sundar","Satya"],
    'position':["president","secreatary","accountant","defence secreatary"]
}
# Create function to get random words
def get_word(type,temp_dict):
    words = temp_dict[type]
    index = random.randint(0, 3)
    words = words[index]
    return words
# Create function to create the whole story
def create_story():
    temp_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('name', temp_dict),
        get_word('number', temp_dict),
        get_word('adjective', temp_dict),
        get_word('color', temp_dict),
        get_word('noun', temp_dict),
        get_word('food', temp_dict),
        get_word('city', temp_dict),
        get_word('structure', temp_dict),
        get_word('clothing', temp_dict),
        get_word('adjective', temp_dict),
        get_word('celebrity', temp_dict),
        get_word('number', temp_dict),
        get_word('friend', temp_dict),
        get_word('position', temp_dict),
        )
# Print the story
print("Mad Libs Story")
print(create_story())