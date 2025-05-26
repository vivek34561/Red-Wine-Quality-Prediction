import setuptools 

with open("README.md" , "r" , encoding = "utf-8") as f:
    long_description = f.read()
    
    
__version__ = "0.0.0"    

REPO_NAME  = "Red-Wine-Quality-Prediction"
AUTHOR_NAME = "vivek34561"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "vivekgupta3749@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for Red Wine Quality Prediction",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
)
