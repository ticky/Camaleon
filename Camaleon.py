# coding=utf8
import sublime, sublime_plugin
import os

class CamaleonCommand(sublime_plugin.WindowCommand):
    def run(self, interval = 1):

        camaleonSettings = sublime.load_settings('Camaleon.sublime-settings')
        sublimeSettings  = sublime.load_settings('Preferences.sublime-settings')
        currentScheme = int(camaleonSettings.get('currentScheme'))

        if len(camaleonSettings.get('camaleon')) == 0:
            return

        if (currentScheme > len(camaleonSettings.get('camaleon'))-1):
            currentScheme = 0

        # Interval is positive, check if int+
        if interval > 0 and (currentScheme+interval > len(camaleonSettings.get('camaleon'))-1):
            currentScheme = currentScheme + interval - len(camaleonSettings.get('camaleon'))
        elif interval < 0 and ((currentScheme+interval > len(camaleonSettings.get('camaleon'))-1) or currentScheme+interval < 0):
            currentScheme = currentScheme + interval + len(camaleonSettings.get('camaleon'))
        else:
            currentScheme = currentScheme+interval

        # check if we're already using the same theme
        if camaleonSettings.get('camaleon')[currentScheme][0] == sublimeSettings.get('theme'):
            pass
        else:
            sublimeSettings.set('theme', camaleonSettings.get('camaleon')[currentScheme][0]);

        # check if we're already using the same color_scheme
        if camaleonSettings.get('camaleon')[currentScheme][1] == sublimeSettings.get('color_scheme'):
            pass
        else:
            sublimeSettings.set('color_scheme', camaleonSettings.get('camaleon')[currentScheme][1]);

        camaleonSettings.set('currentScheme', currentScheme);
        sublime.save_settings('Preferences.sublime-settings')
        sublime.save_settings('Camaleon.sublime-settings')

        status = u'Camaléon: Now using \'%(chrome)s\' theme and \'%(theme)s\' colour scheme.' % {
                "chrome":   os.path.basename(camaleonSettings.get('camaleon')[currentScheme][0]).split(".")[0],
                "theme":    os.path.basename(camaleonSettings.get('camaleon')[currentScheme][1]).split(".")[0]
            }

        sublime.status_message(status)

class CamaleonRandomColourSchemeCommand(sublime_plugin.WindowCommand):
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

            sublimeSettings.set('color_scheme', randomScheme);

            sublime.save_settings('Preferences.sublime-settings')

            sublime.status_message(u'Camaléon: Randomly chose \'%s\' colour scheme.' % os.path.basename(randomScheme).split(".")[0])