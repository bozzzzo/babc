import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="babc",
    version="0.0.1",
    author="Bozo Dragojevic",
    author_email="bozzo@apache.org",
    description="python abc experiments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bozzzzo/babc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
