# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class MeasurementSettings(object):


    swagger_types = { 
        'weight_unit': 'str',
        'dimensions_unit': 'str'
    }

    attribute_map = { 
        'weight_unit': 'weightUnit',
        'dimensions_unit': 'dimensionsUnit'
    }

    def __init__(self, weight_unit=None, dimensions_unit=None):  # noqa: E501
        """MeasurementSettings - a model defined in Swagger"""  # noqa: E501
        

        self._weight_unit = None
        self._dimensions_unit = None
        self.discriminator = None

        self.weight_unit = weight_unit
        self.dimensions_unit = dimensions_unit


    @property
    def weight_unit(self):
        """Gets the weight_unit of this MeasurementSettings.  # noqa: E501


        :return: The weight_unit of this MeasurementSettings.  # noqa: E501
        :rtype: str
        """
        return self._weight_unit

    @weight_unit.setter
    def weight_unit(self, weight_unit):
        """Sets the weight_unit of this MeasurementSettings.


        :param weight_unit: The weight_unit of this MeasurementSettings.
        :type: str
        """
        allowed_values = ["pound", "kilogram"]  # noqa: E501
        if weight_unit is not None and weight_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `weight_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(weight_unit, allowed_values)
            )

        self._weight_unit = weight_unit

    @property
    def dimensions_unit(self):
        """Gets the dimensions_unit of this MeasurementSettings.  # noqa: E501


        :return: The dimensions_unit of this MeasurementSettings.  # noqa: E501
        :rtype: str
        """
        return self._dimensions_unit

    @dimensions_unit.setter
    def dimensions_unit(self, dimensions_unit):
        """Sets the dimensions_unit of this MeasurementSettings.


        :param dimensions_unit: The dimensions_unit of this MeasurementSettings.
        :type: str
        """
        allowed_values = ["inch", "cm", "foot", "meter"]  # noqa: E501
        if dimensions_unit is not None and dimensions_unit not in allowed_values:
            raise ValueError(
                "Invalid value for `dimensions_unit` ({0}), must be one of {1}"  # noqa: E501
                .format(dimensions_unit, allowed_values)
            )

        self._dimensions_unit = dimensions_unit


    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MeasurementSettings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MeasurementSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
