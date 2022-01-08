import time
import random

"""
    Submitted by Michael Smith  
    GIT: https://github.com/mdsmit5x/Siemens_Jan_7_2022/
"""
class Question1(object):
    """
    You have two arrays of integers.

a = [47,24,95,184,13,3,12,18]
b = [83,9,32,29,52,90,108,14]
Provide 2 or 3 different ways to calculate the pair of values (one value in each array) 
with the smallest non-negative difference.

Return the elements in the array and the smallest non-negative difference.

For example, the answer with array a & b above is b = 14 and a = 13 because their 
difference is 14-13 = 1, which is the smallest non-negative difference.

We are not looking for the most optimal code, but a variety of methods you could use 
calculate the smallest different and why you would select one method over another.
    """

    def __init__(self, array1, array2):
        self.array1 = array1
        self.array2 = array2
        self.array1_sorted = None

    def fails_edge_test(self):
        
        if (self.array1 is None or 
            self.array2 is None or
            len(self.array1) < 1 or
            len(self.array2) < 1    ):
            return True

        return False

    """
        Check every element in array1 against every element in array2
        The check does a subtraction and then takes the absolute value of that
        Return the smallest result of the check and the two numbers involved
        
        NOTE: There is some ambiguity as to what is meant by "smallest non-negative difference".
        It is assumed that this means the absolute value of the differences.
        Another interpretation is shown on line 65 and line 66 below

    """
    def runStupidBruteForce(self):
        if self.fails_edge_test():
            return None
        
        element1_result = self.array1[0]
        element2_result = self.array2[0]
        minimum = abs(self.array1[0] - self.array2[0])
        for element1 in self.array1:
            for element2 in self.array2:
                if element1 == element2:
                    return  [element1, element2, 0]
                # If we are certain about the array order 
                # and using the non-negative difference between array1 & array2, 
                # then the next two lines instead should be
                # test = element1 - element2
                # if test > 0 and test < minimum
                test = abs(element1 - element2)
                if test < minimum:
                    element1_result = element1
                    element2_result = element2
                    minimum = test

        return [element1_result, element2_result, minimum]

    
    """
        Sort array1 and array2
        In an element by element comparison in ascending order compare
        the element from one array with the element of the other array
        There are two indices which point to the location in the sorted arrays
        from which the comparisons are being made.
        Insure the that pointers point to roughly the same values in both arrays
        as closely as possible.
        Check the difference between the compared elements and remember
        the smallest difference.
        Return that smallest difference and the numbers that were used to
        find that difference.

        NOTE: There is some ambiguity as to what is meant by "smallest non-negative difference".
        It is assumed that this means the absolute value of the differences.
        Another interpretation is shown on line 119 and line 120 below
    """
    def runSortedDifference(self):
        if self.fails_edge_test():
            return None

        if self.array1_sorted is None:
            self.array1_sorted = sorted(self.array1)
            self.array2_sorted = sorted(self.array2)

        index1 = 0
        index2 = 0
        element1 = self.array1_sorted[index1]
        element2 = self.array2_sorted[index2]
        
        element1_result = element1
        element2_result = element2
        minimum = abs(element1 - element2)
        array1_length =  len(self.array1_sorted)    # for speed reasons only ask for the len() once
        array2_length =  len(self.array2_sorted)    # This assumes that the sorted array is not changing
        while (index1 < array1_length  and
               index2 < array2_length):
            if element1 == element2:
                return  [element1, element2, 0]

            # If we are certain about the array order 
            # and using the non-negative difference between array1 & array2, 
            # then the next two lines should instead be
            # test = element1 - element2
            # if test > 0 and test < minimum
            test = abs(element1 - element2)
            if test < minimum:
                element1_result = element1
                element2_result = element2
                minimum = test

            # find out why the gap is widening between two numbers
            if element1 > element2:
                index2 += 1
                if index2 >= array2_length:
                    break

                element2 = self.array2_sorted[index2]
            else:       # element2 > element1, since we know that they are not equal
                index1 += 1
                if index1 >= array1_length:
                    break
                element1 = self.array1_sorted[index1]

        return [element1_result, element2_result, minimum]

    def find_chance_of_zero_for_answer(self, upper_range):
        if self.fails_edge_test():
            return None

        total_compares = 0;
        array_size = len(self.array1)
        for i in range(1,array_size):
            total_compares += array_size - i
        single_chance = (upper_range - 1) / upper_range
        chance = pow(single_chance,total_compares)

        return 1 - chance

class Question2:
    """
    Create 2 lists of random integers between 1 and 1,000,000. 
    Each list should be 5,000 integers long.

    Apply the multiple methods you derived in Question 1 with the 2 new arrays of 
    integers you calculate in this question.

    Which algorithm performed best? Which algorithm performed worst? And why? 
    What is the Big0 notation for each of your methods?

    MUCH OF THIS CLASS IS FOR TRACKING THE TIMING OF Question1 FUNCTIONS
    """

    def __init__(self, array_size, upper_range):
        self.array_size = array_size
        self.upper_range = upper_range
        self.start_time = None
        self.array1 = []
        self.array2 = []

    def generate_arrays(self):
        for i in range(1,self.array_size):
            element1 = int(0.5 + random.random() * self.upper_range)
            element2 = int(0.5 + random.random() * self.upper_range)
            self.array1.append(element1)
            self.array2.append(element2)            

    def report_and_reset_time(self, message):
        if self.start_time is None:
            print("Starting Timer : ", message)
            self.start_time = time.time()
            return
        end_time = time.time()
        result = end_time - self.start_time
        print("Elapsed Time ", str(result), " : ", message)
        self.start_time = end_time
        return result

    def reset_time(self):        
            self.start_time = time.time()

    def doTest(self):
        start_time = time.time()
        message = "Question2 Start size=" + str(self.array_size) + ",  upper range=" + str(self.upper_range)
        self.report_and_reset_time(message)
        self.generate_arrays()        
        q1 = Question1(self.array1, self.array2)
        
        self.reset_time()
        chance = q1.find_chance_of_zero_for_answer(self.upper_range)
        self.report_and_reset_time("Question 1 find_chance_of_zero_for_answer")
        print('run_chance_of_zero_for_answer = ',str(100 * chance), ' % ')

        self.reset_time()

        print("Sorted Diff Answer = ",q1.runSortedDifference())
        self.report_and_reset_time("Question 1 Sorted Diff with sort")
        q1.runSortedDifference()
        self.report_and_reset_time("Question 1 Sorted Diff")

        
        print("Brute Force Answer = ",q1.runStupidBruteForce())
        result = self.report_and_reset_time("Question 1 Brute Force")
        return result

def sample_test():
    big = 1000000   * 1000000       # 1,000,000 times bigger than required
    as_specified = 1000000

    test_cases = [ [50,as_specified], [500,as_specified], [2500,as_specified],  [5000,as_specified],  [5000,as_specified], [5000,as_specified],
                   [50,big], [500,big], [2500,big],  [5000,big],  [5000,big], [5000,big]]

    for test_case in test_cases:
        q2 = Question2(test_case[0], test_case[1])
        q2.doTest()
        print("")
        print("---------------------------------------------")
        print("")

sample_test()