import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pixeldifference',
    version='1.0.0',
    author="Paul Biswell",
    author_email="pblabsdev@gmail.com",
    description="Get the total RGB or hexadecimal pixel differences between two images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pbiswell/pixeldifference",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["pillow"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Education',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Education',
        'Topic :: Multimedia :: Graphics',
        
    ],
    keywords=[
        "pixeldifference", "image-pixel-difference", "pixel", "image",
        "compare", "pixels", "RGB", "hex", "hexadecimal",
    ],
)
