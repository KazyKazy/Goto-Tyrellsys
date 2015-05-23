import sublime, sublime_plugin
import subprocess, webbrowser

# available commands
# target_package_selected
# target_search_from_input

def query(text):
    url = 'http://www.tyrellsys.com/' + text.replace(' ', '%20')
    webbrowser.open_new_tab(url)

class TargetPackageSelectedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)

            query(text)

class TargetSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel('Search for http://www.tyrellsys.com/ ', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        query(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
