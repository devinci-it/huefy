
import hashlib
import logging
import json
import pkg_resources
from huefy.theme import Theme  # Assuming Theme class is in src folder

class ThemeManager:
    """
    A class to manage and validate themes for the Hue application.

    Attributes:
        config (dict): Configuration loaded from 'hue.config'.
        default_theme (str): Default theme name.
        themes_dir (str): Directory where theme files are stored.
        manifest_file (str): Name of the manifest file listing theme hashes.
        log_file (str): Path to the log file for logging theme management activities.
        theme_file (str): Currently selected theme file path.

    Methods:
        __init__():
            Initializes a ThemeManager instance, loading configuration from 'hue.config'.

        load_config():
            Loads configuration settings from 'hue.config' file.

        validate_theme(theme_file=None):
            Validates the specified theme file against its hash in the manifest.

        setup_logging():
            Sets up logging configuration to log theme management activities.

        log_message(message):
            Logs a message to the log file.

        get_theme_instance(theme_file=None):
            Loads and returns a Theme instance based on configuration or specified theme file.

    Usage Example:
        theme_manager = ThemeManager()
        theme_manager.setup_logging()
        theme = theme_manager.get_theme_instance()
        if theme:
            print(f"Loaded theme: {theme.list_theme_attributes()}")

    """
    def __init__(self):
        """
        Initializes a ThemeManager instance by loading configuration settings.
        """
        self.config = self.load_config()
        self.default_theme = self.config.get('default_theme', 'monokai')
        self.themes_dir = self.config.get('themes_dir', 'themes.d')
        self.manifest_file = self.config.get('manifest_file', 'MANIFEST')
        self.log_file = self.config.get('log_file', 'theme.log')
        self.theme_file = None

    def load_config(self):
        """
        Load configuration from 'hue.config' file.

        Returns:
        dict: Configuration settings loaded from the file.
        """
        config = {}
        try:
            with pkg_resources.resource_stream('huefy', 'hue.config') as config_file:
                config = json.load(config_file)
        except IOError as e:
            print(f"Error reading config file: {e}")
        return config

    def validate_theme(self, theme_file=None):
        """
        Validate the theme by comparing its hash with the hash in the MANIFEST file.

        Args:
        theme_file (str): Optional. Path to the theme file to validate.

        Returns:
        bool: True if the theme is valid, False otherwise.
        """
        if not theme_file:
            theme_file = pkg_resources.resource_filename('huefy', f'themes.d/{self.default_theme}')

        manifest_path = pkg_resources.resource_filename('huefy', f'themes.d/{self.manifest_file}')
        if not pkg_resources.resource_exists('huefy', theme_file):
            print(f"Theme file {theme_file} does not exist.")
            return False

        try:
            with pkg_resources.resource_stream('huefy', self.manifest_file) as manifest:
                for line in manifest:
                    if line.strip():
                        manifest_theme_file, expected_hash = line.split()
                        manifest_theme_file = pkg_resources.resource_filename('huefy', f'themes.d/{manifest_theme_file}')
                        if theme_file == manifest_theme_file:
                            with pkg_resources.resource_stream('huefy', theme_file) as theme:
                                actual_hash = hashlib.sha256(theme.read()).hexdigest()
                                if actual_hash != expected_hash:
                                    print(f"Theme {theme_file} does not match expected hash.")
                                    return False
                            return True
                print(f"Theme file {theme_file} not found in MANIFEST.")
                return False
        except IOError as e:
            print(f"Error reading MANIFEST file: {e}")
            return False

    def setup_logging(self):
        """
        Setup logging configuration to log theme management activities.
        """
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def log_message(self, message):
        """
        Log a message to the log file.

        Args:
        message (str): Message to log.
        """
        logging.info(message)

    def get_theme_instance(self, theme_file=None):
        """
        Load and return a Theme instance based on configuration or a specified theme file.

        Args:
        theme_file (str): Optional. Path to the theme file to load.

        Returns:
        Theme: Initialized Theme object with the loaded theme data.
        """
        if not theme_file:
            theme_file = pkg_resources.resource_filename('huefy', f'themes.d/{self.default_theme}')

        theme = Theme.from_file(theme_file)
        if theme:
            self.log_message(f"Loaded theme from file: {theme_file}")
        return theme
