# Easter Fleet — agreed progression and integration boundary

Owen's requirements, 2026-10-13:
1. Keep Shippy Ships. Players need both a purchase path and a build path.
2. NPC pirate crews man roaming hostile ships. They attack every player faction,
   including player pirates; sharing a pirate label is not an alliance.
3. Progression: vanilla boat → small Shippy vessel → board/capture/crew a large
   physics-driven pirate ship. Large ships cannot be purchased or player-built.

## Working baseline and actual status

The live household server is Fabric Minecraft 26.2 / Java 25 with Shippy Ships
1.0.23.1. This session has not removed a mod, changed a live world or restarted
Minecraft. The forks are source foundations, not installed replacements.

Shippy's existing recipes include a ship builder from three logs in a row and a
shapeless conversion of that builder to a cog builder. Noor previously sold only
vanilla boats. An isolated Easter Navy branch stages one cog builder for £0.75,
readable shop text and namespaced item resolution. This is an initial tunable
price, not a claim that encounter economics or combat balance are settled.
A build/harness can verify catalog/namespace handling; an in-game purchase and
construction still need playtesting before a release claim.

Easter Skies, Easter Pirates and Easter Sails are credited forks of the respective
upstream projects. Their selected default branches all target Minecraft 1.20.1.
Keeping their version declarations honest is intentional: changing a version
string cannot port physics mixins, rendering, entity persistence or networking.
No live-world downgrade is proposed.

## Division of work

| Layer | Intended role | What must be demonstrated |
|---|---|---|
| Unmodified Shippy | Small player-built/purchased/lootable ships | Item purchase, build, boarding and NPC control on 26.2 |
| Easter Skies | Large hull physics, collision, moving blocks and persistence | Supported 26.2 server/client pair and bounded loaded ship count |
| Easter Pirates | Encounters, hostile NPC crews, combat and capture | Faction-independent targeting and durable ownership transfer |
| Easter Sails | Wind propulsion and helm/sail behavior | Reliable control of captured large hulls |
| Easter Navy | Economy, factions, shop and household gameplay integration | Existing money/crime rules retained; no shop shortcut to large ships |

Do not merge Shippy source into these forks. Its installed custom license forbids
modification, decompilation and reverse engineering. It permits server/modpack
use with credit. Use unchanged mod behavior and documented integration points.
Distribution hosting permissions need separate review before a public release.

## Capture and crew contract (target behavior)

- Hostile encounter crews remain hostile to citizens, Navy and player pirates.
- Friendly/recruited player crew is a distinct allegiance, not a hostile pirate
  with a team-name exception.
- Boarding, neutralizing defenders and taking control of the helm precede capture.
- Transfer ship ownership atomically on the server; simultaneous boarders cannot
  both acquire it. Persist encounter provenance, ownership and roster with a
  schema version; cover restart, logout, unloaded chunks and sunk/damaged hulls.
- Large-ship creation/assembly must enforce encounter provenance on the server.
  Removing recipes alone is insufficient: helm assembly, commands and generic
  builder paths would otherwise bypass capture-only acquisition.
- Refit and repair an acquired hull without turning that permission into a
  free large-ship factory. No new hull-size, price or crew-pay numbers are settled.
- Keep encounters away from protected spawn/welcome areas; bound active crews
  and ships. Generate no additional live terrain for development tests.
- Ranged combat, cannon ownership, friendly crew and boarding passengers need
  tests with both engine families before promising interoperability.

## Code findings, not performance claims

Pirates has autonomous MotionInvokingBlockEntity control, Sails/Eureka compatibility
paths and hostile PirateEntity player targeting. Its FriendlyPirateEntity is a
separate recruitable implementation. These are starting points; they do not
prove 26.2 support or integration with Shippy entity boats.

Pirates' Fabric metadata also requires vlib. Its controller references Eureka
and Sails APIs; those dependency and class-loading paths must be audited before
claiming the three named mods form a standalone complete runtime stack.
Version pins differ: the forked Skies is 2.4.12, Pirates declares VS 2.4.8.1,
and Sails declares VS 2.4.7+5f9e6e7dcc while its Fabric manifest requires >=2.4.11.
Resolve this mismatch through compilation and runtime tests, not blind version edits.

## Validation sequence

1. Verify each fork's provenance, licenses, branding and preserved technical IDs.
2. Compile the upstream-version baseline with a suitable Java/Gradle toolchain.
3. Build an isolated 26.2 port spike for Skies before addon migration.
4. Test Shippy NPC boarding/steering using supported interfaces; do not assume
   player-controlled input also supports an NPC helmsman.
5. Exercise hostility, capture races, persistence and player crews in an isolated
   disposable test world, never a downgraded copy of the live world.
6. Compare measured tick time, CPU/memory, network traffic and frame rate for
   Shippy-only, large-ship-only and mixed encounters with the same workloads.
7. Deploy a backed-up, compatible release only after those checks and playtesting.

Naming and legal ownership are specified in [EASTER_SHIP_LAW.md](EASTER_SHIP_LAW.md).
Family can always pilot; guests only while the owner is online. Ships have legal
consequences for unauthorized control/theft, with no physical code protection.

The pure FleetRules prototype in Easter Pirates expresses acquisition/hostility
rules for later adapters. It is not yet wired to Minecraft events or ship factories.
