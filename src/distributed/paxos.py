class PaxosNode:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.proposal_id = None
        self.accepted_id = None
        self.accepted_value = None
        self.promised_id = None

    def prepare(self, proposal_id):
        self.proposal_id = proposal_id
        num_okay = 0
        for peer in self.peers:
            if peer.promise(self.proposal_id):
                num_okay += 1
        if num_okay > len(self.peers) // 2:
            self.send_accept_requests()

    def promise(self, proposal_id):
        if self.promised_id is None or proposal_id > self.promised_id:
            self.promised_id = proposal_id
            return True
        return False

    def send_accept_requests(self):
        num_accepted = 0
        for peer in self.peers:
            if peer.accept(self.proposal_id, self.accepted_value):
                num_accepted += 1
        if num_accepted > len(self.peers) // 2:
            self.consensus_reached()

    def accept(self, proposal_id, value):
        if proposal_id >= self.promised_id:
            self.accepted_id = proposal_id
            self.accepted_value = value if value is not None else self.accepted_value
            return True
        return False

    def consensus_reached(self):
        print(f"Node {self.node_id} reached consensus with value {self.accepted_value}")

# Example usage
nodes = [PaxosNode(i, []) for i in range(5)]
for node in nodes:
    node.peers = [n for n in nodes if n != node]

# Initiating the Paxos algorithm
proposer = nodes[0]
proposer.prepare(proposal_id=1)
