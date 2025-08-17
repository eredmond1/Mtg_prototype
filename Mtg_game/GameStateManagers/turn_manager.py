from TurnState.untap_step import UntapStep
from TurnState.draw_step import DrawStep
from TurnState.combat_manager import CombatManager
from TurnState.main_phase import MainPhase
from TurnState.end_step import EndStep




class TurnManager:
    def execute(self, player):
        untap_step = UntapStep(player)
        draw_step = DrawStep(player)
        combat_manager = CombatManager(player)
        main_phase = MainPhase(player)
        end_steep = EndStep(player)
        
        untap_step.execute(player)
        draw_step.execute(player)
        main_phase.execute(player)
        
        while valid_choice == False:
            combat_choice = input("select 1 to attact and 0 to mvoe on: ")
            valid_choice = False
            
            if combat_choice == "1":
                valid_choice = True
                combat_manager.ec
        
        
        
        
         
        
        