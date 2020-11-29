# -*- coding: utf-8 -*-

import time

# !! This is the configuration of Nikola. !! #
# !!  You should edit it to your liking.  !! #


# ! Some settings can be different in different languages.
# ! A comment stating (translatable) is used to denote those.
# ! There are two ways to specify a translatable setting:
# ! (a) BLOG_TITLE = "My Blog"
# ! (b) BLOG_TITLE = {"en": "My Blog", "es": "Mi Blog"}
# ! Option (a) is used when you don't want that setting translated.
# ! Option (b) is used for settings that are different in different languages.


# Data about this site
BLOG_AUTHOR = "Jan Grosser"  # (translatable)
BLOG_TITLE = "cat /dev/brain/ideas >> blog"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link. Don't forget the protocol (http/https)!
SITE_URL = "https://www.jan-grosser.de/"
# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "https://www.jan-grosser.de/"
BLOG_EMAIL = "webmaster@jan-grosser.de"
BLOG_DESCRIPTION = "Private Webseite von Jan Grosser"  # (translatable)

# Nikola is multilingual!
#
# Currently supported languages are:
#
# en        English
# af        Afrikaans
# ar        Arabic
# az        Azerbaijani
# bg        Bulgarian
# bs        Bosnian
# ca        Catalan
# cs        Czech [ALTERNATIVELY cz]
# da        Danish
# de        German
# el        Greek [NOT gr]
# eo        Esperanto
# es        Spanish
# et        Estonian
# eu        Basque
# fa        Persian
# fi        Finnish
# fr        French
# fur       Friulian
# gl        Galician
# he        Hebrew
# hi        Hindi
# hr        Croatian
# hu        Hungarian
# ia        Interlingua
# id        Indonesian
# it        Italian
# ja        Japanese [NOT jp]
# ko        Korean
# lt        Lithuanian
# ml        Malayalam
# nb        Norwegian (Bokmål)
# nl        Dutch
# pa        Punjabi
# pl        Polish
# pt        Portuguese
# pt_br     Portuguese (Brazil)
# ru        Russian
# sk        Slovak
# sl        Slovene
# sq        Albanian
# sr        Serbian (Cyrillic)
# sr_latin  Serbian (Latin)
# sv        Swedish
# te        Telugu
# th        Thai
# tr        Turkish [NOT tr_TR]
# uk        Ukrainian
# ur        Urdu
# vi        Vietnamese
# zh_cn     Chinese (Simplified)
# zh_tw     Chinese (Traditional)
#
# If you want to use Nikola with a non-supported language you have to provide
# a module containing the necessary translations
# (cf. the modules at nikola/data/themes/base/messages/).
# If a specific post is not translated to a language, then the version
# in the default language will be shown instead.

# What is the default language?
DEFAULT_LANG = "de"

# What other languages do you have?
# The format is {"translationcode" : "path/to/translation" }
# the path will be used as a prefix for the generated pages location
TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

# What will translated input files be named like?

# If you have a page something.rst, then something.pl.rst will be considered
# its Polish translation.
#     (in the above example: path == "something", ext == "rst", lang == "pl")
# this pattern is also used for metadata:
#     something.meta -> something.pl.meta

TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'

# Links for the sidebar / navigation bar.  (translatable)
# This is a dict.  The keys are languages, and values are tuples.
#
# For regular links:
#     ('https://getnikola.com/', 'Nikola Homepage')
#
# For submenus:
#     (
#         (
#             ('https://apple.com/', 'Apple'),
#             ('https://orange.com/', 'Orange'),
#         ),
#         'Fruits'
#     )
#
# WARNING: Support for submenus is theme-dependent.
#          Only one level of submenus is supported.
# WARNING: Some themes, including the default Bootstrap 4 theme,
#          may present issues if the menu is too large.
#          (in Bootstrap, the navbar can grow too large and cover contents.)
# WARNING: If you link to directories, make sure to follow
#          ``STRIP_INDEXES``.  If it’s set to ``True``, end your links
#          with a ``/``, otherwise end them with ``/index.html`` — or
#          else they won’t be highlighted when active.

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/index.html", "Home"),
#        ("/archive.html", "Archiv"),
        ("/categories/", "Stöbern"),
        ("https://github.com/rzbrk", "GitHub"),
        ("/rss.xml", "RSS-Feed"),
        ("/pages/impressum/index.html", "Impressum/Datenschutz"),
    ),
}

# Alternative navigation links. Works the same way NAVIGATION_LINKS does,
# although themes may not always support them. (translatable)
# (Bootstrap 4: right-side of navbar, Bootblog 4: right side of title)
NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: ()
}

# Name of the theme to use.
#THEME = "bootblog4"
THEME = "bootstrap4"

# Primary color of your theme. This will be used to customize your theme.
# Must be a HEX value.
THEME_COLOR = '#5670d4'

# Theme configuration. Fully theme-dependent. (translatable)
# Examples below are for bootblog4.
# bootblog4 supports: featured_large featured_small featured_on_mobile
#                     featured_large_image_on_mobile featured_strip_html sidebar
# bootstrap4 supports: navbar_light (defaults to False)
THEME_CONFIG = {
    DEFAULT_LANG: {
        # Show the latest featured post in a large box, with the previewimage as its background.
        'featured_large': False,
        # Show the first (remaining) two featured posts in small boxes.
        'featured_small': False,
        # Show featured posts on mobile.
        'featured_on_mobile': True,
        # Show image in `featured_large` on mobile.
        # `featured_small` displays them only on desktop.
        'featured_large_image_on_mobile': True,
        # Strip HTML from featured post text.
        'featured_strip_html': False,
        # Contents of the sidebar, If empty, the sidebar is not displayed.
        'sidebar': ''
    }
}

# POSTS and PAGES contains (wildcard, destination, template) tuples.
# (translatable)
#
# The wildcard is used to generate a list of source files
# (whatever/thing.rst, for example).
#
# That fragment could have an associated metadata file (whatever/thing.meta),
# and optionally translated files (example for Spanish, with code "es"):
#     whatever/thing.es.rst and whatever/thing.es.meta
#
#     This assumes you use the default TRANSLATIONS_PATTERN.
#
# From those files, a set of HTML fragment files will be generated:
# cache/whatever/thing.html (and maybe cache/whatever/thing.html.es)
#
# These files are combined with the template to produce rendered
# pages, which will be placed at
# output/TRANSLATIONS[lang]/destination/pagename.html
#
# where "pagename" is the "slug" specified in the metadata file.
# The page might also be placed in /destination/pagename/index.html
# if PRETTY_URLS are enabled.
#
# The difference between POSTS and PAGES is that POSTS are added
# to feeds, indexes, tag lists and archives and are considered part
# of a blog, while PAGES are just independent HTML pages.
#
# Finally, note that destination can be translated, i.e. you can
# specify a different translation folder per language. Example:
#     PAGES = (
#         ("pages/*.rst", {"en": "pages", "de": "seiten"}, "page.tmpl"),
#         ("pages/*.md", {"en": "pages", "de": "seiten"}, "page.tmpl"),
#     )

POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
    # Old posts
    ("posts_old/*.html", "posts", "post.tmpl"),
)
PAGES = (
    ("pages/*.rst", "pages", "page.tmpl"),
    ("pages/*.md", "pages", "page.tmpl"),
    ("pages/*.txt", "pages", "page.tmpl"),
    ("pages/*.html", "pages", "page.tmpl"),
)


# Below this point, everything is optional

# Post's dates are considered in UTC by default, if you want to use
# another time zone, please set TIMEZONE to match. Check the available
# list from Wikipedia:
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# (e.g. 'Europe/Zurich')
# Also, if you want to use a different time zone in some of your posts,
# you can use the ISO 8601/RFC 3339 format (ex. 2012-03-30T23:00:00+02:00)
TIMEZONE = "Europe/Berlin"

# If you want to use ISO 8601 (also valid RFC 3339) throughout Nikola
# (especially in new_post), set this to True.
# Note that this does not affect DATE_FORMAT.
# FORCE_ISO8601 = False

# Date format used to display post dates. (translatable)
# Used by babel.dates, CLDR style: http://cldr.unicode.org/translation/date-time
# You can also use 'full', 'long', 'medium', or 'short'
# DATE_FORMAT = 'yyyy-MM-dd HH:mm'
DATE_FORMAT = 'yyyy-MM-dd'

# Date format used to display post dates, if local dates are used. (translatable)
# Used by Luxon: https://moment.github.io/luxon/docs/manual/formatting
# Example for presets: {'preset': True, 'format': 'DATE_FULL'}
# LUXON_DATE_FORMAT = {
#     DEFAULT_LANG: {'preset': False, 'format': 'yyyy-MM-dd HH:mm'},
# }

# Date fanciness.
#
# 0 = using DATE_FORMAT and TIMEZONE (without JS)
# 1 = using LUXON_DATE_FORMAT and local user time (JS, using Luxon)
# 2 = using a string like “2 days ago” (JS, using Luxon)
#
# Your theme must support it, Bootstrap already does.
# DATE_FANCINESS = 0

# Customize the locale/region used for a language.
# For example, to use British instead of US English: LOCALES = {'en': 'en_GB'}
# LOCALES = {}

# One or more folders containing files to be copied as-is into the output.
# The format is a dictionary of {source: relative destination}.
# Default is:
# FILES_FOLDERS = {'files': ''}
# Which means copy 'files' into 'output'
FILES_FOLDERS = {'files': 'files'}

# One or more folders containing code listings to be processed and published on
# the site. The format is a dictionary of {source: relative destination}.
# Default is:
# LISTINGS_FOLDERS = {'listings': 'listings'}
# Which means process listings from 'listings' into 'output/listings'

# A mapping of languages to file-extensions that represent that language.
# Feel free to add or delete extensions to any list, but don't add any new
# compilers unless you write the interface for it yourself.
#
# The default compiler for `new_post` is the first entry in the POSTS tuple.
#
# 'rest' is reStructuredText
# 'markdown' is Markdown
# 'html' assumes the file is HTML and just copies it
COMPILERS = {
    "rest": ['.rst', '.txt'],
    "markdown": ['.md', '.mdown', '.markdown'],
    "textile": ['.textile'],
    "txt2tags": ['.t2t'],
    "bbcode": ['.bb'],
    "wiki": ['.wiki'],
    "ipynb": ['.ipynb'],
    "html": ['.html', '.htm'],
    # PHP files are rendered the usual way (i.e. with the full templates).
    # The resulting files have .php extensions, making it possible to run
    # them without reconfiguring your server to recognize them.
    "php": ['.php'],
    # Pandoc detects the input from the source filename
    # but is disabled by default as it would conflict
    # with many of the others.
    # "pandoc": ['.rst', '.md', '.txt'],
}

# Enable reST directives that insert the contents of external files such
# as "include" and "raw." This maps directly to the docutils file_insertion_enabled
# config. See: http://docutils.sourceforge.net/docs/user/config.html#file-insertion-enabled
# REST_FILE_INSERTION_ENABLED = True

# Create by default posts in one file format?
# Set to False for two-file posts, with separate metadata.
# ONE_FILE_POSTS = True

# Preferred metadata format for new posts
# "Nikola": reST comments, wrapped in a HTML comment if needed (default)
# "YAML": YAML wrapped in "---"
# "TOML": TOML wrapped in "+++"
# "Pelican": Native markdown metadata or reST docinfo fields. Nikola style for other formats.
# METADATA_FORMAT = "Nikola"

# Use date-based path when creating posts?
# Can be enabled on a per-post basis with `nikola new_post -d`.
# The setting is ignored when creating pages.
# NEW_POST_DATE_PATH = False

# What format to use when creating posts with date paths?
# Default is '%Y/%m/%d', other possibilities include '%Y' or '%Y/%m'.
# NEW_POST_DATE_PATH_FORMAT = '%Y/%m/%d'

# If this is set to True, the DEFAULT_LANG version will be displayed for
# untranslated posts.
# If this is set to False, then posts that are not translated to a language
# LANG will not be visible at all in the pages in that language.
# SHOW_UNTRANSLATED_POSTS = True

# Nikola supports logo display.  If you have one, you can put the URL here.
# Final output is <img src="LOGO_URL" id="logo" alt="BLOG_TITLE">.
# The URL may be relative to the site root.
# LOGO_URL = ''

# When linking posts to social media, Nikola provides Open Graph metadata
# which is used to show a nice preview. This includes an image preview
# taken from the post's previewimage metadata field.
# This option lets you use an image to be used if the post doesn't have it.
# The default is None, valid values are URLs or output paths like
# "/images/foo.jpg"
# DEFAULT_PREVIEW_IMAGE = None

# If you want to hide the title of your website (for example, if your logo
# already contains the text), set this to False.
# SHOW_BLOG_TITLE = True

# Paths for different autogenerated bits. These are combined with the
# translation paths.

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag RSS_EXTENSION (RSS feed for a tag)
# (translatable)
# TAG_PATH = "categories"

# By default, the list of tags is stored in
#     output / TRANSLATION[lang] / TAG_PATH / index.html
# (see explanation for TAG_PATH). This location can be changed to
#     output / TRANSLATION[lang] / TAGS_INDEX_PATH
# with an arbitrary relative path TAGS_INDEX_PATH.
# (translatable)
# TAGS_INDEX_PATH = "tags.html"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = False
TAG_PAGES_ARE_INDEXES = True

# Set descriptions for tag pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the tag list or index page’s title.
# TAG_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for tag pages. The default is "Posts about TAG".
# TAG_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a tag publicly, you can mark it as hidden.
# The tag will not be displayed on the tag list page and posts.
# Tag pages will still be generated.
HIDDEN_TAGS = ['mathjax']

# Only include tags on the tag list/overview page if there are at least
# TAGLIST_MINIMUM_POSTS number of posts or more with every tag. Every tag
# page is still generated, linked from posts, and included in the sitemap.
# However, more obscure tags can be hidden from the tag index page.
# TAGLIST_MINIMUM_POSTS = 1

# A list of dictionaries specifying tags which translate to each other.
# Format: a list of dicts {language: translation, language2: translation2, …}
# For example:
#   [
#     {'en': 'private', 'de': 'Privat'},
#     {'en': 'work', 'fr': 'travail', 'de': 'Arbeit'},
#   ]
# TAG_TRANSLATIONS = []

# If set to True, a tag in a language will be treated as a translation
# of the literally same tag in all other languages. Enable this if you
# do not translate tags, for example.
# TAG_TRANSLATIONS_ADD_DEFAULTS = True

# Final locations are:
# output / TRANSLATION[lang] / CATEGORY_PATH / index.html (list of categories)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.html (list of posts for a category)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category RSS_EXTENSION (RSS feed for a category)
# (translatable)
# CATEGORY_PATH = "categories"
# CATEGORY_PREFIX = "cat_"

# By default, the list of categories is stored in
#     output / TRANSLATION[lang] / CATEGORY_PATH / index.html
# (see explanation for CATEGORY_PATH). This location can be changed to
#     output / TRANSLATION[lang] / CATEGORIES_INDEX_PATH
# with an arbitrary relative path CATEGORIES_INDEX_PATH.
# (translatable)
# CATEGORIES_INDEX_PATH = "categories.html"

# If CATEGORY_ALLOW_HIERARCHIES is set to True, categories can be organized in
# hierarchies. For a post, the whole path in the hierarchy must be specified,
# using a forward slash ('/') to separate paths. Use a backslash ('\') to escape
# a forward slash or a backslash (i.e. '\//\\' is a path specifying the
# subcategory called '\' of the top-level category called '/').
CATEGORY_ALLOW_HIERARCHIES = False
# If CATEGORY_OUTPUT_FLAT_HIERARCHY is set to True, the output written to output
# contains only the name of the leaf category and not the whole path.
CATEGORY_OUTPUT_FLAT_HIERARCHY = False

# If CATEGORY_PAGES_ARE_INDEXES is set to True, each category's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# CATEGORY_PAGES_ARE_INDEXES = False
CATEGORY_PAGES_ARE_INDEXES = True

# Set descriptions for category pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the category list or index page’s title.
# CATEGORY_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for category pages. The default is "Posts about CATEGORY".
# CATEGORY_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a category publicly, you can mark it as hidden.
# The category will not be displayed on the category list page.
# Category pages will still be generated.
HIDDEN_CATEGORIES = []

# A list of dictionaries specifying categories which translate to each other.
# Format: a list of dicts {language: translation, language2: translation2, …}
# See TAG_TRANSLATIONS example above.
# CATEGORY_TRANSLATIONS = []

# If set to True, a category in a language will be treated as a translation
# of the literally same category in all other languages. Enable this if you
# do not translate categories, for example.
# CATEGORY_TRANSLATIONS_ADD_DEFAULTS = True

# If no category is specified in a post, the destination path of the post
# can be used in its place. This replaces the sections feature. Using
# category hierarchies is recommended.
# CATEGORY_DESTPATH_AS_DEFAULT = False

# If True, the prefix will be trimmed from the category name, eg. if the
# POSTS destination is "foo/bar", and the path is "foo/bar/baz/quux",
# the category will be "baz/quux" (or "baz" if only the first directory is considered).
# Note that prefixes coming from translations are always ignored.
# CATEGORY_DESTPATH_TRIM_PREFIX = False

# If True, only the first directory of a path will be used.
# CATEGORY_DESTPATH_FIRST_DIRECTORY_ONLY = True

# Map paths to prettier category names. (translatable)
# CATEGORY_DESTPATH_NAMES = {
#    DEFAULT_LANG: {
#        'webdev': 'Web Development',
#        'webdev/django': 'Web Development/Django',
#        'random': 'Odds and Ends',
#    },
# }

# By default, category indexes will appear in CATEGORY_PATH and use
# CATEGORY_PREFIX. If this is enabled, those settings will be ignored (except
# for the index) and instead, they will follow destination paths (eg. category
# 'foo' might appear in 'posts/foo'). If the category does not come from a
# destpath, first entry in POSTS followed by the category name will be used.
# For this setting, category hierarchies are required and cannot be flattened.
# CATEGORY_PAGES_FOLLOW_DESTPATH = False

# If ENABLE_AUTHOR_PAGES is set to True and there is more than one
# author, author pages are generated.
# ENABLE_AUTHOR_PAGES = True

# Path to author pages. Final locations are:
# output / TRANSLATION[lang] / AUTHOR_PATH / index.html (list of authors)
# output / TRANSLATION[lang] / AUTHOR_PATH / author.html (list of posts by an author)
# output / TRANSLATION[lang] / AUTHOR_PATH / author RSS_EXTENSION (RSS feed for an author)
# (translatable)
# AUTHOR_PATH = "authors"

# If AUTHOR_PAGES_ARE_INDEXES is set to True, each author's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# AUTHOR_PAGES_ARE_INDEXES = False

# Set descriptions for author pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the author list or index page’s title.
# AUTHOR_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "Juanjo Conti": "Python coder and writer.",
#        "Roberto Alsina": "Nikola father."
#    },
# }


