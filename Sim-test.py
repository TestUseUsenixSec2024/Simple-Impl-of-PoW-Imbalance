import hashlib
import random
import string

total_hashrate = 10
diff = 5
data_rand = "".join(random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()123456789", 20))
time = 100

class Node:
    def __init__(self, name, hashrate_ratio):
        self.name = name
        self.flag = False
        self.nouce = random.randint(0, 10000000)
        self.hashrate_ratio = hashrate_ratio 
        self.hashrate = int(total_hashrate * hashrate_ratio)  
        self.blocks_mined = 0  

    def mine_block(self, difficulty):
        for _ in range(self.hashrate):
            self.nonce = self.nonce + random.randint(0, 10)
            data = data_rand + f"Block data with nonce {self.nonce}"
            hash_attempt = hashlib.sha256(data.encode()).hexdigest()
            if hash_attempt[:difficulty] == "0" * difficulty:
                self.blocks_mined += 1
                # print(f"{self.name} mined a block: {hash_attempt}")
                self.flag = True
                break

result = [0] * 4

for k in range(time):
    print(f"Round {k}")

    node = [Node] * 4
    for i in range(4):
        node[i] = Node("Node " + str(i + 1), 0.1 * (i + 1))

    for i in range(100):
        win_flag = False
        for n in node:
            n.nonce = random.randint(0, 1000000)
        data_rand = "".join(
            random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()123456789", 10)
        )
        while win_flag == False:
            for n in node:
                n.mine_block(diff)
                if n.flag == True:
                    n.flag = False
                    win_flag = True
                    break

    for i in range(4):
        result[i] = result[i] + node[i].blocks_mined

for i in range(4):
    print(f"{node[i].name} have {node[i].hashrate} and mined {(result[i]/time)} blocks")
