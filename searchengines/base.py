import subprocess
import re


class Base:
    """
        This is the base search engine class.
        Override it to define new search engines.
    """

    SETTINGS = [
        "path_to_executable",
        "mandatory_options",
        "common_options"
    ]

    RE_LINE_NO = re.compile(":(\d+):")

    def __init__(self, settings):
        """
            Receives the sublime.Settings object
        """
        self.settings = settings
        for setting_name in self.__class__.SETTINGS:
            setattr(self, setting_name, self.settings.get(self._full_settings_name(setting_name), ''))
        pass

    def run(self, query, folders):
        """
            Run the search engine. Return a list of tuples, where first element is
            the absolute file path, and optionally row information, separated
            by a semicolon, and the second element is the result string
        """
        command_line = self._command_line(query, folders)
        print("Running: %s" % command_line)
        pipe = subprocess.Popen(command_line, shell=True, stdout=subprocess.PIPE)
        output, error = pipe.communicate()
        if error:
            print("error code is ",error)
            return None
        return self._parse_output(self._sanitize_output(output).strip())

    def _command_line(self, query, folders):
        """
            Prepare a command line for the search engine.
        """
        return " ".join([
            self.path_to_executable,
            self.mandatory_options,
            self.common_options,
            query
            ] + [("\"" + f + "\"") for f in folders ] )

    def _sanitize_output(self, output):
        return str(output, errors='replace')

    def _parse_output(self, output):
        lines = output.split("\n")
        line_parts = [ self._pase_line(line)   for line in lines if self._pase_line(line)[0] ]
        return line_parts

    def _pase_line(self,line):
        lineno = Base.RE_LINE_NO.findall(line);
        
        if len(lineno)==0:
            return None,None
        lineno = lineno[0];
        index = line.find(lineno);
        filename = line[0:index-1]
        lineinfo = line[index:]
        return (filename,lineinfo)

    def _full_settings_name(self, name):
        return "search_in_project_%s_%s" % (self.__class__.__name__, name)

    def _filter_lines_without_matches(self, line_parts):
        return filter(lambda line: len(line) >= 2, line_parts)
