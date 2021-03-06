from setuptools import setup, find_packages


install_requires = [
    'jupyter',
    'notebook==5.7.5',
    'tornado==4.5.3',
    'networkx==2.4',
    'jsonpath-rw>=1.4.0',
    'requests>=2.21.0',
    'graphviz>=0.11.1',
    'aiohttp',
    'pandas',
    'pyyaml'
]


setup(
    name="biothings_explorer",
    version="0.0.1",
    author="Jiwen Xin, Chunlei Wu",
    author_email="cwu@scripps.edu",
    description="Python Client for BioThings Explorer",
    license="BSD",
    keywords="schema biothings",
    url="https://github.com/biothings/biothings_explorer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    install_requires=install_requires,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True
)
