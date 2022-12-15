import unittest
import AlgoCoinGame as CG
import time


class MyTestCase(unittest.TestCase):
    testcase1 = [1, 5, 10, 25]

    testcase2 = [1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25]

    testcase3 = [1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25]

    testcase4 = [1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 1, 5, 10, 25]

    testcase5 = [1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 1, 5, 10, 25, 1]

    def test_case1(self):
        n = len(self.testcase1)
        print(f"test_case 1 \nsize: {n}")
        start_time = time.time()
        brute1 = CG.BruteCoinGame()
        result1 = brute1.brute_coin_game(self.testcase1, 0, n - 1)
        end_time = time.time() - start_time
        print("brute 1 time: %s" % end_time)
        self.assertEqual(30, result1)

        start_time = time.time()
        greed1 = CG.GreedyCoinGame(self.testcase1, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 1 time: %s" % end_time)
        self.assertEqual(30, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(self.testcase1, n)
        end_time = time.time() - start_time
        print("dp 1 time: %s" % end_time)
        self.assertEqual(30, result3)

    def test_case2(self):
        n = len(self.testcase2)
        print(f"test_case 2 \nsize: {n}")
        start_time = time.time()
        brute1 = CG.BruteCoinGame()
        result1 = brute1.brute_coin_game(self.testcase2, 0, n - 1)
        end_time = time.time() - start_time
        print("brute 2 time: %s" % end_time)
        self.assertEqual(90, result1)

        start_time = time.time()
        greed1 = CG.GreedyCoinGame(self.testcase2, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 2 time: %s" % end_time)
        self.assertEqual(90, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(self.testcase2, n)
        end_time = time.time() - start_time
        print("dp 2 time: %s" % end_time)
        self.assertEqual(90, result3)

    def test_case3(self):
        n = len(self.testcase3)
        print(f"test_case 3 \nsize: {n}")
        start_time = time.time()
        brute1 = CG.BruteCoinGame()
        result1 = brute1.brute_coin_game(self.testcase3, 0, n - 1)
        end_time = time.time() - start_time
        print("brute 3 time: %s" % end_time)
        self.assertEqual(180, result1)

        start_time = time.time()
        greed1 = CG.GreedyCoinGame(self.testcase3, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 3 time: %s" % end_time)
        self.assertEqual(180, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(self.testcase3, n)
        end_time = time.time() - start_time
        print("dp 3 time: %s" % end_time)
        self.assertEqual(180, result3)

    def test_case4(self):
        n = len(self.testcase4)
        print(f"test_case 4 \nsize: {n}")
        start_time = time.time()
        brute1 = CG.BruteCoinGame()
        result1 = brute1.brute_coin_game(self.testcase4, 0, n - 1)
        end_time = time.time() - start_time
        print("brute 4 time: %s" % end_time)
        self.assertEqual(210, result1)

        start_time = time.time()
        greed1 = CG.GreedyCoinGame(self.testcase4, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 4 time: %s" % end_time)
        self.assertEqual(210, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(self.testcase4, n)
        end_time = time.time() - start_time
        print("dp 4 time: %s" % end_time)
        self.assertEqual(210, result3)

    def test_case5(self):
        n = len(self.testcase5)
        print(f"test_case 5 \nsize: {n}")
        start_time = time.time()
        brute1 = CG.BruteCoinGame()
        result1 = brute1.brute_coin_game(self.testcase5, 0, n - 1)
        end_time = time.time() - start_time
        print("brute 5 time: %s" % end_time)
        self.assertEqual(78, result1)

        start_time = time.time()
        greed1 = CG.GreedyCoinGame(self.testcase5, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 5 time: %s" % end_time)
        self.assertEqual(78, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(self.testcase5, n)
        end_time = time.time() - start_time
        print("dp 5 time: %s" % end_time)
        self.assertEqual(78, result3)


if __name__ == '__main__':
    unittest.main()
