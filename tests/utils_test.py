import unittest
import sys
import os
from unittest.mock import MagicMock

sys.path.append(os.path.realpath("."))

import fawkes.utils.utils as utils


class UtilsTest(unittest.TestCase):

    def test_check_for_explicit_content(self):
    	tweet = "Here"
    	result = utils.check_for_explicit_content(tweet);
    	self.assertEqual(result,True)

    def test_check_tweet_authenticity(self):
    	tweet_message = "ABC"
    	twitter_handle_blacklist = "Some"
    	result = utils.check_tweet_authenticity(tweet_message,twitter_handle_blacklist);
    	self.assertEqual(result,True)


if __name__ == "__main__":
    unittest.main()
