# printdir
A simple package that prints the current directory with the `ls` command called using Python.

# Prerequisite Tooling
The following are tools needed to further develop and build the package.
- Python3
- dpkg
- python3-stdeb
- dh-python

# Intallation
```$ dpkg -i printdir```

# Usage
```$ printdir```

# Useful commands
## Building the package
```python3 setup.py --command-packages=stdeb.command bdist_deb```

## Installing the package
```sudo dpkg -i ./deb_dist/python3-printdir_1.0.0-1_all.deb```

## Removing the package
```sudo apt remove --purge python3-printdir -y```

# License
printdir is released under the MIT license. See LICENSE for details.

# Contact
Checkout my other projects at Github, [@christophermilian](https://github.com/christophermilian)
