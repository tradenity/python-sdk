# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class TaxSettings(object):


    swagger_types = { 
        'price_include_tax': 'bool',
        'tax_class_based_on': 'str'
    }

    attribute_map = { 
        'price_include_tax': 'priceIncludeTax',
        'tax_class_based_on': 'taxClassBasedOn'
    }

    def __init__(self, price_include_tax=None, tax_class_based_on=None):  # noqa: E501
        """TaxSettings - a model defined in Swagger"""  # noqa: E501
        

        self._price_include_tax = None
        self._tax_class_based_on = None
        self.discriminator = None

        if price_include_tax is not None:
            self.price_include_tax = price_include_tax
        if tax_class_based_on is not None:
            self.tax_class_based_on = tax_class_based_on


    @property
    def price_include_tax(self):
        """Gets the price_include_tax of this TaxSettings.  # noqa: E501


        :return: The price_include_tax of this TaxSettings.  # noqa: E501
        :rtype: bool
        """
        return self._price_include_tax

    @price_include_tax.setter
    def price_include_tax(self, price_include_tax):
        """Sets the price_include_tax of this TaxSettings.


        :param price_include_tax: The price_include_tax of this TaxSettings.
        :type: bool
        """

        self._price_include_tax = price_include_tax

    @property
    def tax_class_based_on(self):
        """Gets the tax_class_based_on of this TaxSettings.  # noqa: E501


        :return: The tax_class_based_on of this TaxSettings.  # noqa: E501
        :rtype: str
        """
        return self._tax_class_based_on

    @tax_class_based_on.setter
    def tax_class_based_on(self, tax_class_based_on):
        """Sets the tax_class_based_on of this TaxSettings.


        :param tax_class_based_on: The tax_class_based_on of this TaxSettings.
        :type: str
        """
        allowed_values = ["shippingAddress", "billingAddress"]  # noqa: E501
        if tax_class_based_on is not None and tax_class_based_on not in allowed_values:
            raise ValueError(
                "Invalid value for `tax_class_based_on` ({0}), must be one of {1}"  # noqa: E501
                .format(tax_class_based_on, allowed_values)
            )

        self._tax_class_based_on = tax_class_based_on


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
        if issubclass(TaxSettings, dict):
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
        if not isinstance(other, TaxSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
