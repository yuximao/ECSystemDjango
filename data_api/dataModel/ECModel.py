import string
import joblib
import nltk

nltk.download('punkt')  # delete this if you already have it

def get_tokens(text):
    lower = text.lower()
    remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
    no_punctuation = lower.translate(remove_punctuation_map)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

def read_test(file):
    text=[]
    iter_f = iter(file)
    strs = ""
    for line in iter_f:  # loop the files and get the text
        strs = strs + str(line)
    strs_list = get_tokens(strs)
    final_str = ""
    for s in strs_list:  # loop and save the token
        final_str = final_str + s
        final_str = final_str + " "
    text.append(final_str)  # save the final result to the list
    return text


def ecModel(path):

    test_content = read_test(path)

    text_clf = joblib.load('data_api/dataModel/data.pkl')
    predicted = text_clf.predict(test_content)
    return predicted

def get_label(x):
    return {
        '0': 'alt.atheism',
        '1': 'comp.graphics',
        '2': 'comp.os.ms-windows.misc',
        '3': 'comp.sys.ibm.pc.hardware',
        '4': 'comp.sys.mac.hardware',
        '5': 'comp.windows.x',
        '6': 'misc.forsale',
        '7': 'rec.autos',
        '8': 'rec.motorcycles',
        '9': 'rec.sport.baseball',
        '10': 'rec.sport.hockey',
        '11': 'sci.crypt',
        '12': 'sci.electronics',
        '13': 'sci.med',
        '14': 'sci.space',
        '15': 'soc.religion.christian',
        '16': 'talk.politics.guns',
        '17': 'talk.politics.mideast',
        '18': 'talk.politics.misc',
        '19': 'talk.religion.misc'
    }.get(x, 'not in classification')
