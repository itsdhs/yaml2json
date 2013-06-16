import sublime, sublime_plugin, subprocess
import os, sys

EXE_PATH = "./yaml2json.py"

class YamlToJsonCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		result, err = exe("%s" % EXE_PATH,
			self.view.substr(self.view.sel()[0]).encode('utf-8'))

		if len(err) != 0:
			self.view.set_status('yaml2json', "yaml2json: %s" % err)
			sys.stderr.write("ERROR: %s\n" % err)
			sublime.set_timeout(self.clear, 10000)
		else:
			self.view.replace(edit, self.view.sel()[0], result.decode('utf-8'))
			sublime.set_timeout(self.clear, 0)

	def clear(self):
		self.view.erase_status('yaml2json')

class JsonToYamlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		result, err = exe("%s --reverse" % EXE_PATH,
			self.view.substr(self.view.sel()[0]).encode('utf-8'))

		if len(err) != 0:
			self.view.set_status('json2yaml', "json2yaml: %s" % err)
			sys.stderr.write("ERROR: %s\n" % err)
			sublime.set_timeout(self.clear, 10000)
		else:
			self.view.replace(edit, self.view.sel()[0], result.decode('utf-8'))
			sublime.set_timeout(self.clear, 0)

	def clear(self):
		self.view.erase_status('json2yaml')

def exe(cmd, stream):
	p = subprocess.Popen(cmd, bufsize=-1, 
		cwd=os.path.dirname(__file__),
		stdout=subprocess.PIPE, 
		stderr=subprocess.PIPE,
		stdin=subprocess.PIPE,
		shell=True)

	result, err = p.communicate(stream)

	return result, err
