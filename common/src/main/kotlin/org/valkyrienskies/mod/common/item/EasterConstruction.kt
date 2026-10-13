package org.valkyrienskies.mod.common.item

import net.minecraft.network.chat.Component
import net.minecraft.world.item.context.UseOnContext

/** Player progression is capture-only for physics ships. Existing hulls remain unprotected. */
internal object EasterConstruction {
    fun allowed(ctx: UseOnContext): Boolean {
        if (ctx.player?.hasPermissions(2) == true) return true
        ctx.player?.sendSystemMessage(Component.literal(
            "Large ships must be captured from NPC pirates. Build or buy a Shippy boat to board one."
        ))
        return false
    }
}
