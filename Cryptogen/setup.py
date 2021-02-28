import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cryptogen", 
    version="0.0.1",
    author="Aniruddha Kulkarni",
    author_email="aniruddha.k1911@gmail.com",
    description="A package to encrypt/decrypt the images/data using ""SMART"" Image Processing Algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/battcheeks/Cryptogen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers" 
    ],
    python_requires='>=3.6',
    keywords=["cryptography","Encryption","Decryption","Image Processing"],
    license="MIT",include_package_data=True,zip_safe=True,
)