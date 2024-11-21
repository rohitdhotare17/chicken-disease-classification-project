import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()


    __version__="0.0.0"

    REPO_NAME="chicken-disease-classification-project"
    AUTHOR_USER_NAME="rohitdhotare17"
    SRC_REPO="cnnClassifier"
    AUTHOR_EMAIL="rohitdhotare2001@gmail.com"


    setuptools.setup(
        name=SRC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="a small python package for chicken disease classificaiton app",
        long_description=long_description,
        long_description_content="text/markdown",
        url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        project_urls={
            "bug tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        },
        package_dir={"": "src"},
        package=setuptools.find_packages(where="src")
    )