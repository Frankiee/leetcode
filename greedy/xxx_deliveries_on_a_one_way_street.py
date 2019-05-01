# https://github.com/postmates/interview/blob/master/backend/onsite/section_a/one_way_street.md  # noqa
# Deliveries on a One Way Street

# Suppose you have a walking courier standing on a one way street,
# whose home is further down the street. Along the way there are deliveries
# scheduled on the street as pickups and dropoffs. The courier wants to do
# as many deliveries as possible on their way home, but they can only do one
# delivery at a time since they can only carry one package at a time. Write
# an algorithm to find the maximum number of deliveries they can do.
#
# def get_max_deliveries(start, end, deliveries):
#       # start, end are positions on a number line as integers, ie start =
#       2, end = 80
#       # deliveries is an array of pickups and dropoffs as positions on a
#       number line ex [ [ 4, 20 ], [ 7, 21 ] ... ]
# Expected time to solve (~30 min) This ends up being a class of problem
# called Interval Scheduling (
# https://en.wikipedia.org/wiki/Interval_scheduling) Also see
# https://en.wikipedia.org/wiki/Activity_selection_problem
#
# Greedy algorithm of taking closest endpoints and eliminating conflicts


import unittest


class Delivery(object):
    def __init__(self, start, end, value=1):
        super(Delivery, self).__init__()
        self.start = start
        self.end = end

    def __repr__(self):
        return 'd({},{})'.format(self.start, self.end)


def get_max_deliveries_optimal(start, end, deliveries):
    # start, end are positions on a number line as integers,
    # ie start = 2, end = 80
    # deliveries is an array of Delivery Objects
    # Returns an array of chosen deliveries in order
    sorted_delivs = sorted(deliveries, key=lambda x: x.end)
    choices = []
    current_start = start
    for deliv in sorted_delivs:
        if deliv.start < current_start:
            continue
        if deliv.end > end:
            break
        choices.append(deliv)
        current_start = deliv.end

    return choices


# TESTS
class TestDelivery(unittest.TestCase):
    @staticmethod
    def get_max_deliveries(*args):
        return get_max_deliveries_optimal(*args)

    @staticmethod
    def conflicts(delivery, other_delivery):
        return (
            other_delivery.start < delivery.start < other_delivery.end or
            other_delivery.start < delivery.end < other_delivery.end or
            (
                delivery.start < other_delivery.start and
                delivery.end > other_delivery.end
            )
        )

    def assert_no_conflicts(self, deliveries):
        for i, delivery in enumerate(deliveries):
            for j, other_delivery in enumerate(deliveries):
                if i != j:
                    self.assertFalse(self.conflicts(delivery, other_delivery))

    def assert_none_before_or_after(self, deliveries, start, end):
        for delivery in deliveries:
            self.assertTrue(delivery.start > start and delivery.end < end)

    def test_3_simple(self):
        d1 = Delivery(1, 3)
        d2 = Delivery(2, 4)
        d3 = Delivery(3, 6)

        TEST_CASE = [d1, d2, d3]
        start = 0
        end = 10
        results = self.get_max_deliveries(start, end, TEST_CASE)
        expected_results = [d1, d3]
        self.assertEqual(len(results), len(expected_results))
        self.assert_no_conflicts(results)
        self.assert_none_before_or_after(results, start, end)

    def test_3_out_of_order(self):
        d1 = Delivery(1, 3)
        d2 = Delivery(2, 4)
        d3 = Delivery(3, 6)

        TEST_CASE = [d1, d3, d2]
        start = 0
        end = 10
        results = self.get_max_deliveries(start, end, TEST_CASE)
        expected_results = [d1, d3]
        self.assertEqual(len(results), len(expected_results))
        self.assert_no_conflicts(results)
        self.assert_none_before_or_after(results, start, end)

    def test_job_before_start(self):
        d1 = Delivery(1, 4)
        d2 = Delivery(3, 5)
        d3 = Delivery(4, 6)
        d4 = Delivery(5, 9)

        TEST_CASE = [d1, d3, d2, d4]
        start = 2
        end = 10
        results = self.get_max_deliveries(start, end, TEST_CASE)
        expected_results = [d2, d4]
        self.assertEqual(len(results), len(expected_results))
        self.assert_no_conflicts(results)
        self.assert_none_before_or_after(results, start, end)

    def test_job_after_end(self):
        d1 = Delivery(1, 4)
        d2 = Delivery(3, 5)
        d3 = Delivery(4, 6)
        d4 = Delivery(8, 9)

        TEST_CASE = [d1, d3, d2, d4]
        start = 0
        end = 10
        results = self.get_max_deliveries(start, end, TEST_CASE)
        expected_results = [d1, d3, d4]
        self.assertEqual(len(results), len(expected_results))
        self.assert_no_conflicts(results)
        self.assert_none_before_or_after(results, start, end)

        results = self.get_max_deliveries(0, 8, TEST_CASE)
        expected_results = [d1, d3]
        self.assertEqual(len(results), len(expected_results))
        self.assert_no_conflicts(results)
        self.assert_none_before_or_after(results, start, end)

    def test_big_job_little_jobs(self):
        d1 = Delivery(1, 9)
        d2 = Delivery(3, 5)
        d3 = Delivery(6, 8)
        d4 = Delivery(8, 9)

        TEST_CASE = [d1, d3, d2, d4]
        start = 0
        end = 10
        results = self.get_max_deliveries(start, end, TEST_CASE)
        expected_results = [d2, d3, d4]
        self.assertEqual(len(results), len(expected_results))
        self.assert_no_conflicts(results)
        self.assert_none_before_or_after(results, start, end)
