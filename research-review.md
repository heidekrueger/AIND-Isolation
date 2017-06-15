# Research Review

# Alpha Go Paper
## Summary
The authors start by describing two common methods used in algorithmic game playing whenever the search space is too large to be searched exhaustively. In particular, they briefly describe _position evaluation_ -- the method employed in the lectures of our class -- and stochastic breadth reduction using sampling algorithms, such as Monte Carlo rollouts. Highly oversimplified, these MC tree search methods randomly sample move vectors from the current position until end-game in order to gain information about the winning probability of the immideate legal moves. The authors note that while combinations of these methods have been applied to create Go-agents that achieve human amateur-level play, they have not been sufficient to reach expert-level play in the past.

Instead, they propose the use of deep convolutional neural networks, a method common in computer vision in order to reduce the search tree, by using two separate CNNs: a _value network_ for position evaluation and a _policy network_ for breadth reduction.

### Training the nets
 * $p_\sigma$: policy network trained from human expert moves (supervised)
 * $p_\rho$: policy network trained through self play via Reinforcement Learning, based on $p_\sigma$
 * $v_\theta$: value network that predicts winner of positions (labels: winners by self play)



# Link
https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf
