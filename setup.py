import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cowpoke-mkbergman",
    version="0.0.1",
    author="Michael K Bergman",
    author_email="mike@mkbergman.com",
    description="Code in support of the 'Cooking with Python and KBpedia' (CWPK) series",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cognonto/cowpoke",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)