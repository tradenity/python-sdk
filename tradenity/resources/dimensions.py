# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class Dimensions(object):


    swagger_types = { 
        'width': 'float',
        'height': 'float',
        'depth': 'float',
        'unit': 'str'
    }

    attribute_map = { 
        'width': 'width',
        'height': 'height',
        'depth': 'depth',
        'unit': 'unit'
    }

    def __init__(self, width=None, height=None, depth=None, unit=None):  # noqa: E501
        """Dimensions - a model defined in Swagger"""  # noqa: E501
        

        self._width = None
        self._height = None
        self._depth = None
        self._unit = None
        self.discriminator = None

        self.width = width
        self.height = height
        self.depth = depth
        self.unit = unit


    @property
    def width(self):
        """Gets the width of this Dimensions.  # noqa: E501


        :return: The width of this Dimensions.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this Dimensions.


        :param width: The width of this Dimensions.
        :type: float
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this Dimensions.  # noqa: E501


        :return: The height of this Dimensions.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this Dimensions.


        :param height: The height of this Dimensions.
        :type: float
        """

        self._height = height

    @property
    def depth(self):
        """Gets the depth of this Dimensions.  # noqa: E501


        :return: The depth of this Dimensions.  # noqa: E501
        :rtype: float
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this Dimensions.


        :param depth: The depth of this Dimensions.
        :type: float
        """

        self._depth = depth

    @property
    def unit(self):
        """Gets the unit of this Dimensions.  # noqa: E501


        :return: The unit of this Dimensions.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Dimensions.


        :param unit: The unit of this Dimensions.
        :type: str
        """
        allowed_values = ["cm", "inch", "foot"]  # noqa: E501
        if unit is not None and unit not in allowed_values:
            raise ValueError(
                "Invalid value for `unit` ({0}), must be one of {1}"  # noqa: E501
                .format(unit, allowed_values)
            )

        self._unit = unit


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
        if issubclass(Dimensions, dict):
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
        if not isinstance(other, Dimensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
