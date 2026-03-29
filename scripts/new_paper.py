#!/usr/bin/env python3
"""Generate a new paper entry from the standard template.

Usage:
    python scripts/new_paper.py \
        --title "FourCastNet: A Global Data-driven Weather Forecasting Model" \
        --domain ocean-forecasting \
        --year 2023 \
        --venue "arXiv preprint" \
        --url "https://arxiv.org/abs/2202.11214" \
        --code-url "https://github.com/NVlabs/FourCastNet" \
        --status backlog \
        --priority high \
        --project ocean-sr
"""

import argparse
import datetime
import os
import re
import subprocess
import sys

VALID_DOMAINS = [
    "ocean-forecasting",
    "scientific-sr",
    "uncertainty-calibration",
    "code-agent",
]

VALID_STATUSES = ["backlog", "curated"]
VALID_PRIORITIES = ["high", "medium", "low"]

VALID_PROJECTS = [
    "ocean-sr",
    "chl-sr-reliability",
    "agent-loss-migration",
    "none",
]

TEMPLATE_BODY = """
## One-Line Verdict

<!-- A single evaluative sentence — what this paper actually achieves, not what it claims. -->

## Project Relation

<!-- Which project(s) does this serve? Be specific about HOW it relates. -->

## Why Noteworthy

<!-- 2-3 sentences: why this paper matters to OUR work specifically. -->

## Core Method

<!-- 3-5 sentences describing the actual technical approach. -->

## Hidden Assumptions & Weaknesses

<!-- What the authors do NOT say. Limitations they understate. Conditions where this breaks. -->

## Reading Advice

<!-- Which sections to read carefully, which to skim. Prerequisites. -->

## Reproduction Value

<!-- Is it worth reimplementing? Effort estimate. Is released code usable? -->

## Evidence

<!-- Key quantitative results. Specific tables/figures/metrics. At least 3 for curated. -->

## Notes

<!-- Connections to other entries. Open questions. Follow-up ideas. -->
"""


def title_to_slug(title: str, max_length: int = 60) -> str:
    """Convert a paper title to a filename-safe slug."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    slug = slug.strip("-")
    if len(slug) > max_length:
        slug = slug[:max_length].rstrip("-")
    return slug


def get_git_username() -> str:
    """Get the current git user name, or 'unknown'."""
    try:
        result = subprocess.run(
            ["git", "config", "user.name"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        name = result.stdout.strip()
        return name if name else "unknown"
    except Exception:
        return "unknown"


def main():
    parser = argparse.ArgumentParser(
        description="Generate a new paper entry from the standard template."
    )
    parser.add_argument("--title", required=True, help="Full paper title")
    parser.add_argument(
        "--domain",
        required=True,
        choices=VALID_DOMAINS,
        help="Research domain",
    )
    parser.add_argument("--year", required=True, type=int, help="Publication year")
    parser.add_argument("--venue", required=True, help="Conference or journal")
    parser.add_argument("--url", required=True, help="Paper URL")
    parser.add_argument("--code-url", default=None, help="Code repository URL")
    parser.add_argument(
        "--status",
        default="backlog",
        choices=VALID_STATUSES,
        help="Entry status (default: backlog)",
    )
    parser.add_argument(
        "--priority",
        default="medium",
        choices=VALID_PRIORITIES,
        help="Priority (default: medium)",
    )
    parser.add_argument(
        "--project",
        default="none",
        choices=VALID_PROJECTS,
        help="Related project (default: none)",
    )

    args = parser.parse_args()

    # Build file path
    slug = title_to_slug(args.title)
    filename = f"{args.year}-{slug}.md"

    # Find repo root (look for domains/ directory)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    target_dir = os.path.join(repo_root, "domains", args.domain, args.status)
    target_path = os.path.join(target_dir, filename)

    # Create directory if needed
    os.makedirs(target_dir, exist_ok=True)

    # Check if file already exists
    if os.path.exists(target_path):
        print(f"ERROR: File already exists: {target_path}", file=sys.stderr)
        sys.exit(1)

    # Get metadata
    added_by = get_git_username()
    added_date = datetime.date.today().isoformat()
    code_url = f'"{args.code_url}"' if args.code_url else "null"

    # Generate front matter
    front_matter = f"""---
title: "{args.title}"
authors: ["TODO"]
year: {args.year}
venue: "{args.venue}"
url: "{args.url}"
code_url: {code_url}
domain: "{args.domain}"
tags: ["TODO"]
status: "{args.status}"
added_by: "{added_by}"
added_date: "{added_date}"
projects: ["{args.project}"]
priority: "{args.priority}"
---"""

    # Write file
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(front_matter)
        f.write(TEMPLATE_BODY)

    print(f"Created: {target_path}")
    print(f"Next steps:")
    print(f"  1. Fill in authors and tags in the front matter")
    print(f"  2. Complete all body sections")
    print(f"  3. Open a PR: git checkout -b paper/{args.domain}/{slug}")


if __name__ == "__main__":
    main()
