from setuptools import setup, find_packages


with open("README.md") as file:
    readme = file.read()


setup(
    name="fintools",
    version="0.0.0",
    description="Financial Tools",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="iteso",
    packages=find_packages(where="src"),
    package_dir={
        "": "src"
    },
    include_package_data=True,
    scripts=[
        "bin/fintools"
    ],
    python_requires=">3.5, <4"
)
