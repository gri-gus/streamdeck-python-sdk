import setuptools

VERSION = "0.1.5"

with open("README.md", "r") as file:
    long_description = file.read()

requirements = [
    "decohints>=1.0.7",
    "pydantic>=1.10.5",
    "typing_extensions>=4.5.0",
    "websocket-client>=1.5.1",
]

setuptools.setup(
    name="streamdeck_sdk",
    version=VERSION,
    author="Grigoriy Gusev",
    author_email="thegrigus@gmail.com",
    description="Library for creating Stream Deck plugins in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gri-gus/streamdeck-python-sdk",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
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
)
