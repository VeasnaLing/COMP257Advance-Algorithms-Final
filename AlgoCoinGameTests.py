import unittest
import AlgoCoinGame as CG
import time


class MyTestCase(unittest.TestCase):
    testcase1 = [1, 5, 10, 25]

    testcase2 = [1, 5, 10, 25, 5, 5, 10, 25, 1, 5, 10, 25]

    testcase3 = [1, 5, 10, 25, 10, 5, 10, 25, 1, 5, 10, 25, 10, 5, 10, 25, 5, 5, 10, 25, 1, 5, 10, 25]

    testcase4 = [10, 5, 10, 25, 10, 5, 10, 25, 10, 5, 10, 5, 1, 5, 10, 5, 1, 5, 10, 25, 1, 5, 10, 25,
                 1, 5, 10, 25]

    testcase5 = [1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 1, 5, 10, 25, 1]

    testcase6 = [1, 5, 10, 25, 1, 5, 1, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 5, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 1, 25, 1, 5, 10, 1,
                 25, 5, 10, 5, 1, 5, 10, 25, 25, 1, 5, 10, 1, 25, 1, 5, 10, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 5, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 25, 25, 1, 5, 10, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 5]

    testcase7 = [1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 1,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 5,
                 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 25, 1, 5, 10, 5,
                 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 5,
                 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 1,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 5,
                 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 25, 1, 5, 10, 5,
                 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 5,
                 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 1,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 5,
                 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 25, 1, 5, 10, 5,
                 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 10, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 1,
                 25, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25,
                 5, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 6,
                 25, 5, 10, 25, 1, 5, 10, 10, 5, 1, 5, 25, 1, 5, 10, 25, 1, 5, 10, 25, 1, 5, 10, 5]

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
        print("\n===============================================")

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
        print("\n===============================================")

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
        print("\n===============================================")

    def test_case4(self):
        n = len(self.testcase4)
        print(f"test_case 4 \nsize: {n}")
        start_time = time.time()
        brute1 = CG.BruteCoinGame()
        result1 = brute1.brute_coin_game(self.testcase4, 0, n - 1)
        end_time = time.time() - start_time
        print("brute 4 time: %s" % end_time)
        self.assertEqual(175, result1)

        start_time = time.time()
        greed1 = CG.GreedyCoinGame(self.testcase4, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 4 time: %s" % end_time)
        self.assertEqual(155, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(self.testcase4, n)
        end_time = time.time() - start_time
        print("dp 4 time: %s" % end_time)
        self.assertEqual(175, result3)
        print("\n===============================================")

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
        print("\n===============================================")

    def test_case6(self):
        n = len(self.testcase6)
        print(f"test_case 6 \nsize: {n}")
        start_time = time.time()
        greed1 = CG.GreedyCoinGame(self.testcase6, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 6 time: %s" % end_time)
        self.assertEqual(733, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(self.testcase6, n)
        end_time = time.time() - start_time
        print("dp 6 time: %s" % end_time)
        self.assertEqual(895, result3)
        print("\n===============================================")

    def test_case7(self):
        n = len(self.testcase7)
        print(f"test_case 7 \nsize: {n}")
        start_time = time.time()
        greed1 = CG.GreedyCoinGame(self.testcase7, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 7 time: %s" % end_time)
        self.assertEqual(6060, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(self.testcase7, n)
        end_time = time.time() - start_time
        print("dp 7 time: %s" % end_time)
        self.assertEqual(8709, result3)
        print("\n===============================================")


if __name__ == '__main__':
    unittest.main()
