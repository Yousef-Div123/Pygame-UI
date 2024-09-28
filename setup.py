from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="PYGAME_GUI_EXT",
    version="0.0.2",
    description="A gui extension for pygame",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yousef-Div123/Pygame-UI",
    author="YousefDiv",
    author_email="yousefdiv123@outlook.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["pygame >= 2.1.2"],
    extras_require={
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3"
)