# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


import pprint
import re  # noqa: F401

import six


class LineItem(object):


    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'unit_price': 'int',
        'quantity': 'int',
        'product': 'Product',
        'taxes': 'list[TaxRate]',
        'promotions': 'list[Promotion]',
        'subtotal': 'int',
        'total': 'int',
        'shipping_amount': 'int',
        'tax_amount': 'int',
        'discount_amount': 'int'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'unit_price': 'unitPrice',
        'quantity': 'quantity',
        'product': 'product',
        'taxes': 'taxes',
        'promotions': 'promotions',
        'subtotal': 'subtotal',
        'total': 'total',
        'shipping_amount': 'shippingAmount',
        'tax_amount': 'taxAmount',
        'discount_amount': 'discountAmount'
    }

    def __init__(self, id=None, meta=None, unit_price=None, quantity=None, product=None, taxes=None, promotions=None, subtotal=None, total=None, shipping_amount=None, tax_amount=None, discount_amount=None):  # noqa: E501
        """LineItem - a model defined in Swagger"""  # noqa: E501
        self._id = id

        self._meta = None
        self._unit_price = None
        self._quantity = None
        self._product = None
        self._taxes = None
        self._promotions = None
        self._subtotal = None
        self._total = None
        self._shipping_amount = None
        self._tax_amount = None
        self._discount_amount = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.unit_price = unit_price
        self.quantity = quantity
        self.product = product
        if taxes is not None:
            self.taxes = taxes
        if promotions is not None:
            self.promotions = promotions
        if subtotal is not None:
            self.subtotal = subtotal
        if total is not None:
            self.total = total
        if shipping_amount is not None:
            self.shipping_amount = shipping_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if discount_amount is not None:
            self.discount_amount = discount_amount

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
        """Gets the meta of this LineItem.  # noqa: E501


        :return: The meta of this LineItem.  # noqa: E501
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this LineItem.


        :param meta: The meta of this LineItem.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def unit_price(self):
        """Gets the unit_price of this LineItem.  # noqa: E501


        :return: The unit_price of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this LineItem.


        :param unit_price: The unit_price of this LineItem.
        :type: int
        """

        self._unit_price = unit_price

    @property
    def quantity(self):
        """Gets the quantity of this LineItem.  # noqa: E501


        :return: The quantity of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItem.


        :param quantity: The quantity of this LineItem.
        :type: int
        """

        self._quantity = quantity

    @property
    def product(self):
        """Gets the product of this LineItem.  # noqa: E501


        :return: The product of this LineItem.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this LineItem.


        :param product: The product of this LineItem.
        :type: Product
        """

        self._product = product

    @property
    def taxes(self):
        """Gets the taxes of this LineItem.  # noqa: E501


        :return: The taxes of this LineItem.  # noqa: E501
        :rtype: list[TaxRate]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this LineItem.


        :param taxes: The taxes of this LineItem.
        :type: list[TaxRate]
        """

        self._taxes = taxes

    @property
    def promotions(self):
        """Gets the promotions of this LineItem.  # noqa: E501


        :return: The promotions of this LineItem.  # noqa: E501
        :rtype: list[Promotion]
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """Sets the promotions of this LineItem.


        :param promotions: The promotions of this LineItem.
        :type: list[Promotion]
        """

        self._promotions = promotions

    @property
    def subtotal(self):
        """Gets the subtotal of this LineItem.  # noqa: E501


        :return: The subtotal of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this LineItem.


        :param subtotal: The subtotal of this LineItem.
        :type: int
        """

        self._subtotal = subtotal

    @property
    def total(self):
        """Gets the total of this LineItem.  # noqa: E501


        :return: The total of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this LineItem.


        :param total: The total of this LineItem.
        :type: int
        """

        self._total = total

    @property
    def shipping_amount(self):
        """Gets the shipping_amount of this LineItem.  # noqa: E501


        :return: The shipping_amount of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._shipping_amount

    @shipping_amount.setter
    def shipping_amount(self, shipping_amount):
        """Sets the shipping_amount of this LineItem.


        :param shipping_amount: The shipping_amount of this LineItem.
        :type: int
        """

        self._shipping_amount = shipping_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this LineItem.  # noqa: E501


        :return: The tax_amount of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this LineItem.


        :param tax_amount: The tax_amount of this LineItem.
        :type: int
        """

        self._tax_amount = tax_amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this LineItem.  # noqa: E501


        :return: The discount_amount of this LineItem.  # noqa: E501
        :rtype: int
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this LineItem.


        :param discount_amount: The discount_amount of this LineItem.
        :type: int
        """

        self._discount_amount = discount_amount


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
        if issubclass(LineItem, dict):
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
        if not isinstance(other, LineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
