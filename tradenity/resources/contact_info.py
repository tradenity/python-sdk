# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class ContactInfo(object):


    swagger_types = { 
        'contact_name': 'str',
        'email': 'str',
        'phone': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'city': 'str',
        'state': 'str',
        'zip_code': 'str',
        'country': 'str'
    }

    attribute_map = { 
        'contact_name': 'contactName',
        'email': 'email',
        'phone': 'phone',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'city': 'city',
        'state': 'state',
        'zip_code': 'zipCode',
        'country': 'country'
    }

    def __init__(self, contact_name=None, email=None, phone=None, address_line1=None, address_line2=None, city=None, state=None, zip_code=None, country=None):  # noqa: E501
        """ContactInfo - a model defined in Swagger"""  # noqa: E501
        

        self._contact_name = None
        self._email = None
        self._phone = None
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._state = None
        self._zip_code = None
        self._country = None
        self.discriminator = None

        self.contact_name = contact_name
        self.email = email
        self.phone = phone
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country


    @property
    def contact_name(self):
        """Gets the contact_name of this ContactInfo.  # noqa: E501


        :return: The contact_name of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this ContactInfo.


        :param contact_name: The contact_name of this ContactInfo.
        :type: str
        """

        self._contact_name = contact_name

    @property
    def email(self):
        """Gets the email of this ContactInfo.  # noqa: E501


        :return: The email of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ContactInfo.


        :param email: The email of this ContactInfo.
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this ContactInfo.  # noqa: E501


        :return: The phone of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ContactInfo.


        :param phone: The phone of this ContactInfo.
        :type: str
        """

        self._phone = phone

    @property
    def address_line1(self):
        """Gets the address_line1 of this ContactInfo.  # noqa: E501


        :return: The address_line1 of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this ContactInfo.


        :param address_line1: The address_line1 of this ContactInfo.
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this ContactInfo.  # noqa: E501


        :return: The address_line2 of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this ContactInfo.


        :param address_line2: The address_line2 of this ContactInfo.
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this ContactInfo.  # noqa: E501


        :return: The city of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ContactInfo.


        :param city: The city of this ContactInfo.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this ContactInfo.  # noqa: E501


        :return: The state of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ContactInfo.


        :param state: The state of this ContactInfo.
        :type: str
        """

        self._state = state

    @property
    def zip_code(self):
        """Gets the zip_code of this ContactInfo.  # noqa: E501


        :return: The zip_code of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this ContactInfo.


        :param zip_code: The zip_code of this ContactInfo.
        :type: str
        """

        self._zip_code = zip_code

    @property
    def country(self):
        """Gets the country of this ContactInfo.  # noqa: E501


        :return: The country of this ContactInfo.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ContactInfo.


        :param country: The country of this ContactInfo.
        :type: str
        """

        self._country = country


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
        if issubclass(ContactInfo, dict):
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
        if not isinstance(other, ContactInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