# If you do not want to display an author publicly, you can mark it as hidden.
# The author will not be displayed on the author list page and posts.
# Tag pages will still be generated.
HIDDEN_AUTHORS = ['Guest']

# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
# (translatable)
# INDEX_PATH = ""

# Optional HTML that displayed on “main” blog index.html files.
# May be used for a greeting. (translatable)
FRONT_INDEX_HEADER = {
    DEFAULT_LANG: ''
}

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
# CREATE_SINGLE_ARCHIVE = False
# Create year, month, and day archives each with a (long) list of posts
# (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
# CREATE_FULL_ARCHIVES = False
# If monthly archives or full archives are created, adds also one archive per day
# CREATE_DAILY_ARCHIVE = False
# Create previous, up, next navigation links for archives
# CREATE_ARCHIVE_NAVIGATION = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / DAY / index.html
# (translatable)
# ARCHIVE_PATH = ""
# ARCHIVE_FILENAME = "archive.html"

# If ARCHIVES_ARE_INDEXES is set to True, each archive page which contains a list
# of posts will contain the posts themselves. If set to False, it will be just a
# list of links.
# ARCHIVES_ARE_INDEXES = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Extension for RSS feed files
# RSS_EXTENSION = ".xml"

# RSS filename base (without extension); used for indexes and galleries.
# (translatable)
# RSS_FILENAME_BASE = "rss"

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / RSS_FILENAME_BASE RSS_EXTENSION
# (translatable)
# RSS_PATH = ""

# Final location for the blog main Atom feed is:
# output / TRANSLATION[lang] / ATOM_PATH / ATOM_FILENAME_BASE ATOM_EXTENSION
# (translatable)
# ATOM_PATH = ""

# Atom filename base (without extension); used for indexes.
# (translatable)
ATOM_FILENAME_BASE = "feed"

# Extension for Atom feed files
# ATOM_EXTENSION = ".atom"

