# 
# @file This source file is part of the CAMEL Handler python open source package.
# @author Alexandros Raikos <araikos@unipi.gr>
# @version 1.0.0
#

# TODO @alexandrosraikos: Write the validation unit test.

import unittest
import os

from camel_handler import CAMELModel

class ValidationTest(unittest.TestCase):

    def test_model_validation(self):
        """
        Test using the data directory.
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print("Initialising CAMEL model validation..")
        model = CAMELModel(dir_path + "/data/Genom.xmi")
        print("Getting deployment model metadata..")
        print(model.get_deployment_metadata())
        print("Setting deployment model metadata..")
        model.set_deployment_metadata(
            'ComponentSparkWorker',
            'configSpark',
            'memoryWidth',
            'type:StringValue',
            '256GB'
            )


if __name__ == "__main__":
    unittest.main()