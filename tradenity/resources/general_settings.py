# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class GeneralSettings(object):


    swagger_types = { 
        'local': 'str',
        'time_zone': 'str',
        'add_new_customers_to': 'CustomerGroup'
    }

    attribute_map = { 
        'local': 'local',
        'time_zone': 'timeZone',
        'add_new_customers_to': 'addNewCustomersTo'
    }

    def __init__(self, local=None, time_zone=None, add_new_customers_to=None):  # noqa: E501
        """GeneralSettings - a model defined in Swagger"""  # noqa: E501
        

        self._local = None
        self._time_zone = None
        self._add_new_customers_to = None
        self.discriminator = None

        if local is not None:
            self.local = local
        if time_zone is not None:
            self.time_zone = time_zone
        if add_new_customers_to is not None:
            self.add_new_customers_to = add_new_customers_to


    @property
    def local(self):
        """Gets the local of this GeneralSettings.  # noqa: E501


        :return: The local of this GeneralSettings.  # noqa: E501
        :rtype: str
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this GeneralSettings.


        :param local: The local of this GeneralSettings.
        :type: str
        """

        self._local = local

    @property
    def time_zone(self):
        """Gets the time_zone of this GeneralSettings.  # noqa: E501


        :return: The time_zone of this GeneralSettings.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this GeneralSettings.


        :param time_zone: The time_zone of this GeneralSettings.
        :type: str
        """

        self._time_zone = time_zone

    @property
    def add_new_customers_to(self):
        """Gets the add_new_customers_to of this GeneralSettings.  # noqa: E501


        :return: The add_new_customers_to of this GeneralSettings.  # noqa: E501
        :rtype: CustomerGroup
        """
        return self._add_new_customers_to

    @add_new_customers_to.setter
    def add_new_customers_to(self, add_new_customers_to):
        """Sets the add_new_customers_to of this GeneralSettings.


        :param add_new_customers_to: The add_new_customers_to of this GeneralSettings.
        :type: CustomerGroup
        """

        self._add_new_customers_to = add_new_customers_to


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
        if issubclass(GeneralSettings, dict):
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
        if not isinstance(other, GeneralSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
