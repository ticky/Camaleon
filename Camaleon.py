# coding=utf8
import sublime, sublime_plugin
import os

class CamaleonCommand(sublime_plugin.WindowCommand):
    def run(self, type = 'next'):

        camaleonSettings = sublime.load_settings('Camaleon.sublime-settings')
        sublimeSettings  = sublime.load_settings('Preferences.sublime-settings')
        current = intcamaleonSettings.get('current'))

        try:
        camaleonSettings.get('camaleon')[current][0]
        except:
            current = 0
            try:
            camaleonSettings.get('camaleon')[current][0]
            except:
                return # total empty
        try:
            if type == 'next':
            camaleonSettings.get('camaleon')[current+1][0]
                next = current+1
            else:
            camaleonSettings.get('camaleon')[current-1][0]
                next = current-1
                if next < 0:
                    next = lencamaleonSettings.get('camaleon'))-1
        except:
            try:
                if type == 'next':
                    next = 0
                else:
                    next = lencamaleonSettings.get('camaleon'))-1
            camaleonSettings.get('camaleon')[next][0]
            except:
                return # total empty

        # chrome change

        # check if we're already using the same colour theme
        ifcamaleonSettings.get('camaleon')[next][0] == sublimeSettings.get('theme'):
            pass
        else:
            sublimeSettings.set('theme',camaleonSettings.get('camaleon')[next][0]);

        # colour scheme change

        sublimeSettings.set('color_scheme',camaleonSettings.get('camaleon')[next][1]);
        sublime.save_settings('Preferences.sublime-settings')

        camaleonSettings.set('current', next);
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