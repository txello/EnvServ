from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="envserv",
    version="1.0",
    description="Environment model",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/txello/EnvServ",
    author="txello",
    author_email="txello@inbox.ru",
    keywords="env model",
    packages=["envserv"],
    license="MIT",
    install_requires=["python-dotenv"],
    include_package_data=True
    
)