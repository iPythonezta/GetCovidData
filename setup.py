import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(

    name="GetCovidData",
    version="1.1.1",
    author="Huzaifa Azhar",
    description="A simple python package to get Covid Stats just by using simple commands!",
    readme = "README.md",
    long_description=long_description,
     long_description_content_type='text/markdown',
    install_requires=["bs4"]
)