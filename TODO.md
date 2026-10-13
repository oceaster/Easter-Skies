# Easter Skies backlog

## ES-01 — 26.2 physics port (not started)
Scope: Minecraft/Fabric mixins, ship storage, rendering and native/core dependencies.
Keep the 1.20.1 baseline reproducible. Identify a working Java/Gradle toolchain and
compile Fabric before touching the live mod stack. Acceptance: isolated 26.2
server/client launch, ship assembly/collision/save/reload and bounded tick cost.
Do not mark a version-string change as a port.

## ES-02 — capture-only large hulls (blocked by ES-01)
Enforce encounter provenance at authoritative creation/assembly paths. No player
crafting/shop/helm bypass. Acceptance: every factory denies an unproven player-built
large hull; generated encounter hulls and refits of acquired hulls remain usable.

## ES-03 — ship registry and law adapters (blocked by ES-01)
Nameable large ships; stable ship ID, persistent ownership and source-container
lookup through moving coordinates. Integrate the named-ship law in EASTER_SHIP_LAW.md
using the existing owner's home roster. Never block piloting or chest theft.
Acceptance: guest owner logout changes ongoing pilot legality; actual storage
withdrawals trigger crime once; unrelated passengers/failed moves do not.

## ES-04 — mixed fleet evaluation (not started)
Compare the unchanged Shippy small-vessel stack against the isolated physics stack
and a mixed test. Measure CPU/tick time, memory, packet traffic, FPS and persistence.
No live-world downgrade, new terrain generation or assumed compatibility.

## Completed source-foundation work
Easter branding, original notices, exact provenance and local AGENTS/PROJECT/TODO
context are staged. check_fork.py verifies these; it does not verify a mod runtime.
The agreed progression and capture/crew goals are in EASTER_FLEET.md.