# Slug the Tag URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# Slug the Author URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_AUTHOR_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
# REDIRECTIONS = []
REDIRECTIONS = [
("art/100_guenther-oettinger-als-fremdsp.html", "/pages/sorry/index.html"),
("art/101_hype-um-apple-ipad.html", "/pages/sorry/index.html"),
("art/103_lust_auf_ne_spritztour.html", "/pages/sorry/index.html"),
("art/104_image-fulgurator.html", "/pages/sorry/index.html"),
("art/106_pikapika.html", "/pages/sorry/index.html"),
("art/107_probleme-mit-eingebundenen-vid.html", "/pages/sorry/index.html"),
("art/108_einaeugiger-bert.html", "/pages/sorry/index.html"),
("art/109_sensation-so-ist-pythagoras-ge.html", "/pages/sorry/index.html"),
("art/10_minuscule-insekten-ganz-privat.html", "/pages/sorry/index.html"),
("art/110_mein-erster-stop-motion-film.html", "/pages/sorry/index.html"),
("art/111_astronauten-in-der-iss-schwere.html", "/pages/sorry/index.html"),
("art/112_stop-and-go-da-blick-noch-wer-.html", "/pages/sorry/index.html"),
("art/115_nils-als-astronaut-mir-rakete.html", "/pages/sorry/index.html"),
("art/116_ein-guter-tag-fuer-die-freihei.html", "/pages/sorry/index.html"),
("art/118_heute-vor-einem-jahr-koelner-s.html", "/pages/sorry/index.html"),
("art/119_hartnaeckige-leichen-im-window.html", "/pages/sorry/index.html"),
("art/11_windows-eingesperrt.html", "/pages/sorry/index.html"),
("art/121_zimmer-frei.html", "/pages/sorry/index.html"),
("art/122_update-manager-fuer-windows.html", "/pages/sorry/index.html"),
("art/123_unlocker-gesperrte-dateien-loe.html", "/pages/sorry/index.html"),
("art/124_dont-be-evil.html", "/pages/sorry/index.html"),
("art/125_vor-50-jahren-startete-die-ers.html", "/pages/sorry/index.html"),
("art/126_wie-funktionieren-und-wozu-bra.html", "/pages/sorry/index.html"),
("art/127_neu-google-home-view.html", "/pages/sorry/index.html"),
("art/128_ehe-helpdesk.html", "/pages/sorry/index.html"),
("art/129_guter-tag.html", "/pages/sorry/index.html"),
("art/12_usb-in-der-virtual-machine-unt.html", "/pages/sorry/index.html"),
("art/130_zugerschwg-offener-brief-des-a.html", "/pages/sorry/index.html"),
("art/131_augmented-reality.html", "/pages/sorry/index.html"),
("art/132_bei-uns-piepts.html", "/pages/sorry/index.html"),
("art/133_blaumeisen-sammeln-eifrig-nist.html", "/pages/sorry/index.html"),
("art/134_nistkasten-bilder-nun-auf-flic.html", "/pages/sorry/index.html"),
("art/135_erste-erfahrungen-mit-geocachi.html", "/pages/sorry/index.html"),
("art/136_das-ende-des-pariser-urkilos.html", "/pages/sorry/index.html"),
("art/137_mehr-glueck-beim-geocachen.html", "/pages/sorry/index.html"),
("art/138_ein-fingerzeig.html", "/pages/sorry/index.html"),
("art/139_die-blaumeisen-sorgen-fuer-nac.html", "/pages/sorry/index.html"),
("art/13_zeitsynchronisation.html", "/pages/sorry/index.html"),
("art/140_gczii-aktuell-keine-cache-info.html", "/pages/sorry/index.html"),
("art/142_werbespot-der-piratenpartei-zu.html", "/pages/sorry/index.html"),
("art/143_nistkasten-einmal-uebernachtun.html", "/pages/sorry/index.html"),
("art/145_die-eier-sind-da.html", "/pages/sorry/index.html"),
("art/146_die-muppets-stand-by-me.html", "/pages/sorry/index.html"),
("art/147_kueken-sind-geschluepft.html", "/pages/sorry/index.html"),
("art/148_bilder-vom-meisen-nachwuchs.html", "/pages/sorry/index.html"),
("art/149_aus-dem-leben-von-meiseneltern.html", "/pages/sorry/index.html"),
("art/14_usbprog.html", "/pages/sorry/index.html"),
("art/150_datumsformat-in-joomla-aendern.html", "/pages/sorry/index.html"),
("art/151_schwund-bei-den-meisen.html", "/pages/sorry/index.html"),
("art/152_schwund-bei-den-meisen-2.html", "/pages/sorry/index.html"),
("art/153_google-street-view-der-grosse-.html", "/pages/sorry/index.html"),
("art/154_gefaehrliche-handystrahlung.html", "/pages/sorry/index.html"),
("art/155_die-meisen-hatten-besuch.html", "/pages/sorry/index.html"),
("art/156_bye-bye-meisen.html", "/pages/sorry/index.html"),
("art/157_modellautos-flott-gemacht.html", "/pages/sorry/index.html"),
("art/158_nistkasten-20.html", "/pages/sorry/index.html"),
("art/159_flashmobs-gegen-kernkraft-in-d.html", "/pages/sorry/index.html"),
("art/15_kassetten-digitalisieren.html", "/pages/sorry/index.html"),
("art/160_steve-jobs-der-digitale-diktat.html", "/pages/sorry/index.html"),
("art/161_steve-jobs-der-digitale-diktat.html", "/pages/sorry/index.html"),
("art/162_steve-jobs-der-digitale-diktat.html", "/pages/sorry/index.html"),
("art/163_top-kill.html", "/pages/sorry/index.html"),
("art/164_blog-zum-start-des-deutschen-s.html", "/pages/sorry/index.html"),
("art/165_neue-rundfunkgebuehren-ab-2013.html", "/pages/sorry/index.html"),
("art/166_htc-touch-diamond-2-wo-ist-das.html", "/pages/sorry/index.html"),
("art/167_reparaturumbau-der-ferngesteue.html", "/pages/sorry/index.html"),
("art/168_wasserverbrauch-waehrend-wm.html", "/pages/sorry/index.html"),
("art/169_deutscher-radarsatellit-tandem.html", "/pages/sorry/index.html"),
("art/16_du-bist-terrorist.html", "/pages/sorry/index.html"),
("art/170_arte-dokumentation-ueber-nordk.html", "/pages/sorry/index.html"),
("art/171_ssh-zugriff-in-opensuse-aktivi.html", "/pages/sorry/index.html"),
("art/172_karikatur-zur-oelkatastrophe-i.html", "/pages/sorry/index.html"),
("art/173_terminal-multiplexer-screen-fu.html", "/pages/sorry/index.html"),
("art/174_ssh-client-fuer-windows-mobile.html", "/pages/sorry/index.html"),
("art/175_odyssee-durch-die-linux-distro.html", "/pages/sorry/index.html"),
("art/176_lego_bauanleitungen_downloaden.html", "/pages/sorry/index.html"),
("art/177_bootchart_durchblick_durch_den.html", "/pages/sorry/index.html"),
("art/178_samsung-scx-4200-unter-opensus.html", "/pages/sorry/index.html"),
("art/17_eier-ueber-haeuser-werfen.html", "/pages/sorry/index.html"),
("art/180_kommandozeile-und-zwischenabla.html", "/pages/sorry/index.html"),
("art/181_liquid-democracy.html", "/pages/sorry/index.html"),
("art/182_gameboy-emulator.html", "/pages/sorry/index.html"),
("art/183_it-infrastuktur-in-deutschland.html", "/pages/sorry/index.html"),
("art/184_hilfe-fuer-pakistan.html", "/pages/sorry/index.html"),
("art/187_hab-mich-von-suse-getrennt.html", "/pages/sorry/index.html"),
("art/188_lecker-sushi.html", "/pages/sorry/index.html"),
("art/189_google-anzeigen-kampagne.html", "/pages/sorry/index.html"),
("art/18_dropbox-intelligenter-online-s.html", "/pages/sorry/index.html"),
("art/190_pdfsam-pdfs-bearbeiten.html", "/pages/sorry/index.html"),
("art/191_elektronischer-perso.html", "/pages/sorry/index.html"),
("art/192_bsi-basisschutz-leicht-gemacht.html", "/pages/sorry/index.html"),
("art/193_probleme-mit-include-dateien-b.html", "/pages/sorry/index.html"),
("art/194_film-qspace-touristsq-im-septe.html", "/pages/sorry/index.html"),
("art/195_indect-eu-plant-ueberwachung-m.html", "/pages/sorry/index.html"),
("art/196_gps-track-aufzeichnungen-auf-e.html", "/pages/sorry/index.html"),
("art/197_dont-be-evil-reloaded.html", "/pages/sorry/index.html"),
("art/198_elektronischer-perso-reloaded.html", "/pages/sorry/index.html"),
("art/199_esa-will-mondlander.html", "/pages/sorry/index.html"),
("art/19_opennas_1_9_fuer_all6250_und_l.html", "/pages/sorry/index.html"),
("art/1_neue-webseite-online.html", "/pages/sorry/index.html"),
("art/200_buugle.html", "/pages/sorry/index.html"),
("art/201_good-bye-champ.html", "/pages/sorry/index.html"),
("art/202_uebereifrigen-bildschirmschone.html", "/pages/sorry/index.html"),
("art/203_neue-schwachstelle-im-eperso-e.html", "/pages/sorry/index.html"),
("art/204_rosetta-mission-anhand-lego-mo.html", "/pages/sorry/index.html"),
("art/205_vor-63-jahren-startete-sputnik.html", "/pages/sorry/index.html"),
("art/206_teleskop-ausgegraben.html", "/pages/sorry/index.html"),
("art/207_konsumwahn-und-elektroschrott.html", "/pages/sorry/index.html"),
("art/208_broschuere-zu-dos-und-donts-im.html", "/pages/sorry/index.html"),
("art/20_sprunghoehe-auf-dem-mond.html", "/pages/sorry/index.html"),
("art/210_terrorhysterie-und-ihre-auswir.html", "/pages/sorry/index.html"),
("art/211_chipaxxs-das-auslesen-von-rfid.html", "/pages/sorry/index.html"),
("art/212_linkvalidator-skript-ueberarbe.html", "/pages/sorry/index.html"),
("art/213_holpriger-start-des-epersos.html", "/pages/sorry/index.html"),
("art/214_woran-erkenne-ich-einen-terror.html", "/pages/sorry/index.html"),
("art/215_dezember-raumfahrttechnisch-er.html", "/pages/sorry/index.html"),
("art/216_dokumentation-akte-ccc.html", "/pages/sorry/index.html"),
("art/217_elektrischer-reporter-zur-netz.html", "/pages/sorry/index.html"),
("art/218_alte_ssh_host_keys_aus_der_dat.html", "/pages/sorry/index.html"),
("art/219_jhelioviewer-fuer-sonnenanbete.html", "/pages/sorry/index.html"),
("art/21_mathematische-gleichungen-in-j.html", "/pages/sorry/index.html"),
("art/220_horstbox-login-und-referrer.html", "/pages/sorry/index.html"),
("art/221_christmas-20.html", "/pages/sorry/index.html"),
("art/222_toll-der-neue-perso.html", "/pages/sorry/index.html"),
("art/223_alle-kinder-lernen-lesen.html", "/pages/sorry/index.html"),
("art/224_total-commander-fuer-windows-m.html", "/pages/sorry/index.html"),
("art/225_pocketputty-fuer-windows-mobil.html", "/pages/sorry/index.html"),
("art/226_neuer-nas-server-laeuft-networ.html", "/pages/sorry/index.html"),
("art/227_tragisch-warum-die-saebelzahn-.html", "/pages/sorry/index.html"),
("art/228_joomla-16-verfuegbar.html", "/pages/sorry/index.html"),
("art/229_fiktive-zdf-doku-q2030-austand.html", "/pages/sorry/index.html"),
("art/22_keepass-fuer-unterwegs.html", "/pages/sorry/index.html"),
("art/230_terrasar-x-und-tandem-x-als-do.html", "/pages/sorry/index.html"),
("art/231_mein-browser-macht-keks-diaet.html", "/pages/sorry/index.html"),
("art/232_hugin-opensource-panorama-tool.html", "/pages/sorry/index.html"),
("art/233_strato-speedplus-das-rockt.html", "/pages/sorry/index.html"),
("art/234_moby-wait-for-me.html", "/pages/sorry/index.html"),
("art/236_dostips-the-dos-batch-guide.html", "/pages/sorry/index.html"),
("art/237_dead-drops-digitale-oeffentlic.html", "/pages/sorry/index.html"),
("art/238_keepassx-mag-keine-symbolische.html", "/pages/sorry/index.html"),
("art/23_screenshots-auf-dem-pocketpc-e.html", "/pages/sorry/index.html"),
("art/240_geplante-obsoleszens-konsumier.html", "/pages/sorry/index.html"),
("art/241_einfacher-weg-wiedergabelisten.html", "/pages/sorry/index.html"),
("art/242_moby-ep-qbe-the-oneq-kostenlos.html", "/pages/sorry/index.html"),
("art/243_cookiesafe-funktioniert-aktuel.html", "/pages/sorry/index.html"),
("art/244_elektroschrott-gehoert-bald-wi.html", "/pages/sorry/index.html"),
("art/245_navigationssystem-anno-1920.html", "/pages/sorry/index.html"),
("art/246_ihr-bundeskriminalamt-kommt-.html", "/pages/sorry/index.html"),
("art/247_eieiei-was-haben-wir-denn-da.html", "/pages/sorry/index.html"),
("art/248_space-shuttle-ist-das-konzept-.html", "/pages/sorry/index.html"),
("art/249_gczii-komfortabel-auf-dem-smar.html", "/pages/sorry/index.html"),
("art/24_pikapika-geniale-lichtkunst.html", "/pages/sorry/index.html"),
("art/250_die-kohlmeisen-sind-gestern-ge.html", "/pages/sorry/index.html"),
("art/251_horror-ubuntu-update.html", "/pages/sorry/index.html"),
("art/252_update-aus-dem-nistkasten.html", "/pages/sorry/index.html"),
("art/253_ein-ei-ist-noch-nicht-geschlue.html", "/pages/sorry/index.html"),
("art/254_es-sind-doch-acht.html", "/pages/sorry/index.html"),
("art/255_embedde-player-in-diesem-blog-.html", "/pages/sorry/index.html"),
("art/256_geeks-meet-lego.html", "/pages/sorry/index.html"),
("art/257_nestlinge-werden-langsam-flueg.html", "/pages/sorry/index.html"),
("art/258_verschwendung-kostbarer-lebens.html", "/pages/sorry/index.html"),
("art/259_garmin-bringt-neue-etrex-gerae.html", "/pages/sorry/index.html"),
("art/25_neu-stopp-schilder-im-internet.html", "/pages/sorry/index.html"),
("art/260_herzlichen-glueckwunsch-christ.html", "/pages/sorry/index.html"),
("art/261_sind-sie-katholik.html", "/pages/sorry/index.html"),
("art/262_ics-kalender-import-in-windows.html", "/pages/sorry/index.html"),
("art/265_milestone-caching-in-koeln.html", "/pages/sorry/index.html"),
("art/266_video-warum-creative-commons.html", "/pages/sorry/index.html"),
("art/267_video-vom-lost-place-cache-qst.html", "/pages/sorry/index.html"),
("art/268_bald-bald-bald-garmin-dakota-2.html", "/pages/sorry/index.html"),
("art/269_impressionen-vom-chaos-communi.html", "/pages/sorry/index.html"),
("art/26_fleischeslust.html", "/pages/sorry/index.html"),
("art/270_geocaching-challenges-sind-onl.html", "/pages/sorry/index.html"),
("art/271_20-jahre-linux-herzlichen-glue.html", "/pages/sorry/index.html"),
("art/273_factoring-the-time.html", "/pages/sorry/index.html"),
("art/274_staatstrojaner.html", "/pages/sorry/index.html"),
("art/275_ubuntu-rolle-rueckwaerts.html", "/pages/sorry/index.html"),
("art/276_ssl-in-der-krise.html", "/pages/sorry/index.html"),
("art/277_gott-sieht-alles.html", "/pages/sorry/index.html"),
("art/278_qr_code_mit_kontaktdaten_erste.html", "/pages/sorry/index.html"),
("art/279_40_jahre_mikroprozessor.html", "/pages/sorry/index.html"),
("art/27_das-wahre-gesicht-des-obamas.html", "/pages/sorry/index.html"),
("art/280_mein-geocaching-wochenende-mit.html", "/pages/sorry/index.html"),
("art/284_gefaehrlich_gebrauchte_speiche.html", "/pages/sorry/index.html"),
("art/287_den-bock-zum-gaertner-machen.html", "/pages/sorry/index.html"),
("art/288_die-erfindung-des-fernrohrs-.html", "/pages/sorry/index.html"),
("art/28_krieg-der-welten-von-o-welles-.html", "/pages/sorry/index.html"),
("art/290_geloest-auto-type-bug-in-keepa.html", "/pages/sorry/index.html"),
("art/291_digitales-lesen-und-oeffentlic.html", "/pages/sorry/index.html"),
("art/292_samsung-scx-4200-laeuft-unter-.html", "/pages/sorry/index.html"),
("art/293_wlan_empfang_ueber_geeignete_k.html", "/pages/sorry/index.html"),
("art/294_syntax_error_im_spiegel.html", "/pages/sorry/index.html"),
("art/295_lost-place-qstadt-im-waldq.html", "/pages/sorry/index.html"),
("art/296_neues_blog_backbone_in_arbeit.html", "/pages/sorry/index.html"),
("art/297_hdparm_festplatte_eine_auszeit.html", "/pages/sorry/index.html"),
("art/298_wirklichkeit-ist-der-zweckmaes.html", "/pages/sorry/index.html"),
("art/299_maus-geschwindigkeit-unter-ubu.html", "/pages/sorry/index.html"),
("art/29_suchmaschinen-zu-firefox-suche.html", "/pages/sorry/index.html"),
("art/2_rex-the-dog-bubblicious-stop-m.html", "/pages/sorry/index.html"),
("art/300_revolution-os-die-geschichte-v.html", "/pages/sorry/index.html"),
("art/301_aktuelles-vom-neuen-blog-backb.html", "/pages/sorry/index.html"),
("art/302_nasas-rover-curiosity-auf-dem-.html", "/pages/sorry/index.html"),
("art/303_choasradiocccde-down.html", "/pages/sorry/index.html"),
("art/304_perl-datums-und-zeiteingabe-ue.html", "/pages/sorry/index.html"),
("art/305_screenshots-von-perlpress.html", "/pages/sorry/index.html"),
("art/307_jabberorg-opfer-einer-dos-atta.html", "/pages/sorry/index.html"),
("art/308_wer-so-heisst-muss-perfekt-sei.html", "/pages/sorry/index.html"),
("art/30_newcomb-benford-analyse-bundes.html", "/pages/sorry/index.html"),
("art/310_server-status-info-via-xmppjab.html", "/pages/sorry/index.html"),
("art/311_stop-motion-video-the-marker-m.html", "/pages/sorry/index.html"),
("art/312_traceroute_wo_lang_laufen_mein.html", "/pages/sorry/index.html"),
("art/313_firmware-updates-bei-garmin-oh.html", "/pages/sorry/index.html"),
("art/314_koordinateposition-mit-marker-.html", "/pages/sorry/index.html"),
("art/315_http-fehler-503-beim-einreiche.html", "/pages/sorry/index.html"),
("art/316_dosensuche.html", "/pages/sorry/index.html"),
("art/317_technischer-fortschritt.html", "/pages/sorry/index.html"),
("art/318_facebook-become-a-fan.html", "/pages/sorry/index.html"),
("art/319_deja-vu-.html", "/pages/sorry/index.html"),
("art/31_gruener-damm-digitale-zensur-i.html", "/pages/sorry/index.html"),
("art/320_mal_wieder_ein_posting_zum_aut.html", "/pages/sorry/index.html"),
("art/321_immer-wieder-nett-samsung-scx-.html", "/pages/sorry/index.html"),
("art/322_best-of-web-3.html", "/pages/sorry/index.html"),
("art/323_leistungsschutzrecht-stoppen.html", "/pages/sorry/index.html"),
("art/324_notification_service_fuer_upda.html", "/pages/sorry/index.html"),
("art/325_suechtig-nach-pinball-machines.html", "/pages/sorry/index.html"),
("art/326_gebrauchte-speicherkarte-2.html", "/pages/sorry/index.html"),
("art/327_taegliches_frisches_obst_gemue.html", "/pages/sorry/index.html"),
("art/328_der-brief-als-reines-qbad-news.html", "/pages/sorry/index.html"),
("art/329_beobachtung-des-erdvorbeiflugs.html", "/pages/sorry/index.html"),
("art/32_gewitter-vom-weltraum-aus-beob.html", "/pages/sorry/index.html"),
("art/331_gelbes_feuerwehr_auto.html", "/pages/sorry/index.html"),
("art/332_avra_1_3_0_kompilieren.html", "/pages/sorry/index.html"),
("art/333_led-cube.html", "/pages/sorry/index.html"),
("art/334_mini-howto-atmel-avr-risc-mc-u.html", "/pages/sorry/index.html"),
("art/335_erster-erfolgreiche-3d-positio.html", "/pages/sorry/index.html"),
("art/336_linux_bash_dateinamen_in_lower.html", "/pages/sorry/index.html"),
("art/337_ip_adresse_eines_geraetes_im_l.html", "/pages/sorry/index.html"),
("art/338_nut-again-simons-cat.html", "/pages/sorry/index.html"),
("art/33_cygwin-leistungsfaehige-linuxk.html", "/pages/sorry/index.html"),
("art/340_fototour-mit-canon-eos-400d.html", "/pages/sorry/index.html"),
("art/342_ssh_zugriff_auf_strato_webspac.html", "/pages/sorry/index.html"),
("art/344_impressum.html", "/pages/sorry/index.html"),
("art/345_neue_webseite_online.html", "/pages/sorry/index.html"),
("art/348_stetig_kleine_veraenderungen.html", "/pages/sorry/index.html"),
("art/349_perlpress_auf_github_veroeffen.html", "/pages/sorry/index.html"),
("art/34_pen-trick-fail-dummes-fleisch-.html", "/pages/sorry/index.html"),
("art/35_pio-macht-das-brennen-langsam.html", "/pages/sorry/index.html"),
("art/360_openrhreinruhr_2013.html", "/pages/sorry/index.html"),
("art/361_radio_code_renault_gamme.html", "/pages/sorry/index.html"),
("art/362_suchmaschinen.html", "/pages/sorry/index.html"),
("art/363_jp2a_-_ascii_kunst.html", "/pages/sorry/index.html"),
("art/36_40-jahre-mondlandung.html", "/pages/sorry/index.html"),
("art/364_youtube_api_ueberpruefen_ob_vi.html", "/pages/sorry/index.html"),
("art/365_atmel_avr_risc_uc_unter_gnulin.html", "/pages/sorry/index.html"),
("art/366_linux_verzeichnis_fuer_gemeins.html", "/pages/sorry/index.html"),
("art/367_wernher_von_braun_visioonaer_m.html", "/pages/sorry/index.html"),
("art/368_fug_--_rfo.html", "/pages/sorry/index.html"),
("art/369_linux_datei_vor_versehentliche.html", "/pages/sorry/index.html"),
("art/370_fortschrittsanzeige_fuer_gpart.html", "/pages/sorry/index.html"),
("art/375_fish_shell.html", "/pages/sorry/index.html"),
("art/376_artemis_-_subterranean_hidden.html", "/pages/sorry/index.html"),
("art/377_fehlender_speicherplatz_bei_li.html", "/pages/sorry/index.html"),
("art/378_behoerdisch.html", "/pages/sorry/index.html"),
("art/379_erfahrungsbericht_dokumentatio.html", "/pages/sorry/index.html"),
("art/37_disney-und-v-braun-popularisie.html", "/pages/sorry/index.html"),
("art/380_astrofotografie_mit_der_digita.html", "/pages/sorry/index.html"),
("art/382_pomplamoose_-_pharrel_meshup.html", "/pages/sorry/index.html"),
("art/384_musik-clips_von_youttube_als_m.html", "/pages/sorry/index.html"),
("art/385_xum1541_dateien_zwischen_linux.html", "/pages/sorry/index.html"),
("art/38_hochaufloesende-lro-bilder-der.html", "/pages/sorry/index.html"),
("art/39_lisa-laufroboter-der-uni-hanno.html", "/pages/sorry/index.html"),
("art/3_allvideoplugin-fuer-joomla.html", "/pages/sorry/index.html"),
("art/40_imma-aerga-middi-dechnig-.html", "/pages/sorry/index.html"),
("art/41_flatrate-schneiden.html", "/pages/sorry/index.html"),
("art/42_baubericht-ferngesteuerte-ente.html", "/pages/sorry/index.html"),
("art/43_kommentar-funktion-aktiviert.html", "/pages/sorry/index.html"),
("art/44_ich-bin-pirat.html", "/pages/sorry/index.html"),
("art/45_jungfernfahrt-der-ferngesteuer.html", "/pages/sorry/index.html"),
("art/46_piratenpartei-werbevideo.html", "/pages/sorry/index.html"),
("art/47_neu-feiere-geburtstag-umsonst-.html", "/pages/sorry/index.html"),
("art/48_openoffice-beine-machen.html", "/pages/sorry/index.html"),
("art/49_troisdorfer-piraten-ruesten-fu.html", "/pages/sorry/index.html"),
("art/4_story-of-stuff-die-kehrseite-u.html", "/pages/sorry/index.html"),
("art/50_alles-schwindel-bemannte-mondl.html", "/pages/sorry/index.html"),
("art/51_schaeubles-schoene-neue-welt.html", "/pages/sorry/index.html"),
("art/52_die-gute-alte-zeit-.html", "/pages/sorry/index.html"),
("art/53_rette-deine-freiheit.html", "/pages/sorry/index.html"),
("art/54_der-server-opennasinfo-ist-vor.html", "/pages/sorry/index.html"),
("art/55_opennas-server-umgezogen.html", "/pages/sorry/index.html"),
("art/56_bundestagswahl-danke-troisdorf.html", "/pages/sorry/index.html"),
("art/57_un-spider-katastrophenhilfe-au.html", "/pages/sorry/index.html"),
("art/58_neues-thinkpad.html", "/pages/sorry/index.html"),
("art/59_the-periodic-table-of-videos.html", "/pages/sorry/index.html"),
("art/5_hurra-die-nas-ist-da.html", "/pages/sorry/index.html"),
("art/60_system-wiederherstellung-mit-d.html", "/pages/sorry/index.html"),
("art/61_mysqldumper-datenbanken-komfor.html", "/pages/sorry/index.html"),
("art/62_thinkpad-r400-kleiner-wehmutst.html", "/pages/sorry/index.html"),
("art/63_clown-im-weltraum.html", "/pages/sorry/index.html"),
("art/64_taz--bild.html", "/pages/sorry/index.html"),
("art/65_das-ging-ja-mal-fix-.html", "/pages/sorry/index.html"),
("art/66_opennas-server-umgezogen.html", "/pages/sorry/index.html"),
("art/67_externe-links-in-joomla-ueberp.html", "/pages/sorry/index.html"),
("art/68_05-09102009-spacecraft-operati.html", "/pages/sorry/index.html"),
("art/69_peenemuende.html", "/pages/sorry/index.html"),
("art/6_pegelwander-testschaltung.html", "/pages/sorry/index.html"),
("art/70_verfressener-hund.html", "/pages/sorry/index.html"),
("art/71_umweltplakette-bequem-online-b.html", "/pages/sorry/index.html"),
("art/72_forschung-rettet-die-welt.html", "/pages/sorry/index.html"),
("art/73_bundestagspetition-zu-open-acc.html", "/pages/sorry/index.html"),
("art/74_dat-jibbets-nur-in-koeln.html", "/pages/sorry/index.html"),
("art/76_deutsche-mondlandung.html", "/pages/sorry/index.html"),
("art/77_was-kommt-nach-umts.html", "/pages/sorry/index.html"),
("art/78_zeitreise-prince-of-persia.html", "/pages/sorry/index.html"),
("art/79_frohe-weihnachten.html", "/pages/sorry/index.html"),
("art/7_pegelwandler-in-nas-einbauen.html", "/pages/sorry/index.html"),
("art/80_iso-abbilder-unter-windows-mou.html", "/pages/sorry/index.html"),
("art/81_frohes-neues-jahr.html", "/pages/sorry/index.html"),
("art/82_mogeln-in-prince-of-persia.html", "/pages/sorry/index.html"),
("art/83_man-brennt-der-lange.html", "/pages/sorry/index.html"),
("art/84_gibt-es-eine-web20-generation.html", "/pages/sorry/index.html"),
("art/85_absichern-des-wlan.html", "/pages/sorry/index.html"),
("art/86_das-mysterium-heizkoerper-vent.html", "/pages/sorry/index.html"),
("art/87_virtuelle-desktops-unter-windo.html", "/pages/sorry/index.html"),
("art/88_unterirdische-performance-bei-.html", "/pages/sorry/index.html"),
("art/89_die-datenkrake-google.html", "/pages/sorry/index.html"),
("art/8_kabel-flechten.html", "/pages/sorry/index.html"),
("art/90_alles-augenwischerei-sicherhei.html", "/pages/sorry/index.html"),
("art/91_brief-feedreader-fuer-firefox.html", "/pages/sorry/index.html"),
("art/92_wieso-nacktscanner.html", "/pages/sorry/index.html"),
("art/93_haitis-immobilienkrise.html", "/pages/sorry/index.html"),
("art/94_keepass-passwort-datenbank-mit.html", "/pages/sorry/index.html"),
("art/95_joomla-zugriffszaehler-fuer-al.html", "/pages/sorry/index.html"),
("art/96_online-petition-gegen-elena.html", "/pages/sorry/index.html"),
("art/97_auto-type-bei-keepassx.html", "/pages/sorry/index.html"),
("art/98_windows-tool-pfad-in-zwischena.html", "/pages/sorry/index.html"),
("art/99_path-scanner-dateien-mit-lange.html", "/pages/sorry/index.html"),
("art/9_opennas_installieren.html", "/pages/sorry/index.html"),
("tag/754_ssl/index.html", "/pages/sorry/index.html"),
("tag/694_schwerefeld/index.html", "/pages/sorry/index.html"),
("tag/893_tmc/index.html", "/pages/sorry/index.html"),
("tag/705_wdr/index.html", "/pages/sorry/index.html"),
("tag/479_wifi/index.html", "/pages/sorry/index.html"),
("tag/639_caschys_blog/index.html", "/pages/sorry/index.html"),
("tag/706_bericht_aus_bruessel/index.html", "/pages/sorry/index.html"),
("tag/43_eierwurf/index.html", "/pages/sorry/index.html"),
("tag/518_bp/index.html", "/pages/sorry/index.html"),
("tag/52_astronaut/index.html", "/pages/sorry/index.html"),
("tag/682_plusminus/index.html", "/pages/sorry/index.html"),
("tag/595_bootchart/index.html", "/pages/sorry/index.html"),
("tag/621_scummvm/index.html", "/pages/sorry/index.html"),
("tag/570_ssh/index.html", "/pages/sorry/index.html"),
("tag/716_osten/index.html", "/pages/sorry/index.html"),
("tag/1027_wysiwyg/index.html", "/pages/sorry/index.html"),
("tag/233_oberpfaffenhofen/index.html", "/pages/sorry/index.html"),
("tag/548_setup/index.html", "/pages/sorry/index.html"),
("tag/86_obama/index.html", "/pages/sorry/index.html"),
("tag/358_zwischenablage/index.html", "/pages/sorry/index.html"),
("tag/37_zensur/page2.html", "/pages/sorry/index.html"),
("tag/37_zensur/index.html", "/pages/sorry/index.html"),
("tag/255_fahrzeug/index.html", "/pages/sorry/index.html"),
("tag/171_merkel/index.html", "/pages/sorry/index.html"),
("tag/672_karte/index.html", "/pages/sorry/index.html"),
("tag/612_visualboy_advance/index.html", "/pages/sorry/index.html"),
("tag/766_dragon/index.html", "/pages/sorry/index.html"),
("tag/314_virtual_desktop/index.html", "/pages/sorry/index.html"),
("tag/5_joomla/page3.html", "/pages/sorry/index.html"),
("tag/5_joomla/page2.html", "/pages/sorry/index.html"),
("tag/5_joomla/index.html", "/pages/sorry/index.html"),
("tag/319_vossware/index.html", "/pages/sorry/index.html"),
("tag/809_acpi/index.html", "/pages/sorry/index.html"),
("tag/626_flutkatastrophe/index.html", "/pages/sorry/index.html"),
("tag/935_baronin/index.html", "/pages/sorry/index.html"),
("tag/207_grub/index.html", "/pages/sorry/index.html"),
("tag/717_westen/index.html", "/pages/sorry/index.html"),
("tag/1020_russen/index.html", "/pages/sorry/index.html"),
("tag/578_terminal/index.html", "/pages/sorry/index.html"),
("tag/399_einsturz/index.html", "/pages/sorry/index.html"),
("tag/321_strato/index.html", "/pages/sorry/index.html"),
("tag/902_ecrypt_utils/index.html", "/pages/sorry/index.html"),
("tag/248_haustier/index.html", "/pages/sorry/index.html"),
("tag/213_elemente/index.html", "/pages/sorry/index.html"),
("tag/696_champ/index.html", "/pages/sorry/index.html"),
("tag/31_uhr/index.html", "/pages/sorry/index.html"),
("tag/936_creative_commons/index.html", "/pages/sorry/index.html"),
("tag/140_telefoncode/index.html", "/pages/sorry/index.html"),
("tag/1106_partition/index.html", "/pages/sorry/index.html"),
("tag/604_liquid_democracy/index.html", "/pages/sorry/index.html"),
("tag/549_deinstallation/index.html", "/pages/sorry/index.html"),
("tag/1100_fug/index.html", "/pages/sorry/index.html"),
("tag/598_lilo/index.html", "/pages/sorry/index.html"),
("tag/700_bildschirmschoner/index.html", "/pages/sorry/index.html"),
("tag/114_shuttle/index.html", "/pages/sorry/index.html"),
("tag/951_staatstrojaner/index.html", "/pages/sorry/index.html"),
("tag/356_pfad/index.html", "/pages/sorry/index.html"),
("tag/945_challenges/index.html", "/pages/sorry/index.html"),
("tag/1112_amtsdeutsch/index.html", "/pages/sorry/index.html"),
("tag/89_killer/index.html", "/pages/sorry/index.html"),
("tag/396_koehler/index.html", "/pages/sorry/index.html"),
("tag/577_screen/index.html", "/pages/sorry/index.html"),
("tag/210_periodic_table_of_videos/index.html", "/pages/sorry/index.html"),
("tag/368_werbung/index.html", "/pages/sorry/index.html"),
("tag/224_presse/index.html", "/pages/sorry/index.html"),
("tag/535_rundfunk/index.html", "/pages/sorry/index.html"),
("tag/502_kernkraft/index.html", "/pages/sorry/index.html"),
("tag/810_luefter/index.html", "/pages/sorry/index.html"),
("tag/449_kilogramm/index.html", "/pages/sorry/index.html"),
("tag/153_haare/index.html", "/pages/sorry/index.html"),
("tag/334_rss/index.html", "/pages/sorry/index.html"),
("tag/1038_perlpress/index.html", "/pages/sorry/index.html"),
("tag/336_brief/index.html", "/pages/sorry/index.html"),
("tag/1109_df/index.html", "/pages/sorry/index.html"),
("tag/254_auto/index.html", "/pages/sorry/index.html"),
("tag/348_jooma/index.html", "/pages/sorry/index.html"),
("tag/702_digitale_signatur/index.html", "/pages/sorry/index.html"),
("tag/972_intel/index.html", "/pages/sorry/index.html"),
("tag/622_digitale_infrastruktur/index.html", "/pages/sorry/index.html"),
("tag/692_alexander_lehmann/index.html", "/pages/sorry/index.html"),
("tag/407_vogelhaus/index.html", "/pages/sorry/index.html"),
("tag/50_raumfahrt/page5.html", "/pages/sorry/index.html"),
("tag/50_raumfahrt/page3.html", "/pages/sorry/index.html"),
("tag/50_raumfahrt/page2.html", "/pages/sorry/index.html"),
("tag/50_raumfahrt/index.html", "/pages/sorry/index.html"),
("tag/50_raumfahrt/page6.html", "/pages/sorry/index.html"),
("tag/50_raumfahrt/page4.html", "/pages/sorry/index.html"),
("tag/212_periodensystem/index.html", "/pages/sorry/index.html"),
("tag/579_remote/index.html", "/pages/sorry/index.html"),
("tag/144_s65/index.html", "/pages/sorry/index.html"),
("tag/1094_usbprog/index.html", "/pages/sorry/index.html"),
("tag/688_smart_1/index.html", "/pages/sorry/index.html"),
("tag/470_datum/index.html", "/pages/sorry/index.html"),
("tag/667_indect/index.html", "/pages/sorry/index.html"),
("tag/689_buugle/index.html", "/pages/sorry/index.html"),
("tag/311_ventil/index.html", "/pages/sorry/index.html"),
("tag/418_sonne/index.html", "/pages/sorry/index.html"),
("tag/218_freeware/index.html", "/pages/sorry/index.html"),
("tag/12_abfall/index.html", "/pages/sorry/index.html"),
("tag/475_meise/index.html", "/pages/sorry/index.html"),
("tag/1111_behoerdisch/index.html", "/pages/sorry/index.html"),
("tag/839_panorama/index.html", "/pages/sorry/index.html"),
("tag/156_fernsteuerung/index.html", "/pages/sorry/index.html"),
("tag/1080_public_key/index.html", "/pages/sorry/index.html"),
("tag/985_bilder/index.html", "/pages/sorry/index.html"),
("tag/309_heizkoerper/index.html", "/pages/sorry/index.html"),
("tag/932_import/index.html", "/pages/sorry/index.html"),
("tag/120_brennen/index.html", "/pages/sorry/index.html"),
("tag/713_sputnik/index.html", "/pages/sorry/index.html"),
("tag/97_mp3/index.html", "/pages/sorry/index.html"),
("tag/1054_tcp/index.html", "/pages/sorry/index.html"),
("tag/593_boot/index.html", "/pages/sorry/index.html"),
("tag/993_netzpolitik/index.html", "/pages/sorry/index.html"),
("tag/180_plakate/index.html", "/pages/sorry/index.html"),
("tag/665_weltraum_tourist/index.html", "/pages/sorry/index.html"),
("tag/792_ndr/index.html", "/pages/sorry/index.html"),
("tag/750_http/index.html", "/pages/sorry/index.html"),
("tag/495_batterie/index.html", "/pages/sorry/index.html"),
("tag/860_tauschboerse/index.html", "/pages/sorry/index.html"),
("tag/552_ferngesteuerte_ente/index.html", "/pages/sorry/index.html"),
("tag/759_ausweisapp/index.html", "/pages/sorry/index.html"),
("tag/33_usb/index.html", "/pages/sorry/index.html"),
("tag/76_gesetz/index.html", "/pages/sorry/index.html"),
("tag/132_lro/index.html", "/pages/sorry/index.html"),
("tag/295_gnome/index.html", "/pages/sorry/index.html"),
("tag/182_zeitung/index.html", "/pages/sorry/index.html"),
("tag/72_nacht/index.html", "/pages/sorry/index.html"),
("tag/217_sicherung/index.html", "/pages/sorry/index.html"),
("tag/30_rtc/index.html", "/pages/sorry/index.html"),
("tag/437_nistkasten/page5.html", "/pages/sorry/index.html"),
("tag/437_nistkasten/page3.html", "/pages/sorry/index.html"),
("tag/437_nistkasten/page2.html", "/pages/sorry/index.html"),
("tag/437_nistkasten/index.html", "/pages/sorry/index.html"),
("tag/437_nistkasten/page4.html", "/pages/sorry/index.html"),
("tag/494_akku/index.html", "/pages/sorry/index.html"),
("tag/291_feuerwerk/index.html", "/pages/sorry/index.html"),
("tag/960_https/index.html", "/pages/sorry/index.html"),
("tag/1081_ftp/index.html", "/pages/sorry/index.html"),
("tag/231_comsatbw/index.html", "/pages/sorry/index.html"),
("tag/426_verheiratet/index.html", "/pages/sorry/index.html"),
("tag/40_physik/index.html", "/pages/sorry/index.html"),
("tag/1061_xdotool/index.html", "/pages/sorry/index.html"),
("tag/758_crypt_ssleay/index.html", "/pages/sorry/index.html"),
("tag/992_neelie_kroes/index.html", "/pages/sorry/index.html"),
("tag/954_quellen_tkue/index.html", "/pages/sorry/index.html"),
("tag/648_virenscanner/index.html", "/pages/sorry/index.html"),
("tag/498_logitech/index.html", "/pages/sorry/index.html"),
("tag/376_bert/index.html", "/pages/sorry/index.html"),
("tag/741_anschlaege/index.html", "/pages/sorry/index.html"),
("tag/1028_hdparm/index.html", "/pages/sorry/index.html"),
("tag/989_wiederherstellen/index.html", "/pages/sorry/index.html"),
("tag/567_pjoengjang/index.html", "/pages/sorry/index.html"),
("tag/135_roboter/index.html", "/pages/sorry/index.html"),
("tag/267_umts/index.html", "/pages/sorry/index.html"),
("tag/616_vba_m/index.html", "/pages/sorry/index.html"),
("tag/87_usa/index.html", "/pages/sorry/index.html"),
("tag/163_yvcomments/index.html", "/pages/sorry/index.html"),
("tag/1002_ebook/index.html", "/pages/sorry/index.html"),
("tag/780_sdo/index.html", "/pages/sorry/index.html"),
("tag/693_du_bist_terrorist/index.html", "/pages/sorry/index.html"),
("tag/765_falcon_9/index.html", "/pages/sorry/index.html"),
("tag/701_eperso/index.html", "/pages/sorry/index.html"),
("tag/938_lizenz/index.html", "/pages/sorry/index.html"),
("tag/258_aliens/index.html", "/pages/sorry/index.html"),
("tag/643_ccc/page2.html", "/pages/sorry/index.html"),
("tag/643_ccc/index.html", "/pages/sorry/index.html"),
("tag/159_modellbau/index.html", "/pages/sorry/index.html"),
("tag/298_wlan/index.html", "/pages/sorry/index.html"),
("tag/525_tandem/index.html", "/pages/sorry/index.html"),
("tag/934_stromdieb/index.html", "/pages/sorry/index.html"),
("tag/328_flugzeug/index.html", "/pages/sorry/index.html"),
("tag/743_chipaxxs/index.html", "/pages/sorry/index.html"),
("tag/537_ard/index.html", "/pages/sorry/index.html"),
("tag/633_sushi/index.html", "/pages/sorry/index.html"),
("tag/101_suchmaschine/index.html", "/pages/sorry/index.html"),
("tag/854_dead_drops/index.html", "/pages/sorry/index.html"),
("tag/150_mastercode/index.html", "/pages/sorry/index.html"),
("tag/215_datenbank/index.html", "/pages/sorry/index.html"),
("tag/118_eingabeaufforderung/index.html", "/pages/sorry/index.html"),
("tag/959_uswsusp/index.html", "/pages/sorry/index.html"),
("tag/727_podcast/index.html", "/pages/sorry/index.html"),
("tag/160_basteln/index.html", "/pages/sorry/index.html"),
("tag/833_andromeda/index.html", "/pages/sorry/index.html"),
("tag/912_geek/index.html", "/pages/sorry/index.html"),
("tag/953_onlinedurchsuchung/index.html", "/pages/sorry/index.html"),
("tag/289_sylvester/index.html", "/pages/sorry/index.html"),
("tag/767_akatsuki/index.html", "/pages/sorry/index.html"),
("tag/11_konsumgesellschaft/index.html", "/pages/sorry/index.html"),
("tag/1022_brandenburg/index.html", "/pages/sorry/index.html"),
("tag/268_isdn/index.html", "/pages/sorry/index.html"),
("tag/10_recycling/index.html", "/pages/sorry/index.html"),
("tag/699_caffeine/index.html", "/pages/sorry/index.html"),
("tag/644_epass/index.html", "/pages/sorry/index.html"),
("tag/540_gez/index.html", "/pages/sorry/index.html"),
("tag/653_avr_studio/index.html", "/pages/sorry/index.html"),
("tag/603_konsole/index.html", "/pages/sorry/index.html"),
("tag/545_benachrichtigung/index.html", "/pages/sorry/index.html"),
("tag/226_bundesgerichtshof/index.html", "/pages/sorry/index.html"),
("tag/824_home_server/index.html", "/pages/sorry/index.html"),
("tag/1097_verzeichnis/index.html", "/pages/sorry/index.html"),
("tag/419_sonnenwind/index.html", "/pages/sorry/index.html"),
("tag/1070_avr/index.html", "/pages/sorry/index.html"),
("tag/868_kosumgesellschaft/index.html", "/pages/sorry/index.html"),
("tag/624_afghanistan/index.html", "/pages/sorry/index.html"),
("tag/191_tsunami/index.html", "/pages/sorry/index.html"),
("tag/13_elektroschrott/index.html", "/pages/sorry/index.html"),
("tag/301_wpa/index.html", "/pages/sorry/index.html"),
("tag/439_vogel/page2.html", "/pages/sorry/index.html"),
("tag/439_vogel/index.html", "/pages/sorry/index.html"),
("tag/742_hysterie/index.html", "/pages/sorry/index.html"),
("tag/155_ente/index.html", "/pages/sorry/index.html"),
("tag/335_liferea/index.html", "/pages/sorry/index.html"),
("tag/634_kochen/index.html", "/pages/sorry/index.html"),
("tag/1085_openrheinruhr/index.html", "/pages/sorry/index.html"),
("tag/2_stop_motion/index.html", "/pages/sorry/index.html"),
("tag/638_pdftk/index.html", "/pages/sorry/index.html"),
("tag/1026_disqus/index.html", "/pages/sorry/index.html"),
("tag/467_kueken/page2.html", "/pages/sorry/index.html"),
("tag/467_kueken/index.html", "/pages/sorry/index.html"),
("tag/1008_treiber/index.html", "/pages/sorry/index.html"),
("tag/715_russland/index.html", "/pages/sorry/index.html"),
("tag/796_pocketputty/index.html", "/pages/sorry/index.html"),
("tag/362_ipad/index.html", "/pages/sorry/index.html"),
("tag/253_pkw/index.html", "/pages/sorry/index.html"),
("tag/956_unity/index.html", "/pages/sorry/index.html"),
("tag/1044_eclipse/index.html", "/pages/sorry/index.html"),
("tag/330_bombe/index.html", "/pages/sorry/index.html"),
("tag/631_ubuntu/page2.html", "/pages/sorry/index.html"),
("tag/631_ubuntu/index.html", "/pages/sorry/index.html"),
("tag/469_nestlinge/index.html", "/pages/sorry/index.html"),
("tag/925_schandmaennchen_de/index.html", "/pages/sorry/index.html"),
("tag/200_thinkpad/index.html", "/pages/sorry/index.html"),
("tag/994_meinungsfreiheit/index.html", "/pages/sorry/index.html"),
("tag/104_bendorf/index.html", "/pages/sorry/index.html"),
("tag/244_simons_cat/index.html", "/pages/sorry/index.html"),
("tag/400_u_bahn/index.html", "/pages/sorry/index.html"),
("tag/1102_loeschen/index.html", "/pages/sorry/index.html"),
("tag/273_dos/index.html", "/pages/sorry/index.html"),
("tag/751_webserver/index.html", "/pages/sorry/index.html"),
("tag/782_magnetosphaere/index.html", "/pages/sorry/index.html"),
("tag/975_prozessor/index.html", "/pages/sorry/index.html"),
("tag/222_bild/index.html", "/pages/sorry/index.html"),
("tag/377_baer/index.html", "/pages/sorry/index.html"),
("tag/216_backup/index.html", "/pages/sorry/index.html"),
("tag/583_htc_touch_diamond_2/index.html", "/pages/sorry/index.html"),
("tag/413_yast/index.html", "/pages/sorry/index.html"),
("tag/655_error/index.html", "/pages/sorry/index.html"),
("tag/337_addon/index.html", "/pages/sorry/index.html"),
("tag/627_spendenbereitschaft/index.html", "/pages/sorry/index.html"),
("tag/96_radio/index.html", "/pages/sorry/index.html"),
("tag/842_speedplus/index.html", "/pages/sorry/index.html"),
("tag/645_pauswg/index.html", "/pages/sorry/index.html"),
("tag/601_scanner/index.html", "/pages/sorry/index.html"),
("tag/391_planet/index.html", "/pages/sorry/index.html"),
("tag/458_nachwuchs/index.html", "/pages/sorry/index.html"),
("tag/1069_feuerwehrauto/index.html", "/pages/sorry/index.html"),
("tag/615_emulator/index.html", "/pages/sorry/index.html"),
("tag/984_dateien/index.html", "/pages/sorry/index.html"),
("tag/875_playlist/index.html", "/pages/sorry/index.html"),
("tag/251_feinstaubplakette/index.html", "/pages/sorry/index.html"),
("tag/814_rsync/index.html", "/pages/sorry/index.html"),
("tag/529_radar/index.html", "/pages/sorry/index.html"),
("tag/837_astronomie/index.html", "/pages/sorry/index.html"),
("tag/318_powertoy/index.html", "/pages/sorry/index.html"),
("tag/127_von_braun/index.html", "/pages/sorry/index.html"),
("tag/970_qrencode/index.html", "/pages/sorry/index.html"),
("tag/884_cookie_monster/index.html", "/pages/sorry/index.html"),
("tag/88_fliege/index.html", "/pages/sorry/index.html"),
("tag/143_m65/index.html", "/pages/sorry/index.html"),
("tag/536_staatsvertrag/index.html", "/pages/sorry/index.html"),
("tag/789_chrismas_2_0/index.html", "/pages/sorry/index.html"),
("tag/47_speicher/index.html", "/pages/sorry/index.html"),
("tag/187_allnet_all6250_linux_netzwerk/index.html", "/pages/sorry/index.html"),
("tag/363_hype/index.html", "/pages/sorry/index.html"),
("tag/471_format/index.html", "/pages/sorry/index.html"),
("tag/275_computerspiel/index.html", "/pages/sorry/index.html"),
("tag/385_ffmpeg/index.html", "/pages/sorry/index.html"),
("tag/1101_ext/index.html", "/pages/sorry/index.html"),
("tag/1116_imagemagick/index.html", "/pages/sorry/index.html"),
("tag/1043_bazaar/index.html", "/pages/sorry/index.html"),
("tag/1039_rover/index.html", "/pages/sorry/index.html"),
("tag/73_japan/index.html", "/pages/sorry/index.html"),
("tag/166_ferngesteurte_ente/index.html", "/pages/sorry/index.html"),
("tag/433_augmented_reality/index.html", "/pages/sorry/index.html"),
("tag/320_hoster/index.html", "/pages/sorry/index.html"),
("tag/365_armee/index.html", "/pages/sorry/index.html"),
("tag/235_peenemuende/index.html", "/pages/sorry/index.html"),
("tag/683_manipulation/index.html", "/pages/sorry/index.html"),
("tag/80_kinderpornographie/index.html", "/pages/sorry/index.html"),
("tag/452_paris/index.html", "/pages/sorry/index.html"),
("tag/794_kinn/index.html", "/pages/sorry/index.html"),
("tag/719_teleskop/index.html", "/pages/sorry/index.html"),
("tag/544_touch_diamond_2/index.html", "/pages/sorry/index.html"),
("tag/551_anwendungen/index.html", "/pages/sorry/index.html"),
("tag/438_blaumeise/page3.html", "/pages/sorry/index.html"),
("tag/438_blaumeise/page2.html", "/pages/sorry/index.html"),
("tag/438_blaumeise/index.html", "/pages/sorry/index.html"),
("tag/447_si/index.html", "/pages/sorry/index.html"),
("tag/263_fake/index.html", "/pages/sorry/index.html"),
("tag/836_satelliten/index.html", "/pages/sorry/index.html"),
("tag/903_home/index.html", "/pages/sorry/index.html"),
("tag/983_digitalkamera/index.html", "/pages/sorry/index.html"),
("tag/709_rosetta/index.html", "/pages/sorry/index.html"),
("tag/849_bash/index.html", "/pages/sorry/index.html"),
("tag/241_vergeltungswaffe/index.html", "/pages/sorry/index.html"),
("tag/462_blaumeisen/index.html", "/pages/sorry/index.html"),
("tag/383_pythagoras/index.html", "/pages/sorry/index.html"),
("tag/1098_rechte/index.html", "/pages/sorry/index.html"),
("tag/138_handy/index.html", "/pages/sorry/index.html"),
("tag/711_komet/index.html", "/pages/sorry/index.html"),
("tag/920_etrex/index.html", "/pages/sorry/index.html"),
("tag/1117_pomplamoose/index.html", "/pages/sorry/index.html"),
("tag/637_pdfsam/index.html", "/pages/sorry/index.html"),
("tag/584_unterwegs/index.html", "/pages/sorry/index.html"),
("tag/1096_api/index.html", "/pages/sorry/index.html"),
("tag/1032_realitaet/index.html", "/pages/sorry/index.html"),
("tag/826_mediathek/index.html", "/pages/sorry/index.html"),
("tag/919_garmin/index.html", "/pages/sorry/index.html"),
("tag/435_fernseher/index.html", "/pages/sorry/index.html"),
("tag/256_koeln/index.html", "/pages/sorry/index.html"),
("tag/372_blitz/index.html", "/pages/sorry/index.html"),
("tag/45_integration/index.html", "/pages/sorry/index.html"),
("tag/691_personalausweis/index.html", "/pages/sorry/index.html"),
("tag/68_pocketpc/index.html", "/pages/sorry/index.html"),
("tag/441_geocaching/page3.html", "/pages/sorry/index.html"),
("tag/441_geocaching/page2.html", "/pages/sorry/index.html"),
("tag/441_geocaching/index.html", "/pages/sorry/index.html"),
("tag/441_geocaching/page4.html", "/pages/sorry/index.html"),
("tag/690_bundesregierung/index.html", "/pages/sorry/index.html"),
("tag/600_samsung_scx_4200/index.html", "/pages/sorry/index.html"),
("tag/22_schittstelle/index.html", "/pages/sorry/index.html"),
("tag/29_ntp/index.html", "/pages/sorry/index.html"),
("tag/798_datei_manager/index.html", "/pages/sorry/index.html"),
("tag/703_pin/index.html", "/pages/sorry/index.html"),
("tag/516_top_kill/index.html", "/pages/sorry/index.html"),
("tag/897_kohlmeise/index.html", "/pages/sorry/index.html"),
("tag/429_bka/index.html", "/pages/sorry/index.html"),
("tag/350_zaehler/index.html", "/pages/sorry/index.html"),
("tag/192_flut/index.html", "/pages/sorry/index.html"),
("tag/962_zertifikate/index.html", "/pages/sorry/index.html"),
("tag/232_gsoc/index.html", "/pages/sorry/index.html"),
("tag/476_tot/index.html", "/pages/sorry/index.html"),
("tag/885_lts/index.html", "/pages/sorry/index.html"),
("tag/845_geschwindigkeit/index.html", "/pages/sorry/index.html"),
("tag/457_fingerzeig/index.html", "/pages/sorry/index.html"),
("tag/46_simulation/index.html", "/pages/sorry/index.html"),
("tag/42_spass/index.html", "/pages/sorry/index.html"),
("tag/1086_freie_software/index.html", "/pages/sorry/index.html"),
("tag/69_pikapika/index.html", "/pages/sorry/index.html"),
("tag/327_flughafen/index.html", "/pages/sorry/index.html"),
("tag/670_gpx/index.html", "/pages/sorry/index.html"),
("tag/917_ernaehrung/index.html", "/pages/sorry/index.html"),
("tag/339_flash/index.html", "/pages/sorry/index.html"),
("tag/284_mount/index.html", "/pages/sorry/index.html"),
("tag/398_stadtarchiv/index.html", "/pages/sorry/index.html"),
("tag/1090_code/index.html", "/pages/sorry/index.html"),
("tag/591_bauanleitungen/index.html", "/pages/sorry/index.html"),
("tag/1035_film/index.html", "/pages/sorry/index.html"),
("tag/630_islam/index.html", "/pages/sorry/index.html"),
("tag/19_rs232/index.html", "/pages/sorry/index.html"),
("tag/211_chemie/index.html", "/pages/sorry/index.html"),
("tag/944_chaos_communication_congress/index.html", "/pages/sorry/index.html"),
("tag/129_apollo/index.html", "/pages/sorry/index.html"),
("tag/381_kuscheltier/index.html", "/pages/sorry/index.html"),
("tag/562_kontrollzentrum/index.html", "/pages/sorry/index.html"),
("tag/36_ueberwachung/page2.html", "/pages/sorry/index.html"),
("tag/36_ueberwachung/index.html", "/pages/sorry/index.html"),
("tag/969_vcard/index.html", "/pages/sorry/index.html"),
("tag/366_oesterreich/index.html", "/pages/sorry/index.html"),
("tag/208_mbr/index.html", "/pages/sorry/index.html"),
("tag/921_legend/index.html", "/pages/sorry/index.html"),
("tag/997_galileo/index.html", "/pages/sorry/index.html"),
("tag/48_mond/page2.html", "/pages/sorry/index.html"),
("tag/48_mond/index.html", "/pages/sorry/index.html"),
("tag/1110_speicherplatz/index.html", "/pages/sorry/index.html"),
("tag/698_gfz/index.html", "/pages/sorry/index.html"),
("tag/607_direkte_demokratie/index.html", "/pages/sorry/index.html"),
("tag/835_scheinbare_helligkeit/index.html", "/pages/sorry/index.html"),
("tag/428_spam/index.html", "/pages/sorry/index.html"),
("tag/149_papuautils/index.html", "/pages/sorry/index.html"),
("tag/459_landtagswahl/index.html", "/pages/sorry/index.html"),
("tag/933_dom/index.html", "/pages/sorry/index.html"),
("tag/147_eeprom/index.html", "/pages/sorry/index.html"),
("tag/788_referrer/index.html", "/pages/sorry/index.html"),
("tag/265_buzz_aldrin/index.html", "/pages/sorry/index.html"),
("tag/664_space_tourists/index.html", "/pages/sorry/index.html"),
("tag/373_projektor/index.html", "/pages/sorry/index.html"),
("tag/317_dexpot/index.html", "/pages/sorry/index.html"),
("tag/650_spyware/index.html", "/pages/sorry/index.html"),
("tag/1005_buch/index.html", "/pages/sorry/index.html"),
("tag/980_twitter/index.html", "/pages/sorry/index.html"),
("tag/1104_strace/index.html", "/pages/sorry/index.html"),
("tag/83_zuhause/index.html", "/pages/sorry/index.html"),
("tag/940_groundspeak/index.html", "/pages/sorry/index.html"),
("tag/1099_acl/index.html", "/pages/sorry/index.html"),
("tag/278_weihnachten/index.html", "/pages/sorry/index.html"),
("tag/179_bundestagswahl/index.html", "/pages/sorry/index.html"),
("tag/865_verschluesselung/index.html", "/pages/sorry/index.html"),
("tag/575_karikatur/index.html", "/pages/sorry/index.html"),
("tag/748_lesegeraet/index.html", "/pages/sorry/index.html"),
("tag/1108_fish/index.html", "/pages/sorry/index.html"),
("tag/1040_curiosity/index.html", "/pages/sorry/index.html"),
("tag/963_certificate_authority/index.html", "/pages/sorry/index.html"),
("tag/987_speicherkarte/index.html", "/pages/sorry/index.html"),
("tag/151_friseur/index.html", "/pages/sorry/index.html"),
("tag/392_inertialsystem/index.html", "/pages/sorry/index.html"),
("tag/574_shell/index.html", "/pages/sorry/index.html"),
("tag/510_steve_jobs/index.html", "/pages/sorry/index.html"),
("tag/412_update/page2.html", "/pages/sorry/index.html"),
("tag/412_update/index.html", "/pages/sorry/index.html"),
("tag/791_extra3/index.html", "/pages/sorry/index.html"),
("tag/464_brut/index.html", "/pages/sorry/index.html"),
("tag/861_offline/index.html", "/pages/sorry/index.html"),
("tag/982_photorec/index.html", "/pages/sorry/index.html"),
("tag/420_zdf/index.html", "/pages/sorry/index.html"),
("tag/654_programmieren/index.html", "/pages/sorry/index.html"),
("tag/456_handschuh/index.html", "/pages/sorry/index.html"),
("tag/146_esn/index.html", "/pages/sorry/index.html"),
("tag/482_strahlung/index.html", "/pages/sorry/index.html"),
("tag/7_plugin/index.html", "/pages/sorry/index.html"),
("tag/296_web_2_0/index.html", "/pages/sorry/index.html"),
("tag/27_minuscule/index.html", "/pages/sorry/index.html"),
("tag/979_garmin_dakota/index.html", "/pages/sorry/index.html"),
("tag/415_gesperrt/index.html", "/pages/sorry/index.html"),
("tag/269_lte_long_term_evolution/index.html", "/pages/sorry/index.html"),
("tag/930_ics/index.html", "/pages/sorry/index.html"),
("tag/597_dmesg/index.html", "/pages/sorry/index.html"),
("tag/896_datenschleuder/index.html", "/pages/sorry/index.html"),
("tag/64_dropbox/index.html", "/pages/sorry/index.html"),
("tag/506_strom/index.html", "/pages/sorry/index.html"),
("tag/6_allvideoplugin/index.html", "/pages/sorry/index.html"),
("tag/1059_schavan/index.html", "/pages/sorry/index.html"),
("tag/344_katastrophe/index.html", "/pages/sorry/index.html"),
("tag/440_flickr/index.html", "/pages/sorry/index.html"),
("tag/588_distribution/index.html", "/pages/sorry/index.html"),
("tag/323_ixquick/index.html", "/pages/sorry/index.html"),
("tag/806_network_attached_storage/index.html", "/pages/sorry/index.html"),
("tag/779_soho/index.html", "/pages/sorry/index.html"),
("tag/395_ursula_von_der_leyen/index.html", "/pages/sorry/index.html"),
("tag/679_chip/index.html", "/pages/sorry/index.html"),
("tag/651_perso/index.html", "/pages/sorry/index.html"),
("tag/16_opennas/page2.html", "/pages/sorry/index.html"),
("tag/16_opennas/index.html", "/pages/sorry/index.html"),
("tag/500_flashmob/index.html", "/pages/sorry/index.html"),
("tag/784_horstbox/index.html", "/pages/sorry/index.html"),
("tag/106_statistik/index.html", "/pages/sorry/index.html"),
("tag/95_angriff/index.html", "/pages/sorry/index.html"),
("tag/406_webcam/index.html", "/pages/sorry/index.html"),
("tag/134_lroc/index.html", "/pages/sorry/index.html"),
("tag/762_venus/index.html", "/pages/sorry/index.html"),
("tag/812_dns/index.html", "/pages/sorry/index.html"),
("tag/968_qr_code/index.html", "/pages/sorry/index.html"),
("tag/894_bundeskriminalamt/index.html", "/pages/sorry/index.html"),
("tag/840_hugin/index.html", "/pages/sorry/index.html"),
("tag/139_mobiltelefon/index.html", "/pages/sorry/index.html"),
("tag/322_google/page2.html", "/pages/sorry/index.html"),
("tag/322_google/index.html", "/pages/sorry/index.html"),
("tag/1012_inssider/index.html", "/pages/sorry/index.html"),
("tag/520_oelkatastrophe/index.html", "/pages/sorry/index.html"),
("tag/128_disney/index.html", "/pages/sorry/index.html"),
("tag/542_smartphone/index.html", "/pages/sorry/index.html"),
("tag/668_eu/index.html", "/pages/sorry/index.html"),
("tag/329_terrorismus/index.html", "/pages/sorry/index.html"),
("tag/760_terrorist/index.html", "/pages/sorry/index.html"),
("tag/316_arbeitsflaeche/index.html", "/pages/sorry/index.html"),
("tag/236_usedom/index.html", "/pages/sorry/index.html"),
("tag/834_pegasus/index.html", "/pages/sorry/index.html"),
("tag/354_petition/index.html", "/pages/sorry/index.html"),
("tag/44_runge_kutta/index.html", "/pages/sorry/index.html"),
("tag/54_nasa/index.html", "/pages/sorry/index.html"),
("tag/349_zugriff/index.html", "/pages/sorry/index.html"),
("tag/245_hund/index.html", "/pages/sorry/index.html"),
("tag/61_windows_mobile/page2.html", "/pages/sorry/index.html"),
("tag/61_windows_mobile/index.html", "/pages/sorry/index.html"),
("tag/620_opensuse_repository/index.html", "/pages/sorry/index.html"),
("tag/250_umweltzone/index.html", "/pages/sorry/index.html"),
("tag/1072_lowercase/index.html", "/pages/sorry/index.html"),
("tag/891_navigationssystem/index.html", "/pages/sorry/index.html"),
("tag/625_krieg/index.html", "/pages/sorry/index.html"),
("tag/846_moby/index.html", "/pages/sorry/index.html"),
("tag/863_passwoerter/index.html", "/pages/sorry/index.html"),
("tag/564_nordkorea/index.html", "/pages/sorry/index.html"),
("tag/8_muell/index.html", "/pages/sorry/index.html"),
("tag/270_breitband/index.html", "/pages/sorry/index.html"),
("tag/280_weihnachtsbaum/index.html", "/pages/sorry/index.html"),
("tag/465_muppets/index.html", "/pages/sorry/index.html"),
("tag/51_wissenschaft/index.html", "/pages/sorry/index.html"),
("tag/472_uhrzeit/index.html", "/pages/sorry/index.html"),
("tag/605_liquid_feedback/index.html", "/pages/sorry/index.html"),
("tag/56_mathematik/index.html", "/pages/sorry/index.html"),
("tag/685_stgb/index.html", "/pages/sorry/index.html"),
("tag/838_cookies/index.html", "/pages/sorry/index.html"),
("tag/451_urkilo/index.html", "/pages/sorry/index.html"),
("tag/1013_wifi_analyzer/index.html", "/pages/sorry/index.html"),
("tag/324_daten/index.html", "/pages/sorry/index.html"),
("tag/199_dlr/index.html", "/pages/sorry/index.html"),
("tag/873_m3u/index.html", "/pages/sorry/index.html"),
("tag/783_jhelioviewer/index.html", "/pages/sorry/index.html"),
("tag/652_avra/index.html", "/pages/sorry/index.html"),
("tag/848_ms_dos/index.html", "/pages/sorry/index.html"),
("tag/658__pragma/index.html", "/pages/sorry/index.html"),
("tag/386_traegheit/index.html", "/pages/sorry/index.html"),
("tag/629_terror/index.html", "/pages/sorry/index.html"),
("tag/807_via_epia_m10000/index.html", "/pages/sorry/index.html"),
("tag/628_atombomben/index.html", "/pages/sorry/index.html"),
("tag/195_un/index.html", "/pages/sorry/index.html"),
("tag/388_beschleunigung/index.html", "/pages/sorry/index.html"),
("tag/173_bundeskanzleramt/index.html", "/pages/sorry/index.html"),
("tag/1093_ascii/index.html", "/pages/sorry/index.html"),
("tag/710_philae/index.html", "/pages/sorry/index.html"),
("tag/115_blitze/index.html", "/pages/sorry/index.html"),
("tag/889_entsorgung/index.html", "/pages/sorry/index.html"),
("tag/164_piratenpartei/page2.html", "/pages/sorry/index.html"),
("tag/164_piratenpartei/index.html", "/pages/sorry/index.html"),
("tag/991_plagiat/index.html", "/pages/sorry/index.html"),
("tag/409_infrarot/index.html", "/pages/sorry/index.html"),
("tag/474_nestling/index.html", "/pages/sorry/index.html"),
("tag/590_lego/index.html", "/pages/sorry/index.html"),
("tag/795_gesichter/index.html", "/pages/sorry/index.html"),
("tag/172_ackermann/index.html", "/pages/sorry/index.html"),
("tag/240_zweiter_weltkrieg/index.html", "/pages/sorry/index.html"),
("tag/539_fefe/index.html", "/pages/sorry/index.html"),
("tag/922_bundespraesident/index.html", "/pages/sorry/index.html"),
("tag/867_obsoleszenz/index.html", "/pages/sorry/index.html"),
("tag/829_demografischer_wandel/index.html", "/pages/sorry/index.html"),
("tag/282_cd/index.html", "/pages/sorry/index.html"),
("tag/941_lost_place_cache/index.html", "/pages/sorry/index.html"),
("tag/3_animation/index.html", "/pages/sorry/index.html"),
("tag/345_krise/index.html", "/pages/sorry/index.html"),
("tag/119_kommandozeile/index.html", "/pages/sorry/index.html"),
("tag/738_angst/index.html", "/pages/sorry/index.html"),
("tag/355_auto_type/index.html", "/pages/sorry/index.html"),
("tag/926_katholische_kirche/index.html", "/pages/sorry/index.html"),
("tag/436_brille/index.html", "/pages/sorry/index.html"),
("tag/673_osm/index.html", "/pages/sorry/index.html"),
("tag/721_taukappe/index.html", "/pages/sorry/index.html"),
("tag/484_mobilfunk/index.html", "/pages/sorry/index.html"),
("tag/1046_jabber/index.html", "/pages/sorry/index.html"),
("tag/347_keefox/index.html", "/pages/sorry/index.html"),
("tag/939_dosenfischer/index.html", "/pages/sorry/index.html"),
("tag/24_flechten/index.html", "/pages/sorry/index.html"),
("tag/90_interview/index.html", "/pages/sorry/index.html"),
("tag/556_serbien/index.html", "/pages/sorry/index.html"),
("tag/15_netzwerk/page2.html", "/pages/sorry/index.html"),
("tag/15_netzwerk/index.html", "/pages/sorry/index.html"),
("tag/566_musik/page2.html", "/pages/sorry/index.html"),
("tag/566_musik/index.html", "/pages/sorry/index.html"),
("tag/1056_firmware/index.html", "/pages/sorry/index.html"),
("tag/272_dosbox/index.html", "/pages/sorry/index.html"),
("tag/785_router/index.html", "/pages/sorry/index.html"),
("tag/394_stop/index.html", "/pages/sorry/index.html"),
("tag/726_deutschlandfunk/index.html", "/pages/sorry/index.html"),
("tag/1003_epub/index.html", "/pages/sorry/index.html"),
("tag/1047_xmpp/index.html", "/pages/sorry/index.html"),
("tag/1087_konferenz/index.html", "/pages/sorry/index.html"),
("tag/281_iso/index.html", "/pages/sorry/index.html"),
("tag/65_kennwort/index.html", "/pages/sorry/index.html"),
("tag/302_wpa2/index.html", "/pages/sorry/index.html"),
("tag/1057_koordinate/index.html", "/pages/sorry/index.html"),
("tag/729_abmahnung/index.html", "/pages/sorry/index.html"),
("tag/913_lebensmittel/index.html", "/pages/sorry/index.html"),
("tag/81_kinder/index.html", "/pages/sorry/index.html"),
("tag/1011_iwlist/index.html", "/pages/sorry/index.html"),
("tag/408_voegel/index.html", "/pages/sorry/index.html"),
("tag/1009_scanimage/index.html", "/pages/sorry/index.html"),
("tag/1066_supermarkt/index.html", "/pages/sorry/index.html"),
("tag/380_auge/index.html", "/pages/sorry/index.html"),
("tag/981_testdisk/index.html", "/pages/sorry/index.html"),
("tag/432_ak_zensur/index.html", "/pages/sorry/index.html"),
("tag/1074_ip/index.html", "/pages/sorry/index.html"),
("tag/443_schatz/index.html", "/pages/sorry/index.html"),
("tag/384_patent/index.html", "/pages/sorry/index.html"),
("tag/1075_mac/index.html", "/pages/sorry/index.html"),
("tag/924_bellvue/index.html", "/pages/sorry/index.html"),
("tag/929_microsoft_outlook/index.html", "/pages/sorry/index.html"),
("tag/341_hawai/index.html", "/pages/sorry/index.html"),
("tag/9_umwelt/index.html", "/pages/sorry/index.html"),
("tag/387_kraft/index.html", "/pages/sorry/index.html"),
("tag/1015_der_spiegel/index.html", "/pages/sorry/index.html"),
("tag/1082_impressum/index.html", "/pages/sorry/index.html"),
("tag/1033_dradio/index.html", "/pages/sorry/index.html"),
("tag/82_protest/index.html", "/pages/sorry/index.html"),
("tag/988_eraser/index.html", "/pages/sorry/index.html"),
("tag/206_booten/index.html", "/pages/sorry/index.html"),
("tag/775_server/index.html", "/pages/sorry/index.html"),
("tag/264_amerika/index.html", "/pages/sorry/index.html"),
("tag/219_space_tourism/index.html", "/pages/sorry/index.html"),
("tag/442_gps/page3.html", "/pages/sorry/index.html"),
("tag/442_gps/page2.html", "/pages/sorry/index.html"),
("tag/442_gps/index.html", "/pages/sorry/index.html"),
("tag/53_verschwoerung/index.html", "/pages/sorry/index.html"),
("tag/825_content_management_system/index.html", "/pages/sorry/index.html"),
("tag/4_video/page2.html", "/pages/sorry/index.html"),
("tag/4_video/index.html", "/pages/sorry/index.html"),
("tag/958_hibernate/index.html", "/pages/sorry/index.html"),
("tag/25_flashen/index.html", "/pages/sorry/index.html"),
("tag/361_apple/index.html", "/pages/sorry/index.html"),
("tag/504_schweiz/index.html", "/pages/sorry/index.html"),
("tag/661_mega/index.html", "/pages/sorry/index.html"),
("tag/1122_diskette/index.html", "/pages/sorry/index.html"),
("tag/107_wahl/index.html", "/pages/sorry/index.html"),
("tag/864_kennwoerter/index.html", "/pages/sorry/index.html"),
("tag/507_energie/index.html", "/pages/sorry/index.html"),
("tag/519_oel/index.html", "/pages/sorry/index.html"),
("tag/214_mysql/index.html", "/pages/sorry/index.html"),
("tag/286_laufwerk/index.html", "/pages/sorry/index.html"),
("tag/78_partei/index.html", "/pages/sorry/index.html"),
("tag/423_ehe/index.html", "/pages/sorry/index.html"),
("tag/558_wasserverbrauch/index.html", "/pages/sorry/index.html"),
("tag/136_hannover/index.html", "/pages/sorry/index.html"),
("tag/378_teddy/index.html", "/pages/sorry/index.html"),
("tag/859_pda/index.html", "/pages/sorry/index.html"),
("tag/514_app/index.html", "/pages/sorry/index.html"),
("tag/403_druckauftrag/index.html", "/pages/sorry/index.html"),
("tag/657_assembler/index.html", "/pages/sorry/index.html"),
("tag/249_feinstaub/index.html", "/pages/sorry/index.html"),
("tag/331_al_kaida/index.html", "/pages/sorry/index.html"),
("tag/91_orson_welles/index.html", "/pages/sorry/index.html"),
("tag/898_space_shuttle/index.html", "/pages/sorry/index.html"),
("tag/360_datei/index.html", "/pages/sorry/index.html"),
("tag/221_clown/index.html", "/pages/sorry/index.html"),
("tag/1062_tastatur/index.html", "/pages/sorry/index.html"),
("tag/965_deutscher_karikaturenpreis/index.html", "/pages/sorry/index.html"),
("tag/761_glonass/index.html", "/pages/sorry/index.html"),
("tag/66_software/index.html", "/pages/sorry/index.html"),
("tag/466_stand_by_me/index.html", "/pages/sorry/index.html"),
("tag/110_green_dam/index.html", "/pages/sorry/index.html"),
("tag/1065_pinnball_machine_spielautomat/index.html", "/pages/sorry/index.html"),
("tag/123_dma/index.html", "/pages/sorry/index.html"),
("tag/602_mac_os_x/index.html", "/pages/sorry/index.html"),
("tag/1014_access_point/index.html", "/pages/sorry/index.html"),
("tag/1084_github/index.html", "/pages/sorry/index.html"),
("tag/74_taschenlampe/index.html", "/pages/sorry/index.html"),
("tag/730_copyright/index.html", "/pages/sorry/index.html"),
("tag/623_pakistan/index.html", "/pages/sorry/index.html"),
("tag/914_verschwendung/index.html", "/pages/sorry/index.html"),
("tag/379_nils/index.html", "/pages/sorry/index.html"),
("tag/770_it/index.html", "/pages/sorry/index.html"),
("tag/34_programmer/index.html", "/pages/sorry/index.html"),
("tag/1019_lost_place/index.html", "/pages/sorry/index.html"),
("tag/292_cheat/index.html", "/pages/sorry/index.html"),
("tag/781_sonnensturm/index.html", "/pages/sorry/index.html"),
("tag/57_gleichungen/index.html", "/pages/sorry/index.html"),
("tag/246_tier/index.html", "/pages/sorry/index.html"),
("tag/390_iss/index.html", "/pages/sorry/index.html"),
("tag/352_phpmyadmin/index.html", "/pages/sorry/index.html"),
("tag/342_erdbeben/index.html", "/pages/sorry/index.html"),
("tag/787_firefox_erweiterung/index.html", "/pages/sorry/index.html"),
("tag/430_internetsperren/index.html", "/pages/sorry/index.html"),
("tag/635_streetview/index.html", "/pages/sorry/index.html"),
("tag/640_pdf/index.html", "/pages/sorry/index.html"),
("tag/193_satellit/page2.html", "/pages/sorry/index.html"),
("tag/193_satellit/index.html", "/pages/sorry/index.html"),
("tag/75_ehrensenf/index.html", "/pages/sorry/index.html"),
("tag/687_lunar_lander/index.html", "/pages/sorry/index.html"),
("tag/1029_standby/index.html", "/pages/sorry/index.html"),
("tag/77_bundestag/index.html", "/pages/sorry/index.html"),
("tag/98_firefox/index.html", "/pages/sorry/index.html"),
("tag/786_refcontrol/index.html", "/pages/sorry/index.html"),
("tag/243_v1/index.html", "/pages/sorry/index.html"),
("tag/176_sun/index.html", "/pages/sorry/index.html"),
("tag/189_un_spider/index.html", "/pages/sorry/index.html"),
("tag/108_iran/index.html", "/pages/sorry/index.html"),
("tag/1041_chaosradio/index.html", "/pages/sorry/index.html"),
("tag/369_skandal/index.html", "/pages/sorry/index.html"),
("tag/999_digitales_lesen/index.html", "/pages/sorry/index.html"),
("tag/1021_russische_kaserne/index.html", "/pages/sorry/index.html"),
("tag/223_taz/index.html", "/pages/sorry/index.html"),
("tag/671_easymap/index.html", "/pages/sorry/index.html"),
("tag/895_bundestrojaner/index.html", "/pages/sorry/index.html"),
("tag/697_ddr/index.html", "/pages/sorry/index.html"),
("tag/1068_asteroid/index.html", "/pages/sorry/index.html"),
("tag/169_geburtstag/index.html", "/pages/sorry/index.html"),
("tag/70_kunst/index.html", "/pages/sorry/index.html"),
("tag/966_facebook/index.html", "/pages/sorry/index.html"),
("tag/229_cms/index.html", "/pages/sorry/index.html"),
("tag/59_windows/page3.html", "/pages/sorry/index.html"),
("tag/59_windows/page2.html", "/pages/sorry/index.html"),
("tag/59_windows/index.html", "/pages/sorry/index.html"),
("tag/59_windows/page4.html", "/pages/sorry/index.html"),
("tag/813_dhcp/index.html", "/pages/sorry/index.html"),
("tag/431_zugerschwg/index.html", "/pages/sorry/index.html"),
("tag/21_elektronik/index.html", "/pages/sorry/index.html"),
("tag/560_tandem_x/index.html", "/pages/sorry/index.html"),
("tag/764_spacex/index.html", "/pages/sorry/index.html"),
("tag/294_loesung/index.html", "/pages/sorry/index.html"),
("tag/276_spiel/index.html", "/pages/sorry/index.html"),
("tag/84_grillen/index.html", "/pages/sorry/index.html"),
("tag/234_weilheim/index.html", "/pages/sorry/index.html"),
("tag/587_fedora/index.html", "/pages/sorry/index.html"),
("tag/978_dnf/index.html", "/pages/sorry/index.html"),
("tag/740_london/index.html", "/pages/sorry/index.html"),
("tag/686_esa/index.html", "/pages/sorry/index.html"),
("tag/477_kadaver/index.html", "/pages/sorry/index.html"),
("tag/417_mariner/index.html", "/pages/sorry/index.html"),
("tag/178_troisdorf/index.html", "/pages/sorry/index.html"),
("tag/1067_post/index.html", "/pages/sorry/index.html"),
("tag/174_openoffice/index.html", "/pages/sorry/index.html"),
("tag/998_fernrohr/index.html", "/pages/sorry/index.html"),
("tag/511_auslandsjournal/index.html", "/pages/sorry/index.html"),
("tag/414_secunia/index.html", "/pages/sorry/index.html"),
("tag/62_keepass/index.html", "/pages/sorry/index.html"),
("tag/910_adobe/index.html", "/pages/sorry/index.html"),
("tag/974_transistoren/index.html", "/pages/sorry/index.html"),
("tag/641_elektronischer_personalausweis/index.html", "/pages/sorry/index.html"),
("tag/877_copypath/index.html", "/pages/sorry/index.html"),
("tag/797_total_commander/index.html", "/pages/sorry/index.html"),
("tag/252_deutschland/index.html", "/pages/sorry/index.html"),
("tag/1076_scan/index.html", "/pages/sorry/index.html"),
("tag/238_a4/index.html", "/pages/sorry/index.html"),
("tag/501_kampagne/index.html", "/pages/sorry/index.html"),
("tag/346_passwort/index.html", "/pages/sorry/index.html"),
("tag/478_privatsphaere/index.html", "/pages/sorry/index.html"),
("tag/389_scheinkraft/index.html", "/pages/sorry/index.html"),
("tag/401_drucker/index.html", "/pages/sorry/index.html"),
("tag/553_rc/index.html", "/pages/sorry/index.html"),
("tag/1091_duckduckgo/index.html", "/pages/sorry/index.html"),
("tag/614_nintendo/index.html", "/pages/sorry/index.html"),
("tag/1016_parship/index.html", "/pages/sorry/index.html"),
("tag/486_katze/index.html", "/pages/sorry/index.html"),
("tag/194_weltraum/index.html", "/pages/sorry/index.html"),
("tag/880_kostenlos/index.html", "/pages/sorry/index.html"),
("tag/32_mikrocontroller/page2.html", "/pages/sorry/index.html"),
("tag/32_mikrocontroller/index.html", "/pages/sorry/index.html"),
("tag/872_sandisk_sansa_clip/index.html", "/pages/sorry/index.html"),
("tag/71_licht/index.html", "/pages/sorry/index.html"),
("tag/899_all/index.html", "/pages/sorry/index.html"),
("tag/434_3d/index.html", "/pages/sorry/index.html"),
("tag/585_mini_itx/index.html", "/pages/sorry/index.html"),
("tag/1113_wiki/index.html", "/pages/sorry/index.html"),
("tag/512_idiot/index.html", "/pages/sorry/index.html"),
("tag/773_netzneutralitaet/index.html", "/pages/sorry/index.html"),
("tag/239_v2/index.html", "/pages/sorry/index.html"),
("tag/1105_fortschritt/index.html", "/pages/sorry/index.html"),
("tag/804_internetverbindung/index.html", "/pages/sorry/index.html"),
("tag/1092_jp2a/index.html", "/pages/sorry/index.html"),
("tag/116_wetter/index.html", "/pages/sorry/index.html"),
("tag/94_mars/index.html", "/pages/sorry/index.html"),
("tag/887_mozilla/index.html", "/pages/sorry/index.html"),
("tag/606_bundesvorstand/index.html", "/pages/sorry/index.html"),
("tag/555_wm/index.html", "/pages/sorry/index.html"),
("tag/99_addons/index.html", "/pages/sorry/index.html"),
("tag/58_computer/page2.html", "/pages/sorry/index.html"),
("tag/58_computer/index.html", "/pages/sorry/index.html"),
("tag/455_gczii/index.html", "/pages/sorry/index.html"),
("tag/844_performance/index.html", "/pages/sorry/index.html"),
("tag/162_kommentare/index.html", "/pages/sorry/index.html"),
("tag/908_avreloaded/index.html", "/pages/sorry/index.html"),
("tag/274_prince_of_persia/index.html", "/pages/sorry/index.html"),
("tag/20_schnittstelle/index.html", "/pages/sorry/index.html"),
("tag/563_antenne/index.html", "/pages/sorry/index.html"),
("tag/841_opensource/index.html", "/pages/sorry/index.html"),
("tag/513_apps/index.html", "/pages/sorry/index.html"),
("tag/528_astrium/index.html", "/pages/sorry/index.html"),
("tag/185_microsoft/index.html", "/pages/sorry/index.html"),
("tag/869_umweltzerstoerung/index.html", "/pages/sorry/index.html"),
("tag/1051_hausmeister/index.html", "/pages/sorry/index.html"),
("tag/23_kabel/index.html", "/pages/sorry/index.html"),
("tag/1078_fotografie/index.html", "/pages/sorry/index.html"),
("tag/646_bsi/index.html", "/pages/sorry/index.html"),
("tag/971_mikroprozessor/index.html", "/pages/sorry/index.html"),
("tag/205_suse/index.html", "/pages/sorry/index.html"),
("tag/370_image_fulgurator/index.html", "/pages/sorry/index.html"),
("tag/183_schaeuble/index.html", "/pages/sorry/index.html"),
("tag/204_opensuse/page2.html", "/pages/sorry/index.html"),
("tag/204_opensuse/index.html", "/pages/sorry/index.html"),
("tag/808_mini_itx/index.html", "/pages/sorry/index.html"),
("tag/332_rfid/index.html", "/pages/sorry/index.html"),
("tag/18_festplatte/index.html", "/pages/sorry/index.html"),
("tag/649_firewall/index.html", "/pages/sorry/index.html"),
("tag/543_htc/index.html", "/pages/sorry/index.html"),
("tag/527_eads/index.html", "/pages/sorry/index.html"),
("tag/444_cache/index.html", "/pages/sorry/index.html"),
("tag/756_cpan/index.html", "/pages/sorry/index.html"),
("tag/1034_maus/index.html", "/pages/sorry/index.html"),
("tag/446_garmin_etrex_legend/index.html", "/pages/sorry/index.html"),
("tag/158_wasser/index.html", "/pages/sorry/index.html"),
("tag/569_dokumentation/index.html", "/pages/sorry/index.html"),
("tag/425_helpdesk/index.html", "/pages/sorry/index.html"),
("tag/961_tls/index.html", "/pages/sorry/index.html"),
("tag/547_einstellungen/index.html", "/pages/sorry/index.html"),
("tag/351_mysqldumper/index.html", "/pages/sorry/index.html"),
("tag/749_linkvalidator/index.html", "/pages/sorry/index.html"),
("tag/310_thermostat/index.html", "/pages/sorry/index.html"),
("tag/830_gesellschaft/index.html", "/pages/sorry/index.html"),
("tag/515_1984/index.html", "/pages/sorry/index.html"),
("tag/531_baikonur/index.html", "/pages/sorry/index.html"),
("tag/739_madrid/index.html", "/pages/sorry/index.html"),
("tag/142_siemens/index.html", "/pages/sorry/index.html"),
("tag/416_pioneer/index.html", "/pages/sorry/index.html"),
("tag/1000_kindle/index.html", "/pages/sorry/index.html"),
("tag/823_joomla_1_6/index.html", "/pages/sorry/index.html"),
("tag/374_projektion/index.html", "/pages/sorry/index.html"),
("tag/901_kohlmeisen/index.html", "/pages/sorry/index.html"),
("tag/371_julius_von_bismark/index.html", "/pages/sorry/index.html"),
("tag/618_gamepad/index.html", "/pages/sorry/index.html"),
("tag/820_meteorit/index.html", "/pages/sorry/index.html"),
("tag/480_heise/index.html", "/pages/sorry/index.html"),
("tag/608_repraesentative_demokratie/index.html", "/pages/sorry/index.html"),
("tag/202_lenovo/index.html", "/pages/sorry/index.html"),
("tag/1042_schaltjahr/index.html", "/pages/sorry/index.html"),
("tag/632_scannen/index.html", "/pages/sorry/index.html"),
("tag/704_hacker/index.html", "/pages/sorry/index.html"),
("tag/532_oeffentlich/index.html", "/pages/sorry/index.html"),
("tag/157_kamera/index.html", "/pages/sorry/index.html"),
("tag/1088_renault/index.html", "/pages/sorry/index.html"),
("tag/190_naturkatastrophe/index.html", "/pages/sorry/index.html"),
("tag/858_notebook/index.html", "/pages/sorry/index.html"),
("tag/778_known_hosts/index.html", "/pages/sorry/index.html"),
("tag/340_nacktscanner/index.html", "/pages/sorry/index.html"),
("tag/201_ibm/index.html", "/pages/sorry/index.html"),
("tag/260_fraunhofer_gesellschaft/index.html", "/pages/sorry/index.html"),
("tag/102_browser/index.html", "/pages/sorry/index.html"),
("tag/990_guttenberg/index.html", "/pages/sorry/index.html"),
("tag/769_deutschalnd/index.html", "/pages/sorry/index.html"),
("tag/35_atmel/index.html", "/pages/sorry/index.html"),
("tag/497_line_extender/index.html", "/pages/sorry/index.html"),
("tag/293_mogeln/index.html", "/pages/sorry/index.html"),
("tag/957_suspend/index.html", "/pages/sorry/index.html"),
("tag/38_staat/index.html", "/pages/sorry/index.html"),
("tag/949_comic/index.html", "/pages/sorry/index.html"),
("tag/130_oberhausen/index.html", "/pages/sorry/index.html"),
("tag/732_irights/index.html", "/pages/sorry/index.html"),
("tag/203_rescue_recovery/index.html", "/pages/sorry/index.html"),
("tag/509_natur/index.html", "/pages/sorry/index.html"),
("tag/862_usb_stick/index.html", "/pages/sorry/index.html"),
("tag/421_home_view/index.html", "/pages/sorry/index.html"),
("tag/707_de_maiziere/index.html", "/pages/sorry/index.html"),
("tag/125_neil_armstrong/index.html", "/pages/sorry/index.html"),
("tag/1053_traceroute/index.html", "/pages/sorry/index.html"),
("tag/888_wertstofftonne/index.html", "/pages/sorry/index.html"),
("tag/790_jesus/index.html", "/pages/sorry/index.html"),
("tag/611_gameboy/index.html", "/pages/sorry/index.html"),
("tag/538_blog/page2.html", "/pages/sorry/index.html"),
("tag/538_blog/index.html", "/pages/sorry/index.html"),
("tag/487_auszug/index.html", "/pages/sorry/index.html"),
("tag/883_cookiesafe/index.html", "/pages/sorry/index.html"),
("tag/427_mail/index.html", "/pages/sorry/index.html"),
("tag/763_jaxa/index.html", "/pages/sorry/index.html"),
("tag/168_2009/index.html", "/pages/sorry/index.html"),
("tag/619_logitech_precision/index.html", "/pages/sorry/index.html"),
("tag/333_feed/index.html", "/pages/sorry/index.html"),
("tag/1119_c64/index.html", "/pages/sorry/index.html"),
("tag/122_pio/index.html", "/pages/sorry/index.html"),
("tag/815_snapshot/index.html", "/pages/sorry/index.html"),
("tag/325_datenschutz/page2.html", "/pages/sorry/index.html"),
("tag/325_datenschutz/index.html", "/pages/sorry/index.html"),
("tag/299_wep/index.html", "/pages/sorry/index.html"),
("tag/410_led/index.html", "/pages/sorry/index.html"),
("tag/870_ausbeutung/index.html", "/pages/sorry/index.html"),
("tag/684_urkundenfaelschung/index.html", "/pages/sorry/index.html"),
("tag/857_usb_host/index.html", "/pages/sorry/index.html"),
("tag/948_primfaktor/index.html", "/pages/sorry/index.html"),
("tag/461_uebernachtung/index.html", "/pages/sorry/index.html"),
("tag/695_magnetfeld/index.html", "/pages/sorry/index.html"),
("tag/943_empfaenger/index.html", "/pages/sorry/index.html"),
("tag/445_rotter_see/index.html", "/pages/sorry/index.html"),
("tag/675_trackaufzeichnung/index.html", "/pages/sorry/index.html"),
("tag/642_bmi/index.html", "/pages/sorry/index.html"),
("tag/714_sowjetusion/index.html", "/pages/sorry/index.html"),
("tag/109_china/index.html", "/pages/sorry/index.html"),
("tag/678_zapper/index.html", "/pages/sorry/index.html"),
("tag/209_ersatzteil/index.html", "/pages/sorry/index.html"),
("tag/831_doppelstern/index.html", "/pages/sorry/index.html"),
("tag/647_basisschutz/index.html", "/pages/sorry/index.html"),
("tag/1025_php/index.html", "/pages/sorry/index.html"),
("tag/121_dvd/index.html", "/pages/sorry/index.html"),
("tag/367_streitkraefte/index.html", "/pages/sorry/index.html"),
("tag/41_perl/page2.html", "/pages/sorry/index.html"),
("tag/41_perl/index.html", "/pages/sorry/index.html"),
("tag/1120_retro/index.html", "/pages/sorry/index.html"),
("tag/463_eier/page2.html", "/pages/sorry/index.html"),
("tag/463_eier/index.html", "/pages/sorry/index.html"),
("tag/879_download/index.html", "/pages/sorry/index.html"),
("tag/382_satire/index.html", "/pages/sorry/index.html"),
("tag/881_cookie/index.html", "/pages/sorry/index.html"),
("tag/1095_youtube/index.html", "/pages/sorry/index.html"),
("tag/1114_konfiguration/index.html", "/pages/sorry/index.html"),
("tag/175_java/index.html", "/pages/sorry/index.html"),
("tag/659_include/index.html", "/pages/sorry/index.html"),
("tag/878_amazon/index.html", "/pages/sorry/index.html"),
("tag/198_enmap/index.html", "/pages/sorry/index.html"),
("tag/900_apptodate/index.html", "/pages/sorry/index.html"),
("tag/145_imei/index.html", "/pages/sorry/index.html"),
("tag/871_mp3_player/index.html", "/pages/sorry/index.html"),
("tag/747_transponder/index.html", "/pages/sorry/index.html"),
("tag/995_informationsfreiheit/index.html", "/pages/sorry/index.html"),
("tag/375_allvideo/index.html", "/pages/sorry/index.html"),
("tag/1007_ubuntu_11_10/index.html", "/pages/sorry/index.html"),
("tag/181_ralph_coleman/index.html", "/pages/sorry/index.html"),
("tag/636_spiegel/index.html", "/pages/sorry/index.html"),
("tag/271_modem/index.html", "/pages/sorry/index.html"),
("tag/1071_led_cube/index.html", "/pages/sorry/index.html"),
("tag/816_dinosaurier/index.html", "/pages/sorry/index.html"),
("tag/152_flatrate/index.html", "/pages/sorry/index.html"),
("tag/882_erweiterung/index.html", "/pages/sorry/index.html"),
("tag/720_astroscan/index.html", "/pages/sorry/index.html"),
("tag/1064_leistungsschutzrecht/index.html", "/pages/sorry/index.html"),
("tag/133_mondlandungsluege/index.html", "/pages/sorry/index.html"),
("tag/1001_oyo/index.html", "/pages/sorry/index.html"),
("tag/942_stadt_im_wald/index.html", "/pages/sorry/index.html"),
("tag/1_internet/page3.html", "/pages/sorry/index.html"),
("tag/1_internet/page2.html", "/pages/sorry/index.html"),
("tag/1_internet/index.html", "/pages/sorry/index.html"),
("tag/1_internet/page4.html", "/pages/sorry/index.html"),
("tag/184_piratenpartie/index.html", "/pages/sorry/index.html"),
("tag/359_lange_dateinamen/index.html", "/pages/sorry/index.html"),
("tag/592_spielzeug/index.html", "/pages/sorry/index.html"),
("tag/167_bundetag/index.html", "/pages/sorry/index.html"),
("tag/680_fingerabdruecke/index.html", "/pages/sorry/index.html"),
("tag/950_xkcd/index.html", "/pages/sorry/index.html"),
("tag/290_neujahr/index.html", "/pages/sorry/index.html"),
("tag/283_abbild/index.html", "/pages/sorry/index.html"),
("tag/892_podcacher/index.html", "/pages/sorry/index.html"),
("tag/523_bohrplattform/index.html", "/pages/sorry/index.html"),
("tag/17_linux/page5.html", "/pages/sorry/index.html"),
("tag/17_linux/page3.html", "/pages/sorry/index.html"),
("tag/17_linux/page2.html", "/pages/sorry/index.html"),
("tag/17_linux/page7.html", "/pages/sorry/index.html"),
("tag/17_linux/index.html", "/pages/sorry/index.html"),
("tag/17_linux/page6.html", "/pages/sorry/index.html"),
("tag/17_linux/page4.html", "/pages/sorry/index.html"),
("tag/177_piraten/index.html", "/pages/sorry/index.html"),
("tag/1073_nmap/index.html", "/pages/sorry/index.html"),
("tag/141_sperre/index.html", "/pages/sorry/index.html"),
("tag/67_screenshots/index.html", "/pages/sorry/index.html"),
("tag/237_wernher_von_braun/index.html", "/pages/sorry/index.html"),
("tag/468_nest/index.html", "/pages/sorry/index.html"),
("tag/85_essen/index.html", "/pages/sorry/index.html"),
("tag/1018_if/index.html", "/pages/sorry/index.html"),
("tag/39_ei/index.html", "/pages/sorry/index.html"),
("tag/326_sicherheit/index.html", "/pages/sorry/index.html"),
("tag/405_spooler/index.html", "/pages/sorry/index.html"),
("tag/906_player/index.html", "/pages/sorry/index.html"),
("tag/55_erde/index.html", "/pages/sorry/index.html"),
("tag/599_soluto/index.html", "/pages/sorry/index.html"),
("tag/771_elektrischer_reporter/index.html", "/pages/sorry/index.html"),
("tag/357_dateiname/index.html", "/pages/sorry/index.html"),
("tag/708_innenminister/index.html", "/pages/sorry/index.html"),
("tag/259_forschung/index.html", "/pages/sorry/index.html"),
("tag/93_krieg_der_welten/index.html", "/pages/sorry/index.html"),
("tag/546_kalender/index.html", "/pages/sorry/index.html"),
("tag/1079_canon_eos_400d/index.html", "/pages/sorry/index.html"),
("tag/197_terrasar_x/index.html", "/pages/sorry/index.html"),
("tag/489_kaiman/index.html", "/pages/sorry/index.html"),
("tag/976_ftf/index.html", "/pages/sorry/index.html"),
("tag/1023_css/index.html", "/pages/sorry/index.html"),
("tag/731_piraterie/index.html", "/pages/sorry/index.html"),
("tag/586_debian/index.html", "/pages/sorry/index.html"),
("tag/343_immobilienkrise/index.html", "/pages/sorry/index.html"),
("tag/557_sued_afrika/index.html", "/pages/sorry/index.html"),
("tag/1121_1541/index.html", "/pages/sorry/index.html"),
("tag/1024_static_html/index.html", "/pages/sorry/index.html"),
("tag/257_ausserirdische/index.html", "/pages/sorry/index.html"),
("tag/581_tool/index.html", "/pages/sorry/index.html"),
("tag/422_street_view/index.html", "/pages/sorry/index.html"),
("tag/967_google_street_view/index.html", "/pages/sorry/index.html"),
("tag/230_links/index.html", "/pages/sorry/index.html"),
("tag/565_kim_jung_il/index.html", "/pages/sorry/index.html"),
("tag/505_greenpeace/index.html", "/pages/sorry/index.html"),
("tag/312_temperatur/index.html", "/pages/sorry/index.html"),
("tag/196_disaster/index.html", "/pages/sorry/index.html"),
("tag/843_webhoster/index.html", "/pages/sorry/index.html"),
("tag/402_warteschlange/index.html", "/pages/sorry/index.html"),
("tag/228_gericht/index.html", "/pages/sorry/index.html"),
("tag/947_primzahl/index.html", "/pages/sorry/index.html"),
("tag/526_terrasar/index.html", "/pages/sorry/index.html"),
("tag/568_arte/index.html", "/pages/sorry/index.html"),
("tag/1045_gedit/index.html", "/pages/sorry/index.html"),
("tag/453_ptb/index.html", "/pages/sorry/index.html"),
("tag/473_sprachpaket/index.html", "/pages/sorry/index.html"),
("tag/353_elena/index.html", "/pages/sorry/index.html"),
("tag/977_stf/index.html", "/pages/sorry/index.html"),
("tag/851_batch/index.html", "/pages/sorry/index.html"),
("tag/1060_doktortitel/index.html", "/pages/sorry/index.html"),
("tag/832_heavens_above/index.html", "/pages/sorry/index.html"),
("tag/768_chaos_computer_club/index.html", "/pages/sorry/index.html"),
("tag/14_nas/page2.html", "/pages/sorry/index.html"),
("tag/14_nas/index.html", "/pages/sorry/index.html"),
("tag/113_porno/index.html", "/pages/sorry/index.html"),
("tag/596_hal/index.html", "/pages/sorry/index.html"),
("tag/117_cygwin/index.html", "/pages/sorry/index.html"),
("tag/242_rakete/index.html", "/pages/sorry/index.html"),
("tag/1115_astrofotografie/index.html", "/pages/sorry/index.html"),
("tag/103_politik/page2.html", "/pages/sorry/index.html"),
("tag/103_politik/index.html", "/pages/sorry/index.html"),
("tag/266_loriot/index.html", "/pages/sorry/index.html"),
("tag/161_webseite/index.html", "/pages/sorry/index.html"),
("tag/805_gprs/index.html", "/pages/sorry/index.html"),
("tag/225_bgh/index.html", "/pages/sorry/index.html"),
("tag/220_weltraumtourismus/index.html", "/pages/sorry/index.html"),
("tag/170_berlin/index.html", "/pages/sorry/index.html"),
("tag/227_klage/index.html", "/pages/sorry/index.html"),
("tag/728_recht/index.html", "/pages/sorry/index.html"),
("tag/186_freiheit/index.html", "/pages/sorry/index.html"),
("tag/1103_gparted/index.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page10.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page5.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page3.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page12.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page15.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page13.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page16.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page2.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page14.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page9.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page7.html", "/pages/sorry/index.html"),
("cat/2_aktuell/index.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page6.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page8.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page11.html", "/pages/sorry/index.html"),
("cat/2_aktuell/page4.html", "/pages/sorry/index.html"),
("cat/7_wissenschaft/page2.html", "/pages/sorry/index.html"),
("cat/7_wissenschaft/index.html", "/pages/sorry/index.html"),
("cat/4_basteln/page5.html", "/pages/sorry/index.html"),
("cat/4_basteln/page3.html", "/pages/sorry/index.html"),
("cat/4_basteln/page2.html", "/pages/sorry/index.html"),
("cat/4_basteln/index.html", "/pages/sorry/index.html"),
("cat/4_basteln/page6.html", "/pages/sorry/index.html"),
("cat/4_basteln/page4.html", "/pages/sorry/index.html"),
("cat/6_elektronik/page2.html", "/pages/sorry/index.html"),
("cat/6_elektronik/index.html", "/pages/sorry/index.html"),
("cat/5_buntes/page19.html", "/pages/sorry/index.html"),
("cat/5_buntes/page20.html", "/pages/sorry/index.html"),
("cat/5_buntes/page10.html", "/pages/sorry/index.html"),
("cat/5_buntes/page5.html", "/pages/sorry/index.html"),
("cat/5_buntes/page3.html", "/pages/sorry/index.html"),
("cat/5_buntes/page12.html", "/pages/sorry/index.html"),
("cat/5_buntes/page17.html", "/pages/sorry/index.html"),
("cat/5_buntes/page15.html", "/pages/sorry/index.html"),
("cat/5_buntes/page13.html", "/pages/sorry/index.html"),
("cat/5_buntes/page18.html", "/pages/sorry/index.html"),
("cat/5_buntes/page16.html", "/pages/sorry/index.html"),
("cat/5_buntes/page2.html", "/pages/sorry/index.html"),
("cat/5_buntes/page21.html", "/pages/sorry/index.html"),
("cat/5_buntes/page14.html", "/pages/sorry/index.html"),
("cat/5_buntes/page9.html", "/pages/sorry/index.html"),
("cat/5_buntes/page7.html", "/pages/sorry/index.html"),
("cat/5_buntes/index.html", "/pages/sorry/index.html"),
("cat/5_buntes/page6.html", "/pages/sorry/index.html"),
("cat/5_buntes/page8.html", "/pages/sorry/index.html"),
("cat/5_buntes/page11.html", "/pages/sorry/index.html"),
("cat/5_buntes/page4.html", "/pages/sorry/index.html"),
("cat/9_raumfahrt/page5.html", "/pages/sorry/index.html"),
("cat/9_raumfahrt/page3.html", "/pages/sorry/index.html"),
("cat/9_raumfahrt/page2.html", "/pages/sorry/index.html"),
("cat/9_raumfahrt/index.html", "/pages/sorry/index.html"),
("cat/9_raumfahrt/page6.html", "/pages/sorry/index.html"),
("cat/9_raumfahrt/page4.html", "/pages/sorry/index.html"),
("cat/3_hardware/page5.html", "/pages/sorry/index.html"),
("cat/3_hardware/page3.html", "/pages/sorry/index.html"),
("cat/3_hardware/page2.html", "/pages/sorry/index.html"),
("cat/3_hardware/index.html", "/pages/sorry/index.html"),
("cat/3_hardware/page4.html", "/pages/sorry/index.html"),
("cat/10_privat/index.html", "/pages/sorry/index.html"),
("cat/1_aktuell/page3.html", "/pages/sorry/index.html"),
("cat/1_aktuell/page2.html", "/pages/sorry/index.html"),
("cat/1_aktuell/index.html", "/pages/sorry/index.html"),
("cat/13_astronomie/index.html", "/pages/sorry/index.html"),
("cat/11_geocaching/page3.html", "/pages/sorry/index.html"),
("cat/11_geocaching/page2.html", "/pages/sorry/index.html"),
("cat/11_geocaching/index.html", "/pages/sorry/index.html"),
("cat/8_politik/page5.html", "/pages/sorry/index.html"),
("cat/8_politik/page3.html", "/pages/sorry/index.html"),
("cat/8_politik/page2.html", "/pages/sorry/index.html"),
("cat/8_politik/index.html", "/pages/sorry/index.html"),
("cat/8_politik/page6.html", "/pages/sorry/index.html"),
("cat/8_politik/page4.html", "/pages/sorry/index.html"),
("page10.html", "/pages/sorry/index.html"),
("page11.html", "/pages/sorry/index.html"),
("page12.html", "/pages/sorry/index.html"),
("page13.html", "/pages/sorry/index.html"),
("page14.html", "/pages/sorry/index.html"),
("page15.html", "/pages/sorry/index.html"),
("page16.html", "/pages/sorry/index.html"),
("page17.html", "/pages/sorry/index.html"),
("page18.html", "/pages/sorry/index.html"),
("page19.html", "/pages/sorry/index.html"),
("page20.html", "/pages/sorry/index.html"),
("page21.html", "/pages/sorry/index.html"),
("page22.html", "/pages/sorry/index.html"),
("page23.html", "/pages/sorry/index.html"),
("page24.html", "/pages/sorry/index.html"),
("page25.html", "/pages/sorry/index.html"),
("page26.html", "/pages/sorry/index.html"),
("page27.html", "/pages/sorry/index.html"),
("page28.html", "/pages/sorry/index.html"),
("page29.html", "/pages/sorry/index.html"),
("page2.html", "/pages/sorry/index.html"),
("page30.html", "/pages/sorry/index.html"),
("page31.html", "/pages/sorry/index.html"),
("page32.html", "/pages/sorry/index.html"),
("page33.html", "/pages/sorry/index.html"),
("page34.html", "/pages/sorry/index.html"),
("page35.html", "/pages/sorry/index.html"),
("page36.html", "/pages/sorry/index.html"),
("page37.html", "/pages/sorry/index.html"),
("page38.html", "/pages/sorry/index.html"),
("page39.html", "/pages/sorry/index.html"),
("page3.html", "/pages/sorry/index.html"),
("page40.html", "/pages/sorry/index.html"),
("page41.html", "/pages/sorry/index.html"),
("page42.html", "/pages/sorry/index.html"),
("page43.html", "/pages/sorry/index.html"),
("page44.html", "/pages/sorry/index.html"),
("page45.html", "/pages/sorry/index.html"),
("page46.html", "/pages/sorry/index.html"),
("page47.html", "/pages/sorry/index.html"),
("page48.html", "/pages/sorry/index.html"),
("page49.html", "/pages/sorry/index.html"),
("page4.html", "/pages/sorry/index.html"),
("page50.html", "/pages/sorry/index.html"),
("page51.html", "/pages/sorry/index.html"),
("page52.html", "/pages/sorry/index.html"),
("page53.html", "/pages/sorry/index.html"),
("page54.html", "/pages/sorry/index.html"),
("page55.html", "/pages/sorry/index.html"),
("page56.html", "/pages/sorry/index.html"),
("page57.html", "/pages/sorry/index.html"),
("page58.html", "/pages/sorry/index.html"),
("page59.html", "/pages/sorry/index.html"),
("page5.html", "/pages/sorry/index.html"),
("page60.html", "/pages/sorry/index.html"),
("page61.html", "/pages/sorry/index.html"),
("page62.html", "/pages/sorry/index.html"),
("page63.html", "/pages/sorry/index.html"),
("page64.html", "/pages/sorry/index.html"),
("page65.html", "/pages/sorry/index.html"),
("page66.html", "/pages/sorry/index.html"),
("page67.html", "/pages/sorry/index.html"),
("page68.html", "/pages/sorry/index.html"),
("page6.html", "/pages/sorry/index.html"),
("page7.html", "/pages/sorry/index.html"),
("page8.html", "/pages/sorry/index.html"),
("page9.html", "/pages/sorry/index.html"),
        ]

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
DEPLOY_COMMANDS = {
    'default': [
#        "rsync -rav --delete output/ joe@my.site:/srv/www/site",
        "rsync --checksum --recursive --delete --verbose --compress --progress -e ssh output/ www.jan-grosser.de@ssh.strato.de:nikola/",
    ]
}

