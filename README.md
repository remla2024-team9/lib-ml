# lib-ml
* Contains the pre-processing logic for data that is used for training or queries.
* The library is versioned automatically, by picking-up on the corresponding Git version tag.
* A workflow is used to automatically release the library to the PyPi package registry.

## Adding the package to your project

The package is available on [PyPi](https://pypi.org/project/remla2024-team9-lib-ml/).

If you are using `pip`:
```bash
pip install remla2024-team9-lib-ml
```

If you are using `poetry`:
```bash
poetry add remla2024-team9-lib-ml
```

## Usage

### Load and Split Data

```python
from remla2024_team9_lib_ml.data_split import load_and_split_data

# Example data input
data = [
    "Label1\tFeature1",
    "Label2\tFeature2",
    "Label3\tFeature3"
]

features, labels = load_and_split_data(data)
```

### Encode Labels

```python
from remla2024_team9_lib_ml.encode_labels import encode_labels

# Example lists of labels
train_labels = ['cat', 'dog', 'mouse']
val_labels = ['cat', 'dog']
test_labels = ['mouse', 'dog']

# Encoding the labels
train_labels_encoded, val_labels_encoded, test_labels_encoded = encode_labels(train_labels, val_labels, test_labels)

# Outputs will be numpy arrays of encoded labels
print("Encoded Train Labels:", train_labels_encoded)
print("Encoded Validation Labels:", val_labels_encoded)
print("Encoded Test Labels:", test_labels_encoded)
```

### Tokenize Features

```python
from remla2024_team9_lib_ml.tokenize_features import tokenize_features

# Example lists of feature data (textual)
train_features = ["hello world", "hello there", "hello everyone"]
val_features = ["hello again", "hello hello"]
test_features = ["hello there", "world hello"]

# Tokenize and pad the features, specifying the desired sequence length
sequence_length = 50  # This can be adjusted based on your model's requirements
x_train, x_val, x_test, tokenizer = tokenize_features(
    train_features, val_features, test_features, sequence_length=sequence_length
)

# Outputs will be numpy arrays of tokenized features, and the tokenizer used
print("Tokenized Train Features:", x_train)
print("Tokenized Validation Features:", x_val)
print("Tokenized Test Features:", x_test)
print("Tokenizer Details:", tokenizer)
```

### Tokenize URL

```python
from remla2024_team9_lib_ml.tokenize_url import tokenize_url

# Example URL
url = "https://www.google.com"

# Assuming the tokenizer has been fit already during the training stage
sequence_length = 200  # This can be adjusted depending on your specific requirements
tokenized_url = tokenize_url(tokenizer, url, sequence_length)

# Output will be a numpy array containing the tokenized URL
print("Tokenized URL:", tokenized_url)
```

## Triggering a new release

1. Update the version number in `pyproject.toml`.

Either set the specific version number:
```bash
poetry version A.B.C
```

Or you can also use version increment rules:
```bash
poetry version patch # A.B.C -> A.B.(C+1)
poetry version minor # A.B.C -> A.(B+1).0
poetry version major # A.B.C -> (A+1).0.0
```

2. Add, commit, and push the change.
```bash
git add pyproject.toml
git commit -m "updated version number"
git push
```

3. Create a new tag with the version number.
```bash
git tag vA.B.C
```

4. Push the tag.
```bash
git push origin vA.B.C
```

The last action will trigger the automated release workflow.

## Implementation Details

* To publish to PyPi, we created an API Token and added it to the GitHub repository secrets.
* The token is stored in the `PYPI_API_TOKEN` secret, and is used in the release workflow.
* The release worfklow **FAILS** if you do not set the `pyproject.toml` version number to be the same as the tag version number.