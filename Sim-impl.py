import hashlib
import random
import string

total_hashrate = 100
diff = 6
data_rand = "".join(random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()123456789", 20))
time = 2
num = 1


class Node:
    def __init__(self, name, hashrate_ratio):
        self.name = name
        self.flag = False
        self.nouce = random.randint(0, 100000000000)
        self.hashrate_ratio = hashrate_ratio
        self.hashrate = int(total_hashrate * hashrate_ratio)
        self.blocks_mined = 0

    def mine_block(self, difficulty):
        for _ in range(self.hashrate):
            self.nonce = self.nonce + random.randint(0, 25)
            # self.nonce = self.nonce + 1
            # self.nonce = random.randint(0, 100000000000000000000000)
            data = data_rand + f"Block data with nonce {self.nonce}"
            hash_attempt = hashlib.sha256(data.encode()).hexdigest()
            if hash_attempt[:difficulty] == "0" * difficulty:
                self.blocks_mined += 1
                print(f"{self.name} mined a block: {hash_attempt}")
                self.flag = True
                break


result = [0] * num
res_time = 0

for k in range(time):
    print(f"Round {k}")

    node = [Node] * num
    for i in range(num):
        node[i] = Node("Node " + str(i + 1), 1)

    for i in range(100):
        print(f"Turn {i}")
        win_flag = False
        for n in node:
            n.nonce = random.randint(0, 1000000)
        data_rand = "".join(
            random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()123456789", 10)
        )
        while win_flag == False:
            for n in node:
                n.mine_block(diff)
                res_time = res_time + n.hashrate
                if n.flag == True:
                    n.flag = False
                    win_flag = True
                    break

    for i in range(num):
        result[i] = result[i] + node[i].blocks_mined

for i in range(num):
    print(f"{node[i].name} have {node[i].hashrate} and mined {(result[i]/time)} blocks")
print(f"time cost avg {(res_time/time)} round/sec")
