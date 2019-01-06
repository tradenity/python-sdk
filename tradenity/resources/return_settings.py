# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class ReturnSettings(object):


    swagger_types = { 
        'allow_return': 'bool',
        'return_action': 'str',
        'return_cost': 'int',
        'return_refund_shipping': 'bool'
    }

    attribute_map = { 
        'allow_return': 'allowReturn',
        'return_action': 'returnAction',
        'return_cost': 'returnCost',
        'return_refund_shipping': 'returnRefundShipping'
    }

    def __init__(self, allow_return=None, return_action=None, return_cost=None, return_refund_shipping=None):  # noqa: E501
        """ReturnSettings - a model defined in Swagger"""  # noqa: E501
        

        self._allow_return = None
        self._return_action = None
        self._return_cost = None
        self._return_refund_shipping = None
        self.discriminator = None

        if allow_return is not None:
            self.allow_return = allow_return
        if return_action is not None:
            self.return_action = return_action
        if return_cost is not None:
            self.return_cost = return_cost
        if return_refund_shipping is not None:
            self.return_refund_shipping = return_refund_shipping


    @property
    def allow_return(self):
        """Gets the allow_return of this ReturnSettings.  # noqa: E501


        :return: The allow_return of this ReturnSettings.  # noqa: E501
        :rtype: bool
        """
        return self._allow_return

    @allow_return.setter
    def allow_return(self, allow_return):
        """Sets the allow_return of this ReturnSettings.


        :param allow_return: The allow_return of this ReturnSettings.
        :type: bool
        """

        self._allow_return = allow_return

    @property
    def return_action(self):
        """Gets the return_action of this ReturnSettings.  # noqa: E501


        :return: The return_action of this ReturnSettings.  # noqa: E501
        :rtype: str
        """
        return self._return_action

    @return_action.setter
    def return_action(self, return_action):
        """Sets the return_action of this ReturnSettings.


        :param return_action: The return_action of this ReturnSettings.
        :type: str
        """
        allowed_values = ["refund", "storeCredit"]  # noqa: E501
        if return_action is not None and return_action not in allowed_values:
            raise ValueError(
                "Invalid value for `return_action` ({0}), must be one of {1}"  # noqa: E501
                .format(return_action, allowed_values)
            )

        self._return_action = return_action

    @property
    def return_cost(self):
        """Gets the return_cost of this ReturnSettings.  # noqa: E501


        :return: The return_cost of this ReturnSettings.  # noqa: E501
        :rtype: int
        """
        return self._return_cost

    @return_cost.setter
    def return_cost(self, return_cost):
        """Sets the return_cost of this ReturnSettings.


        :param return_cost: The return_cost of this ReturnSettings.
        :type: int
        """

        self._return_cost = return_cost

    @property
    def return_refund_shipping(self):
        """Gets the return_refund_shipping of this ReturnSettings.  # noqa: E501


        :return: The return_refund_shipping of this ReturnSettings.  # noqa: E501
        :rtype: bool
        """
        return self._return_refund_shipping

    @return_refund_shipping.setter
    def return_refund_shipping(self, return_refund_shipping):
        """Sets the return_refund_shipping of this ReturnSettings.


        :param return_refund_shipping: The return_refund_shipping of this ReturnSettings.
        :type: bool
        """

        self._return_refund_shipping = return_refund_shipping


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
        if issubclass(ReturnSettings, dict):
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
        if not isinstance(other, ReturnSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
