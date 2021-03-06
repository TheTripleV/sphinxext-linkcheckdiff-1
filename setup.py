import subprocess
import setuptools

try:
    ret = subprocess.check_output("git describe --tags --abbrev=0", shell=True,)
    version = ret.decode("utf-8").strip()
except:
    version = "master"

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="sphinxext-linkcheckdiff",
    version=version,
    author="Vasista Vovveti",
    author_email="vasistavovveti@gmail.com",
    description="Sphinx Extension to run diff-only linkchecks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wpilibsuite/sphinxext-linkcheckdiff",
    install_requires=["sphinx>=3.0"],
    packages=["sphinxext"],
    classifiers=[
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Framework :: Sphinx :: Extension",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)
