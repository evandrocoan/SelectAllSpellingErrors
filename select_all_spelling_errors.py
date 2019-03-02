
import sublime
import sublime_plugin

try:
    import cProfile

except:
    cProfile = None


class SelectAllSpellingErrorsCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # https://github.com/SublimeTextIssues/Core/issues/127
        if cProfile:
            cProfile.runctx( 'findRegions(self, edit)', globals(), locals() )

        else:
            findRegions(self, edit)


def findRegions(self, edit):

    regionsList = []

    while True:

        self.view.run_command('next_misspelling')

        if self.view.sel()[0] not in regionsList:

            regionsList.append( self.view.sel()[0] )

        else:

            break

    self.view.sel().clear()
    self.view.sel().add_all( regionsList )



