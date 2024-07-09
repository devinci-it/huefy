from setuptools import setup, find_packages

setup(
    name='huefy',
    version='1.3.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        'huefy': ['hue.config','*.theme', 'README.md'],
        'huefy/themes.d': ['*.theme'],
        'scripts': ['*.sh', '*.py'],
    },
    entry_points={
        'console_scripts': [
            'hue = hue:main',
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

