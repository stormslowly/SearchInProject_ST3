
## try the sublime text native find in files. "Find" -> "Find in Files..."
## you will find you don't need this plug-in :(




# Search In Project for Sublime Text3 v1.0

###A plugin for [Sublime Text 3](http://www.sublimetext.com/3).
###it fork from [SearchInProject_SublimeText2](https://github.com/leonid-shevtsov/SearchInProject_SublimeText2)
thanks a lot [Leonid Shevtsov](http://leonid.shevtsov.me) for learning a lot from you

## Synopsis

This plugin makes it possible to use various external search tools (`grep`, `ack`, `ag`, `git grep`, or `findstr`) to find strings aross your entire current Sublime Text project.

It opens a quick selection panel to browse results, and highlights matches inside files.

It's easy to add another search tool, if you so desire.

## Installation

Copy the folder into the Packages folder.

## Usage

* Use the key binding (`⌘⌥⇧F` on OS X, `Ctrl+Alt+Shift+F` on Windows), or
* Call the "Search in Project" command;
* Enter the search query; **the query is passed directly to the shell command.** You are responsible for escaping the query, but on the up side you can specify any command line options to go with it. This plugin doesn't make an effort to abstract you away from search tools, but provides a convenient way of running them from Sublime Text 2 instead.
* Hit `Enter` (`Return`). In a short while you'll be presented with a "quck select" panel with the search results. Select any file from that panel (it supports fuzzy searching) to go to the match. The search string will be highlighted with an outline and a circle symbol in the gutter area.

If you select text and then run Search In Project, it will pre-fill the search string with the selection text; for example, to search for a word project-wide, do `⌘D, ⌘⌥⇧F, ↩`

If you run Search In Project again, it will remember the last search string, so the next search is just an `↩` away.

## Configuration

Configuration is stored in a separate, user-specific `SearchInProject.sublime-settings` file. See the default file for configuration options; links to both could be
found in the main menu in `Preferences -> Package Settings -> Search In Project`.

On any OS I recommend you to install [ack](http://betterthangrep.com/), and use it instead of the default `grep`/`findstr`, because it's much faster. [Here's how to install ack on Windows](http://stackoverflow.com/questions/1023710/how-can-i-install-and-use-ack-library-on-windows).

* * *
## Change log
### 2013-2-23
* add function that goto the line where you select from the panle
* make it compatiable with sublime text 2
