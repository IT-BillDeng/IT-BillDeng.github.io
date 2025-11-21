#!/usr/bin/env python3
"""
Generate Jekyll publication markdown files from a BibTeX export
(e.g., from Google Scholar).

Requirements:
    pip install pybtex

Usage:
    python generate_md_from_bib.py --bib bibtex.bib --output ../_publications

Notes:
- Outputs one .md per entry with front matter expected by academicpages.
- Derives venue from `booktitle` (conference) or `journal`.
- Date uses year/month/day if present; otherwise defaults to YYYY-01-01.
"""

import argparse
import os
import re
from datetime import datetime
from pathlib import Path

from pybtex.database.input import bibtex


def slugify(title: str) -> str:
    """Build a URL-safe slug from the title."""
    clean = title.replace("{", "").replace("}", "").replace("\\", "")
    clean = re.sub(r"\s+", "-", clean)
    clean = re.sub(r"[^a-zA-Z0-9_-]", "", clean)
    clean = re.sub(r"-{2,}", "-", clean)
    return clean.strip("-").lower()


def format_authors(entry_persons) -> str:
    """Return authors as 'First Last, First Last'."""
    authors = []
    for person in entry_persons:
        first = " ".join(person.first_names)
        last = " ".join(person.last_names)
        parts = [p for p in (first, last) if p]
        authors.append(" ".join(parts))
    return ", ".join(authors)


def build_date(fields: dict) -> str:
    year = fields.get("year", "1900")
    month = fields.get("month", "01")
    day = fields.get("day", "01")
    # Handle month abbreviations or numeric
    try:
        if isinstance(month, str) and month.isalpha():
            month_num = datetime.strptime(month[:3], "%b").month
            month = f"{month_num:02d}"
        else:
            month = f"{int(month):02d}"
    except Exception:
        month = "01"
    try:
        day = f"{int(day):02d}"
    except Exception:
        day = "01"
    return f"{year}-{month}-{day}"


def main():
    parser = argparse.ArgumentParser(description="Generate publication markdown from BibTeX.")
    parser.add_argument("--bib", required=True, help="Path to BibTeX file (export from Google Scholar).")
    parser.add_argument(
        "--output",
        default="../_publications",
        help="Output directory for markdown files (default: ../_publications)",
    )
    args = parser.parse_args()

    bib_path = Path(args.bib).expanduser()
    out_dir = Path(args.output).expanduser()
    out_dir.mkdir(parents=True, exist_ok=True)

    parser_bib = bibtex.Parser()
    bibdata = parser_bib.parse_file(str(bib_path))

    for bib_id, entry in bibdata.entries.items():
        fields = entry.fields
        title = fields.get("title", "").replace("{", "").replace("}", "").replace("\\", "")
        if not title:
            print(f"[skip] {bib_id}: missing title")
            continue

        # venue
        venue = fields.get("booktitle") or fields.get("journal") or ""
        venue = venue.replace("{", "").replace("}", "").replace("\\", "")

        # collection/category logic
        category = "conferences" if "booktitle" in fields else "manuscripts"

        date_str = build_date(fields)
        slug = slugify(title)
        md_name = f"{date_str}-{slug}.md"
        permalink = f"/publication/{date_str}-{slug}"

        authors_fmt = format_authors(entry.persons.get("author", []))

        # citation (simple)
        citation = f"{authors_fmt}. \"{title}.\" {venue}, {fields.get('year', '')}."

        # Build front matter
        lines = [
            "---",
            f'title: "{title}"',
            "collection: publications",
            f"category: {category}",
            f"permalink: {permalink}",
            f"date: {date_str}",
            f"venue: '{venue}'",
            f"citation: '{citation}'",
            "excerpt: ''",  # placeholder, fill if needed
            "bibtex: |",
        ]

        # BibTeX block (as provided)
        raw_bib = entry.to_string("bibtex")
        for bib_line in raw_bib.splitlines():
            lines.append(f"  {bib_line}")
        lines.append("---")

        # Optional note/excerpt
        if "note" in fields:
            lines.append(fields["note"])

        md_path = out_dir / md_name
        md_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"[ok] wrote {md_path}")


if __name__ == "__main__":
    main()
