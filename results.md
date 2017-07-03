This script evaluates the performance of the custom_score evaluation
function against a baseline agent using alpha-beta search and iterative
deepening (ID) called `AB_Improved`. The three `AB_Custom` agents use
ID and alpha-beta search with the custom_score functions defined in
game_agent.py.

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random       9  |   1    10  |   0    10  |   0     9  |   1
    2       MM_Open      6  |   4     6  |   4     7  |   3     8  |   2
    3      MM_Center     7  |   3     8  |   2     7  |   3     6  |   4
    4     MM_Improved    5  |   5     3  |   7     4  |   6     6  |   4
    5       AB_Open      5  |   5     6  |   4     4  |   6     6  |   4
    6      AB_Center     6  |   4     5  |   5     7  |   3     5  |   5
    7     AB_Improved    5  |   5     6  |   4     3  |   7     3  |   7
--------------------------------------------------------------------------
           Win Rate:      61.4%        62.9%        60.0%        61.4%



### As is:



                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random       9  |   1     7  |   3    10  |   0     8  |   2
    2       MM_Open      8  |   2     8  |   2     7  |   3     4  |   6
    3      MM_Center     8  |   2     9  |   1     6  |   4     9  |   1
    4     MM_Improved    5  |   5     5  |   5     3  |   7     4  |   6
    5       AB_Open      6  |   4     6  |   4     5  |   5     9  |   1
    6      AB_Center     4  |   6     7  |   3     4  |   6     3  |   7
    7     AB_Improved    8  |   2     5  |   5     4  |   6     3  |   7
--------------------------------------------------------------------------
           Win Rate:      68.6%        67.1%        55.7%        57.1%


D:\dev\AInanodegree\AIND-Isolation (master)
(aind) λ python tournament.py

This script evaluates the performance of the custom_score evaluation
function against a baseline agent using alpha-beta search and iterative
deepening (ID) called `AB_Improved`. The three `AB_Custom` agents use
ID and alpha-beta search with the custom_score functions defined in
game_agent.py.

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random    Traceback (most recent call last):
  File "tournament.py", line 159, in <module>
    main()
  File "tournament.py", line 155, in main
    play_matches(cpu_agents, test_agents, NUM_MATCHES)
  File "tournament.py", line 102, in play_matches
    counts = play_round(agent, test_agents, wins, num_matches)
  File "tournament.py", line 63, in play_round
    winner, _, termination = game.play(time_limit=TIME_LIMIT)
  File "D:\dev\AInanodegree\AIND-Isolation\isolation\isolation.py", line 326, in play
    curr_move = self._active_player.get_move(game_copy, time_left)
  File "D:\dev\AInanodegree\AIND-Isolation\game_agent.py", line 356, in get_move
    best_move = self.alphabeta(game, depth)
  File "D:\dev\AInanodegree\AIND-Isolation\game_agent.py", line 537, in alphabeta
    current_val = self.minval(game.forecast_move(move), depth - 1, alpha, beta)
  File "D:\dev\AInanodegree\AIND-Isolation\game_agent.py", line 446, in minval
    return self.score(game, self)
  File "D:\dev\AInanodegree\AIND-Isolation\game_agent.py", line 120, in custom_score_3
    blockable_moves = player_moves & opp_moves
TypeError: unsupported operand type(s) for &: 'list' and 'list'

D:\dev\AInanodegree\AIND-Isolation (master)
(aind) λ python tournament.py

This script evaluates the performance of the custom_score evaluation
function against a baseline agent using alpha-beta search and iterative
deepening (ID) called `AB_Improved`. The three `AB_Custom` agents use
ID and alpha-beta search with the custom_score functions defined in
game_agent.py.

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random       9  |   1     8  |   2    10  |   0    10  |   0
    2       MM_Open      6  |   4     7  |   3     6  |   4     7  |   3
    3      MM_Center     6  |   4     6  |   4     8  |   2     8  |   2
    4     MM_Improved    5  |   5     6  |   4     2  |   8     4  |   6
    5       AB_Open      5  |   5     3  |   7     6  |   4     3  |   7
    6      AB_Center     4  |   6     5  |   5     5  |   5     5  |   5
    7     AB_Improved    5  |   5     5  |   5     5  |   5     3  |   7
