# Easter Skies development rules

This is the Easter Fleet experimental fork of ValkyrienSkies/Valkyrien-Skies-2. Preserve upstream
history, license files, authors and per-file notices. Read EASTER_CREDITS.md and
FORK_PROVENANCE.json before publishing artifacts.

Read PROJECT.md and the relevant TODO.md ticket. The agreed progression lives at
https://github.com/oceaster/Easter-Skies/blob/easter/foundation/EASTER_FLEET.md.
Keep Shippy as the baseline: vanilla boat → Shippy vessel → captured large ship.
NPC pirate crews attack all player factions. Large ships are capture-only.

The current baseline is Minecraft 1.20.1. The target server is Minecraft 26.2.
Do not relabel an unsupported binary, downgrade a live world, install experimental
jars or restart game services. Only an isolated tested port can justify promotion.
Keep technical mod IDs and package namespaces stable until a coordinated migration
has concrete compatibility evidence. No source copying from proprietary Shippy.

Use suitable Java/Gradle tooling, isolated outputs and bounded resources. A pure
policy test is not a physics/runtime test. Report exact dependency, compile and
playtest gaps; never claim a feature works from branding or a build alone.
