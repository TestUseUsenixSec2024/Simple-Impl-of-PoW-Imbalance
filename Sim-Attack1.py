import hashlib
import random
import string

total_hashrate = 1000
diff = 5
data_rand = "".join(random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()123456789", 20))
time = 20
atk = 0.2
Num = 3
Rio = (1 - atk) / (Num)
att_win = 0
h = 0


class Node:
    def __init__(self, name, hashrate_ratio, block):
        self.name = name
        self.flag = False
        self.nonce = random.randint(0, 10000000)
        self.block = block
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

    def reset(self, block):
        self.nouce = random.randint(0, 10000000)
        self.block = block
        self.flag = False


result = [0] * Num
result_e = 0

for k in range(time):
    print(f"Round {k}")

    node = [Node] * Num
    for i in range(Num):
        node[i] = Node("Node " + str(i + 1), Rio, data_rand)
    node_m = Node("Node evil", atk, data_rand)
    win_flag = False
    h = 0

    while h < 100:

        if win_flag == True:
            print("hround" + str(h))
            win_flag = False
            for n in node:
                data_rand = "".join(
                    random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()123456789", 10)
                )
                n.reset
        node_m.mine_block(diff)
        if node_m.flag == True:
            node_m.flag = False
            print("eround" + str(node_m.blocks_mined))
            data_rand = "".join(
                random.sample("abcdefghijklmnopqrstuvwxyz!@#$%^&*()123456789", 10)
            )
            node_m.reset
            if h < node_m.blocks_mined:
                print("evil win")
                h = 1000
                att_win = att_win + 1
                break
        for n in node:
            n.mine_block(diff)
            if n.flag == True:
                n.flag = False
                win_flag = True
                h = h + 1
                if h > node_m.blocks_mined + 40:
                    print("honest win")
                    h = 1000
                break

    result_e = result_e + node_m.blocks_mined
    for i in range(Num):
        result[i] = result[i] + node[i].blocks_mined


for i in range(Num):
    print(f"{node[i].name} have {node[i].hashrate} and mined {(result[i]/time)} blocks")
print(f"{node_m.name} have {node_m.hashrate} and mined {(result_e/time)} blocks")
print(f"evil win {att_win} times")
