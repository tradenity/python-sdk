# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class Photo(object):


    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'title': 'str',
        'description': 'str',
        'position': 'int',
        'mime_type': 'str',
        'storage_type': 'str',
        'storage_path': 'str',
        'url': 'str',
        'account': 'Account'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'title': 'title',
        'description': 'description',
        'position': 'position',
        'mime_type': 'mimeType',
        'storage_type': 'storageType',
        'storage_path': 'storagePath',
        'url': 'url',
        'account': 'account'
    }

    def __init__(self, id=None, meta=None, name=None, title=None, description=None, position=None, mime_type=None, storage_type=None, storage_path=None, url=None, account=None):  # noqa: E501
        """Photo - a model defined in Swagger"""  # noqa: E501
        self._id = id

        self._meta = None
        self._name = None
        self._title = None
        self._description = None
        self._position = None
        self._mime_type = None
        self._storage_type = None
        self._storage_path = None
        self._url = None
        self._account = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.title = title
        if description is not None:
            self.description = description
        if position is not None:
            self.position = position
        self.mime_type = mime_type
        self.storage_type = storage_type
        self.storage_path = storage_path
        if url is not None:
            self.url = url
        if account is not None:
            self.account = account

    @property
    def id(self):
        if self._id:
            return self._id
        elif self.meta is None:
            return None
        else:
            self._id = self.meta.href.split("/")[-1]
            return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def meta(self):
        """Gets the meta of this Photo.  # noqa: E501


        :return: The meta of this Photo.  # noqa: E501
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Photo.


        :param meta: The meta of this Photo.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Photo.  # noqa: E501


        :return: The name of this Photo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Photo.


        :param name: The name of this Photo.
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """Gets the title of this Photo.  # noqa: E501


        :return: The title of this Photo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Photo.


        :param title: The title of this Photo.
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this Photo.  # noqa: E501


        :return: The description of this Photo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Photo.


        :param description: The description of this Photo.
        :type: str
        """

        self._description = description

    @property
    def position(self):
        """Gets the position of this Photo.  # noqa: E501


        :return: The position of this Photo.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Photo.


        :param position: The position of this Photo.
        :type: int
        """

        self._position = position

    @property
    def mime_type(self):
        """Gets the mime_type of this Photo.  # noqa: E501


        :return: The mime_type of this Photo.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this Photo.


        :param mime_type: The mime_type of this Photo.
        :type: str
        """

        self._mime_type = mime_type

    @property
    def storage_type(self):
        """Gets the storage_type of this Photo.  # noqa: E501


        :return: The storage_type of this Photo.  # noqa: E501
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this Photo.


        :param storage_type: The storage_type of this Photo.
        :type: str
        """

        self._storage_type = storage_type

    @property
    def storage_path(self):
        """Gets the storage_path of this Photo.  # noqa: E501


        :return: The storage_path of this Photo.  # noqa: E501
        :rtype: str
        """
        return self._storage_path

    @storage_path.setter
    def storage_path(self, storage_path):
        """Sets the storage_path of this Photo.


        :param storage_path: The storage_path of this Photo.
        :type: str
        """

        self._storage_path = storage_path

    @property
    def url(self):
        """Gets the url of this Photo.  # noqa: E501


        :return: The url of this Photo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Photo.


        :param url: The url of this Photo.
        :type: str
        """

        self._url = url

    @property
    def account(self):
        """Gets the account of this Photo.  # noqa: E501


        :return: The account of this Photo.  # noqa: E501
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Photo.


        :param account: The account of this Photo.
        :type: Account
        """

        self._account = account


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
        if issubclass(Photo, dict):
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
        if not isinstance(other, Photo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
