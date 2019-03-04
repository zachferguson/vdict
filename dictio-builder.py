#-------------------------------------------------------------------------------
# Name:        dictionary cleaner
# Purpose:
#
# Author:      Ferguson
#
# Created:     24/02/2019
# Copyright:   (c) Ferguson 2019
# Licence:     <completely open>
#-------------------------------------------------------------------------------
import json

def find_entry(line):  # 
    stripped = line.rstrip('\n')
    separators = ["-", ";", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    chars = list(stripped)
    result = True
    for char in chars:
        if char not in separators and char.isalpha is False or char.isalpha() and char.isupper() is False:
            result = False
    passes = 0;
    for char in chars:
        if char in separators:
            passes += 1
    if passes == len(chars) - 1:
        result = False
    if len(line) == 0:
        result = False
    return result


def subdivide_contents(body):  # cut up the contents of each word entry and return a dictionary
    r_dict = {}
    r_dict["pronunciation"] = body[0:body.find(',')]
    if body.find("Etym") != -1:
        r_dict["partofspeech"] = body[body.find(',')+1:body.find("Etym")]
        r_dict["etymology"] = body[body.find("[")+1:body.find("]")]
    else:
        if body.find("Defn") != -1:
            r_dict["partofspeech"] = body[body.find(',')+1:body.find("Defn")]
        else:
            r_dict["partofspeech"] = body[body.find(',')+1:body.find("1")]

    # divide definition(s)
    definition = {}
    def_locations = []
    if body.find("1") != -1:
        i = 0
        while i < len(body):
            if body[i].isdigit():
                # append character, index
                def_locations.append([body[i], i])
            i += 1
        z = 0
        while z < len(def_locations):
            if z+1 < len(def_locations):
                definition[def_locations[z][0]] = body[def_locations[z][1]+3:def_locations[z+1][1]]
            else:
                definition[def_locations[z][0]] = body[def_locations[z][1]+3:]
            z += 1
        r_dict["definition"] = definition
    return r_dict
    

def make_dictionary (filename):  # primary function: parse Websters dict., save result as a Python/JSON dict.
    try:  # try to open the Websters dictionary text file
        print("opening " + filename + ".txt")
        file = filename + ".txt, encoding = 'utf-8'"
        dict = open('sample.txt', encoding = 'utf-8')
        js = open("dictio.js", "w")
        tempdict = dict.readlines()
        words = []
        toJSON = {}
        for item in tempdict:  # parse lines in Websters, create list of word entries
            check = item.rstrip('\n')
            if not check or len(check):
                pass
            if find_entry(check) is True:
                words.append(check)
        word = "A"
        contents = ""
        for item in tempdict:  # parse Websters, add lines to appropriate word key/value  in python dict.
            if item.rstrip('\n') in words:  # if line is in words, create a key for that word
                if item[0] == word[0] and word[-1] > item[-1] or item[0] > word[0]:
                    toJSON[word] = {'word': word}
                    remaining = subdivide_contents(contents)  # break up word entry into keys/values (pronunciation, etc)
                    for category in remaining:
                        toJSON[word][category] = remaining[category]  # add keys/values to word entry in python dict.
                word = ""
                contents = ""
                word = item.rstrip('\n')
            else:
                contents += item.rstrip('\n') + " "

        json.dump(toJSON, js, indent=2)
        #js.write(json.dumps(toJSON));  # write the completed python dict as JSON to a js file
        # ------------------------------------------ for testing only
        for item in toJSON:
            print(item)
            print('-------------------------------')
        # ----------------------------------------- end testing
    finally:
        dict.close()
        js.close()
        print('complete')

# pg29765 is full dictionary filename
make_dictionary("sample")

