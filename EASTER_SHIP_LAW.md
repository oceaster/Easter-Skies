# Named ships: ownership and law

Owen's requirements, 2026-10-13:
- Large ships can be named.
- Ships are never protected by code. Boarding, piloting, theft and damage remain
  possible; the law assigns consequences instead of rejecting those actions.
- Ship ownership and relationships should resemble the existing home mechanics.
- Owners and family can pilot at any time.
- Guests can pilot crime-free only while the owner is online.
- Other piloting of a named ship is a crime and immediate piracy.
- Taking items from a named ship's chest is a crime for a non-family member.

## Permissions versus consequences

| Completed action on a registered named ship | Owner | Family | Guest, owner online | Guest, owner offline | Stranger |
|---|---|---|---|---|---|
| Pilot | lawful | lawful | lawful | crime + immediate piracy | crime + immediate piracy |
| Take from ship storage | lawful | lawful | theft | theft | theft |
| Boarding/opening a chest without taking anything | no named-ship crime implied | same | same | same | same |

No row blocks the physical action. Unrelated existing combat/crime rules still
apply. The rules above do not invent a price for theft or a rule for hull damage.

## Same owner roster, separate property behavior

The existing Easter Navy HouseAccess roster is keyed by the owner's canonical
in-game name and shared across their homes. Its roles are OWNER, FAMILY, GUEST
and STRANGER, with exclusive family/guest membership. Removing family demotes
them to guest. Ships must consult that same owner's roster, not a copied ship
list and not the real-world Easter Family context used by AI agents.

Family cannot edit the owner's relationship lists. A ship-only owner will need
the same owner-facing roster management even without owning a house.
Home rules remain unchanged: their code protection is not copied onto ships.
Only ship ownership and law share the roster.

## Required server-side evidence

- Stable engine ship ID and persistent owner identity independent of display name.
- Owner-controlled name, bounded text and normalized public rendering. Do not use
  a player's client-supplied name or a name collision as proof of ownership.
- Online means present in the Minecraft server player list, not Discord, DSH,
  the web app, a cached login flag or physical proximity.
- Re-evaluate a guest's current piloting relationship while control continues:
  owner disconnect, invitation removal and ownership transfer change the result.
  A successful boarding check cannot grant permanent legal piloting.
- Pilot means the active steering/helm controller, not every passenger. Motion
  from inertia after someone stops controlling the helm is not fresh piloting.
- Confirm an actual positive transfer from the ship's storage. Opening a chest,
  viewing contents, failed/full-inventory moves and putting items in are not theft.
  Cover shift-click, drag/swap, double chest, cargo menus and relevant automation.
- Resolve the source container to a stable ship ID even when the ship moves,
  unloads or uses shipyard coordinates. Do not guess from a nearby hull's name.
- Crime deduplication keys include actor, stable ship and action/control episode;
  tick checks must not generate endless fines for one continuous piloting act.
- Immediate piracy must use the existing crime/faction/bounty pathway. Setting
  a cosmetic tag while leaving Navy privileges active is not implementation.
- Theft pricing, repair/damage laws, unnamed-vessel law and automation attribution
  are not yet specified. Do not silently copy unrelated house denial behavior.

The ShipLaw prototype in Easter Pirates compiles and exercises this truth table.
It is not wired to live containers, controllers, registration or criminal state.
Naming, theft detection and immediate piracy still need runtime integration.
