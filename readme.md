# Camaleón

Camaleón for Sublime Text 2 allows you to quickly cycle between user-defined
combinations of chrome themes and colour schemes.

## Installation

Checkout this repository into your Packages directory (More info soon)

## Usage

* F8:			Cycle predefined chrome+colour schemes.
* Shift+F8:		Cycle predefined chrome+colour schemes in reverse.
* Control+F8	Choose a random colour scheme.

Chrome+colour schemes are defined in "Camaleon.sublime-settings". Copy this file
into your User package directory to make changes.

## Recent Changes

* Improved support for Mac OS X
* Allowed choosing a random colour scheme from anywhere in your Packages
  directory.
* Removed backwards-compatibility with old versions (pre-build 2174) of Sublime
  Text 2.
* Genericised check to prevent switching theme when we're using the same theme
  already (Doesn't just check for Soda)
* Added all available commands to the command palette, and made sure the
  keyboard shortcuts are displayed, and tweaked the copy (Colour, anyone?)

## Original Version

The original version of Camaleón, by Tito Bouzout, is available here:
https://github.com/SublimeText/Camaleon