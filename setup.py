from setuptools import setup, find_packages

setup(
    name="tangyuan-core",
    version="1.0.0",
    author="TangYuan (汤圆)",
    author_email="tangyuan@local",
    description="Ultra-lightweight, zero-dependency core for digital guardians. Native socket communication, <10KB footprint.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tangyuan/tangyuan-core",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[],  # Zero external dependencies!
    extras_require={
        "dev": ["pytest", "black", "flake8"],
    },
)