--------------------------------------------------------------------------
           Win Rate:      57.1%        57.1%        60.0%        57.1%


D:\dev\AInanodegree\AIND-Isolation (master)
(aind) λ python tournament.py

This script evaluates the performance of the custom_score evaluation
function against a baseline agent using alpha-beta search and iterative
deepening (ID) called `AB_Improved`. The three `AB_Custom` agents use
ID and alpha-beta search with the custom_score functions defined in
game_agent.py.

                        *************************
                             Playing Matches
                        *************************

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random       8  |   2     9  |   1    10  |   0     9  |   1
    2       MM_Open      5  |   5     7  |   3     6  |   4     6  |   4
    3      MM_Center     7  |   3     9  |   1     8  |   2     8  |   2
    4     MM_Improved    5  |   5     6  |   4     6  |   4     5  |   5
    5       AB_Open      6  |   4     6  |   4     5  |   5     5  |   5
    6      AB_Center     6  |   4     6  |   4     2  |   8     5  |   5
    7     AB_Improved    6  |   4     5  |   5     5  |   5     7  |   3
--------------------------------------------------------------------------
           Win Rate:      61.4%        68.6%        60.0%        64.3%


Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random       9  |   1     7  |   3     8  |   2     9  |   1
    2       MM_Open      4  |   6     5  |   5     4  |   6     7  |   3
    3      MM_Center     8  |   2     6  |   4     7  |   3     8  |   2
    4     MM_Improved    5  |   5     6  |   4     6  |   4     5  |   5
    5       AB_Open      5  |   5     5  |   5     4  |   6     6  |   4
    6      AB_Center     5  |   5     5  |   5     4  |   6     6  |   4
    7     AB_Improved    4  |   6     6  |   4     5  |   5     5  |   5
--------------------------------------------------------------------------
           Win Rate:      57.1%        57.1%        54.3%        65.7%

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random      10  |   0    10  |   0     9  |   1     9  |   1
    2       MM_Open      7  |   3     7  |   3     5  |   5     5  |   5
    3      MM_Center     6  |   4     5  |   5     9  |   1     7  |   3
    4     MM_Improved    4  |   6     8  |   2     5  |   5     5  |   5
    5       AB_Open      6  |   4     7  |   3     6  |   4     5  |   5
    6      AB_Center     4  |   6     6  |   4     5  |   5     3  |   7
    7     AB_Improved    6  |   4     4  |   6     7  |   3     5  |   5
--------------------------------------------------------------------------
           Win Rate:      61.4%        67.1%        65.7%        55.7%

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random      10  |   0     8  |   2     9  |   1     8  |   2
    2       MM_Open      9  |   1     6  |   4     9  |   1     5  |   5
    3      MM_Center     7  |   3     9  |   1     8  |   2     8  |   2
    4     MM_Improved    6  |   4     5  |   5     7  |   3     6  |   4
    5       AB_Open      4  |   6     7  |   3     6  |   4     4  |   6
    6      AB_Center     7  |   3     5  |   5     7  |   3     5  |   5
    7     AB_Improved    4  |   6     7  |   3     5  |   5     4  |   6
--------------------------------------------------------------------------
           Win Rate:      67.1%        67.1%        72.9%        57.1%

 Match #   Opponent    AB_Improved   AB_Custom   AB_Custom_2  AB_Custom_3
                        Won | Lost   Won | Lost   Won | Lost   Won | Lost
    1       Random      10  |   0     9  |   1    10  |   0     6  |   4
    2       MM_Open      7  |   3     8  |   2     5  |   5     8  |   2
    3      MM_Center     7  |   3     7  |   3     8  |   2    10  |   0
    4     MM_Improved    5  |   5     3  |   7     3  |   7     4  |   6
    5       AB_Open      5  |   5     7  |   3     4  |   6     4  |   6
    6      AB_Center     5  |   5     5  |   5     5  |   5     5  |   5
    7     AB_Improved    4  |   6     6  |   4     3  |   7     5  |   5
--------------------------------------------------------------------------
           Win Rate:      61.4%        64.3%        54.3%        60.0%