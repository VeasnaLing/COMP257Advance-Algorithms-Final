# Veasna Ling
# COMP 257 Advance Algorithms

class BruteCoinGame:
    print("running brute function: ")

    def brute_coin_game(self, coin_list, i, j):
        if i == j:
            return coin_list[i]
        if i + 1 == j:
            return max(coin_list[i], coin_list[j])
        
        choose_left = coin_list[i] + min(self.brute_coin_game(coin_list, i + 2, j),
                                         self.brute_coin_game(coin_list, i + 1, j - 1))
        choose_right = coin_list[j] + min(self.brute_coin_game(coin_list, i + 1, j - 1),
                                          self.brute_coin_game(coin_list, i, j - 2))

        return max(choose_left, choose_right)


class GreedyCoinGame:
    def __init__(self, coin_arr, n):
        self.coin_arr = coin_arr
        self.n = n
        self.dp_list = [[0] * n for _ in range(n)]

    def create_dp_array(self):
        if self.n == 1:
            return self.dp_list[0]
        if self.n == 2:
            return max(self.dp_list[0], self.dp_list[1])

        for k in range(self.n):
            for i in range(self.n - k):
                j = i + k
                if i == j:
                    self.dp_list[i][j] = self.coin_arr[i]
                elif j - i == 1:
                    self.dp_list[i][j] = max(self.coin_arr[i], self.coin_arr[j])
                else:
                    choose_left = self.coin_arr[i] + min(self.dp_list[i + 2][j], self.dp_list[i + 1][j - 1])
                    choose_right = self.coin_arr[j] + min(self.dp_list[i + 1][j - 1], self.dp_list[i][j - 2])
                    self.dp_list[i][j] = max(choose_left, choose_right)

    def choose_coin(self, i, j):
        left_val = self.coin_arr[i] + min(self.dp_list[i + 1][j - 1], self.dp_list[i + 2][j])
        right_val = self.coin_arr[j] + min(self.dp_list[i + 1][j - 1], self.dp_list[i][j - 2])
        if left_val >= right_val:
            return 0
        else:
            return 1

    def greed_function(self):
        print("running greedy function: ")
        player_one_sum = 0
        left_coin = 0
        right_coin = self.n - 1
        self.create_dp_array()
        for i in range(self.n):
            if i % 2 == 0:
                if self.coin_arr[left_coin] > self.coin_arr[right_coin]:
                    player_one_sum += self.coin_arr[left_coin]
                    left_coin += 1
                else:
                    player_one_sum += self.coin_arr[right_coin]
                    right_coin -= 1
            else:
                choose = self.choose_coin(left_coin, right_coin)
                if choose == 0:
                    left_coin += 1
                else:
                    right_coin -= 1
        return player_one_sum


class DPCoinGame:
    def dp_function(self, coin_arr, n):
        print("running DP function:")
        dp_list = [[0] * n for _ in range(n)]
        if n == 1:
            return coin_arr[0]
        if n == 2:
            return max(coin_arr[0], coin_arr[1])

        for gap in range(n):
            for i in range(n - gap):
                j = i + gap
                if i == j:
                    dp_list[i][j] = coin_arr[i]
                elif j - i == 1:
                    dp_list[i][j] = max(coin_arr[i], coin_arr[j])
                else:
                    choose_left = coin_arr[i] + min(dp_list[i + 2][j], dp_list[i + 1][j - 1])
                    choose_right = coin_arr[j] + min(dp_list[i + 1][j - 1], dp_list[i][j - 2])
                    dp_list[i][j] = max(choose_left, choose_right)

        return dp_list[0][n - 1]


if __name__ == "__main__":
    coinList = [1, 5, 10, 25]
    print(coinList)
    n = len(coinList)

    brute = BruteCoinGame()
    print(f"max {brute.brute_coin_game(coinList, 0, n - 1)}")

    greedy = GreedyCoinGame(coinList, n)
    print(f"max {greedy.greed_function()}")

    dp = DPCoinGame()
    print(f"max {dp.dp_function(coinList, n)}")
