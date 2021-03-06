"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


infinity = float('inf')


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_winner(player):
        return float("inf")

    if game.is_loser(player):
        return float("-inf")

    player_moves = float(len(game.get_legal_moves(player)))
    opp_moves = float(len(game.get_legal_moves(game.get_opponent(player))))

    return 2*player_moves * player_moves - opp_moves**1.5


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    if game.is_winner(player):
        return float("inf")

    if game.is_loser(player):
        return float("-inf")

    # For now: negative number of opposing moves
    player_moves = float(len(game.get_legal_moves(player)))
    opp_moves = float(len(game.get_legal_moves(game.get_opponent(player))))

    return player_moves**1.5 - 2 * opp_moves

def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    # TODO: finish this function!  

    if game.is_winner(player):
        return float("inf")

    if game.is_loser(player):
        return float("-inf")

    player_moves = game.get_legal_moves(player)
    opp_moves =game.get_legal_moves(game.get_opponent(player))
    blockable_moves = set(player_moves) & set(opp_moves)

    if len(player_moves) == 1 and len(blockable_moves) == 1:
        # opponent can block only move --> bad, but not -infty
        return -100

    return 2.0 * len(player_moves) - 1.0 * len(opp_moves)


class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minval(self, game, depth):
        """ Returns the value of minimal utility of possible moves """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:  # terminal node
            return self.score(game, self)

        legal_moves = game.get_legal_moves()
        if not legal_moves:  # opposing player can't move
            return infinity

        return min([self.maxval(game.forecast_move(move), depth - 1)
                    for move in legal_moves])

    def maxval(self, game, depth):
        """ Returns the value of the maximal utility of possible moves """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return self.score(game, self)

        legal_moves = game.get_legal_moves()
        if not legal_moves:  # player can't move
            return -infinity

        return max([self.minval(game.forecast_move(move), depth - 1)
                    for move in legal_moves]
                  )

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth < 1:
            raise ValueError("Depth must be at least 1")

        legal_moves = game.get_legal_moves()

        if not legal_moves:
            return (-1, -1)

        vals = []

        for move in legal_moves:
            vals.append(self.minval(game.forecast_move(move), depth-1))

        #print(vals)
        #print(legal_moves[vals.index(max(vals))])
        return legal_moves[vals.index(max(vals))]


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        if not game.get_legal_moves():
            return (-1, -1)

        # Opening Move if applicable
        if game.move_count == 0:
            # take center of the board (or something close if even-sized field)
            return (game.width // 2, game.height // 2)

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        depth = 1
        while True: #always true condition will be broken by timeout eventually
            try:
                # The try/except block will automatically catch the exception
                # raised when the timer is about to expire.
                best_move = self.alphabeta(game, depth)
                depth = depth + 1

            except SearchTimeout:
                break  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def maxval(self, game, depth, alpha, beta):
        """ Returns the value of the maximal utility of possible moves or
            a lower bound on it if it can be inferred that this value will
            be higher than the limit

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float # TODO: remove later?
            Beta limits the upper bound of search on maximizing layers

        """

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return self.score(game, self)

        legal_moves = game.get_legal_moves()
        if not legal_moves:  # player can't move
            return -infinity

        current_max = -infinity

        for move in legal_moves:
            # get val of current move and update current_max
            current_max = max(
                current_max,
                self.minval(
                    game.forecast_move(move),
                    depth - 1,
                    alpha=alpha,
                    beta=beta
                )
            )

            if current_max >= beta:
                # prune remaining moves: this branch will be eliminated anyway
                return current_max

            alpha = max(alpha, current_max)

        return current_max

    def minval(self, game, depth, alpha, beta):
        """ Returns the value of the maximal utility of possible moves or
            a lower bound on it if it can be inferred that this value will
            be higher than the limit

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float # TODO: remove later?
            Beta limits the upper bound of search on maximizing layers

        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth == 0:
            return self.score(game, self)

        legal_moves = game.get_legal_moves()
        if not legal_moves:  # player can't move
            return infinity

        current_min = infinity

        for move in legal_moves:
            # get val of current move and update current_max
            current_min = min(
                current_min,
                self.maxval(
                    game.forecast_move(move),
                    depth - 1,
                    alpha=alpha,
                    beta=beta
                )
            )

            if current_min <= alpha:
                # prune remaining moves: this branch will be eliminated anyway
                return current_min

            beta = min(beta, current_min)

        return current_min

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        if depth < 1:
            raise ValueError("Depth must be at least 1")

        best_val = float("-inf")
        best_move = (-1, -1)

        legal_moves = game.get_legal_moves()

        if not legal_moves:
            return (-1, -1)

        #vals = []
        current_val = best_val
        for move in legal_moves:
            # get value of current move and adjust alpha for next search (horizontally)
            current_val = self.minval(game.forecast_move(move), depth - 1, alpha, beta)
            alpha = max(alpha, current_val)

            if current_val > best_val: # new best move found:
                best_val = current_val
                best_move = move

            if current_val >= beta: 
                # hopeless: will be pruned in parent node, no need to eval more moves
                return best_move


        #return legal_moves[vals.index(max(vals))]
        return best_move