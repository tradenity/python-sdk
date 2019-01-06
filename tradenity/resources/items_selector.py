# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class ItemsSelector(object):


    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'categories': 'list[Category]',
        'brands': 'list[Brand]',
        'collections': 'list[Collection]',
        'products': 'list[Product]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'categories': 'categories',
        'brands': 'brands',
        'collections': 'collections',
        'products': 'products'
    }

    def __init__(self, id=None, meta=None, categories=None, brands=None, collections=None, products=None):  # noqa: E501
        """ItemsSelector - a model defined in Swagger"""  # noqa: E501
        self._id = id

        self._meta = None
        self._categories = None
        self._brands = None
        self._collections = None
        self._products = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if categories is not None:
            self.categories = categories
        if brands is not None:
            self.brands = brands
        if collections is not None:
            self.collections = collections
        if products is not None:
            self.products = products

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
        """Gets the meta of this ItemsSelector.  # noqa: E501


        :return: The meta of this ItemsSelector.  # noqa: E501
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ItemsSelector.


        :param meta: The meta of this ItemsSelector.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def categories(self):
        """Gets the categories of this ItemsSelector.  # noqa: E501


        :return: The categories of this ItemsSelector.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ItemsSelector.


        :param categories: The categories of this ItemsSelector.
        :type: list[Category]
        """

        self._categories = categories

    @property
    def brands(self):
        """Gets the brands of this ItemsSelector.  # noqa: E501


        :return: The brands of this ItemsSelector.  # noqa: E501
        :rtype: list[Brand]
        """
        return self._brands

    @brands.setter
    def brands(self, brands):
        """Sets the brands of this ItemsSelector.


        :param brands: The brands of this ItemsSelector.
        :type: list[Brand]
        """

        self._brands = brands

    @property
    def collections(self):
        """Gets the collections of this ItemsSelector.  # noqa: E501


        :return: The collections of this ItemsSelector.  # noqa: E501
        :rtype: list[Collection]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """Sets the collections of this ItemsSelector.


        :param collections: The collections of this ItemsSelector.
        :type: list[Collection]
        """

        self._collections = collections

    @property
    def products(self):
        """Gets the products of this ItemsSelector.  # noqa: E501


        :return: The products of this ItemsSelector.  # noqa: E501
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this ItemsSelector.


        :param products: The products of this ItemsSelector.
        :type: list[Product]
        """

        self._products = products


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
        if issubclass(ItemsSelector, dict):
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
        if not isinstance(other, ItemsSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
