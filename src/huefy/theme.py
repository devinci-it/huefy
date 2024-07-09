import re
import os

class Theme:
    """
    Represents a theme with ANSI escape sequences stored as properties.
    
    Attributes:
    _theme_data (dict): Dictionary containing theme data with keys as ANSI escape sequence names (without 'ESC_' prefix).
    _esc_character (str): Character prefix for ANSI escape sequences.
    
    Methods:
    __init__(theme_data=None, esc_character='\033'):
        Initializes a Theme object with the provided theme data dictionary and escape character.
    
    _validate_theme_data():
        Validates the theme data to ensure keys consist of uppercase letters and underscores only.
    
    _create_static_methods():
        Dynamically creates static properties for each theme data key containing ANSI escape sequences.
    
    _is_ansi_escape(value):
        Static method to check if a given value is a valid ANSI escape sequence.
    
    from_dict(theme_dict):
        Class method to create a Theme object from a dictionary of theme data.
    
    from_file(file_path, esc_character='\033'):
        Class method to create a Theme object from a file containing theme data.
    
    format_text(property_name, text, stringify=False, justify='left', min_width=None, max_width=None, indent=0):
        Formats text with ANSI escape sequences based on provided parameters.
    
    list_theme_attributes():
        Returns a list of all theme attribute names currently defined in the _theme_data.
    """
    default_theme_data = {
        'ESC_RESET': '[0m',
        'ESC_BOLD': '[1m',
        'ESC_HIGHLIGHT': '[3m',
        'ESC_UNDERLINE': '[4m'
    }
    def __init__(self, theme_data=None, esc_character='\033'):
        """
        Initializes a Theme object with the provided theme data dictionary and escape character.
        
        Args:
        theme_data (dict, optional): Dictionary containing theme data with keys as ANSI escape sequence names (without 'ESC_' prefix).
        esc_character (str, optional): Character prefix for ANSI escape sequences. Defaults to '\033'.
        
        Raises:
        ValueError: If any theme data key contains invalid characters.
        """
        self._theme_data = theme_data or {}
        self._esc_character = esc_character
        self._theme_data.update(self.default_theme_data)  # Merge with default theme data
        if theme_data:
            self._validate_theme_data()  # Validate theme data on initialization
            self._create_static_methods() # Create static methods for theme data properties

    def _validate_theme_data(self):
        """
        Validates the theme data to ensure keys consist of uppercase letters and underscores only.
        
        Raises:
        ValueError: If any theme data key contains invalid characters.
        """
        valid_keys = re.compile(r'^[A-Z_]+$')
        for key in self._theme_data:
            if not valid_keys.match(key):
                raise ValueError(f"Invalid theme key: {key}. Key must consist of uppercase letters and underscores only.")

    def _create_static_methods(self):
        """
        Dynamically creates static properties for each theme data key containing ANSI escape sequences.
        """
        for key, value in self._theme_data.items():
            key = key.replace('ESC_', '')
            setattr(self, key.lower(), self._esc_character + value)

    @staticmethod
    def _is_ansi_escape(value):
        """
        Static method to check if a given value is a valid ANSI escape sequence.
        
        Args:
        value (str): Value to check.
        
        Returns:
        bool: True if the value is a valid ANSI escape sequence, False otherwise.
        """
        ansi_pattern = re.compile(r'\033\[\d+(;\d+)*m')
        return bool(ansi_pattern.match(value))

    @classmethod
    def from_dict(cls, theme_dict, esc_character='\033'):
        """
        Class method to create a Theme object from a dictionary of theme data.
        
        Args:
        theme_dict (dict): Dictionary containing theme data with keys as ANSI escape sequence names (without 'ESC_' prefix).
        esc_character (str, optional): Character prefix for ANSI escape sequences. Defaults to '\033'.
        
        Returns:
        Theme: Initialized Theme object with the provided theme data.
        
        Raises:
        ValueError: If any theme data key contains invalid characters.
        """
        return cls(theme_dict, esc_character)

    @classmethod
    def from_file(cls, file_path, esc_character='\033'):
        """
        Class method to create a Theme object from a file containing theme data.
        
        Args:
        file_path (str): Path to the file containing theme data.
        esc_character (str, optional): Character prefix for ANSI escape sequences. Defaults to '\033'.
        
        Returns:
        Theme: Initialized Theme object with the theme data loaded from the file.
        
        Raises:
        ValueError: If any theme data key contains invalid characters.
        IOError: If the file cannot be read or does not exist.
        """
        try:
            with open(file_path, 'r') as file:
                theme_dict = {key.strip(): value.strip() for line in file
                              if line.strip() and not line.startswith("#")
                              for key, value in [line.strip().split('=')]}
            return cls(theme_dict, esc_character)
        except IOError as e:
            raise IOError(f"Error reading file {file_path}: {e}")

    def list_theme_attributes(self):
        """
        Returns a list of all theme attribute names currently defined in the _theme_data.
        
        Returns:
        list: List of theme attribute names.
        """
        return list(self._theme_data.keys())
    


    @staticmethod
    def paint (theme, property_name, text:str, stringify=False, indent=0):
        """
        Returns a string with the text colored according to the hue value.
        
        Args:
        theme (Theme): The theme object containing the ANSI escape sequences.
        text (str): The text to color.
        hue (int): The hue value to determine the color.
        
        Returns:
        str: The colored text string.
        """
        reset_sequence = "\033[0m"

        # Check if the theme object has the specified property
        if hasattr(theme, property_name):
            attribute = getattr(theme, property_name)
        else:
            attribute = theme.reset

        # Indentation setup
        indent_spaces = ' ' * indent if indent else ''

        # Construct the formatted text with attribute and reset
        formatted_text = f"{reset_sequence}{attribute}{indent_spaces}{text}{reset_sequence}"

        # Optionally return or print the formatted text
        if stringify:
            return formatted_text
        else:
            print(formatted_text)

    

if __name__ == "__main__":
    # Directory containing theme files
    script_dir = os.path.dirname(os.path.abspath(__file__))

    theme_directory = os.path.join(script_dir,"../themes.d/")

    # List all .theme files in the directory
    theme_files = [f for f in os.listdir(theme_directory) if f.endswith('.theme')]

    # Loop through each theme file
    for theme_file in theme_files:
        theme_path = os.path.join(theme_directory, theme_file)
        theme = Theme().from_file(theme_path)

        # Demonstrate usage
        print(f"""
        Demo of theme file: {theme_file}
        Initialize the Theme class using data from {theme_file}.
        """)


        # Demonstrate custom method huefy
        attributes = [each.replace("ESC_", "").lower() for each in theme.list_theme_attributes()]
        print("\nDemonstrating custom method 'huefy':")
        for attribute in attributes:
            theme.paint(theme, attribute, f"This is a test {attribute} string")

        # List all theme attributes
        print("\n\tList of theme attributes:", theme.list_theme_attributes())
 