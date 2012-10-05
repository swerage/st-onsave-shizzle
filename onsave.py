import sublime
import sublime_plugin

class OnSave(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    #g_settings = sublime.load_settings(__name__ + '.sublime-settings')
    #settings = view.settings()

    #switched_off = settings.get('onsave_off', g_settings.get('onsave_off'), True)

    #if switched_off
     # return

    self.view.run_command("jsformat")
    self.view.run_command("alignment")
