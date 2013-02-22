from Data.Packages.SearchInProject_ST3.searchengines import base


class FindStr (base.Base):
    """Uses Windows built-in findstr command."""

    def _command_line(self, query, folders):
        return " ".join([
            self.path_to_executable,
            self.mandatory_options,
            self.common_options,
            '"/d:%s"' % ":".join(folders),
            query,
            "*.*"
            ])
    def _sanitize_output(self, output):

        output = output[1:] # omit the fist line of 
        output =  str(output, errors='replace')
        end = output.find("\n");
        return output[end+1:]
    def _parse_output(self, output):
        lines = output.split("\n")
        line_parts = [line.split(":") for line in lines]
        line_parts = self._filter_lines_without_matches(line_parts)
        return [(":".join(line[0:-2]), ":".join(line[-2:]).strip()) for line in line_parts]

engine_class = FindStr
