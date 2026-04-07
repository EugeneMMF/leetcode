class Solution:
    def rankTeams(self, votes: list[str]) -> str:
        num_positions = len(votes[0])
        
        team_stats = {}
        
        for team_char in votes[0]:
            team_stats[team_char] = [0] * num_positions
            
        for vote_str in votes:
            for position, team_char in enumerate(vote_str):
                team_stats[team_char][position] += 1
                
        teams = list(team_stats.keys())
        
        teams.sort(key=lambda team: tuple([-count for count in team_stats[team]] + [team]))
        
        return "".join(teams)