# github_deploy configuration
# For more details, read the manual:
# https://getnikola.com/handbook.html#deploying-to-github
# You will need to configure the deployment branch on GitHub.
GITHUB_SOURCE_BRANCH = 'src'
GITHUB_DEPLOY_BRANCH = 'master'

# The name of the remote where you wish to push to, using github_deploy.
GITHUB_REMOTE_NAME = 'origin'

# Whether or not github_deploy should commit to the source branch automatically
# before deploying.
GITHUB_COMMIT_SOURCE = True

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <https://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Executable for the "yui_compressor" filter (defaults to 'yui-compressor').
# YUI_COMPRESSOR_EXECUTABLE = 'yui-compressor'

# Executable for the "closure_compiler" filter (defaults to 'closure-compiler').
# CLOSURE_COMPILER_EXECUTABLE = 'closure-compiler'

# Executable for the "optipng" filter (defaults to 'optipng').
# OPTIPNG_EXECUTABLE = 'optipng'

# Executable for the "jpegoptim" filter (defaults to 'jpegoptim').
# JPEGOPTIM_EXECUTABLE = 'jpegoptim'

# Executable for the "html_tidy_withconfig", "html_tidy_nowrap",
# "html_tidy_wrap", "html_tidy_wrap_attr" and "html_tidy_mini" filters
# (defaults to 'tidy5').
# HTML_TIDY_EXECUTABLE = 'tidy5'

