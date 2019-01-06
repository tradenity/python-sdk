# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class InventorySettings(object):


    swagger_types = { 
        'update_on_new_order': 'bool',
        'update_on_refund': 'bool'
    }

    attribute_map = { 
        'update_on_new_order': 'updateOnNewOrder',
        'update_on_refund': 'updateOnRefund'
    }

    def __init__(self, update_on_new_order=None, update_on_refund=None):  # noqa: E501
        """InventorySettings - a model defined in Swagger"""  # noqa: E501
        

        self._update_on_new_order = None
        self._update_on_refund = None
        self.discriminator = None

        if update_on_new_order is not None:
            self.update_on_new_order = update_on_new_order
        if update_on_refund is not None:
            self.update_on_refund = update_on_refund


    @property
    def update_on_new_order(self):
        """Gets the update_on_new_order of this InventorySettings.  # noqa: E501


        :return: The update_on_new_order of this InventorySettings.  # noqa: E501
        :rtype: bool
        """
        return self._update_on_new_order

    @update_on_new_order.setter
    def update_on_new_order(self, update_on_new_order):
        """Sets the update_on_new_order of this InventorySettings.


        :param update_on_new_order: The update_on_new_order of this InventorySettings.
        :type: bool
        """

        self._update_on_new_order = update_on_new_order

    @property
    def update_on_refund(self):
        """Gets the update_on_refund of this InventorySettings.  # noqa: E501


        :return: The update_on_refund of this InventorySettings.  # noqa: E501
        :rtype: bool
        """
        return self._update_on_refund

    @update_on_refund.setter
    def update_on_refund(self, update_on_refund):
        """Sets the update_on_refund of this InventorySettings.


        :param update_on_refund: The update_on_refund of this InventorySettings.
        :type: bool
        """

        self._update_on_refund = update_on_refund


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
        if issubclass(InventorySettings, dict):
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
        if not isinstance(other, InventorySettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
