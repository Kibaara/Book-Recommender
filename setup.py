from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


## edit variables as per your requirements
    
REPO_NAME = "Personalised E-learning WebApp"
AUTHOR_USER_NAME = "Kibaara"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit' , 'numpy']

setup(
    name=SRC_REPO,
    version = "0.0.1",
    author= AUTHOR_USER_NAME,
    description="A small package for collaborative filtering component",
    long_description= long_description,
    url = f"https://github.com",
    author_email="",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.11",
    install_requires= LIST_OF_REQUIREMENTS
)