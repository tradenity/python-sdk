# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class Weight(object):


    swagger_types = { 
        'amount': 'float',
        'unit': 'str'
    }

    attribute_map = { 
        'amount': 'amount',
        'unit': 'unit'
    }

    def __init__(self, amount=None, unit=None):  # noqa: E501
        """Weight - a model defined in Swagger"""  # noqa: E501
        

        self._amount = None
        self._unit = None
        self.discriminator = None

        self.amount = amount
        self.unit = unit


    @property
    def amount(self):
        """Gets the amount of this Weight.  # noqa: E501


        :return: The amount of this Weight.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Weight.


        :param amount: The amount of this Weight.
        :type: float
        """

        self._amount = amount

    @property
    def unit(self):
        """Gets the unit of this Weight.  # noqa: E501


        :return: The unit of this Weight.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Weight.


        :param unit: The unit of this Weight.
        :type: str
        """
        allowed_values = ["ounce", "pound", "gm", "kg"]  # noqa: E501
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
        if issubclass(Weight, dict):
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
        if not isinstance(other, Weight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
