import sublime
import sublime_plugin
import re

class OnSave(sublime_plugin.EventListener):
  
  def spaceParams(self, match):
    res = re.sub(r'([+\-/*])', r' \1 ', match.group(0))
    res = re.sub(r'\s*(,)\s*', r'\1 ', res)
    ret = ' %s ' % (res.strip())
    
    if res.find(',') == -1 and res[0] == '"' and res[len(res) - 1] == '"':
        ret = res
    
    return ret

  def on_pre_save(self, view):
    if not (re.search('js', view.file_name())):
      return

    inParens = '(?<=\()[^\(\[\]\{\)]+(?=\))'
    inBrackets = '(?<=\{).+(?=\})'
    inSqrBrackets = '(?<=\[).+(?=\])'
    otherCommas = ',(?!\s|$)'

    regions = view.find_all('\(')
    
    for region in regions:
      line = view.line(region)
      
      subLine = view.substr(line)
      subLine = re.sub(inParens, self.spaceParams, subLine)
      subLine = re.sub(inSqrBrackets, self.spaceParams, subLine)
      subLine = re.sub(inBrackets, self.spaceParams, subLine)
      subLine = re.sub(otherCommas, ', ', subLine)

      edit = view.begin_edit()
      view.replace(edit, line, subLine)
      view.end_edit(edit)