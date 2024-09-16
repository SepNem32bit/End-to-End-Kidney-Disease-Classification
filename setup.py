import setuptools

with open("Readme.md","r",encoding="utf-8") as f:
    readme=f.read()

__version__="0.0.0"
repo_name="End-to-End-Kidney-Disease-Classification"
author_git_user_name="SepNem32bit"
#local package
#no need to address the full directory and it can only refer to the DiseaseClasssier without mentioning src folder
src_repo="DiseaseClassifier"
author_email=""

setuptools.setup(
    name=src_repo,
    version=__version__,
    author=author_git_user_name,
    description="end to end AI solution",
    long_description=readme,
    long_description_content="text/markdown",
    url=f"https://github.com/{author_git_user_name}/{repo_name}",
    project_urls={"Bug Tracker":f"https://github.com/{author_git_user_name}/{repo_name}/issues"},
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)