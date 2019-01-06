# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class WebHooks(object):


    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'order_created': 'str',
        'order_changed': 'str',
        'order_refunded': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'order_created': 'orderCreated',
        'order_changed': 'orderChanged',
        'order_refunded': 'orderRefunded'
    }

    def __init__(self, id=None, meta=None, order_created=None, order_changed=None, order_refunded=None):  # noqa: E501
        """WebHooks - a model defined in Swagger"""  # noqa: E501
        self._id = id

        self._meta = None
        self._order_created = None
        self._order_changed = None
        self._order_refunded = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if order_created is not None:
            self.order_created = order_created
        if order_changed is not None:
            self.order_changed = order_changed
        if order_refunded is not None:
            self.order_refunded = order_refunded

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
        """Gets the meta of this WebHooks.  # noqa: E501


        :return: The meta of this WebHooks.  # noqa: E501
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this WebHooks.


        :param meta: The meta of this WebHooks.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def order_created(self):
        """Gets the order_created of this WebHooks.  # noqa: E501


        :return: The order_created of this WebHooks.  # noqa: E501
        :rtype: str
        """
        return self._order_created

    @order_created.setter
    def order_created(self, order_created):
        """Sets the order_created of this WebHooks.


        :param order_created: The order_created of this WebHooks.
        :type: str
        """

        self._order_created = order_created

    @property
    def order_changed(self):
        """Gets the order_changed of this WebHooks.  # noqa: E501


        :return: The order_changed of this WebHooks.  # noqa: E501
        :rtype: str
        """
        return self._order_changed

    @order_changed.setter
    def order_changed(self, order_changed):
        """Sets the order_changed of this WebHooks.


        :param order_changed: The order_changed of this WebHooks.
        :type: str
        """

        self._order_changed = order_changed

    @property
    def order_refunded(self):
        """Gets the order_refunded of this WebHooks.  # noqa: E501


        :return: The order_refunded of this WebHooks.  # noqa: E501
        :rtype: str
        """
        return self._order_refunded

    @order_refunded.setter
    def order_refunded(self, order_refunded):
        """Sets the order_refunded of this WebHooks.


        :param order_refunded: The order_refunded of this WebHooks.
        :type: str
        """

        self._order_refunded = order_refunded


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
        if issubclass(WebHooks, dict):
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
        if not isinstance(other, WebHooks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
