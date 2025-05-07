from setuptools import setup, find_packages

setup(
    name="adminconsult_sdk",
    version="1.0.7",
    author="Ward Cornette",
    author_email="Ward.Cornette@num3rix.fr",
    description="Syneton Admin Consult SDK - REST API Wrapper",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cornettew/adminconsult-sdk",
    packages=find_packages(exclude=["tests*", "examples*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pandas",
        "regex",
        "hvac",
        "requests",
        "SQLAlchemy",
        "sqlalchemy-sqlany",
        "psycopg2-binary"
    ],
    python_requires=">=3.7",
)
