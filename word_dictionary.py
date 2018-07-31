import json
from difflib import get_close_matches

dict_data = json.load(open('data.json', 'r'))


# data is the entire database
# translate function
def translate(word):  # the word we want to search
    word = word.lower()
    if word in dict_data:  # word is key here
        return dict_data[word]

    elif word.title() in dict_data: # words beginning with first letter capitalised
        return dict_data[word.title()]

    elif word.upper() in dict_data: # for all upper case letters such as USA
        return dict_data[word.upper()]


    elif len(get_close_matches(word, dict_data.keys())) > 0:  # list object
        user_input = input(f'Did you mean {get_close_matches(word,dict_data.keys())[0]} instead ? Enter Yes or No ')
        # access the first element of that list using [0]
        if user_input == "Yes":  # pass the value again
            return dict_data[get_close_matches(word, dict_data.keys())[0]]
        elif user_input == "No":

         input1 = input(f'Did you mean {get_close_matches(word,dict_data.keys())[1]} instead ? Enter Yes or No ')
         if input1 == "Yes":
             return dict_data[get_close_matches(word, dict_data.keys())[1]]
        else:
            return "Sorry, try again later!"

    else:
        return "Word not found! Please enter a correct spelling"


word_input = input("enter word:   ")

#print(translate(word_input))
definition = translate(word_input)

# only show the text, not the list, show one definition per line
if type(definition) == list: #checking if it is a list and convert to string
    print('\n'.join([str(item) for item in definition]))
else:
    print(definition)





