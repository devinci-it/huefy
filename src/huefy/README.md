 
# Theme Class

The `Theme` class represents a collection of ANSI escape sequences stored as properties, allowing easy formatting of text with colors and styles in terminal applications.

## Attributes

- **`_theme_data`** (dict): Dictionary containing theme data with keys as ANSI escape sequence names (without 'ESC_' prefix).
- **`_esc_character`** (str): Character prefix for ANSI escape sequences.

## Methods

### `__init__(theme_data=None, esc_character='\033')`

Initializes a `Theme` object with the provided theme data dictionary and escape character.

#### Parameters

- **`theme_data`** (dict, optional): Dictionary containing theme data with keys as ANSI escape sequence names.
- **`esc_character`** (str, optional): Character prefix for ANSI escape sequences. Defaults to '\033'.

#### Exceptions

- **`ValueError`**: Raised if any theme data key contains invalid characters.

### `_validate_theme_data()`

Validates the theme data to ensure keys consist of uppercase letters and underscores only.

#### Exceptions

- **`ValueError`**: Raised if any theme data key contains invalid characters.

### `_create_static_methods()`

Dynamically creates static properties for each theme data key containing ANSI escape sequences.

### `_is_ansi_escape(value)`

Static method to check if a given value is a valid ANSI escape sequence.

#### Parameters

- **`value`** (str): Value to check.

#### Returns

- **`bool`**: True if the value is a valid ANSI escape sequence, False otherwise.

### `from_dict(theme_dict, esc_character='\033')`

Class method to create a `Theme` object from a dictionary of theme data.

#### Parameters

- **`theme_dict`** (dict): Dictionary containing theme data with keys as ANSI escape sequence names.
- **`esc_character`** (str, optional): Character prefix for ANSI escape sequences. Defaults to '\033'.

#### Returns

- **`Theme`**: Initialized `Theme` object with the provided theme data.

#### Exceptions

- **`ValueError`**: Raised if any theme data key contains invalid characters.

### `from_file(file_path, esc_character='\033')`

Class method to create a `Theme` object from a file containing theme data.

#### Parameters

- **`file_path`** (str): Path to the file containing theme data.
- **`esc_character`** (str, optional): Character prefix for ANSI escape sequences. Defaults to '\033'.

#### Returns

- **`Theme`**: Initialized `Theme` object with the theme data loaded from the file.

#### Exceptions

- **`ValueError`**: Raised if any theme data key contains invalid characters.
- **`IOError`**: Raised if the file cannot be read or does not exist.

### `list_theme_attributes()`

Returns a list of all theme attribute names currently defined in the `_theme_data`.

#### Returns

- **`list`**: List of theme attribute names.

### `paint(property_name, text, stringify=False, indent=0)`

Formats text with ANSI escape sequences based on provided parameters.

#### Parameters

- **`property_name`** (str): Name of the theme property to apply.
- **`text`** (str): Text to format with the theme property.
- **`stringify`** (bool, optional): If True, returns the formatted text as a string. Defaults to False.
- **`indent`** (int, optional): Number of spaces to indent the formatted text. Defaults to 0.

#### Returns

- **`str`** or **`None`**: If `stringify` is True, returns the formatted text as a string; otherwise, prints the formatted text directly.

---

## Sample Usage

```python
import os

 theme_data = {
    'ESC_RESET': '[0m',
    'ESC_BOLD': '[1m',
    'ESC_HIGHLIGHT': '[3m',
    'ESC_UNDERLINE': '[4m'
}

# Initialize Theme object
theme = Theme(theme_data)

# Load theme from a file
file_path = 'path/to/theme.txt'
theme_from_file = Theme.from_file(file_path)

# List all theme attributes
print(f"Theme attributes: {theme.list_theme_attributes()}")

# Format text with ANSI escape sequences
formatted_text = theme.paint('HIGHLIGHT', 'Highlighted text', stringify=True)
print(f"Formatted text: {formatted_text}")

# Demonstrate painting without stringify (prints directly)
theme.paint('UNDERLINE', 'Underlined text')

# Iterate through multiple themes
theme_directory = 'path/to/themes/directory'
theme_files = [f for f in os.listdir(theme_directory) if f.endswith('.theme')]

for theme_file in theme_files:
    theme_path = os.path.join(theme_directory, theme_file)
    theme = Theme.from_file(theme_path)

    # Apply theme to text
    theme.paint('BOLD', f"Applying theme from {theme_file}")
```

 