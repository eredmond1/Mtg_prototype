
class MainPhase:
    
    def execute(self, player):
        valid_action = False
        mp_action = input("play a card: 1 \nend main phase: 2\n ")
        while valid_action == False:
            
            if mp_action == "1":
                valid_action = True
                self.play_card(player)
            elif mp_action =="2":
                valid_action = True
            else:
                print("Please select a valid option\n")
                
                
    def play_card(self, player):
        player.print_hand()
        card_choice = int(input("select the card that you want to play: "))
        if ( card_choice <= player.get_hand_count()):
            valid_action = player.play_card(card_choice)
            if valid_action: return 
            
        else:
            print("you can't play this card")
            return
                
            
        
        