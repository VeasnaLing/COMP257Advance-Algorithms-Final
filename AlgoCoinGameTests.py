import unittest
import AlgoCoinGame as CG
import time



class MyTestCase(unittest.TestCase):
    testcase1 = [1, 5, 10, 25]

    testcase2 = [1, 5, 10, 25, 5, 5, 10, 25, 1, 5, 10, 25]

    testcase3 = [1, 5, 10, 25, 10, 5, 10, 25, 1, 5, 10, 25, 10, 5, 10, 25, 5, 5, 10, 25, 1, 5, 10, 25]

    testcase4 = [10, 5, 10, 25, 10, 5, 10, 25, 10, 5, 10, 5, 1, 5, 10, 5, 1, 5, 10, 25, 1, 5, 10, 25,
                 1, 5, 10, 25]

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
        testcase5 = []
        for i in range(1001):
            if i % 2 == 2:
                testcase5.append(25)
            elif i % 3 == 1:
                testcase5.append(10)
            elif i % 2:
                testcase5.append(1)
            else:
                testcase5.append(5)

        n = len(testcase5)
        print(f"test_case 5 \nsize: {n}")
        start_time = time.time()
        greed1 = CG.GreedyCoinGame(testcase5, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 5 time: %s" % end_time)
        self.assertEqual(2012, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(testcase5, n)
        end_time = time.time() - start_time
        print("dp 5 time: %s" % end_time)
        self.assertEqual(2012, result3)
        print("\n===============================================")

    def test_case6(self):
        testcase6 = []
        for i in range(2001):
            if i % 2 == 2:
                testcase6.append(25)
            elif i % 3 == 1:
                testcase6.append(10)
            elif i % 2:
                testcase6.append(1)
            else:
                testcase6.append(5)

        n = len(testcase6)
        print(f"test_case 6 \nsize: {n}")
        start_time = time.time()
        greed1 = CG.GreedyCoinGame(testcase6, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 6 time: %s" % end_time)
        self.assertEqual(4006, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(testcase6, n)
        end_time = time.time() - start_time
        print("dp 6 time: %s" % end_time)
        self.assertEqual(4006, result3)
        print("\n===============================================")

    def test_case7(self):
        testcase7 = []
        for i in range(4001):
            if i % 2 == 2:
                testcase7.append(5)
            elif i % 3 == 1:
                testcase7.append(10)
            elif i % 2:
                testcase7.append(1)
            else:
                testcase7.append(25)

        n = len(testcase7)
        print(f"test_case 7 \nsize: {n}")
        start_time = time.time()
        greed1 = CG.GreedyCoinGame(testcase7, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 7 time: %s" % end_time)
        self.assertEqual(8028, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(testcase7, n)
        end_time = time.time() - start_time
        print("dp 7 time: %s" % end_time)
        self.assertEqual(8028, result3)
        print("\n===============================================")

    def test_case8(self):
        testcase8 = []
        for i in range(8001):
            if i % 2 == 2:
                testcase8.append(5)
            elif i % 3 == 1:
                testcase8.append(10)
            elif i % 2:
                testcase8.append(1)
            else:
                testcase8.append(25)
        # print(testcase8)
        n = len(testcase8)
        print(f"test_case 8 \nsize: {n}")
        start_time = time.time()
        greed1 = CG.GreedyCoinGame(testcase8, n)
        result2 = greed1.greed_function()
        end_time = time.time() - start_time
        print("greed 8 time: %s" % end_time)
        self.assertEqual(16031, result2)

        start_time = time.time()
        dp1 = CG.DPCoinGame()
        result3 = dp1.dp_function(testcase8, n)
        end_time = time.time() - start_time
        print("dp 8 time: %s" % end_time)
        self.assertEqual(16031, result3)
        print("\n===============================================")


if __name__ == '__main__':
    unittest.main()
