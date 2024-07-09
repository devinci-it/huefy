import os
themes = ['monokai', 'material_dark', 'vampire', 'night_owl', 'ayu_dark', 'nord_dark', 'nord_light', 'snow_storm', 'aurora']

themes_directory="themes.d"
def write_theme_to_file(theme_name, theme_data):
    theme_file = os.path.join(themes_directory, f"{theme_name}.theme")
    with open(theme_file, 'w', encoding='utf-8') as f:
        f.write(f"# {theme_name}.theme\n\n")
        for key, value in theme_data.items():
            escaped_value = value.replace("\\", "\\\\")
            f.write(f"{key} = {escaped_value} \n")
themes_data = { 'monokai': {
        # Monokai theme
        # Text formatting
        'ESC_BOLD': "[1m",
        'ESC_ITALIC': "[3m",

        # Colors
        'ESC_SUCCESS': "[1;32m",    # Green bold (success)
        'ESC_INFO': ";34m",         # Blue bold (information)
        'ESC_WARNING': ";33m",      # Yellow bold (warning)
        'ESC_ERROR': ";31m",        # Red bold (error)
        'ESC_ALERT': ";35m",        # Purple bold (alert)
        'ESC_ACCENT': ";36m",       # Cyan (accent)
        'ESC_DULL': ";30m",         # Dark gray (dull)
        'ESC_HIGHLIGHT': ";33m",    # Yellow (highlight)
        'ESC_FADED': ";37m",        # Light gray (faded)

        # Borders
        'ESC_BORDER': ";36m",       # Cyan (border)

        # Specific text uses
        'ESC_HEADER': ";36m",       # Cyan (header)
        'ESC_SUBHEADER': ";33m",    # Yellow (subheader)
        'ESC_PRETEXT': ";37m",      # Light gray (pre-text)
        'ESC_COMMENT': ";90m",      # Dark gray (comment)
        'ESC_CAPTION': "[4;35m",    # Purple underline (caption)

        # Reset
        'ESC_RESET': "[0m"}, 
                   
        'material_dark': {
        # Text formatting
        'ESC_BOLD': "[1m",
        'ESC_ITALIC': "[3m",

        # Colors
        'ESC_SUCCESS': "[1;92m",    # Green bold (success)
        'ESC_INFO': "[1;94m",       # Blue bold (information)
        'ESC_WARNING': "[1;93m",    # Yellow bold (warning)
        'ESC_ERROR': "[1;91m",      # Red bold (error)
        'ESC_ALERT': "[1;95m",      # Purple bold (alert)
        'ESC_ACCENT': "[1;96m",     # Cyan bold (accent)
        'ESC_DULL': "[1;30m",       # Dark gray bold (dull)
        'ESC_HIGHLIGHT': "[1;33m",  # Yellow bold (highlight)
        'ESC_FADED': "[2;37m",      # Light gray dim (faded)

        # Borders
        'ESC_BORDER': "[1;36m",     # Cyan bold (border)

        # Specific text uses
        'ESC_HEADER': "[1;96m",     # Cyan bold (header)
        'ESC_SUBHEADER': "[1;93m",  # Yellow bold (subheader)
        'ESC_PRETEXT': "[2;37m",    # Light gray dim (pre-text)
        'ESC_COMMENT': "[2;90m",    # Dark gray dim (comment)
        'ESC_CAPTION': "[4;94m",    # Light blue underline (caption)

        # Reset
        'ESC_RESET': "[0m",
    },

    'vampire': {
        # Text formatting
        'ESC_BOLD': "[1m",
        'ESC_ITALIC': "[3m",

        # Colors
        'ESC_SUCCESS': "[1;92m",    # Green bold (success)
        'ESC_INFO': "[1;94m",       # Blue bold (information)
        'ESC_WARNING': "[1;93m",    # Yellow bold (warning)
        'ESC_ERROR': "[1;91m",      # Red bold (error)
        'ESC_ALERT': "[1;95m",      # Purple bold (alert)
        'ESC_ACCENT': "[1;36m",     # Cyan bold (accent)
        'ESC_DULL': "[1;30m",       # Dark gray bold (dull)
        'ESC_HIGHLIGHT': "[1;35m",  # Purple bold (highlight)
        'ESC_FADED': "[2;37m",      # Light gray dim (faded)

        # Borders
        'ESC_BORDER': "[1;31m",     # Red bold (border)

        # Specific text uses
        'ESC_HEADER': "[1;91m",     # Red bold (header)
        'ESC_SUBHEADER': "[1;93m",  # Yellow bold (subheader)
        'ESC_PRETEXT': "[2;37m",    # Light gray dim (pre-text)
        'ESC_COMMENT': "[2;90m",    # Dark gray dim (comment)
        'ESC_CAPTION': "[4;95m",    # Purple underline (caption)

        # Reset
        'ESC_RESET': "[0m",
    },

    'night_owl': {
        # Text formatting
        'ESC_BOLD': "[1m",
        'ESC_ITALIC': "[3m",

        # Colors
        'ESC_SUCCESS': "[1;92m",    # Green bold (success)
        'ESC_INFO': "[1;94m",       # Blue bold (information)
        'ESC_WARNING': "[1;93m",    # Yellow bold (warning)
        'ESC_ERROR': "[1;91m",      # Red bold (error)
        'ESC_ALERT': "[1;95m",      # Purple bold (alert)
        'ESC_ACCENT': "[1;97m",     # White bold (accent)
        'ESC_DULL': "[1;30m",       # Dark gray bold (dull)
        'ESC_HIGHLIGHT': "[1;94m",  # Light blue bold (highlight)
        'ESC_FADED': "[2;37m",      # Light gray dim (faded)

        # Borders
        'ESC_BORDER': "[1;35m",     # Purple bold (border)

        # Specific text uses
        'ESC_HEADER': "[1;97m",     # White bold (header)
        'ESC_SUBHEADER': "[1;95m",  # Cyan bold (subheader)
        'ESC_PRETEXT': "[2;37m",    # Light gray dim (pre-text)
        'ESC_COMMENT': "[2;90m",    # Dark gray dim (comment)
        'ESC_CAPTION': "[4;94m",    # Light blue underline (caption)

        # Reset
        'ESC_RESET': "[0m",
    },

    'ayu_dark': {
        # Text formatting
        'ESC_BOLD': "[1m",
        'ESC_ITALIC': "[3m",

        # Colors
        'ESC_SUCCESS': "[1;92m",    # Green bold (success)
        'ESC_INFO': "[1;94m",       # Blue bold (information)
        'ESC_WARNING': "[1;93m",    # Yellow bold (warning)
        'ESC_ERROR': "[1;91m",      # Red bold (error)
        'ESC_ALERT': "[1;95m",      # Purple bold (alert)
        'ESC_ACCENT': "[1;96m",     # Cyan bold (accent)
        'ESC_DULL': "[1;30m",       # Dark gray bold (dull)
        'ESC_HIGHLIGHT': "[1;92m",  # Green bold (highlight)
        'ESC_FADED': "[2;37m",      # Light gray dim (faded)

        # Borders
        'ESC_BORDER': "[1;96m",     # Cyan bold (border)

        # Specific text uses
        'ESC_HEADER': "[1;94m",     # Light blue bold (header)
        'ESC_SUBHEADER': "[1;93m",  # Yellow bold (subheader)
        'ESC_PRETEXT': "[2;37m",    # Light gray dim (pre-text)
        'ESC_COMMENT': "[2;90m",    # Dark gray dim (comment)
        'ESC_CAPTION': "[4;94m",    # Light blue underline (caption)

        # Reset
        'ESC_RESET': "[0m",
    },

    'nord_dark': {
        # Text formatting
        'ESC_BOLD': "[1m",
        'ESC_ITALIC': "[3m",

        # Colors
        'ESC_SUCCESS': "[1;92m",    # Green bold (success)
        'ESC_INFO': "[1;94m",       # Blue bold (information)
        'ESC_WARNING': "[1;93m",    # Yellow bold (warning)
        'ESC_ERROR': "[1;91m",      # Red bold (error)
        'ESC_ALERT': "[1;95m",      # Purple bold (alert)
        'ESC_ACCENT': "[1;96m",     # Cyan bold (accent)
        'ESC_DULL': "[1;30m",       # Dark gray bold (dull)
        'ESC_HIGHLIGHT': "[1;93m",  # Yellow bold (highlight)
        'ESC_FADED': "[2;37m",      # Light gray dim (faded)

        # Borders
        'ESC_BORDER': "[1;34m",     # Blue bold (border)

        # Specific text uses
        'ESC_HEADER': "[1;96m",     # Cyan bold (header)
        'ESC_SUBHEADER': "[1;94m",  # Light blue bold (subheader)
        'ESC_PRETEXT': "[2;37m",    # Light gray dim (pre-text)
        'ESC_COMMENT': "[2;90m",    # Dark gray dim (comment)
        'ESC_CAPTION': "[4;94m",    # Light blue underline (caption)

        # Reset
        'ESC_RESET': "[0m",
    },

    'nord_light': {
        # Text formatting
        'ESC_BOLD': "[1m",
        'ESC_ITALIC': "[3m",

        # Colors
        'ESC_SUCCESS': "[1;92m",    # Green bold (success)
        'ESC_INFO': "[1;94m",       # Blue bold (information)
        'ESC_WARNING': "[1;93m",    # Yellow bold (warning)
        'ESC_ERROR': "[1;91m",      # Red bold (error)
        'ESC_ALERT': "[1;95m",      # Purple bold (alert)
        'ESC_ACCENT': "[1;30m",     # Dark gray bold (accent)
        'ESC_DULL': "[1;37m",       # White bold (dull)
        'ESC_HIGHLIGHT': "[1;95m",  # Purple bold (highlight)
        'ESC_FADED': "[2;37m",      # Light gray dim (faded)

        # Borders
        'ESC_BORDER': "[1;96m",     # Cyan bold (border)

        # Specific text uses
        'ESC_HEADER': "[1;94m",     # Light blue bold (header)
        'ESC_SUBHEADER': "[1;93m",  # Yellow bold (subheader)
        'ESC_PRETEXT': "[2;37m",    # Light gray dim (pre-text)
        'ESC_COMMENT': "[2;90m",    # Dark gray dim (comment)
        'ESC_CAPTION': "[4;95m",    # Purple underline (caption)

        # Reset
        'ESC_RESET': "[0m",
    },

    'snow_storm': {
        # Text formatting
        'ESC_BOLD': "[1m",
        'ESC_ITALIC': "[3m",

        # Colors
        'ESC_SUCCESS': "[1;92m",    # Green bold (success)
        'ESC_INFO': "[1;94m",       # Blue bold (information)
        'ESC_WARNING': "[1;93m",    # Yellow bold (warning)
        'ESC_ERROR': "[1;91m",      # Red bold (error)
        'ESC_ALERT': "[1;95m",      # Purple bold (alert)
        'ESC_ACCENT': "[1;96m",     # Cyan bold (accent)
        'ESC_DULL': "[1;30m",       # Dark gray bold (dull)
        'ESC_HIGHLIGHT': "[1;97m",  # White bold (highlight)
        'ESC_FADED': "[2;37m",      # Light gray dim (faded)

        # Borders
        'ESC_BORDER': "[1;97m",     # White bold (border)

        # Specific text uses
        'ESC_HEADER': "[1;97m",     # White bold (header)
        'ESC_SUBHEADER': "[1;95m",  # Purple bold (subheader)
        'ESC_PRETEXT': "[2;37m",    # Light gray dim (pre-text)
        'ESC_COMMENT': "[2;90m",    # Dark gray dim (comment)
        'ESC_CAPTION': "[4;94m",    # Light blue underline (caption)

        # Reset
        'ESC_RESET': "[0m",
    },

    'aurora': {
        # Text formatting
        'ESC_BOLD': "[1m",
        'ESC_ITALIC': "[3m",

        # Colors
        'ESC_SUCCESS': "[1;92m",    # Green bold (success)
        'ESC_INFO': "[1;94m",       # Blue bold (information)
        'ESC_WARNING': "[1;93m",    # Yellow bold (warning)
        'ESC_ERROR': "[1;91m",      # Red bold (error)
        'ESC_ALERT': "[1;95m",      # Purple bold (alert)
        'ESC_ACCENT': "[1;96m",     # Cyan bold (accent)
        'ESC_DULL': "[1;30m",       # Dark gray bold (dull)
        'ESC_HIGHLIGHT': "[1;93m",  # Yellow bold (highlight)
        'ESC_FADED': "[2;37m",      # Light gray dim (faded)

        # Borders
        'ESC_BORDER': "[1;36m",     # Cyan bold (border)

        # Specific text uses
        'ESC_HEADER': "[1;94m",     # Light blue bold (header)
        'ESC_SUBHEADER': "[1;96m",  # Cyan bold (subheader)
        'ESC_PRETEXT': "[2;37m",    # Light gray dim (pre-text)
        'ESC_COMMENT': "[2;90m",    # Dark gray dim (comment)
        'ESC_CAPTION': "[4;94m",    # Light blue underline (caption)

        # Reset
        'ESC_RESET': "[0m",
    },
}


for theme_name, theme_data in themes_data.items():
    write_theme_to_file(theme_name, theme_data)

