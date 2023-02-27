from setuptools import setup
import os

here = os.path.dirname(os.path.realpath(__file__))
HAS_CUDA = os.system("nvidia-smi > /dev/null 2>&1") == 0

VERSION = "0.0.4"
DESCRIPTION = "ChatLLaMA: Open and Efficient Foundation Language Models Runnable In A Single GPU"

packages = [
    "chatllama",
]


def read_file(filename: str):
    try:
        lines = []
        with open(filename) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines if not line.startswith('#')]
        return lines
    except:
        return []


def package_files(ds):
    paths = []
    for d in ds:
        for (path, directories, filenames) in os.walk(d):
            for filename in filenames:
                if '__pycache__' not in str(filename):
                    paths.append(str(os.path.join(path, filename))[len('chatllama/'):])
    return paths

extra_files = package_files(['chatllama/'])


setup(
    name="chatllama",
    version=VERSION,
    author_email="<juncongmoo@gmail.com>",
    description=DESCRIPTION,
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    install_requires=read_file(f"{here}/requirements.txt"),
    keywords=[
        "ChatLLaMA", "LLaMA"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=packages,
    package_data={"chatllama": extra_files},
    url="https://github.com/juncongmoo/chatllama"
)
