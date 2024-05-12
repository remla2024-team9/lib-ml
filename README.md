# lib-ml
Contains the pre-processing logic for data that is used for training or queries.

## Release

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

The last action will trigger the automated release workflow. The workflow will create a new release with the version number.