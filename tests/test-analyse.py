# 
# @file This source file is part of the CAMEL Handler python open source package.
# @author Alexandros Raikos <araikos@unipi.gr>
# @version 1.0.0
#

# TODO @alexandrosraikos: Write the validation unit test.

import unittest
import os

class ValidationTest(unittest.TestCase):
    dir_path = os.path.dirname(os.path.realpath(__file__))

    def test_model_validation(self):
        """
        Test using the data directory.
        """
        print("Initialising CAMEL model validation..")


if __name__ == "__main__":
    unittest.main()