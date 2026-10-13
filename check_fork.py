#!/usr/bin/env python3
"""Verify source provenance and release metadata without claiming a runtime port."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent

def validate(root=ROOT):
    record = json.loads((root / "FORK_PROVENANCE.json").read_text())
    upstream_license = subprocess.check_output(
        ["git", "-C", str(root), "show", record["upstream_commit"] + ":LICENSE"])
    expected = record["license_sha256"]
    assert hashlib.sha256(upstream_license).hexdigest() == expected, "Wrong upstream license provenance"
    assert hashlib.sha256((root / "LICENSE").read_bytes()).hexdigest() == expected, "Original license changed"
    properties = {}
    for line in (root / "gradle.properties").read_text().splitlines():
        if "=" in line and not line.lstrip().startswith("#"):
            key, value = line.split("=", 1)
            properties[key.strip()] = value.strip()
    assert properties["minecraft_version"] == record["baseline_minecraft"], "Unsupported version relabel"
    meta = json.loads((root / "fabric/src/main/resources/fabric.mod.json").read_text())
    expand = lambda text: re.sub(r"\$\{([^}]+)\}", lambda m: properties.get(m[1], m[0]), text)
    assert meta["id"] == record["technical_mod_id"], "Uncoordinated registry-ID rename"
    assert expand(meta["name"]) == record["brand"], "Fork brand is missing"
    assert expand(meta["license"]) == record["license"], "Metadata contradicts original root license"
    assert not meta["description"].startswith("{$"), "Broken Gradle placeholder"
    assert record["baseline_minecraft"] in meta["depends"]["minecraft"], "Incorrect loader version claim"
    credits = (root / "EASTER_CREDITS.md").read_text()
    assert record["upstream"] in credits and "contributors" in credits, "Upstream attribution missing"
    notices = root / "common/src/main/resources/META-INF/easter"
    for filename in ("LICENSE", "EASTER_CREDITS.md", "FORK_PROVENANCE.json"):
        assert (root / filename).read_bytes() == (notices / filename).read_bytes(), "Resource notice differs: " + filename
    if record["license"] == "LGPL-3.0":
        assert "GNU GENERAL PUBLIC LICENSE" in (root / "COPYING").read_text()
        assert (root / "COPYING").read_bytes() == (notices / "COPYING").read_bytes()
    for document in ("AGENTS.md", "PROJECT.md", "TODO.md"):
        assert (root / document).is_file(), "Project-local context missing: " + document
    print(record["brand"] + ": provenance, credits, license metadata, preserved ID and honest version PASS")

if __name__ == "__main__":
    validate()
