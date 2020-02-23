import random


def OnePointSpin(self):
		if bool(random.getrandbits(1)):
			return 1
		else:
			return -1

def TwoPointSpin(self):
		if bool(random.getrandbits(1)):
			return 2
		else:
			return -2


def SimpleStrategy(self):
	return OnePointSpin(self)

def BetHighWhenBelowZeroStrategy(self, currentCount):
	if(currentCount > 0):
		return OnePointSpin(self)
	else:
		return TwoPointSpin(self)

def BetHighWhenBelowNumber(self, currentCount, threshold):
	if(currentCount > threshold):
		return OnePointSpin(self)
	else:
		return TwoPointSpin(self)


class TestRunner:
	currentCount = 0
	testCount = 0
	threshold = 0
	currentStrategy = SimpleStrategy

	results = []

	def __init__(self, testsToRun, strategyToUse):
		self.testCount = testsToRun
		self.results = [None] * testsToRun

	def __init__(self, testsToRun, strategyToUse, thresholdToUse):
		self.testCount = testsToRun
		self.results = [None] * testsToRun
		self.threshold = thresholdToUse

	def RunTests(self):
		for i in range(0,self.testCount):
			result = self.currentStrategy()
			self.results[i] = result
			self.currentCount = self.currentCount + result

		return self.currentCount

	def ReportResults(self):

		print("total: " + str(self.currentCount))

	def ReturnTheResults(self):
		testStrategyAndResults = TestStrategyAndResults(self.currentStrategy, self.threshold)
		testStrategyAndResults.SetResults(self.results, self.currentCount)
		return testStrategyAndResults


class TestStrategyAndResults:
	strategy = SimpleStrategy
	threshold = 0
	results = []
	finalCount = []
	success = False

	def __init__(self, strategy, threshold):
		self.strategy = strategy
		self.threshold = threshold

	def SetResults(self, results, finalCount):
		self.results = results
		self.finalCount = finalCount
		self.success = self.finalCount > 0


   
class MultiTestRunner:
	timeToTestEachStrategy = 0
	StrategiesToTest = []
	allResults = []

	def __init__(self, amountOfIterations, strategiesToTest):
		self.StrategiesToTest = strategiesToTest
		self.timeToTestEachStrategy = amountOfIterations

	def RunTheTests(self):
		allResults = [None] * len(self.StrategiesToTest)
		for x in range(0, len(self.StrategiesToTest)):
			results = [None] * self.timeToTestEachStrategy
			for i in range(0, self.timeToTestEachStrategy):
				
				tester = TestRunner(100, self.StrategiesToTest[x], self.StrategiesToTest[x].threshold)
				tester.RunTests()
				results[i] = tester.ReturnTheResults()
			allResults[x] = results



	def PercentageThatPassed(self):

		
		print('len of allResults: ' + str(len(self.allResults)))
		for i in range(0, len(self.allResults)):
			print('made it')
			amountOfSuccesses = 0
			for j in range(0, len(self.allResults[i])):
				if self.strategiesToTest[i][j].finalCount > 0:
					amountOfSuccess = amountOfSuccesses+1
			print('for strategy ' + str(self.StrategiesToTest[i]) + ' percentage: ' + str(amountOfSuccesses/timeToTestEachStrategy))

		#print('successPercentage: ' + str(amountOfSuccesses/len(strategiesToTest)))





testToRun = [TestStrategyAndResults(BetHighWhenBelowNumber, 10), TestStrategyAndResults(BetHighWhenBelowNumber, 20)]
masterTester = MultiTestRunner(100, testToRun)
masterTester.RunTheTests()
masterTester.PercentageThatPassed()