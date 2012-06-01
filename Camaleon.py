# coding=utf8
import sublime, sublime_plugin
import os

class CamaleonCommand(sublime_plugin.WindowCommand):
    def run(self, schemeInterval = 1, setInterval = 0):

        camaleonSettings    = sublime.load_settings('Camaleon.sublime-settings')
        sublimeSettings     = sublime.load_settings('Preferences.sublime-settings')
        currentScheme       = int(camaleonSettings.get('currentScheme'))
        currentSet          = int(camaleonSettings.get('currentSet'))

        # If we don't have any sets configured, show an error for the user
        if len(camaleonSettings.get('sets')) == 0:
            sublime.status_message(u'Camaléon: No sets configured! Please fix your \'Camaleon.sublime-settings.\'')
            return

        # If we're already out of range (Could happen when editing sets), reset.
        if (currentSet > len(camaleonSettings.get('sets'))-1):
            currentSet = 0
        if (currentScheme > len(camaleonSettings.get('sets')[currentSet].get("schemes"))):
            currentScheme = 0

        # If we're changing sets, ignore the scheme interval
        if (setInterval > 0 or setInterval < 0):
            if setInterval > 0 and (currentSet+setInterval > len(camaleonSettings.get('sets'))-1):
                currentSet = currentSet + setInterval - len(camaleonSettings.get('sets'))
            elif setInterval < 0 and ((currentSet+setInterval > len(camaleonSettings.get('sets'))-1) or currentScheme+schemeInterval < 0):
                currentSet = currentSet + setInterval + len(camaleonSettings.get('sets'))
            else:
                currentSet = currentSet + setInterval

            # Reset to the first scheme in new set.
            currentScheme = 0

        # Otherwise, let's change schemes!
        elif schemeInterval > 0 and (currentScheme+schemeInterval > len(camaleonSettings.get('sets')[currentSet].get("schemes"))-1):
            currentScheme = currentScheme + schemeInterval - len(camaleonSettings.get('sets')[currentSet].get("schemes"))
        elif schemeInterval < 0 and ((currentScheme+schemeInterval > len(camaleonSettings.get('sets')[currentSet].get("schemes"))-1) or currentScheme+schemeInterval < 0):
            currentScheme = currentScheme + schemeInterval + len(camaleonSettings.get('sets')[currentSet].get("schemes"))
        else:
            currentScheme = currentScheme + schemeInterval

        # Grab the names from the set
        newChromeTheme = camaleonSettings.get('sets')[currentSet].get("schemes")[currentScheme][0]
        newColorScheme = camaleonSettings.get('sets')[currentSet].get("schemes")[currentScheme][1]

        # Check if we're already using the same theme
        if newChromeTheme == sublimeSettings.get('theme') or (newChromeTheme is None or len(newChromeTheme) < 1):
            pass
        else:
            sublimeSettings.set('theme', newChromeTheme)

        # Check if we're already using the same color_scheme
        if newColorScheme == sublimeSettings.get('color_scheme') or (newColorScheme is None or len(newColorScheme) < 1):
            pass
        else:
            sublimeSettings.set('color_scheme', newColorScheme)

        # Save Camaléon's settings
        camaleonSettings.set('currentScheme', currentScheme)
        camaleonSettings.set('currentSet', currentSet)
        sublime.save_settings('Preferences.sublime-settings')
        sublime.save_settings('Camaleon.sublime-settings')

        # Notify the user of what's happened
        status = u'Camaléon: Now using \'%(setName)s\' set - \'%(chrome)s\' theme and \'%(theme)s\' colour scheme.' % {
                "setName":  camaleonSettings.get('sets')[currentSet].get("title"),
                "chrome":   os.path.basename(newChromeTheme).split(".")[0],
                "theme":    os.path.basename(newColorScheme).split(".")[0]
            }

        sublime.status_message(status)

class CamaleonRandomCommand(sublime_plugin.WindowCommand):
    def run(self):
        availableSchemes = []
        for dirname, dirnames, filenames in os.walk(sublime.packages_path()):
            for filename in filenames:
                if filename[-7:] == 'tmTheme':
                    availableSchemes.append(os.path.join(dirname, filename))

        from random import choice
        randomScheme = choice(availableSchemes)
        if randomScheme != '':

            sublimeSettings = sublime.load_settings('Preferences.sublime-settings')

            sublimeSettings.set('color_scheme', randomScheme)

            sublime.save_settings('Preferences.sublime-settings')

            sublime.status_message(u'Camaléon: Randomly chose \'%s\' colour scheme.' % os.path.basename(randomScheme).split(".")[0])