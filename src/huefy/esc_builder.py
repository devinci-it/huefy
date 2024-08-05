import colorsys

class AnsiEscapeCodeBuilder:
    """
    A class for constructing ANSI escape codes for terminal text styling.

    Attributes:
        theme (str): The theme of the terminal ('dark' or 'light').
        _styles (list): List of text style codes.
        _fg_color (str): Foreground color code.
        _bg_color (str): Background color code.
        _negative (bool): Whether to use a negative color scheme.

    Class Attributes:
        DEFAULT_COLORS (dict): Default foreground and background colors based on the theme.
    """

    # Define modern shades for default colors
    DEFAULT_COLORS = {
        'dark': {
            'fg': '#e0e0e0',  # Light gray
            'bg': '#1e1e1e'   # Dark gray
        },
        'light': {
            'fg': '#2e2e2e',  # Dark gray
            'bg': '#f0f0f0'   # Light gray
        }
    }

    def __init__(self, theme='dark'):
        """
        Initializes the builder with a theme and sets default colors.

        Parameters:
            theme (str): The theme for the text (default is 'dark').
        """
        self._styles = []
        self._fg_color = None
        self._bg_color = None
        self._theme = theme
        self._negative = False

        # Set default colors based on the theme
        self._set_default_colors()

    def set_bold(self, enabled=True):
        """
        Enable or disable bold text.

        Parameters:
            enabled (bool): Whether to enable bold text (default is True).

        Returns:
            AnsiEscapeCodeBuilder: The current instance for method chaining.
        """
        if enabled:
            self._styles.append('1')
        else:
            self._styles.append('22')  # Reset bold

        return self

    def set_italic(self, enabled=True):
        """
        Enable or disable italic text.

        Parameters:
            enabled (bool): Whether to enable italic text (default is True).

        Returns:
            AnsiEscapeCodeBuilder: The current instance for method chaining.
        """
        if enabled:
            self._styles.append('3')
        else:
            self._styles.append('23')  # Reset italic

        return self

    def set_underline(self, enabled=True):
        """
        Enable or disable underline text.

        Parameters:
            enabled (bool): Whether to enable underline text (default is True).

        Returns:
            AnsiEscapeCodeBuilder: The current instance for method chaining.
        """
        if enabled:
            self._styles.append('4')
        else:
            self._styles.append('24')  # Reset underline

        return self

    def set_fg_color(self, color=None, rgb=None):
        """
        Set the foreground (text) color using HEX, RGB tuple, or HSL.

        Parameters:
            color (str): HEX color code (e.g., '#ffcb00').
            rgb (tuple): RGB color tuple (e.g., (255, 255, 0)).

        Returns:
            AnsiEscapeCodeBuilder: The current instance for method chaining.

        Raises:
            ValueError: If no color or an invalid color is provided.
        """
        if color:
            r, g, b = self._normalize_color(color)
        elif rgb:
            r, g, b = rgb
        else:
            raise ValueError("Invalid color specification. Provide either a color string or RGB tuple.")

        self._fg_color = f'38;2;{r};{g};{b}'
        return self

    def set_bg_color(self, color=None, rgb=None):
        """
        Set the background color using HEX, RGB tuple, or HSL.

        Parameters:
            color (str): HEX color code (e.g., '#072448').
            rgb (tuple): RGB color tuple (e.g., (0, 0, 64)).

        Returns:
            AnsiEscapeCodeBuilder: The current instance for method chaining.

        Raises:
            ValueError: If no color or an invalid color is provided.
        """
        if color:
            r, g, b = self._normalize_color(color)
        elif rgb:
            r, g, b = rgb
        else:
            raise ValueError("Invalid color specification. Provide either a color string or RGB tuple.")

        self._bg_color = f'48;2;{r};{g};{b}'
        return self

    def _set_default_colors(self):
        """
        Set default foreground and background colors based on the theme.
        """
        colors = self.DEFAULT_COLORS.get(self._theme)
        if not colors:
            raise ValueError("Unsupported theme. Use 'dark' or 'light'.")
        
        self.set_fg_color(color=colors['fg'])
        self.set_bg_color(color=colors['bg'])

    def set_theme(self, theme):
        """
        Set the theme and update colors accordingly.

        Parameters:
            theme (str): The new theme name ('dark' or 'light').

        Returns:
            AnsiEscapeCodeBuilder: The current instance for method chaining.

        Raises:
            ValueError: If an unsupported theme is provided.
        """
        self._theme = theme
        self._set_default_colors()
        return self

    def set_negative(self, enabled=True):
        """
        Enable or disable the negative (reversed) color scheme.

        Parameters:
            enabled (bool): Whether to enable negative colors (default is True).

        Returns:
            AnsiEscapeCodeBuilder: The current instance for method chaining.
        """
        self._negative = enabled
        return self

    def _normalize_color(self, color):
        """
        Normalize color input to RGB.

        Parameters:
            color (str): The color input in HEX or HSL format.

        Returns:
            tuple: RGB values.

        Raises:
            ValueError: If the color format is unsupported or invalid.
        """
        if color.startswith('#'):
            # HEX color
            color = color.lstrip('#')
            if len(color) == 6:
                r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
            elif len(color) == 3:
                r, g, b = [int(c * 2, 16) for c in color]
            else:
                raise ValueError("Invalid HEX color format.")
        elif color.startswith('hsl('):
            # HSL color
            hsl = color[4:-1].split(',')
            h, s, l = float(hsl[0]), float(hsl[1].strip('%')) / 100, float(hsl[2].strip('%')) / 100
            r, g, b = colorsys.hls_to_rgb(h / 360, l, s)
            r, g, b = int(r * 255), int(g * 255), int(b * 255)
        else:
            raise ValueError("Unsupported color format. Use HEX or HSL.")

        return r, g, b

    def build(self):
        """
        Construct and return the final ANSI escape code string.

        Returns:
            str: The ANSI escape code string.
        """
        codes = []
        if self._negative:
            # Swap foreground and background colors
            self._fg_color, self._bg_color = self._bg_color, self._fg_color

        if self._fg_color:
            codes.append(self._fg_color)
        if self._bg_color:
            codes.append(self._bg_color)
        codes.extend(self._styles)

        return f'\033[{";".join(codes)}m'

