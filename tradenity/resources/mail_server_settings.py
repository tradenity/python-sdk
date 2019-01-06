# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class MailServerSettings(object):


    swagger_types = { 
        'sender_email': 'str',
        'host': 'str',
        'port': 'int',
        'username': 'str',
        'password': 'str'
    }

    attribute_map = { 
        'sender_email': 'senderEmail',
        'host': 'host',
        'port': 'port',
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, sender_email=None, host=None, port=None, username=None, password=None):  # noqa: E501
        """MailServerSettings - a model defined in Swagger"""  # noqa: E501
        

        self._sender_email = None
        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self.discriminator = None

        if sender_email is not None:
            self.sender_email = sender_email
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password


    @property
    def sender_email(self):
        """Gets the sender_email of this MailServerSettings.  # noqa: E501


        :return: The sender_email of this MailServerSettings.  # noqa: E501
        :rtype: str
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """Sets the sender_email of this MailServerSettings.


        :param sender_email: The sender_email of this MailServerSettings.
        :type: str
        """

        self._sender_email = sender_email

    @property
    def host(self):
        """Gets the host of this MailServerSettings.  # noqa: E501


        :return: The host of this MailServerSettings.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this MailServerSettings.


        :param host: The host of this MailServerSettings.
        :type: str
        """

        self._host = host

    @property
    def port(self):
        """Gets the port of this MailServerSettings.  # noqa: E501


        :return: The port of this MailServerSettings.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this MailServerSettings.


        :param port: The port of this MailServerSettings.
        :type: int
        """

        self._port = port

    @property
    def username(self):
        """Gets the username of this MailServerSettings.  # noqa: E501


        :return: The username of this MailServerSettings.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this MailServerSettings.


        :param username: The username of this MailServerSettings.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this MailServerSettings.  # noqa: E501


        :return: The password of this MailServerSettings.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this MailServerSettings.


        :param password: The password of this MailServerSettings.
        :type: str
        """

        self._password = password


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
        if issubclass(MailServerSettings, dict):
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
        if not isinstance(other, MailServerSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
