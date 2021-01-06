from setuptools import setup, find_packages

with open("README.rst", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name="hr",  
    version="0.0.1",
    author="J montero",
    author_email="jmontero@gmail.com",
    description="User management tool",
    long_description=readme,
    url="https://github.com/pimliprentiss/hr",
    packages=find_packages('src'),
    package_dir={'': 'src'}

)