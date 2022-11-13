from pathlib import Path
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.8'
DESCRIPTION = 'Muestra en letras cualquier valor positivo Ej valor cheques'
PACKAGE_NAME = 'montoenletra'
AUTHOR = 'Roger Jose Retamoza Campo'
EMAIL = 'myasesor@gmail.com'
GITHUB_URL = 'https://github.com/myasesor/montoenletra_package'

setup(
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    entry_points={
        "console_scripts":
            ["pymonto=montoenletra.__main__:main"]
    },
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [
        'monto en letra',
        'numero a letra'
    ],
    install_requires=[ 
        'match',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)