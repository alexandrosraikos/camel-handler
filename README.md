# CAMEL Handler

A Python module which handles CAMEL modeling configuration recommendations. This module concerns accessing and manipulating a .camel here in its parsed XMI format. Find out more information about CAMEL [here](http://camel-dsl.org).

### Important information

**If you haven't been specifically instructed to use this module, then you most likely do not need it.**

This module has been developed in accordance to the requirements of the [MORPHEMIC](https://www.mophemic.cloud/) research project funded by the European Union's Horizon 2020 Research and Innovation program under grant agreement No. 871643.

## Getting started

It is advised to use this library on VS Code, or on any code editor that works with Python code documentation.

Follow the steps below to get started with `camel_handler`.

### Installation

This package can be installed easily via `pip`. Run the commands below:

```bash
# Clone or download the .zip from the Releases tab.
git clone https://www.github.com/alexandrosraikos/camel-handler

# Navigate to the folder.
cd camel-handler

# Install locally
pip install .
```

### Getting and setting deployment metadata

```python
# To get deployment model metadata.
model = CAMELModel(dir_path + "/data/Genom.xmi")
print(model.get_deployment_metadata())

# To set deployment model metadata.
model.set_deployment_metadata(
    'ComponentSparkWorker',
    'configSpark',
    'memoryWidth',
    'type:StringValue',
    '256GB'
)
```

## Unit testing

Please consult the [Unit Testing README](tests/Readme.md) in the `tests` folder.
