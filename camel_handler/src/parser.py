#
# @file This file parses a CAMEL model.
# @author Alexandros Raikos <araikos@unipi.gr>
# @version 1.0.0
#

# Third party dependencies.
import xmi


class CAMELModel:
    """
    The CAMEL Model in `.xmi` format represented as a Python object.
    """

    def __init__(self, path: str):
        """
        Retrieve and parse the CAMEL model data using the given path.

        Parameters
        ----------
        - `path: str`
            A string containg the path to the XMI file.
        """
        # TODO @alexandrosraikos: Retrieve the CAMEL Model from the CDO.
        self.data = xmi.open_file(path)

    def save() -> None:
        # TODO @alexandrosraikos: Save the loaded CAMEL Model to the CDO.
        return

    def get_configurations() -> dict:
        """
        Get the existing CAMEL model configuration.
        """
        # TODO @alexandrosraikos: Extract `git` paths and existing `labels`. 
        # TODO @alexandrosraikos: Append to dictionary as `repositories` and `labels` and return.
        return dict()

    def set_configurations(labels: list) -> None:
        """
        Set the desired CAMEL configuration labels.

        Parameters
        ----------
        - `labels: list`
            A list containing configuration labels to append to the model.
        """
        # TODO @alexandrosraikos: Append the labels to the CAMEL Model.
        # TODO @alexandrosraikos: Save the CAMEL Model to the CDO.
        # 1. Add labels to the model.
        # 2. Save the model.
        return