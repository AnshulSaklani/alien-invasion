class GameStats():
    """Track statistics for alien invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start alien invasion in an active state
        # self.game_active = True

        # Start game in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

        # When a player loses, his score will start from
        # where it was in the beginning of level
        self.scr = 0

    def high(self):
        """ To retain the high score after game is closed"""
        self.high_scr = 0
       
