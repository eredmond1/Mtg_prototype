
from player import Player 
from GameStateManagers.TurnState.combat_manager import CombatManager
from GameStateManagers.game_manager import GameManager


def main():
    # Create players
    player1 = Player("Alice")
    player2 = Player("Bob")
    
    GameManager(player1, player2)
    
    # # Give players creatures
    # player1.add_creature(Creature("Red Dragon", [0,0,0,0,0], 5, 5,["flying"]))
    # player1.add_creature(Creature("Goblin Warrior", [0,0,0,0,0], 2, 1, ["flying"]))
    # player1.add_creature(Creature("Lightning Elemental", [0,0,0,0,0], 4, 1,[]))
    
    # player2.add_creature(Creature("White Knight", [0,0,0,0,0], 2, 3,[]))
    # player2.add_creature(Creature("Wall of Stone", [0,0,0,0,0], 0, 7, []))
    # player2.add_creature(Creature("Guardian Angel", [0,0,0,0,0], 3, 4, ["flying"]))
    
    # # Remove summoning sickness for demo
    # player1.untap_all_creatures()
    # player2.untap_all_creatures()
    
    # print(f"=== MAGIC: THE GATHERING GAME ===")
    # print(f"{player1}")
    # print(f"{player2}")
    
    # turn_count = 1
    # current_attacker = player1
    # current_defender = player2
    
    # # Game loop
    # while player1.life > 0 and player2.life > 0:
    #     print(f"\n{'='*50}")
    #     print(f"TURN {turn_count} - {current_attacker.name}'s Attack Phase")
    #     print(f"{'='*50}")
        
    #     # Create combat manager and run combat
    #     combat = CombatManager(current_attacker, current_defender)
    #     combat.run_combat()
        
    #     # Check for game over
    #     if player1.life <= 0:
    #         print(f"\n🎉 {player2.name} WINS! {player1.name} is defeated!")
    #         break
    #     elif player2.life <= 0:
    #         print(f"\n🎉 {player1.name} WINS! {player2.name} is defeated!")
    #         break
        
    #     # End of turn - untap creatures and heal damage
    #     print(f"\n--- End of {current_attacker.name}'s Turn ---")
    #     current_attacker.untap_all_creatures()
    #     current_defender.untap_all_creatures()
        
    #     # Heal all damage at end of turn
    #     for creature in current_attacker.creatures + current_defender.creatures:
    #         if hasattr(creature, 'heal_all_damage'):
    #             creature.heal_all_damage()
        
    #     print(f"Game State: {player1} | {player2}")
        
    #     # Switch turns
    #     current_attacker, current_defender = current_defender, current_attacker
    #     turn_count += 1
        
    #     # Ask if players want to continue or quit
    #     try:
    #         continue_game = input("\nPress Enter to continue to next turn, or 'q' to quit: ").strip().lower()
    #         if continue_game == 'q':
    #             print("Game ended by player choice.")
    #             break
    #     except KeyboardInterrupt:
    #         print("\nGame ended.")
    #         break
    
    # print(f"\n=== FINAL GAME STATE ===")
    # print(f"{player1}")
    # print(f"{player2}")
    # print("Thanks for playing Magic: The Gathering!")

if __name__ == "__main__":
    main()