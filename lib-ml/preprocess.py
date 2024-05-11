from .encode_labels import encode_labels
from .tokenize_features import tokenize_features
from .data_split import load_and_split_data

def preprocess_data(data):
    """
    Processes the input data through various stages including splitting data,
    tokenizing features, and encoding labels.
    
    Args:
    data (list of str): Raw data lines where each line contains a label and a feature separated by a tab.
    
    Returns:
    tuple: Tuple containing:
        - x (numpy.array): Tokenized and padded feature data.
        - y (numpy.array): Encoded label data.
    """

    # Split data into raw features and labels
    features, labels = load_and_split_data(data)

    # Tokenize features
    x = tokenize_features(features)  # Assuming this function has been adjusted to work with list of features directly

    # Encode labels
    y = encode_labels(labels)  # Assuming this function has been adjusted to work with list of labels directly

    return x, y