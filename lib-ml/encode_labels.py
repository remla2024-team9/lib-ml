import numpy as np
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

def encode_labels(train_labels_path, val_labels_path, test_labels_path, train_save_path, val_save_path, test_save_path):
    """
    Encodes labels from separate files using sklearn LabelEncoder,
    saves the encoded labels on the given paths
    """

    # Load label data
    with open(train_labels_path, 'r', encoding="utf-8") as file:
        train_labels = file.readlines()

    with open(val_labels_path, 'r', encoding="utf-8") as file:
        val_labels = file.readlines()

    with open(test_labels_path, 'r', encoding="utf-8") as file:
        test_labels = file.readlines()


    train_labels = encoder.fit_transform([label.strip() for label in train_labels])
    val_labels = encoder.transform([label.strip() for label in val_labels])
    test_labels = encoder.transform([label.strip() for label in test_labels]) 

    # Save encoded labels
    np.savetxt(train_save_path, train_labels, fmt='%d')
    np.savetxt(val_save_path, val_labels, fmt='%d')
    np.savetxt(test_labels_path, test_labels, fmt='%d')

