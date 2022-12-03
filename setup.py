from setuptools import setup

with open("README.md", "r",encoding="utf-8") as readme_file:
	long_description=readme_file.read()

setup(
	name="printdir",
	version="1.0.0",
	description="Print the current directory structure.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="Christopher Milian",
	author_email="christophermilian16@gmail.com",
	license="MIT",
	packages=['directoryprint'],
	package_dir={'directoryprint':'directoryprint/'},
	classifiers=["Programming Language:: Python :: 3"],
	entry_points={
		'console_scripts': ['printdir = directoryprint.directoryprint:main']
	},
	keywords="directory print out",
	python_requires=">=3.6"
)
