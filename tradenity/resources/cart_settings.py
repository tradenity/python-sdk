# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class CartSettings(object):


    swagger_types = { 
        'auto_clear_shopping_cart': 'str'
    }

    attribute_map = { 
        'auto_clear_shopping_cart': 'autoClearShoppingCart'
    }

    def __init__(self, auto_clear_shopping_cart=None):  # noqa: E501
        """CartSettings - a model defined in Swagger"""  # noqa: E501
        

        self._auto_clear_shopping_cart = None
        self.discriminator = None

        if auto_clear_shopping_cart is not None:
            self.auto_clear_shopping_cart = auto_clear_shopping_cart


    @property
    def auto_clear_shopping_cart(self):
        """Gets the auto_clear_shopping_cart of this CartSettings.  # noqa: E501


        :return: The auto_clear_shopping_cart of this CartSettings.  # noqa: E501
        :rtype: str
        """
        return self._auto_clear_shopping_cart

    @auto_clear_shopping_cart.setter
    def auto_clear_shopping_cart(self, auto_clear_shopping_cart):
        """Sets the auto_clear_shopping_cart of this CartSettings.


        :param auto_clear_shopping_cart: The auto_clear_shopping_cart of this CartSettings.
        :type: str
        """
        allowed_values = ["never", "orderCreated", "orderCompleted"]  # noqa: E501
        if auto_clear_shopping_cart is not None and auto_clear_shopping_cart not in allowed_values:
            raise ValueError(
                "Invalid value for `auto_clear_shopping_cart` ({0}), must be one of {1}"  # noqa: E501
                .format(auto_clear_shopping_cart, allowed_values)
            )

        self._auto_clear_shopping_cart = auto_clear_shopping_cart


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
        if issubclass(CartSettings, dict):
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
        if not isinstance(other, CartSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
