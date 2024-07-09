class TextBuilder:
        """
        Helper class for building formatted text using a builder pattern.
        
        Methods:
        __init__(theme, property_name, **kwargs):
            Initializes a TextBuilder object with the provided theme, property name, and options.
        
        text(text):
            Sets the text to be formatted.
        
        bold():
            Makes the text bold.
        
        underline():
            Underlines the text.
        
        indent(spaces):
            Sets the indentation for the text.
        
        align(alignment):
            Sets the alignment for the text.
        
        max_width(width):
            Sets the maximum width for the text.
        
        iterable():
            Returns a list of formatted strings.
        
        build():
            Returns the formatted text.
        """
        def __init__(self, theme, property_name, **kwargs):
            self.theme = theme
            self.property_name = property_name.upper()
            self.text_content = kwargs.get('text', "")
            self.bold_flag = kwargs.get('bold', False)
            self.underline_flag = kwargs.get('underline', False)
            self.indent_spaces = kwargs.get('indent', 0)
            self.alignment = kwargs.get('align', 'left')
            self.max_width_value = kwargs.get('max_width', None)
            self.iterable_flag = kwargs.get('iterable', False)

        def text(self, text):
            self.text_content = text
            return self

        def bold(self):
            self.bold_flag = True
            return self

        def underline(self):
            self.underline_flag = True
            return self

        def indent(self, spaces):
            self.indent_spaces = spaces
            return self

        def align(self, alignment):
            if alignment not in ['left', 'center', 'right']:
                raise ValueError("Alignment must be 'left', 'center', or 'right'")
            self.alignment = alignment
            return self

        def max_width(self, width):
            self.max_width_value = width
            return self

        def iterable(self):
            self.iterable_flag = True
            return self

        def build(self):
            formatted_text = self.text_content
            
            if self.bold_flag:
                formatted_text = getattr(self.theme, 'bold') + formatted_text
            if self.underline_flag:
                formatted_text = getattr(self.theme, 'underline') + formatted_text
            
            formatted_text = getattr(self.theme, self.property_name.lower()) + formatted_text + self.theme._esc_character + self.theme._theme_data['ESC_RESET']

            if self.indent_spaces > 0:
                formatted_text = ' ' * self.indent_spaces + formatted_text

            if self.max_width_value:
                lines = []
                while len(formatted_text) > self.max_width_value:
                    line = formatted_text[:self.max_width_value]
                    lines.append(line)
                    formatted_text = formatted_text[self.max_width_value:]
                lines.append(formatted_text)
                formatted_text = lines
            
            if self.alignment == 'center':
                if self.iterable_flag and self.max_width_value:
                    formatted_text = [line.center(self.max_width_value) for line in formatted_text]
                else:
                    formatted_text = formatted_text.center(self.max_width_value or len(formatted_text))
            elif self.alignment == 'right':
                if self.iterable_flag and self.max_width_value:
                    formatted_text = [line.rjust(self.max_width_value) for line in formatted_text]
                else:
                    formatted_text = formatted_text.rjust(self.max_width_value or len(formatted_text))

            if self.iterable_flag:
                return formatted_text

            return formatted_text