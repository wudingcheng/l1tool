from setuptools import setup

with open("requirments.txt", 'r') as f:
    required = f.read().splitlines()

setup(
    name="l1tool",
    version="1.0",
    description="L1 Regularizer for GNSS Time series change and offsets detection.",
    license="GPL v3",
    author="WU Dingcheng",
    install_requires=required,
    entry_points={"gui_scripts": [
        "l1tool=l1tool:main"]}

)