# List of XPath expressions which should be used for finding headers
# ({hx} is replaced by headers h1 through h6).
# You must change this if you use a custom theme that does not use
# "e-content entry-content" as a class for post and page contents.
# HEADER_PERMALINKS_XPATH_LIST = ['*//div[@class="e-content entry-content"]//{hx}']
# Include *every* header (not recommended):
# HEADER_PERMALINKS_XPATH_LIST = ['*//{hx}']

# File blacklist for header permalinks. Contains output path
# (eg. 'output/index.html')
# HEADER_PERMALINKS_FILE_BLACKLIST = []

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.atom', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
# GALLERY_FOLDERS = {"galleries": "galleries"}
# More gallery options:
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []

# Use a thumbnail (defined by ".. previewimage:" in the gallery's index) in
# list of galleries for each gallery
GALLERIES_USE_THUMBNAIL = False

# Image to use as thumbnail for those galleries that don't have one
# None: show a grey square
# '/url/to/file': show the image in that url
GALLERIES_DEFAULT_THUMBNAIL = None

# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# If set to True, EXIF data will be copied when an image is thumbnailed or
# resized. (See also EXIF_WHITELIST)
# PRESERVE_EXIF_DATA = False

# If you have enabled PRESERVE_EXIF_DATA, this option lets you choose EXIF
# fields you want to keep in images. (See also PRESERVE_EXIF_DATA)
#
# For a full list of field names, please see here:
# http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf
#
# This is a dictionary of lists. Each key in the dictionary is the
# name of a IDF, and each list item is a field you want to preserve.
# If you have a IDF with only a '*' item, *EVERY* item in it will be
# preserved. If you don't want to preserve anything in a IDF, remove it
# from the setting. By default, no EXIF information is kept.
# Setting the whitelist to anything other than {} implies
# PRESERVE_EXIF_DATA is set to True
# To preserve ALL EXIF data, set EXIF_WHITELIST to {"*": "*"}

