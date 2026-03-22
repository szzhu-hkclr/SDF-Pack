#!/usr/bin/env python3
"""
validate-taxonomy-refs.py
Scans generated skill.md / knowledge.md pages for taxonomy_ref values
and validates them against .devin/taxonomy.yaml.
Exit code 0 = all valid, 1 = violations found.
"""

import re
import sys
import yaml
from pathlib import Path

TAXONOMY_PATH = Path(".devin/taxonomy.yaml")
PAGES = [
    Path("pages/skill.md"),
    Path("pages/skill-zh.md"),
    Path("pages/knowledge.md"),
    Path("pages/knowledge-zh.md"),
]

REF_PATTERN = re.compile(r"\bT([1-8])-L([0-4])\b")


def load_valid_refs(taxonomy_path: Path) -> set[str]:
    """Build set of valid taxonomy_ref strings from taxonomy.yaml."""
    with open(taxonomy_path, "r", encoding="utf-8") as f:
        tax = yaml.safe_load(f)
    valid = set()
    for track_id, track_data in tax.get("tracks", {}).items():
        for level_id in track_data.get("levels", {}):
            valid.add(f"{track_id}-{level_id}")
    return valid


def scan_file(path: Path, valid_refs: set[str]) -> list[dict]:
    """Return list of {file, line, ref} for invalid refs."""
    violations = []
    if not path.exists():
        print(f"  ⚠  File not found: {path}")
        return violations
    with open(path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            for match in REF_PATTERN.finditer(line):
                ref = match.group(0)
                if ref not in valid_refs:
                    violations.append(
                        {"file": str(path), "line": line_no, "ref": ref}
                    )
    return violations


def main() -> int:
    if not TAXONOMY_PATH.exists():
        print(f"✖ Taxonomy file not found: {TAXONOMY_PATH}")
        return 1

    valid_refs = load_valid_refs(TAXONOMY_PATH)
    print(f"✔ Loaded {len(valid_refs)} valid taxonomy refs from {TAXONOMY_PATH}")
    print(f"  Valid refs: {sorted(valid_refs)}\n")

    all_violations = []
    for page in PAGES:
        print(f"  Scanning {page} …")
        violations = scan_file(page, valid_refs)
        all_violations.extend(violations)

    if all_violations:
        print(f"\n✖ Found {len(all_violations)} invalid taxonomy_ref(s):\n")
        for v in all_violations:
            print(f"  {v['file']}:{v['line']}  →  {v['ref']}")
        return 1

    print("\n✔ All taxonomy_ref values are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())