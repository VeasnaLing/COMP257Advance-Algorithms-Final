# Veasna Ling
# COMP 257 Advance Algorithms

# class Brute_Coin_Game:
#
#     def __init__(self, coin_arr, n):
#         self.coin_arr = coin_arr
#         self.n = n
#         self.CDP = []
#
#
#     def DP(self, i, j):
#         if i > j or i >= n or j < 0:
#             return 0
#         k = (i, j)
#         if k in self.CDP:
#             return self.CDP[k]
#
#         opt1 = self.coin_arr[i] + min(self.DP(i + 2, j), self.DP(i + 1, j - 1))
#         opt2 = self.coin_arr[j] + min(self.DP(i + 1, j - 1), self.DP(i, j - 2))
#
#         self.CDP[k] = max(opt1, opt2)
#         return self.CDP[k]
#
#     def choose_coin(self, i, j):
#         left_val = self.coin_arr[i] + min(self.DP(i + 1, j - 1), self.DP(i + 2, j))
#         right_val = self.coin_arr[j] + min(self.DP(i + 1, j - 1), self.DP(i, j - 2))
#
#
#     def brute_coin_game(self):
#         print(self.coin_arr)
#         list_solution = [{"lc": 1, "rc": n - 1, "val": self.coin_arr[0]},
#                          {"lc": 0, "rc": n - 2, "val": self.coin_arr[n - 1]}]
#
#         for i in range(0, n):
#             print(i)
#             temp_sol = []
#             for item in list_solution:
#                 # print(item)
#                 if n % 2 == 0:
#                     left_sol = {"lc": item["lc"] + 1, "rc": item["rc"], "val": item["val"] + self.coin_arr[item["lc"]]}
#                     temp_sol.append(left_sol)
#
#                     right_sol = {"lc": item["lc"], "rc": item["rc"] - 1, "val": item["val"] + self.coin_arr[item["rc"]]}
#                     temp_sol.append(right_sol)
#                 else:
#                     choose = self.choose_coin(item["lc"], item["rc"])

class DP:
    def __init__(self):
        print("Start DP function")

    def dp_function(self, n, list):
        dp_list = [[0]*n]*n
        print(dp_list)
        for gap in range(n):
            for i in range(n-gap):
                j = i + gap
                if i == j:
                    dp_list[i][j] = list[i]
                elif j - i == 1:
                    dp_list[i][j] = max(list[i], list[j])
                else:
                    choose_left = list[i] + min(dp_list[i + 2][j], dp_list[i + 1][j - 1])
                    choose_right = list[i] + min(dp_list[i + 1][j], dp_list[i][j - 2])
                    dp_list[i][j] = max(choose_left, choose_right)
        print(dp_list)

if __name__ == "__main__":
    coinList = [.01, .05, .10, .25]
    print(coinList)
    n = len(coinList)
    # brute = Brute_Coin_Game(coinList, n)
    # brute.brute_coin_game()

    dp = DP()
    dp.dp_function(n, coinList)
