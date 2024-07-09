from setuptools import setup, find_packages

setup(
    name='huefy',
    version='1.2.2',
    packages=find_packages(where='src'),  # Find packages under 'src'
    package_dir={'': 'src'},              # Package root directory is 'src'
    package_data={
        '': ['*.theme', '*.config', '*.py', '*.md'],  # Include all .theme, .config, .py, and .md files
        'src/themes.d': ['*'],
        'src': ['hue.config'],                           # Include hue.config from src directory
        'src':['*.py','*.config']# Include all files in themes.d directory
    },
    entry_points={
        'console_scripts': [
            'hue = hue:main',  # Entry point to your main script 'hue.py'
        ],
    },
    python_requires='>=3.6',
    author='devinci-it',
    description='Terminal color utility',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/devinci-it/hue',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
