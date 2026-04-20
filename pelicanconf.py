AUTHOR = 'Noah Stephenson'
SITENAME = 'Noah Stephenson'
SITEURL = ''

THEME = 'themes/noah'
STATIC_PATHS = ['images']
PAGE_PATHS = ['pages']
DISPLAY_PAGES_ON_MENU = True

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

IGNORE_FILES = ['.#*', 'venv', '__pycache__']

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.extra': {},
    }
}