# EXIF_WHITELIST = {}

# Some examples of EXIF_WHITELIST settings:

# Basic image information:
# EXIF_WHITELIST['0th'] = [
#    "Orientation",
#    "XResolution",
#    "YResolution",
# ]

# If you want to keep GPS data in the images:
# EXIF_WHITELIST['GPS'] = ["*"]

# Embedded thumbnail information:
# EXIF_WHITELIST['1st'] = ["*"]

# If set to True, any ICC profile will be copied when an image is thumbnailed or
# resized.
# PRESERVE_ICC_PROFILES = False

# Folders containing images to be used in normal posts or pages.
# IMAGE_FOLDERS is a dictionary of the form {"source": "destination"},
# where "source" is the folder containing the images to be published, and
# "destination" is the folder under OUTPUT_PATH containing the images copied
# to the site. Thumbnail images will be created there as well.

# To reference the images in your posts, include a leading slash in the path.
# For example, if IMAGE_FOLDERS = {'images': 'images'}, write
#
#   .. image:: /images/tesla.jpg
#
# See the Nikola Handbook for details (in the “Embedding Images” and
# “Thumbnails” sections)

# Images will be scaled down according to IMAGE_THUMBNAIL_SIZE and MAX_IMAGE_SIZE
# options, but will have to be referenced manually to be visible on the site
# (the thumbnail has ``.thumbnail`` added before the file extension by default,
# but a different naming template can be configured with IMAGE_THUMBNAIL_FORMAT).

