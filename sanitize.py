import sublime
import sublime_plugin

class SanitizeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    
    settings = sublime.load_settings("Sanitize.sublime-settings")
    array = settings.get("char_list")

    region = sublime.Region(0, self.view.size())
    content = self.view.substr(region)
    
    for key in array:
      content = content.replace(key, array[key])
      
    # content = content.replace('‘', '\'')
    # content = content.replace('’', '\'')
    # content = content.replace(' ', ' ')
    # content = content.replace('“', '"')
    # content = content.replace('”', '"')
    # content = content.replace('…', '...')
    # content = content.replace('–', '-')
    
    self.view.replace(edit, region, content)
