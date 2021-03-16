from sys import version
import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="yqml",
    version="0.0.2",
    author="Muhamad Tohir",
    author_email="maztohir@gmail.com",
    description="YAML based query language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maztohir/yqml",
    packages=setuptools.find_packages(exclude=("test",)),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3'
    ],
    keywords=[
        'sql', 'python', 'query', 'yaml'
    ],
    python_requires='>=3.6',
    install_requires=[
        'PyYAML==5.4.1'
    ]
)