IMAGE_FOLDERS = {'images': 'images'}
# IMAGE_THUMBNAIL_SIZE = 400
IMAGE_THUMBNAIL_FORMAT = '{name}.thumbnail{ext}'

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to ' old posts, page %d' or ' page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
#
# (translatable) If the following is empty, defaults to BLOG_TITLE:
# INDEXES_TITLE = ""
#
# (translatable) If the following is empty, defaults to ' [old posts,] page %d' (see above):
# INDEXES_PAGES = ""
#
# If the following is True, INDEXES_PAGES is also displayed on the main (the
# newest) index page (index.html):
# INDEXES_PAGES_MAIN = False
#
# If the following is True, index-1.html has the oldest posts, index-2.html the
# second-oldest posts, etc., and index.html has the newest posts. This ensures
# that all posts on index-x.html will forever stay on that page, now matter how
# many new posts are added.
# If False, index-1.html has the second-newest posts, index-2.html the third-newest,
# and index-n.html the oldest posts. When this is active, old posts can be moved
# to other index pages when new posts are added.
# INDEXES_STATIC = True
#
# (translatable) If PRETTY_URLS is set to True, this setting will be used to create
# prettier URLs for index pages, such as page/2/index.html instead of index-2.html.
# Valid values for this settings are:
#   * False,
#   * a list or tuple, specifying the path to be generated,
#   * a dictionary mapping languages to lists or tuples.
# Every list or tuple must consist of strings which are used to combine the path;
# for example:
#     ['page', '{number}', '{index_file}']
# The replacements
#     {number}     --> (logical) page number;
#     {old_number} --> the page number inserted into index-n.html before (zero for
#                      the main page);
#     {index_file} --> value of option INDEX_FILE
# are made.
# Note that in case INDEXES_PAGES_MAIN is set to True, a redirection will be created
# for the full URL with the page number of the main page to the normal (shorter) main
# page URL.
# INDEXES_PRETTY_PAGE_URL = False
#
# If the following is true, a page range navigation will be inserted to indices.
# Please note that this will undo the effect of INDEXES_STATIC, as all index pages
# must be recreated whenever the number of pages changes.
# SHOW_INDEX_PAGE_NAVIGATION = False

