# vdict
A dictionary (like websters, not key/value) for use in Python and Javascript / Node
This dictionary will be in JSON format, with the word, part of speech, pronunciation,
etymology, and definition(s).

vdict-creator.py
The python file to parse and convert the free Websters dictionary
available from Project Gutenberg (https://www.gutenberg.org/ebooks/29765).

sample.txt
A small excerpt from the Websters Dictionary for testing and development before attempting
to parse the whole thing.

vdict.js
The file created by vdict-creator.py. Will probably create both a .py and a .js file
later including methods for all the dictionary stuff you might want to do 
(for Node 'require' and Python 'import')

To-Do's:
- figure out why I'm getting \u00e4 in my results and resolve it
- improve definition parsing (some words are not getting their defs read/created)

Dictionary is Complete To-Do's
- include thesaurus info - synonyms/antonyms
- manually check for errors (no definition, etc) Ouch.
- separate into python importable and node requirable with methods.

Dictionary Stuff
isWord - does the word exist in the dictionary?
getPromunciation - get pronunciation of the word
getPartOfSpeech - return if the word is a noun, verb, etc.
getSynonyms - return synonym list
getAntonyms - return list of antonyms

