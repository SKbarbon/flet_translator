from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_des = str(f.read())

setup(
    name='flet_translator',
    version='1.2.6',
    author='SKbarbon',
    description='A package that help flet developers to make their apps support multiple languages',
    long_description=long_des,
    long_description_content_type='text/markdown',
    url='https://github.com/SKbarbon/flet_translator',
    install_requires=["flet", "sacremoses", "deep-translator"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
)