# If the following is True, a meta name="generator" tag is added to pages. The
# generator tag is used to specify the software used to generate the page
# (it promotes Nikola).
# META_GENERATOR_TAG = True

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored. Set to None to disable.
# Can be any of:
# algol, algol_nu, autumn, borland, bw, colorful, default, emacs, friendly,
# fruity, igor, lovelace, manni, monokai, murphy, native, paraiso-dark,
# paraiso-light, pastie, perldoc, rrt, tango, trac, vim, vs, xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# Check with list(pygments.styles.get_all_styles()) in an interpreter.
#
# CODE_COLOR_SCHEME = 'default'

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
    ("icon", "/files/fatcow_icons/16x16/comment.png", "16x16"),
)

# Show teasers (instead of full posts) in indexes? Defaults to False.
# INDEX_TEASERS = False
INDEX_TEASERS = True

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {post_title}                  The title of the post.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# Append a URL query to the FEED_READ_MORE_LINK in Atom and RSS feeds. Advanced
# option used for traffic source tracking.
# Minimum example for use with Piwik: "pk_campaign=feed"
# The following tags exist and are replaced for you:
# {feedRelUri}                  A relative link to the feed.
# {feedFormat}                  The name of the syndication format.
# Example using replacement for use with Google Analytics:
# "utm_source={feedRelUri}&utm_medium=nikola_feed&utm_campaign={feedFormat}_feed"
FEED_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = ""
# I recommend using the Creative Commons' wizard:
# https://creativecommons.org/choose/
# LICENSE = """
# <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
# <img alt="Creative Commons License BY-NC-SA"
# style="border-width:0; margin-bottom:12px;"
# src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"></a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
# CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by         <a href="https://getnikola.com" rel="nofollow">Nikola</a>         {license}'
CONTENT_FOOTER = '<img alt="Creative Commons License BY" style="border-width:0; margin-bottom:12px;" src="https://i.creativecommons.org/l/by/2.0/88x31.png"><br>If not explicitly specified otherwise this work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/2.0/">Creative Commons Attribution 2.0 Generic License</a>. Proudly made with <a href="https://getnikola.com" rel="nofollow">Nikola</a> and other Free and OpenSource Software.'

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# If you need to use the literal braces '{' and '}' in your footer text, use
# '{{' and '}}' to escape them (str.format is used)
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# A simple copyright tag for inclusion in RSS feeds that works just
# like CONTENT_FOOTER and CONTENT_FOOTER_FORMATS
# RSS_COPYRIGHT = 'Contents © {date} <a href="mailto:{email}">{author}</a> {license}'
RSS_COPYRIGHT = '<img alt="Creative Commons License BY" style="border-width:0; margin-bottom:12px;" src="https://i.creativecommons.org/l/by/2.0/88x31.png"><br>If not explicitly specified otherwise this work is licensed under a <a rel="license" href="https://creativecommons.org/licenses/by/2.0/">Creative Commons Attribution 2.0 Generic License</a>. Proudly made with <a href="https://getnikola.com" rel="nofollow">Nikola</a> and other Free and OpenSource Software.'
# RSS_COPYRIGHT_PLAIN = 'Contents © {date} {author} {license}'
RSS_COPYRIGHT_PLAIN = 'CC-BY-2.0 {author}'
RSS_COPYRIGHT_FORMATS = CONTENT_FOOTER_FORMATS

# To use comments, you can choose between different third party comment
# systems.  The following comment systems are supported by Nikola:
#   disqus, facebook, intensedebate, isso, muut, commento
# You can leave this option blank to disable comments.
COMMENT_SYSTEM = ""
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = ""

# Create index.html for page folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the PAGE_INDEX
#          will not be generated for that directory.
# PAGE_INDEX = False
# Enable comments on pages (i.e. not posts)?
# COMMENTS_IN_PAGES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
# INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
STRIP_INDEXES = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata.
PRETTY_URLS = True

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts (not pages!) by default
# SCHEDULE_ALL = False

# Do you want to add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you want support for the $.$ syntax (which may conflict with running
# text!), just use this config:
# MATHJAX_CONFIG = """
# <script type="text/x-mathjax-config">
# MathJax.Hub.Config({
#     tex2jax: {
#         inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#         displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
#         processEscapes: true
#     },
#     displayAlign: 'center', // Change this to 'left' if you want left-aligned equations.
#     "HTML-CSS": {
#         styles: {'.MathJax_Display': {"margin": 0}}
#     }
# });
# </script>
# """

# Want to use KaTeX instead of MathJax? While KaTeX may not support every
# feature yet, it's faster and the output looks better.
# USE_KATEX = False

# KaTeX auto-render settings. If you want support for the $.$ syntax (which may
# conflict with running text!), just use this config:
# KATEX_AUTO_RENDER = """
# delimiters: [
#     {left: "$$", right: "$$", display: true},
#     {left: "\\\\[", right: "\\\\]", display: true},
#     {left: "\\\\begin{equation*}", right: "\\\\end{equation*}", display: true},
#     {left: "$", right: "$", display: false},
#     {left: "\\\\(", right: "\\\\)", display: false}
# ]
# """

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter': {'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# Defaults are markdown.extensions.(fenced_code|codehilite|extra)
# markdown.extensions.meta is required for Markdown metadata.
MARKDOWN_EXTENSIONS = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.extra']

# Options to be passed to markdown extensions (See https://python-markdown.github.io/reference/)
# Default is {} (no config at all)
# MARKDOWN_EXTENSION_CONFIGS = {}


# Extra options to pass to the pandoc command.
# by default, it's empty, is a list of strings, for example
# ['-F', 'pandoc-citeproc', '--bibliography=/Users/foo/references.bib']
# Pandoc does not demote headers by default.  To enable this, you can use, for example
# ['--base-header-level=2']
# PANDOC_OPTIONS = []

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty (which is
# the default right now)
# (translatable)
# SOCIAL_BUTTONS_CODE = """
# <!-- Social buttons -->
# <div id="addthisbox" class="addthis_toolbox addthis_peekaboo_style addthis_default_style addthis_label_style addthis_32x32_style">
# <a class="addthis_button_more">Share</a>
# <ul><li><a class="addthis_button_facebook"></a>
# <li><a class="addthis_button_google_plusone_share"></a>
# <li><a class="addthis_button_linkedin"></a>
# <li><a class="addthis_button_twitter"></a>
# </ul>
# </div>
# <script src="https://s7.addthis.com/js/300/addthis_widget.js#pubid=ra-4f7088a56bb93798"></script>
# <!-- End of social buttons -->
# """

# Show link to source for the posts?
# SHOW_SOURCELINK = True
# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
# COPY_SOURCES = True

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
# GENERATE_RSS = True

# By default, Nikola does not generates Atom files for indexes and links to
# them. Generate Atom for tags by setting TAG_PAGES_ARE_INDEXES to True.
# Atom feeds are built based on INDEX_DISPLAY_POST_COUNT and not FEED_LENGTH
# Switch between plain-text summaries and full HTML content using the
# FEED_TEASER option. FEED_LINKS_APPEND_QUERY is also respected. Atom feeds
# are generated even for old indexes and have pagination link relations
# between each other. Old Atom feeds with no changes are marked as archived.
# GENERATE_ATOM = False

# Only include teasers in Atom and RSS feeds. Disabling include the full
# content. Defaults to True.
# FEED_TEASERS = True

# Strip HTML from Atom and RSS feed summaries and content. Defaults to False.
# FEED_PLAIN = False

# Number of posts in Atom and RSS feeds.
# FEED_LENGTH = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a FeedBurner feed or something else.
# RSS_LINK = None

# A search form to search this site, for the sidebar. You can use a Google
# custom search (https://www.google.com/cse/)
# Or a DuckDuckGo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- DuckDuckGo custom search -->
# <form method="get" id="search" action="https://duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s">
# <input type="hidden" name="k8" value="#444444">
# <input type="hidden" name="k9" value="#D51920">
# <input type="hidden" name="kt" value="h">
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;">
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a Google search form, here's an example that should just work:
# SEARCH_FORM = """
# <!-- Google custom search -->
# <form method="get" action="https://www.google.com/search" class="navbar-form navbar-right" role="search">
# <div class="form-group">
# <input type="text" name="q" class="form-control" placeholder="Search">
# </div>
# <button type="submit" class="btn btn-primary">
# 	<span class="glyphicon glyphicon-search"></span>
# </button>
# <input type="hidden" name="sitesearch" value="%s">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL

# Use content distribution networks for jQuery, twitter-bootstrap css and js,
# and html5shiv (for older versions of Internet Explorer)
# If this is True, jQuery and html5shiv are served from the Google CDN and
# Bootstrap is served from BootstrapCDN (provided by MaxCDN)
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Check for USE_CDN compatibility.
# If you are using custom themes, have configured the CSS properly and are
# receiving warnings about incompatibility but believe they are incorrect, you
# can set this to False.
# USE_CDN_WARNING = True

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# (translatable)
# BODY_END = ""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '.*\/(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.rst'
# (Note the '.*\/' in the beginning -- matches source paths relative to conf.py)
# FILE_METADATA_REGEXP = None

# Should titles fetched from file metadata be unslugified (made prettier?)
# FILE_METADATA_UNSLUGIFY_TITLES = True

# If enabled, extract metadata from docinfo fields in reST documents.
# If your text files start with a level 1 heading, it will be treated as the
# document title and will be removed from the text.
# USE_REST_DOCINFO_METADATA = False

# If enabled, hide docinfo fields in reST document output
# HIDE_REST_DOCINFO = False

# Map metadata from other formats to Nikola names.
# Supported formats: yaml, toml, rest_docinfo, markdown_metadata
# METADATA_MAPPING = {}
#
# Example for Pelican compatibility:
# METADATA_MAPPING = {
#     "rest_docinfo": {"summary": "description", "modified": "updated"},
#     "markdown_metadata": {"summary": "description", "modified": "updated"}
# }
# Other examples: https://getnikola.com/handbook.html#mapping-metadata-from-other-formats

# Map metadata between types/values. (Runs after METADATA_MAPPING.)
# Supported formats: nikola, yaml, toml, rest_docinfo, markdown_metadata
# The value on the right should be a dict of callables.
# METADATA_VALUE_MAPPING = {}
# Examples:
# METADATA_VALUE_MAPPING = {
#     "yaml": {"keywords": lambda value: ', '.join(value)},  # yaml: 'keywords' list -> str
#     "nikola": {
#         "widgets": lambda value: value.split(', '),  # nikola: 'widgets' comma-separated string -> list
#         "tags": str.lower  # nikola: force lowercase 'tags' (input would be string)
#      }
# }

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards
#     # 'card': 'summary',          # Card type, you can also use 'summary_large_image',
#                                   # see https://dev.twitter.com/cards/types
#     # 'site': '@website',         # twitter nick for the website
#     # 'creator': '@username',     # Username for the content creator / author.
# }

# Bundle JS and CSS into single files to make site loading faster in a HTTP/1.1
# environment but is not recommended for HTTP/2.0 when caching is used.
# Defaults to True.
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Special settings to disable only parts of the indexes plugin.
# Use with care.
# DISABLE_INDEXES = False
# DISABLE_MAIN_ATOM_FEED = False
# DISABLE_MAIN_RSS_FEED = False

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
# EXTRA_PLUGINS_DIRS = []

# Add the absolute paths to directories containing themes to use them.
# For example, the `v7` directory of your clone of the Nikola themes
# repository.
# EXTRA_THEMES_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# Enabling hyphenation has been shown to break math support in some cases,
# use with caution.
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
# DEMOTE_HEADERS = 1

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# If set to True, the tags 'draft', 'mathjax' and 'private' have special
# meaning. If set to False, these tags are handled like regular tags.
USE_TAG_METADATA = False

# If set to True, a warning is issued if one of the 'draft', 'mathjax'
# and 'private' tags are found in a post. Useful for checking that
# migration was successful.
WARN_ABOUT_TAG_METADATA = False

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []

# Add any post types here that you want to be displayed without a title.
# Ir your theme supports it, the titles will not be shown.
TYPES_TO_HIDE_TITLE = []
