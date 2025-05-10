
# Proof of work
Computes hash of the message that starts a certain way (hard to guess).
Provides that as a proof of work.

Does not prevent the lie, but makes it very hard to keep up with the lies. Recompute history. 

# Merkle tree
Used to verify transactions in the block.
Block contains the merkle root in the header.

O(logn) 

# Commit reveal scheme
To come up with a group random number everyone commits to a random number, makes a proof that they have commited, then they reveal.
Verifiers can detect if they were honest.

Dropping of **last revealer** is still a problem. (If for example they see that the random that will be chosen is not in their favour)
