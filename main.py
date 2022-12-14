# Veasna Ling
# COMP 257 Advance Algorithms

class Brute_Coin_Game:

    def __init__(self, coin_arr, n):
        self.coin_arr = coin_arr
        self.n = n
        self.dp_list = [[0] * n for _ in range(n)]

    def dp_function(self):
        # print(self.dp_list)
        for k in range(self.n):
            for i in range(self.n - k):
                j = i + k
                if i == j:
                    self.dp_list[i][j] = self.coin_arr[i]
                elif j - i == 1:
                    self.dp_list[i][j] = max(self.coin_arr[i], self.coin_arr[j])
                else:
                    choose_left = self.coin_arr[i] + min(self.dp_list[i + 2][j], self.dp_list[i + 1][j - 1])
                    choose_right = self.coin_arr[j] + min(self.dp_list[i + 1][j-1], self.dp_list[i][j - 2])
                    self.dp_list[i][j] = max(choose_left, choose_right)

        for cur_list in self.dp_list:
            print(cur_list)

    def choose_coin(self, i, j):
        self.dp_function()
        left_val = self.coin_arr[i] + min(self.dp_list[i + 1][j - 1], self.dp_list[i + 2][j])
        right_val = self.coin_arr[j] + min(self.dp_list[i + 1][j - 1], self.dp_list[i][j - 2])
        print(f"choose ? left_val: {left_val}, right_val: {right_val}")
        if left_val >= right_val:
            return 0
        else:
            return 1

    def brute_coin_game(self):
        print(self.coin_arr)

        # option for first pick from player 1
        print(f"current player 1 choice")
        list_solution = [{"lc": 1, "rc": n - 1, "val": self.coin_arr[0]},
                         {"lc": 0, "rc": n - 2, "val": self.coin_arr[n - 1]}]
        print(list_solution)

        for i in range(1, self.n):
            if i % 2 == 0:
                print(f"current player 1 turn")
            else:
                print(f"current player 2 turn")
            curr_sol = []
            for item_sol in list_solution:
                print(f"current item in solution {item_sol}")
                if i % 2 == 0:
                    left_sol = {"lc": item_sol["lc"] + 1,
                                "rc": item_sol["rc"],
                                "val": item_sol["val"] + self.coin_arr[item_sol["lc"]]}
                    curr_sol.append(left_sol)

                    right_sol = {"lc": item_sol["lc"],
                                 "rc": item_sol["rc"] - 1,
                                 "val": item_sol["val"] + self.coin_arr[item_sol["rc"]]}
                    curr_sol.append(right_sol)

                    print(curr_sol)
                else:
                    choose = self.choose_coin(item_sol["lc"], item_sol["rc"])
                    if choose == 0:
                        curr_sol = {"lc": item_sol["lc"] + 1,
                                    "rc": item_sol["rc"],
                                    "val": item_sol["val"]}
                    else:
                        curr_sol = {"lc": item_sol["lc"],
                                    "rc": item_sol["rc"] - 1,
                                    "val": item_sol["val"]}
                    print(curr_sol)

        return


class DP:
    def __init__(self):
        print("Start DP function")

    def dp_function(self, n, list):
        dp_list = [[0] * n for _ in range(n)]
        # print(dp_list)
        for gap in range(n):
            for i in range(n - gap):
                j = i + gap
                if i == j:
                    dp_list[i][j] = list[i]
                elif j - i == 1:
                    dp_list[i][j] = max(list[i], list[j])
                else:
                    choose_left = list[i] + min(dp_list[i + 2][j], dp_list[i + 1][j - 1])
                    choose_right = list[j] + min(dp_list[i + 1][j - 1], dp_list[i][j - 2])
                    dp_list[i][j] = max(choose_left, choose_right)

        for list in dp_list:
            print(list)


if __name__ == "__main__":
    # coinList = [1, 5, 10, 25, 1, 5, 10, 25]
    coinList = [20, 30, 2, 2, 2, 10]
    print(coinList)
    n = len(coinList)
    # brute = Brute_Coin_Game(coinList, n)
    # brute.brute_coin_game()

    dp = DP()
    dp.dp_function(n, coinList)
