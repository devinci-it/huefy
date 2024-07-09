import os
import hashlib
import logging
import argparse
import json
from src import Theme  

class ThemeManager:
    def __init__(self):
        self.config = self.load_config()
        self.default_theme = self.config.get('default_theme', 'monokai')
        self.themes_dir = self.config.get('themes_dir', 'themes.d')
        self.manifest_file = self.config.get('manifest_file', 'MANIFEST')
        self.log_file = self.config.get('log_file', 'theme.log')
        self.theme_file = None

    def load_config(self):
        """
        Load configuration from hue.config file.
        """
        config = {}
        try:
            with open('hue.config', 'r') as config_file:
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
            theme_file = os.path.join(self.themes_dir, self.default_theme)

        manifest_path = os.path.join(self.themes_dir, self.manifest_file)
        if not os.path.exists(theme_file):
            print(f"Theme file {theme_file} does not exist.")
            return False

        try:
            with open(manifest_path, 'r') as manifest:
                for line in manifest:
                    if line.strip():
                        manifest_theme_file, expected_hash = line.split()
                        manifest_theme_file = os.path.join(self.themes_dir, manifest_theme_file)
                        if theme_file == manifest_theme_file:
                            with open(theme_file, 'rb') as theme:
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
        Setup logging configuration.
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
        Load and return the Theme instance based on configuration or a specified theme file.

        Args:
        theme_file (str): Optional. Path to the theme file to load.

        Returns:
        Theme: Initialized Theme object with the loaded theme data.
        """
        if not theme_file:
            theme_file = os.path.join(self.themes_dir, self.default_theme)

        theme = Theme.from_file(theme_file)
        if theme:
            self.log_message(f"Loaded theme from file: {theme_file}")
        return theme

# Function to handle command line arguments
def handle_arguments():
    parser = argparse.ArgumentParser(description="Manage and validate themes for Hue application.")
    parser.add_argument('-l', '--load', action='store_true', help='Load the specified theme.')
    parser.add_argument('-v', '--validate', action='store_true', help='Validate the specified theme against its hash.')
    parser.add_argument('-t', '--theme', type=str, help='Specify a theme file to load or validate.')
    return parser.parse_args()

if __name__ == "__main__":
    # Initialize ThemeManager instance
    theme_manager = ThemeManager()
    theme_manager.setup_logging()

    # Handle command line arguments
    args = handle_arguments()

    if args.theme:
        # Validate or load a specific theme file
        if args.validate:
            if not theme_manager.validate_theme(args.theme):
                theme_manager.log_message(f"Failed to validate theme: {args.theme}")
                raise ValueError(f"Failed to validate theme: {args.theme}")
            else:
                theme_manager.log_message(f"Theme validated: {args.theme}")
                print(f"Theme validated: {args.theme}")
        elif args.load:
            theme = theme_manager.get_theme_instance(args.theme)
            if theme:
                print(f"Loaded theme: {theme.list_theme_attributes()}")
                theme_manager.log_message(f"Loaded theme: {args.theme}")
        else:
            print("No action specified. Use -l/--load or -v/--validate with -t/--theme.")
    else:
        # Load and validate default theme
        theme = theme_manager.get_theme_instance()
        
        if args.validate or theme_manager.validate_theme:
            if not theme_manager.validate_theme():
                theme_manager.log_message("Failed to validate theme.")
                raise ValueError("Failed to validate theme.")
        else:
            theme_manager.log_message("Skipping theme validation as per configuration.")

        # Export theme instance for importing
        if theme:
            print(f"Theme loaded: {theme.list_theme_attributes()}")
else:
    theme_manager = ThemeManager()
    theme_manager.setup_logging()
    THEME = theme_manager.get_theme_instance()
    
    if not THEME:
        theme_manager.log_message("Failed to load default theme.")
        raise ValueError("Failed to load default theme.")
    theme_manager.log_message("Loaded default theme.")
    