class CombatManager:
    def __init__(self, attacking_player, defending_player):
        self.attacking_player = attacking_player
        self.defending_player = defending_player
        self.attackers = []
        self.combat_assignments = {}  # {attacker: blocker}
    
    def declare_attackers(self):
        """Let attacking player choose attackers"""
        available_attackers = self.attacking_player.get_available_attackers()
        
        if not available_attackers:
            print(f"{self.attacking_player.name} has no creatures that can attack!")
            return
        
        print(f"\n=== {self.attacking_player.name}'s Attack Phase ===")
        print("Available attackers:")
        
        for i, creature in enumerate(available_attackers):
            print(f"{i + 1}. {creature}")
        
        print("0. Done selecting attackers")
        
        while True:
            try:
                choice = int(input("Select attacker (number): "))
                if choice == 0:
                    break
                elif 1 <= choice <= len(available_attackers):
                    creature = available_attackers[choice - 1]
                    if creature not in self.attackers:
                        creature.tap()
                        self.attackers.append(creature)
                        print(f"{creature.name} declares attack!")
                    else:
                        print("Creature already attacking")
                else:
                    print("Invalid choice")
            except ValueError:
                print("Please enter a number")
    
    def declare_blockers(self):
        """Let defending player choose blockers"""
        if not self.attackers:
            print("No attackers to block!")
            return
            
        available_blockers = self.defending_player.get_available_blockers()
        
        print(f"\n=== {self.defending_player.name}'s Block Phase ===")
        
        while True:
            # Show current state
            print(f"\n=== ATTACKING CREATURES ===")
            for i, attacker in enumerate(self.attackers):
                blocked_status = "BLOCKED" if attacker in self.combat_assignments else "UNBLOCKED"
                print(f"{i + 1}. {attacker} - {blocked_status}")
            
            print(f"\n=== {self.defending_player.name}'s DEFENDING CREATURES ===")
            current_blockers = [b for b in available_blockers if b.can_block() and b not in self.combat_assignments.values()]
            
            if not current_blockers:
                print("No creatures available to block")
                break
                
            for i, blocker in enumerate(current_blockers):
                print(f"{i + 1}. {blocker}")
            
            print("\nOptions:")
            print("0. Take remaining damage (stop blocking)")
            print("1. Block an attacker")
            
            try:
                choice = int(input("Choose option (0 or 1): "))
                
                if choice == 0:
                    print(f"{self.defending_player.name} chooses to take remaining damage!")
                    break
                elif choice == 1:
                    # Select blocker
                    blocker_choice = int(input(f"Select your blocker (1-{len(current_blockers)}): "))
                    if 1 <= blocker_choice <= len(current_blockers):
                        selected_blocker = current_blockers[blocker_choice - 1]
                        
                        # Show unblocked attackers
                        unblocked_attackers = [a for a in self.attackers if a not in self.combat_assignments]
                        if not unblocked_attackers:
                            print("All attackers are already blocked!")
                            continue
                            
                        print("\nSelect which attacker to block:")
                        for i, attacker in enumerate(unblocked_attackers):
                            print(f"{i + 1}. {attacker}")
                        
                        attacker_choice = int(input(f"Select attacker to block (1-{len(unblocked_attackers)}): "))
                        if 1 <= attacker_choice <= len(unblocked_attackers):
                            selected_attacker = unblocked_attackers[attacker_choice - 1]
                            
                            # Assign the block
                            self.combat_assignments[selected_attacker] = selected_blocker
                            print(f"\n{selected_blocker.name} blocks {selected_attacker.name}!")
                        else:
                            print("Invalid attacker choice!")
                    else:
                        print("Invalid blocker choice!")
                else:
                    print("Invalid option!")
                    
            except ValueError:
                print("Please enter a number!")
    
    def resolve_combat(self):
        """Resolve combat damage"""
        print(f"\n=== RESOLVING COMBAT DAMAGE ===")
        player_damage = 0
        creatures_to_remove = []
        
        for attacker in self.attackers:
            if attacker in self.combat_assignments:
                # Blocked combat
                blocker = self.combat_assignments[attacker]
                print(f"\n{attacker.name} vs {blocker.name}:")
                
                # Both deal damage simultaneously using get_power()
                attacker_dies = attacker.take_damage(blocker.get_power())
                blocker_dies = blocker.take_damage(attacker.get_power())
                
                if attacker_dies:
                    print(f"  {attacker.name} is destroyed!")
                    creatures_to_remove.append((self.attacking_player, attacker))
                if blocker_dies:
                    print(f"  {blocker.name} is destroyed!")
                    creatures_to_remove.append((self.defending_player, blocker))
            else:
                # Unblocked damage to player using get_power()
                player_damage += attacker.get_power()
        
        # Remove destroyed creatures
        for player, creature in creatures_to_remove:
            player.remove_creature(creature)
        
        # Deal damage to defending player
        if player_damage > 0:
            print(f"\n{self.defending_player.name} takes {player_damage} total damage from unblocked creatures!")
            self.defending_player.take_damage(player_damage)
