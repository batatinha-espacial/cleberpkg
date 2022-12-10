# Cleberpkg - A new package manager for Debian derivates

This is the new package manager for debian derivates.<br>
Warning: We are not responsible for any package downloaded with this tool. Only install a package if you thrust in the authors of the package.

## How to setup

Make sure you have `python3` and `python3-pip` installed before we continue.<br>
Just download and run `sudo python3 install.py` to setup the cleberpkg.

## How to install a package

Run the command `sudo cleberpkg install <package_name>` and the package will be installed.<br>
If the package is already installed or the package doesn't exists it will raise an error.

## How to get info about a package

Run the command `sudo cleberpkg info <package_name>` to get an info about a package.<br>
If the package doesn't exists it will raise an error.

## Removing a package

This should be at the warning too, because you cannot remove a package directly. Only install a package if you thrust the authors.

## Creating a package

This is very easy to do with cleberpkg. And that's one of the reasons that there is a warning in the top of this file.<br>
Just run the command `sudo cleberpkg create`. It will ask for the name of the package, the package's complete name, a description of the package, the dependencies of the package and the link to the .deb file. All respectively.

## That's it

That's it.
