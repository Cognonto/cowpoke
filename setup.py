import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cowpoke',
    version='0.0.2',
    author='Michael K Bergman',
    author_email='mike@mkbergman.com',
    description="Code in support of the 'Cooking with Python and KBpedia' (CWPK) series",
    long_description=long_description,
    long_description_content_type='text/markdown',
	keywords='KBpedia, knowledge graph, build, extract', 
    url='https://github.com/Cognonto/cowpoke',
#    packages=setuptools.find_packages(),
    py_modules=['__main__', 'build', 'config', 'extract', 'mapping', 'setup', 'stats', 'utils', 'visualize'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
	project_urls={ 
        'CWPK blog series': 'https://www.mkbergman.com/cooking-with-python-and-kbpedia/',
        'CWPK Jupyter notebooks': 'https://github.com/Cognonto/CWPK',
        'KBpedia': 'https://kbpedia.org/',
        'Source': 'https://github.com/Cognonto/cowpoke/'}
)
