"""MkDocs hooks for fixing raw HTML image paths in imported pages.

Markdown image syntax is resolved by MkDocs, but raw HTML ``<img>`` tags are
left untouched. When multirepo imports a source page such as
``kcd2026/sponsors.md`` and MkDocs emits it as ``kcd2026/sponsors/index.html``,
raw paths like ``./images/foo.png`` incorrectly resolve in the browser to
``kcd2026/sponsors/images/foo.png`` instead of ``kcd2026/images/foo.png``.
"""

from __future__ import annotations

import posixpath
import re

_IMAGE_SRC_RE = re.compile(
    r"(?P<prefix><img\b[^>]*?\bsrc=)(?P<quote>[\"'])(?P<src>[^\"']+)(?P=quote)",
    re.IGNORECASE,
)

_ABSOLUTE_OR_SPECIAL_RE = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|/|#)", re.IGNORECASE)


def _page_output_dir(dest_uri: str) -> str:
    """Return the URL directory that contains the generated page."""
    normalized = dest_uri.replace("\\", "/")
    directory = posixpath.dirname(normalized)
    return "" if directory == "." else directory


def _rewrite_raw_html_image_sources(markdown: str, src_uri: str, dest_uri: str) -> str:
    """Rewrite relative raw HTML image paths from source-file to output-page context."""
    source_dir = posixpath.dirname(src_uri.replace("\\", "/"))
    if source_dir == ".":
        source_dir = ""
    output_dir = _page_output_dir(dest_uri)

    def replace(match: re.Match[str]) -> str:
        image_src = match.group("src")
        if _ABSOLUTE_OR_SPECIAL_RE.match(image_src):
            return match.group(0)

        source_relative_src = image_src[2:] if image_src.startswith("./") else image_src
        source_target = posixpath.normpath(posixpath.join(source_dir, source_relative_src))
        output_relative_src = posixpath.relpath(source_target, output_dir or ".")
        if output_relative_src == ".":
            output_relative_src = posixpath.basename(source_target)

        return f"{match.group('prefix')}{match.group('quote')}{output_relative_src}{match.group('quote')}"

    return _IMAGE_SRC_RE.sub(replace, markdown)


def on_page_markdown(markdown: str, page, config, files) -> str:  # noqa: ANN001
    """Fix raw HTML image paths before Markdown is rendered."""
    return _rewrite_raw_html_image_sources(markdown, page.file.src_uri, page.file.dest_uri)
