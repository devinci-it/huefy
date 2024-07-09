import argparse
from huefy.theme_manager import ThemeManager

def handle_arguments():
    parser = argparse.ArgumentParser(description="Manage and validate themes for Hue application.")
    parser.add_argument('-l', '--load', action='store_true', help='Load the specified theme.')
    parser.add_argument('-v', '--validate', action='store_true', help='Validate the specified theme against its hash.')
    parser.add_argument('-t', '--theme', type=str, help='Specify a theme file to load or validate.')
    return parser.parse_args()

if __name__ == "__main__":
    theme_manager = ThemeManager()
    theme_manager.setup_logging()

    args = handle_arguments()

    if args.theme:
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
        theme = theme_manager.get_theme_instance()
        
        if args.validate or theme_manager.validate_theme:
            if not theme_manager.validate_theme():
                theme_manager.log_message("Failed to validate theme.")
                raise ValueError("Failed to validate theme.")
        else:
            theme_manager.log_message("Skipping theme validation as per configuration.")

        if theme:
            print(f"Theme loaded: {theme.list_theme_attributes()}")
