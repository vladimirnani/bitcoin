from hashlib import sha256


class Node:
    hash: bytes
    parent = None
    sibling = None
    is_left: bool
    def __init__(self, h):
        self.hash = h

class ProofPair:
    hash: bytes
    is_prepend: bool

class MerkleProof:
    auth_path: list[ProofPair]

    def __init__(self, auth_path):
        self.auth_path = auth_path


text_array = ['tex1', 'text2', 'text3']
node_map: dict[str, Node] = {}

def create_tree(data_array):
    # if not mod 2 add last one
    if len(data_array) % 2 != 0:
        last = data_array[-1]
        data_array.append(last)
    nodes = []

    for t in data_array:
        h = sha256(t.encode('utf-8'))
        n = Node(h.digest())
        nodes.append(n)
        node_map[t] = n

    h = len(nodes) // 2

    while h != 0:
        new_nodes = []
        for i in range (0, h):
            a = nodes[i*2]
            b = nodes[i*2+1]
            hash_sum = a.hash + b.hash
            p = Node(sha256(hash_sum).digest())
            a.parent = p
            a.is_left = True
            b.parent = p
            a.sibling = b
            b.sibling = a
            b.is_left = False
            new_nodes.append(p)
        nodes = new_nodes
        h = len(nodes)//2

    root = nodes[0]
    return root

tree = create_tree(text_array)
trusted_top_hash = tree.hash


def create_merkle_proof(data):
    assert data in node_map

    auth_path = []
    n = node_map[data]

    while n.parent:
        proof_pair = ProofPair()
        proof_pair.is_prepend = n.sibling.is_left
        proof_pair.hash = n.sibling.hash
        auth_path.append(proof_pair)
        n = n.parent

    return MerkleProof(auth_path)

proof = create_merkle_proof(text_array[0])


# trusted source
# 1. creates the full tree
# 2. sends the top hash

# untrusted source
# 1. has the tree
# 2. creates the proof
# 3. sends a chunk (can be malicious) sends a proof as well

# verifier
# receives a chunk and a proof ( not the whole tree )
# wants to verify it
# computes hashes until the root (using the untrusted proof)
# compares the top hash with the computed one

def verify(data_block:str, untrusted_proof: MerkleProof, trusted_root_hash):
    this_h = sha256(data_block.encode('utf-8')).digest()
    # should also check for proof auth path length

    for s in untrusted_proof.auth_path:
        if s.is_prepend:
            this_h = sha256(s.hash + this_h).digest()
        else:
            this_h = sha256(this_h + s.hash).digest()

    root_hash_computed = this_h

    if root_hash_computed != trusted_root_hash:
        print('Merkle proof is invalid')
    else:
        print('Valid!')



verify('tex1', proof, trusted_top_hash)
