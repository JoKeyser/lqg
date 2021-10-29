import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="invlqg",
    version="0.0.1",
    author="Dominik Straub",
    author_email="dominik.straub@tu-darmstadt.de",
    description="Inverse optimal control for linear quadratic Gaussian systems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.rwth-aachen.de/dominik.straub/lqg-tracking",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "numpy>=1.20.3",
        "scipy>=1.6.3",
        "matplotlib>=3.4.2",
        "numpyro==0.7.1",
        "jax==0.2.17",
        "jaxlib==0.1.69",
        "arviz>=0.11.2",
    ],
)
