 
 Theme Manager for Scripts

The Theme Manager script facilitates easy management and validation of themes for your scripts, particularly focusing on the `themes.d` directory configuration and usage of the `Theme` object.

## Configuration

### themes.d Directory

The `themes.d` directory serves as the repository for your theme files. By default, the Theme Manager looks for theme files in this directory unless specified otherwise.

### Configuration File (hue.config)

The configuration file `hue.config` stores essential settings for the Theme Manager, including:

- `default_theme`: Specifies the default theme to load if none is specified explicitly.
- `themes_dir`: Defines the directory where theme files (`*.theme`) are stored.
- `manifest_file`: Indicates the file (`MANIFEST`) containing theme hashes for validation.
- `log_file`: Path to the log file (`theme.log`) for recording theme management activities.

Ensure `hue.config` is correctly configured to align with your environment and requirements.

## Usage

### Importing the Theme Object

To utilize themes in your script, import the `Theme` object from the `src` module:

```python
from src import Theme
```

### Managing Themes

#### Loading a Theme

You can load a theme using its file name or the default theme specified in `hue.config`:

```python
theme_manager = ThemeManager()
theme = theme_manager.get_theme_instance('my_theme.theme')  # Load specific theme
```

#### Validating a Theme

Validate a theme against its hash in the manifest file to ensure integrity:

```python
theme_manager = ThemeManager()
valid = theme_manager.validate_theme('my_theme.theme')  # Validate specific theme
```

### Useful Tidbits

- **Dynamic Theme Loading**: Themes are dynamically loaded and can be swapped during runtime based on your application's needs.
- **Logging**: The Theme Manager logs activities to `theme.log`, providing visibility into theme loading and validation operations.
- **Extensibility**: Customize `hue.config` and extend the `Theme` class as per your project's thematic requirements.

## Example

```python
hue import ThemeManager


# Initialize ThemeManager instance
theme_manager = ThemeManager()
theme_manager.setup_logging()

# Load and validate a specific theme
theme = theme_manager.get_theme_instance('my_theme.theme')
if theme:
    print(f"Loaded theme: {theme.list_theme_attributes()}")

# Validate the loaded theme
valid = theme_manager.validate_theme('my_theme.theme')
if valid:
    print("Theme validated successfully.")
else:
    print("Failed to validate theme.")
```
