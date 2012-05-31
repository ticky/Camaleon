# coding=utf8
import sublime, sublime_plugin
import os

class CamaleonCommand(sublime_plugin.WindowCommand):
    def run(self, interval = 1):

        camaleonSettings = sublime.load_settings('Camaleon.sublime-settings')
        sublimeSettings  = sublime.load_settings('Preferences.sublime-settings')
        current = int(camaleonSettings.get('current'))

        if len(camaleonSettings.get('camaleon')) == 0:
            return

        if (current > len(camaleonSettings.get('camaleon'))-1):
            current = 0

        # Interval is positive, check if int+
        if interval > 0 and (current+interval > len(camaleonSettings.get('camaleon'))-1):
            current = current + interval - len(camaleonSettings.get('camaleon'))
        elif interval < 0 and ((current+interval > len(camaleonSettings.get('camaleon'))-1) or current+interval < 0):
            current = current + interval + len(camaleonSettings.get('camaleon'))
        else:
            current = current+interval

        # check if we're already using the same theme
        if camaleonSettings.get('camaleon')[current][0] == sublimeSettings.get('theme'):
            pass
        else:
            sublimeSettings.set('theme', camaleonSettings.get('camaleon')[current][0]);

        # check if we're already using the same color_scheme
        if camaleonSettings.get('camaleon')[current][1] == sublimeSettings.get('color_scheme'):
            pass
        else:
            sublimeSettings.set('color_scheme', camaleonSettings.get('camaleon')[current][1]);

        camaleonSettings.set('current', current);
        sublime.save_settings('Preferences.sublime-settings')
        sublime.save_settings('Camaleon.sublime-settings')

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

            sublime.status_message(u'Camaleon : Loaded colour scheme : '+randomScheme.decode('utf-8'))