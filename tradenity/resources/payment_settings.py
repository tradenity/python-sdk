# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class PaymentSettings(object):


    swagger_types = { 
        'currency': 'Currency',
        'gateway': 'Gateway'
    }

    attribute_map = { 
        'currency': 'currency',
        'gateway': 'gateway'
    }

    def __init__(self, currency=None, gateway=None):  # noqa: E501
        """PaymentSettings - a model defined in Swagger"""  # noqa: E501
        

        self._currency = None
        self._gateway = None
        self.discriminator = None

        self.currency = currency
        self.gateway = gateway


    @property
    def currency(self):
        """Gets the currency of this PaymentSettings.  # noqa: E501


        :return: The currency of this PaymentSettings.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentSettings.


        :param currency: The currency of this PaymentSettings.
        :type: Currency
        """

        self._currency = currency

    @property
    def gateway(self):
        """Gets the gateway of this PaymentSettings.  # noqa: E501


        :return: The gateway of this PaymentSettings.  # noqa: E501
        :rtype: Gateway
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this PaymentSettings.


        :param gateway: The gateway of this PaymentSettings.
        :type: Gateway
        """

        self._gateway = gateway


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
        if issubclass(PaymentSettings, dict):
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
        if not isinstance(other, PaymentSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
