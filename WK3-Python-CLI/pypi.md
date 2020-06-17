# Description
This is the handson to show how to upload package to PyPi

# Pre-requisite
* Create a PyPI account - https://pypi.org/account/register/
* Create a TestPyPI account - https://test.pypi.org/account/register/
* Install pip in your machine

# Preparing Your Package for Publication
## Naming Your Package
Make sure your package name is unique and easy to remember.
- Brainstorm and do some research to find the perfect name
- Use the [PyPI search](https://pypi.org/search/) to check if a name is already taken.
- The name in PyPi can be different from the one when importing. However, if same name or similar name, it will be easier for your user. 


## Configuring Your Package

Just be a little patient to read through it! It is important to know before publish.

In order for your package to be uploaded to PyPI, you need to provide some basic information about it. This information is typically provided in the form of a setup.py file.

### setup.py
The setup.py file should be placed in the top folder of your package. In our example, it is as below:

```python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from setuptools import setup, find_packages

import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='devops-cli',
    version='0.1.3',
    license='MIT',
    description='DevOps Tool',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Michael Su',
    author_email='michaelsu2014@gmail.com',
    url='https://test.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
    ],
    install_requires=[
        'click==7.1',
        'pandas==1.0.4',
        'requests==2.23.0'
    ],
    entry_points={
        'console_scripts': [
            'devops-cli = cli_tool.click_demo:process',
        ]
    },
)
```
We will only cover some of the options available in setuptools here. The [documentation](https://setuptools.readthedocs.io/en/latest/setuptools.html#basic-use) does a good job of going into all the detail.

The parameters that are 100% necessary in the call to setup() are the following:

- name: the name of your package as it will appear on PyPI
- version: the current version of your package
- packages: the packages and subpackages containing your source code

The last two parameters to setup() deserve special mention:

- install_requires is used to list any dependencies your package has to third party libraries. 

- entry_points is used to create scripts that call a function within your package.
## Documenting Your Package
Before releasing your package to the world, you should add some documentation. Depending on your package, the documentation can be as small as a simple README file, or as big as a full web page with tutorials, example galleries, and an API reference.

At a minimum, you should include a README file with your project. A good README should quickly describe your project, as well as tell your users how to install and use your package. Typically, you want to include your README as the long_description argument to setup(). This will display your README on PyPI.

## Versioning Your Package

Semantic versioning is a good default scheme to use. The version number is given as three numerical components, for instance 0.1.2. The components are called MAJOR, MINOR, and PATCH, and there are simple rules about when to increment each component:

- Increment the MAJOR version when you make incompatible API changes.
- Increment the MINOR version when you add functionality in a backwards-compatible manner.
- Increment the PATCH version when you make backwards-compatible bug fixes. (Source)

## Adding Files to Your Package
Sometimes, you’ll have files inside your package that are not source code files. Examples include data files, binaries, documentation, and—as we have in this project—configuration files.

Tell setup() to copy these non-code files. This is done by setting the include_package_data argument to True:

```python
setup(
    ...
    include_package_data=True,
    ...
)
```

## Checking the command locally
Go to the setup.py folder and run the following command.
```python
python setup.py install
```

then type and you should be able to see the command is working
```python
devops-cli --help
```

# Publishing to PyPI
Your package is finally ready to meet the world outside your computer! In this section, you’ll see how to actually upload your package to PyPI.

If you don’t already have an account on PyPI, now is the time to create one: register your account on PyPI. While you’re at it, you should also register an account on TestPyPI. 
TestPyPI is very useful, as you can try all the steps of publishing a package without any consequences if you mess up. See more https://packaging.python.org/guides/using-testpypi/

To upload your package to PyPI, you’ll use a tool called Twine. You can install Twine using Pip as usual:
```python
$ pip install twine
```

## Building Your Package
Packages on PyPI are not distributed as plain source code. Instead, they are wrapped into distribution packages. The most common formats for distribution packages are source archives and Python wheels.

A source archive consists of your source code and any supporting files wrapped into one tar file. Similarly, a wheel is essentially a zip archive containing your code. In contrast to the source archive, the wheel includes any extensions ready to use.

To create a source archive and a wheel for your package, you can run the following command:
```python
python setup.py sdist bdist_wheel
```
This will create two files in a newly created dist directory, a source archive and a wheel.
Note: On Windows, the source archive will be a .zip file by default. You can choose the format of the source archive [with the --format command line option](https://python.readthedocs.io/en/stable/distutils/sourcedist.html).

You might wonder how setup.py knows what to do with the sdist and bdist_wheel arguments. If you look back to how setup.py was implemented, there is no mention of sdist, bdist_wheel, or any other command line arguments.

All the command line arguments are instead implemented in the upstream [distutils standard library](https://github.com/python/cpython/tree/master/Lib/distutils/command). You can list all available arguments by adding the --help-commands option:

## Testing Your Package
First, you should check that the newly built distribution packages contain the files you expect. On Linux and macOS, you should be able to list the contents of the tar source archive as follows:
```python
$ tar tzf <your package-1.0.0.tar.gz>
```
On Windows, you can use a utility like 7-zip to look inside the corresponding zip file.

You should see all your source code listed, as well as a few new files that have been created containing information you provided in setup.py. In particular, make sure that all subpackages and supporting files are included.

You can also have a look inside the wheel by unzipping it as if it were a zip file. However, if your source archive contains the files you expect, the wheel should be fine as well.

Newer versions of Twine (1.12.0 and above) can also check that your package description will render properly on PyPI. You can run twine check on the files created in dist:

```python
$ twine check dist/*
```
While it won’t catch all problems you might run into, it will for instance let you know if you are using the wrong content type.

## Uploading Your Package
Now you’re ready to actually upload your package to PyPI. For this, you’ll again use the Twine tool, telling it to upload the distribution packages you have built. First, you should upload to TestPyPI to make sure everything works as expected:

```python
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
Twine will ask you for your username and password.

If the upload succeeds, you can quickly head over to TestPyPI, scroll down, and look at your project being proudly displayed among the new releases! Click on your package and make sure everything looks okay. While you can play with TestPyPI as much as you want, you shouldn’t upload dummy packages to PyPI just for testing.

However, if you have your own package to publish, then the moment has finally arrived! With all the preparations taken care of, this final step is short:

```python
$ twine upload dist/*
```
Head over to PyPI and look up your package. You can find it either by searching, by looking at the Your projects page, or by going directly to the URL of your project: pypi.org/project/your-package-name/.

Congratulations! Your package is published on PyPI!

## pip install Your Package
Take a moment to bask in the blue glow of the PyPI web page and (of course) brag to your friends.

Then open up a terminal again. There is one more great pay off!

With your package uploaded to PyPI, you can install it with pip as well:
```python
$ pip install your-package-name
```
Try to type your package command.

## Change your package
If you maintain your package well, you will need to change the source code from time to time. This is easy.

```python
python setup.py sdist bdist_wheel
twine upload dist/*
```
Finally, update your package via pip to see whether your changes worked:

```python
$ pip install YOURPACKAGE --upgrade
```

# Essential Steps

Here are the scripts for uploading test PyPi
```bash
python setup.py sdist bdist_wheel

twine upload --repository testpypi dist/*

pip install -i https://test.pypi.org/simple/ devops-cli==0.1.4

devops-cli -i index.html --email <your email address>

```

# Create .pypirc file

A .pypirc file allows you to define the configuration for package indexes (referred to here as “repositories”), so that you don’t have to enter the URL, username, or password whenever you upload a package with twine or flit.

See more https://packaging.python.org/specifications/pypirc/#pypirc