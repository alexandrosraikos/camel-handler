#
# @file This file parses a CAMEL model.
# @author Alexandros Raikos <araikos@unipi.gr>
# @version 1.0.0
#

from os import supports_follow_symlinks
from typing import Dict

# Third party dependencies.
import xml.etree.ElementTree as ET


class CAMELModel:

    """
    The CAMEL Model in `.xmi` format represented as a Python object.
    """

    def __init__(
        self,
        xml_path: str,
        components_path: str = "deploymentModels/softwareComponents",
        component_name_key: str = "name",
        configuration_name_key: str = "name",
        configurations_tag: str = "configurations",
        download_attribute_key: str = "downloadURL",
        configuration_attribute_value_path: str = "subFeatures/attributes/value",
        attribute_value_name: str = "value",
        ):
        """
        Retrieve and parse the CAMEL model data using the given path.

        Parameters
        ----------
        - `path: str`
            A string containg the path to the XMI file.
        - `components_route: str`
            The XML path to the deployment components array.
        - `component_name_key: str`
            The XML key that refers to the component's name.
        - `configuration_name_key: str`
            The XML key that refers to the configuration's name.
        - `configurations_tag: str`
            The XML tag of the configurations array for each deployment component.
        - `download_attribute_key: str`
            The XML key that refers to the retrieval URL.
        - `configuration_attribute_value_path: str`
            The XML path to the attribute values of all deployment component configurations.
        - `configuration_attribute_value_path: str`
            The XML path to the attribute values of all deployment component configurations.
        - `attribute_value_name: str`
            The XML key that refers to the attribute's value.
        """
        self.file_path = xml_path
        self.tree = ET.parse(xml_path)
        self.data = self.tree.getroot()

        self.components_path = components_path
        self.component_name_key = component_name_key
        self.configuration_name_key = configuration_name_key
        self.configurations_tag = configurations_tag
        self.download_attribute_key = download_attribute_key
        self.configuration_attribute_value_path = configuration_attribute_value_path
        self.attribute_value_name = attribute_value_name


    def get_deployment_metadata(
        self
        ) -> dict:
        """
        Get the deployment model metadata in the form of a dictionary:
        ```python
        [
            component_name => [
                labels => [
                    confinguration_name: => [
                        attribute
                    ]
                ],
                downloads => [
                    configuration_name: url
                ]
            ]
        ]
        ```
        """
        components = self.data.findall(self.components_path)
        configurations = {}

        for component in components:

            # Initialize configuration dicts.
            downloads = {}
            labels = {}

            for configuration in component.findall(self.configurations_tag):                
                # Add download URL.
                downloads[configuration.get(self.component_name_key)] = configuration.get(self.download_attribute_key)
                attributes = []

                # Get all attributes
                for attribute in configuration.findall(self.configuration_attribute_value_path):
                    attributes.append(attribute.get(self.attribute_value_name))
                labels[configuration.get("name")] = attributes

            # Assign labels and downloads
            configurations[component.get(self.component_name_key)] = {}
            configurations[component.get(self.component_name_key)]['labels'] = labels
            configurations[component.get(self.component_name_key)]['downloads'] = downloads

        return configurations

    def set_deployment_metadata(
        self,
        component_name: str,
        configuration_name: str,
        attribute_name: str,
        attribute_type: str,
        attribute_value: str
        ) -> None:
        """
        Set the desired CAMEL configuration labels.

        Parameters
        ----------
        - `component_name: str`
            A string containg the path to the XMI file.
        - `configuration_name: str`
            The name of the configuration.
        - `attribute_name: str`
            The name of the added attribute.
        - `attribute_type: str`
            The type of the added attribute.
        - `attribute_value: str`
            The value of the added attribute.
        """
        for component in self.data.findall(self.components_path):
            if(component.get(self.component_name_key) == component_name):
                for configuration in component.findall(self.configurations_tag):
                    if(configuration.get(self.configuration_name_key) == configuration_name):
                        # Create the new attribute tag.
                        print("Adding!")
                        new_attribute = ET.Element("attribute")
                        new_attribute.set("name", attribute_name)

                        # Create the attribute's value tag.
                        new_value = ET.Element("value")
                        new_value.set("xsi:type", attribute_type)
                        new_value.set("value", attribute_value)

                        new_attribute.append(new_value)
                        configuration.append(new_attribute)

                        self.tree.write(self.file_path)
                        return
        
        raise IndexError("The configuration or component was not found.")

