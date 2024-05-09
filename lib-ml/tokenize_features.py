import pickle

import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(lower=True, char_level=True, oov_token='-n-')

def tokenize_features(train_path, val_path, test_path, train_save_path, val_save_path, test_save_path):
    # Load url data
    with open(train_path, 'r', encoding="utf-8") as file:
        train_features = file.readlines()

    with open(val_path, 'r', encoding="utf-8") as file:
        val_features = file.readlines()

    with open(test_path, 'r', encoding="utf-8") as file:
        test_features = file.readlines()

    tokenizer.fit_on_texts(train_features + val_features + test_features)

    # Tokenize and pad sequences
    x_train = pad_sequences(tokenizer.texts_to_sequences(train_features), maxlen=200)
    x_val = pad_sequences(tokenizer.texts_to_sequences(val_features), maxlen=200)
    x_test = pad_sequences(tokenizer.texts_to_sequences(test_features), maxlen=200)

    # Save tokenized data
    np.savetxt(train_save_path, x_train, fmt='%d')
    np.savetxt(val_save_path, x_val, fmt='%d')
    np.savetxt(test_save_path, x_test, fmt='%d')


def tokenize_url(url: str):
    """
    Tokenizes the given url and returns it. load_tokenizer must be called before calling this function
    """
    return pad_sequences(tokenizer.texts_to_sequences([url]), maxlens=200)


def load_tokenizer(path):
    """
    Loads the tokenizer object at the given path.
    """
    global tokenizer
    with open(path, 'rb') as file:
        tokenizer = pickle.load(file)


def save_tokenizer(path):
    """
    Saves the tokenizer to `path`. tokenize_features() must be called
    before calling this function
    """
    with open(path, 'wb', encoding="utf-8") as file:
        pickle.dump(tokenizer, file)    