import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycalc",
    version="0.0.1",
    author="Elizabeth Lemeshko",
    author_email="lzbth.lemeshko@gmail.com",
    description="Pure-python command-line calculator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/widbnudb/PythonHomework",
    packages=['pycalc'],
    entry_points={
        'console_scripts': [
            'pycalc = pycalc.pycalc'
        ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
