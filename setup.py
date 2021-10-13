from os import path
from subprocess import run
from sys import stderr

from setuptools import find_packages, setup

lib_name = 'streamlit_toggle'
data_dir = path.join(path.dirname(__file__), lib_name, 'frontend')

try:
    run(['npm', 'install'], cwd=data_dir, check=True)
    run(['npm', 'run', 'build'], cwd=data_dir, check=True)
except Exception as e:
    print(f'Error during npm tasks: {e}', file=stderr)
    exit(1)

setup(
    name=lib_name,
    version="1.0.1",
    author="Sam Dobson, Marcel Baltruschat",
    author_email="1309834+samdobson@users.noreply.github.com, 34354523+mrcblt@users.noreply.github.com",
    description="Toggle widget for Streamlit",
    long_description="",
    license='MIT',
    url="https://github.com/mrcblt/streamlit-toggle",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
