import random
import threading
import time

class RaftNode:
    def __init__(self, node_id, all_nodes):
        self.node_id = node_id
        self.all_nodes = all_nodes
        self.state = 'follower'
        self.current_term = 0
        self.voted_for = None
        self.leader = None
        self.reset_election_timeout()

    def reset_election_timeout(self):
        self.election_timeout = time.time() + random.uniform(1.5, 3.0)  # Random timeout between 1.5 and 3 seconds

    def convert_to_candidate(self):
        self.state = 'candidate'
        self.current_term += 1
        self.voted_for = self.node_id
        self.received_votes = 1  # Vote for self
        self.start_election()

    def start_election(self):
        print(f"Node {self.node_id} starting election for term {self.current_term}")
        for node in self.all_nodes:
            if node != self:
                node.request_vote(self)

    def request_vote(self, candidate):
        if (self.voted_for is None or self.voted_for == candidate.node_id) and candidate.current_term >= self.current_term:
            self.voted_for = candidate.node_id
            candidate.receive_vote()
            self.reset_election_timeout()

    def receive_vote(self):
        self.received_votes += 1
        if self.received_votes > len(self.all_nodes) // 2 and self.state == 'candidate':
            self.become_leader()

    def become_leader(self):
        print(f"Node {self.node_id} is now the leader for term {self.current_term}")
        self.state = 'leader'
        self.leader = self
        self.reset_election_timeout()  # Leaders use the timeout to send heartbeats

    def run(self):
        while True:
            if self.state == 'follower' and time.time() > self.election_timeout:
                self.convert_to_candidate()

# Example usage
nodes = [RaftNode(i, []) for i in range(5)]
for node in nodes:
    node.all_nodes = nodes

# Start nodes in separate threads (simplified for example purposes)
threads = [threading.Thread(target=node.run) for node in nodes]
for thread in threads:
    thread.start()
