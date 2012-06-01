# Camaleón

Camaleón for Sublime Text 2 allows you to quickly cycle between user-defined
combinations of chrome themes and colour schemes.

## Installation

Either download the zip version of this repository, and extract it into your
Packages directory, or check out this repository into your Packages directory
using git.

## Usage

### Keyboard Shortcuts

#### Mac

*  F8:					Cycle chrome+colour schemes.
*  Shift+F8:			Cycle chrome+colour schemes in reverse.
*  Command+F8:			Cycle chrome+colour scheme sets.
*  Command+Shift+F8:	Cycle chrome+colour scheme sets in reverse.
*  Control+F8:			Choose a random colour scheme.

#### Windows and Linux

*  F8:					Cycle predefined chrome+colour schemes.
*  Shift+F8:			Cycle predefined chrome+colour schemes in reverse.
*  Control+F8:			Cycle chrome+colour scheme sets.
*  Control+Shift+F8:	Cycle chrome+colour scheme sets in reverse.
*  Alt+F8:				Choose a random colour scheme.

Chrome+colour sets and schemes are defined in "Camaleon.sublime-settings".
Copy this file into your User package directory to make changes.

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
* Improved and streamlined program logic
* Added support for creating sets of chrome+colour schemes. For example, you can
  now create a set of only dark chrome+colour, and a set of only light
  chrome+colour, and switch between them with Command+F8 (Control+F8 on Windows
  and Linux)

## Original Version

The original version of Camaleón, by Tito Bouzout, is available here:
https://github.com/SublimeText/Camaleon