# Configuration settings for Enso.  Eventually this will take
# localization into account too (or we can make a separate module for
# such strings).

# The keys to start, exit, and cancel the quasimode.
# Their values are strings referring to the names of constants defined
# in the os-specific input module in use.
QUASIMODE_START_KEY = "KEYCODE_CAPITAL"
QUASIMODE_END_KEY = "KEYCODE_RETURN"
QUASIMODE_CANCEL_KEY = "KEYCODE_ESCAPE"
QUASIMODE_CANCEL_KEY2 = "KEYCODE_DELETE"

# Whether the Quasimode is actually modal ("sticky").
IS_QUASIMODE_MODAL = False

# Display Enso on active monitor (where mouse cursor is)
# If set to False, Enso displays on primary-monitor.
SHOW_ON_ACTIVE_MONITOR = True

# Amount of time, in seconds (float), to wait from the time
# that the quasimode begins drawing to the time that the
# suggestion list begins to be displayed.  Setting this to a
# value greater than 0 will effectively create a
# "spring-loaded suggestion list" behavior.
QUASIMODE_SUGGESTION_DELAY = 0.2

# The maximum number of suggestions to display in the quasimode.
QUASIMODE_MAX_SUGGESTIONS = 6

# The minimum number of characters the user must type before the
# auto-completion mechanism engages.
QUASIMODE_MIN_AUTOCOMPLETE_CHARS = 2

# Highlight trailing space in the input area.
# To disable the feature set this to None.
QUASIMODE_TRAILING_SPACE_STRING = u"\u00b7" # MIDDLE DOT

# The message displayed when the user types some text that is not a command.
BAD_COMMAND_MSG = "<p><command>%s</command> is not a command.</p>"\
                  "%s"

# Minimum number of characters that should have been typed into the
# quasimode for a bad command message to be shown.
BAD_COMMAND_MSG_MIN_CHARS = 2

# Try to run the program if no matching command found.
# Typing 'msconfig' would run msconfig utility even that it's not in the list
# of learned commands or not directly accessible from desktop/startmenu
NO_COMMAND_FALLBACK = "" # "run %s"

# The captions for the above message, indicating commands that are related
# to the command the user typed.
ONE_SUGG_CAPTION = "<caption>Did you mean <command>%s</command>?</caption>"

# The string that is displayed in the quasimode window when the user
# first enters the quasimode.
QUASIMODE_DEFAULT_HELP = u"Welcome to Enso! Enter a command, " \
    u"or type \u201chelp\u201d for assistance."

# The string displayed when the user has typed some characters but there
# is no matching command.
QUASIMODE_NO_COMMAND_HELP = "There is no matching command. " \
    "Use backspace to delete characters."

# Message XML for the Splash message shown when Enso first loads.
OPENING_MSG_XML = "<p>Welcome to <command>Enso</command>!</p>" + \
    "<caption>Copyright &#169; 2008 Humanized, Inc.</caption>"

# Message XML displayed when the mouse hovers over a mini message.
MINI_MSG_HELP_XML = "<p>The <command>hide mini messages</command>" \
    " and <command>put</command> commands control" \
    " these mini-messages.</p>"

# Message XML for the About message.
ABOUT_MSG_XML = u"<p><command>Enso</command> Community Edition</p>" \
    "<caption> </caption>" \
    "<p>Copyright &#169; 2008 <b>Humanized, Inc.</b></p>" \
    "<p>Copyright &#169; 2008-2010 <b>Enso community</b></p>"

# Optional custom font. If not used, Arial is used on Windows and Helvetica on Linux
# FONT_NAME = {"normal" : "Square 721 Condensed BT CZ", "italic" : "Square 721 Condensed BT CZ"}

# List of default platforms supported by Enso; platforms are specific
# types of providers that provide a suite of platform-specific
# functionality.
DEFAULT_PLATFORMS = ["enso.platform.osx",
                     "enso.platform.linux",
                     "enso.platform.win32"]

# List of modules/packages that support the provider interface to
# provide required platform-specific functionality to Enso.
PROVIDERS = []
PROVIDERS.extend(DEFAULT_PLATFORMS)

# List of modules/packages that support the plugin interface to
# extend Enso.  The plugins are loaded in the order that they
# are specified in this list.
PLUGINS = ["enso.contrib.scriptotron",
           "enso.contrib.help",
           "enso.contrib.google",
           "enso.contrib.evaluate"]

# Detect default system locale and use it for google search.
# If set to False, no locale is forced.
PLUGIN_GOOGLE_USE_DEFAULT_LOCALE = True

# Uncomment and change following to override default Enso commands
# folder placement.
# SCRIPTS_FOLDER_NAME = "c:\\documents\\ensocommands")
# import os; SCRIPTS_FOLDER_NAME = os.path.expanduser("~/.enso_commands")
