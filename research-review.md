# Research Review

# Alpha Go Paper
## Summary
The authors start by describing two common methods used in algorithmic game playing whenever the search space is too large to be searched exhaustively. In particular, they briefly describe _position evaluation_ -- the method employed in the lectures of our class -- and stochastic breadth reduction using sampling algorithms, such as Monte Carlo rollouts. Highly oversimplified, these MC tree search methods randomly sample move vectors from the current position until end-game in order to gain information about the winning probability of the immideate legal moves. The authors note that while combinations of these methods have been applied to create Go-agents that achieve human amateur-level play, they have not been sufficient to reach expert-level play in the past.

Instead, they propose the use of deep convolutional neural networks, a method common in computer vision in order to reduce the search tree, by using two separate CNNs: a _value network_ for position evaluation and a _policy network_ for breadth reduction.

## Alpha Go Agent
 1.  $p_\sigma$: policy network trained from human expert moves (supervised)
 2.  $p_\rho$: policy network trained through self play via Reinforcement Learning, based on $p_\sigma$
 3. $v_\theta$: value network that predicts winner of positions (labels: winners by self play)
 4. AlphaGo Agent uses MCTS using $p_\rho$ for policies and $v_\theta$ for pos. evaluation.

## Expert Policy Network
* alternating conv and rectifier nonlinearities + final softmax --> prob distr over all legal moves $a$: $p(a|s)$ where $s$ is board state.
* trained on history of human expert games
* final architecture: 13 layers
* $57\%$ pred. accuracy (vs $44.4\%$) previous state of the ar

## RL Policy Network
* same structure as $p_\sigma$
* initialize weights from SL network
* then train using RL (play against random previous iteration)

## RL Value Network
* approximate the games value $v^*$ under perfect play
* train on RL-Policy games
* can't train on KGS/real games due to overfitting (too few games)

# Link
https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf
