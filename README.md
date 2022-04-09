Django auto-completions for Xonsh shell


## Installation

To install use pip:

```bash
xpip install xontrib-django
# or: xpip install -U git+https://github.com/jnoortheen/xontrib-django
```

## Usage

```bash
xontrib load django
```

## Releasing your package

- Bump the version of your package.
- Create a GitHub release (The release notes are automatically generated as a draft release after each push).
- And publish with `poetry publish --build` or `twine`
