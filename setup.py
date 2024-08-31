from pathlib import Path

import setuptools

VERSION = "1.0.1"
PACKAGE_DIR = "."
REQUIREMENTS_FILE = "./requirements.txt"
README = "README-PYPI.md"
BASE_DIR = Path(__file__).resolve().parent

with open(REQUIREMENTS_FILE, "r") as f:
    requirements = f.read().splitlines()

with open(README, "r") as file:
    long_description = file.read()

[p.unlink() for p in BASE_DIR.rglob('*.py[co]')]
[p.rmdir() for p in BASE_DIR.rglob('__pycache__')]

setuptools.setup(
    name="streamdeck_sdk",
    version=VERSION,
    author="Grigoriy Gusev",
    author_email="thegrigus@gmail.com",
    description="Library for creating Stream Deck plugins in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gri-gus/streamdeck-python-sdk",
    packages=setuptools.find_packages(where=PACKAGE_DIR),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    license="Apache Software License",
    keywords=[
        "python",
        "sdk",
        "streamdeck",
        "streamdeck-sdk",
        "streamdeck_sdk",
        "stream deck sdk",
        "stream deck",
        "elgato",
        "elgato sdk",
        "elgato stream deck",
        "streamdeck-python-sdk",
        "streamdeck_python_sdk",
        "streamdeck python sdk"
    ],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'streamdeck_sdk=streamdeck_sdk.executable.executable:main',
        ],
    },
)
