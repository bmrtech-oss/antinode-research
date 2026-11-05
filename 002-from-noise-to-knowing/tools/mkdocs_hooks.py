import re

# The site has its own prev/next navigation, so drop the GitHub-only footers.
_FOOTER = re.compile(r"\n*<!-- book-nav:start -->.*?<!-- book-nav:end -->\n?", re.S)


def on_page_markdown(markdown, **kwargs):
    return _FOOTER.sub("\n", markdown)
