# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


from __future__ import absolute_import

import re
import pprint

# python 2 and python 3 compatibility library
import six

from tradenity.api_client import ApiClient


class OrderLineItem(object):
    

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
        'discount_amount': 'int',
        'order': 'Order'
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
        'discount_amount': 'discountAmount',
        'order': 'order'
    }

    api_client = None

    def __init__(self, id=None, meta=None, unit_price=None, quantity=None, product=None, taxes=None, promotions=None, subtotal=None, total=None, shipping_amount=None, tax_amount=None, discount_amount=None, order=None):
        """OrderLineItem - a model defined in Swagger"""
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
        self._order = None
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
        self.order = order

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
        """Gets the meta of this OrderLineItem.


        :return: The meta of this OrderLineItem.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this OrderLineItem.


        :param meta: The meta of this OrderLineItem.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def unit_price(self):
        """Gets the unit_price of this OrderLineItem.


        :return: The unit_price of this OrderLineItem.
        :rtype: int
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this OrderLineItem.


        :param unit_price: The unit_price of this OrderLineItem.
        :type: int
        """

        self._unit_price = unit_price

    @property
    def quantity(self):
        """Gets the quantity of this OrderLineItem.


        :return: The quantity of this OrderLineItem.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this OrderLineItem.


        :param quantity: The quantity of this OrderLineItem.
        :type: int
        """

        self._quantity = quantity

    @property
    def product(self):
        """Gets the product of this OrderLineItem.


        :return: The product of this OrderLineItem.
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this OrderLineItem.


        :param product: The product of this OrderLineItem.
        :type: Product
        """

        self._product = product

    @property
    def taxes(self):
        """Gets the taxes of this OrderLineItem.


        :return: The taxes of this OrderLineItem.
        :rtype: list[TaxRate]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this OrderLineItem.


        :param taxes: The taxes of this OrderLineItem.
        :type: list[TaxRate]
        """

        self._taxes = taxes

    @property
    def promotions(self):
        """Gets the promotions of this OrderLineItem.


        :return: The promotions of this OrderLineItem.
        :rtype: list[Promotion]
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """Sets the promotions of this OrderLineItem.


        :param promotions: The promotions of this OrderLineItem.
        :type: list[Promotion]
        """

        self._promotions = promotions

    @property
    def subtotal(self):
        """Gets the subtotal of this OrderLineItem.


        :return: The subtotal of this OrderLineItem.
        :rtype: int
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this OrderLineItem.


        :param subtotal: The subtotal of this OrderLineItem.
        :type: int
        """

        self._subtotal = subtotal

    @property
    def total(self):
        """Gets the total of this OrderLineItem.


        :return: The total of this OrderLineItem.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this OrderLineItem.


        :param total: The total of this OrderLineItem.
        :type: int
        """

        self._total = total

    @property
    def shipping_amount(self):
        """Gets the shipping_amount of this OrderLineItem.


        :return: The shipping_amount of this OrderLineItem.
        :rtype: int
        """
        return self._shipping_amount

    @shipping_amount.setter
    def shipping_amount(self, shipping_amount):
        """Sets the shipping_amount of this OrderLineItem.


        :param shipping_amount: The shipping_amount of this OrderLineItem.
        :type: int
        """

        self._shipping_amount = shipping_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this OrderLineItem.


        :return: The tax_amount of this OrderLineItem.
        :rtype: int
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this OrderLineItem.


        :param tax_amount: The tax_amount of this OrderLineItem.
        :type: int
        """

        self._tax_amount = tax_amount

    @property
    def discount_amount(self):
        """Gets the discount_amount of this OrderLineItem.


        :return: The discount_amount of this OrderLineItem.
        :rtype: int
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this OrderLineItem.


        :param discount_amount: The discount_amount of this OrderLineItem.
        :type: int
        """

        self._discount_amount = discount_amount

    @property
    def order(self):
        """Gets the order of this OrderLineItem.


        :return: The order of this OrderLineItem.
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this OrderLineItem.


        :param order: The order of this OrderLineItem.
        :type: Order
        """

        self._order = order

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
        if issubclass(OrderLineItem, dict):
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
        if not isinstance(other, OrderLineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    @classmethod
    def get_api_client(cls):
        if cls.api_client is None:
            cls.api_client = ApiClient.instance()
        return cls.api_client


    @classmethod
    def find_all(cls, page_request=None):
        return cls.list_all_order_line_items()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_order_line_items(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_order_line_items(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_order_line_item_by_id(id)

    def create(self):
        new_instance = self.create_order_line_item(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_order_line_item_by_id(self.id, self)

    def delete(self):
        return self.delete_order_line_item_by_id(self.id)



    @classmethod
    def create_order_line_item(cls, order_line_item, **kwargs):
        """Create OrderLineItem

        Create a new OrderLineItem
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_order_line_item(order_line_item, async=True)
        >>> result = thread.get()

        :param async bool
        :param OrderLineItem order_line_item: Attributes of orderLineItem to create (required)
        :return: OrderLineItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_order_line_item_with_http_info(order_line_item, **kwargs)
        else:
            (data) = cls._create_order_line_item_with_http_info(order_line_item, **kwargs)
            return data

    @classmethod
    def _create_order_line_item_with_http_info(cls, order_line_item, **kwargs):
        """Create OrderLineItem

        Create a new OrderLineItem
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_order_line_item_with_http_info(order_line_item, async=True)
        >>> result = thread.get()

        :param async bool
        :param OrderLineItem order_line_item: Attributes of orderLineItem to create (required)
        :return: OrderLineItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_line_item']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_line_item' is set
        if ('order_line_item' not in params or
                params['order_line_item'] is None):
            raise ValueError("Missing the required parameter `order_line_item` when calling `create_order_line_item`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'order_line_item' in params:
            body_params = params['order_line_item']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/orderLineItems', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderLineItem',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_order_line_item_by_id(cls, order_line_item_id, **kwargs):
        """Delete OrderLineItem

        Delete an instance of OrderLineItem by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_order_line_item_by_id(order_line_item_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_line_item_id: ID of orderLineItem to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_order_line_item_by_id_with_http_info(order_line_item_id, **kwargs)
        else:
            (data) = cls._delete_order_line_item_by_id_with_http_info(order_line_item_id, **kwargs)
            return data

    @classmethod
    def _delete_order_line_item_by_id_with_http_info(cls, order_line_item_id, **kwargs):
        """Delete OrderLineItem

        Delete an instance of OrderLineItem by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_order_line_item_by_id_with_http_info(order_line_item_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_line_item_id: ID of orderLineItem to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_line_item_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_line_item_id' is set
        if ('order_line_item_id' not in params or
                params['order_line_item_id'] is None):
            raise ValueError("Missing the required parameter `order_line_item_id` when calling `delete_order_line_item_by_id`")

        collection_formats = {}

        path_params = {}
        if 'order_line_item_id' in params:
            path_params['orderLineItemId'] = params['order_line_item_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/orderLineItems/{orderLineItemId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def get_order_line_item_by_id(cls, order_line_item_id, **kwargs):
        """Find OrderLineItem

        Return single instance of OrderLineItem by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_line_item_by_id(order_line_item_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_line_item_id: ID of orderLineItem to return (required)
        :return: OrderLineItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_order_line_item_by_id_with_http_info(order_line_item_id, **kwargs)
        else:
            (data) = cls._get_order_line_item_by_id_with_http_info(order_line_item_id, **kwargs)
            return data

    @classmethod
    def _get_order_line_item_by_id_with_http_info(cls, order_line_item_id, **kwargs):
        """Find OrderLineItem

        Return single instance of OrderLineItem by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_line_item_by_id_with_http_info(order_line_item_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_line_item_id: ID of orderLineItem to return (required)
        :return: OrderLineItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_line_item_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_line_item_id' is set
        if ('order_line_item_id' not in params or
                params['order_line_item_id'] is None):
            raise ValueError("Missing the required parameter `order_line_item_id` when calling `get_order_line_item_by_id`")

        collection_formats = {}

        path_params = {}
        if 'order_line_item_id' in params:
            path_params['orderLineItemId'] = params['order_line_item_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/orderLineItems/{orderLineItemId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderLineItem',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_order_line_items(cls, **kwargs):
        """List OrderLineItems

        Return a list of OrderLineItems
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_order_line_items(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[OrderLineItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_order_line_items_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_order_line_items_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_order_line_items_with_http_info(cls, **kwargs):
        """List OrderLineItems

        Return a list of OrderLineItems
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_order_line_items_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[OrderLineItem]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'size', 'sort']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/orderLineItems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[OrderLineItem]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_order_line_item_by_id(cls, order_line_item_id, order_line_item, **kwargs):
        """Replace OrderLineItem

        Replace all attributes of OrderLineItem
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_order_line_item_by_id(order_line_item_id, order_line_item, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_line_item_id: ID of orderLineItem to replace (required)
        :param OrderLineItem order_line_item: Attributes of orderLineItem to replace (required)
        :return: OrderLineItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_order_line_item_by_id_with_http_info(order_line_item_id, order_line_item, **kwargs)
        else:
            (data) = cls._replace_order_line_item_by_id_with_http_info(order_line_item_id, order_line_item, **kwargs)
            return data

    @classmethod
    def _replace_order_line_item_by_id_with_http_info(cls, order_line_item_id, order_line_item, **kwargs):
        """Replace OrderLineItem

        Replace all attributes of OrderLineItem
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_order_line_item_by_id_with_http_info(order_line_item_id, order_line_item, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_line_item_id: ID of orderLineItem to replace (required)
        :param OrderLineItem order_line_item: Attributes of orderLineItem to replace (required)
        :return: OrderLineItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_line_item_id', 'order_line_item']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_line_item_id' is set
        if ('order_line_item_id' not in params or
                params['order_line_item_id'] is None):
            raise ValueError("Missing the required parameter `order_line_item_id` when calling `replace_order_line_item_by_id`")
        # verify the required parameter 'order_line_item' is set
        if ('order_line_item' not in params or
                params['order_line_item'] is None):
            raise ValueError("Missing the required parameter `order_line_item` when calling `replace_order_line_item_by_id`")

        collection_formats = {}

        path_params = {}
        if 'order_line_item_id' in params:
            path_params['orderLineItemId'] = params['order_line_item_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'order_line_item' in params:
            body_params = params['order_line_item']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/orderLineItems/{orderLineItemId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderLineItem',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_order_line_item_by_id(cls, order_line_item_id, order_line_item, **kwargs):
        """Update OrderLineItem

        Update attributes of OrderLineItem
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_order_line_item_by_id(order_line_item_id, order_line_item, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_line_item_id: ID of orderLineItem to update. (required)
        :param OrderLineItem order_line_item: Attributes of orderLineItem to update. (required)
        :return: OrderLineItem
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_order_line_item_by_id_with_http_info(order_line_item_id, order_line_item, **kwargs)
        else:
            (data) = cls._update_order_line_item_by_id_with_http_info(order_line_item_id, order_line_item, **kwargs)
            return data

    @classmethod
    def _update_order_line_item_by_id_with_http_info(cls, order_line_item_id, order_line_item, **kwargs):
        """Update OrderLineItem

        Update attributes of OrderLineItem
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_order_line_item_by_id_with_http_info(order_line_item_id, order_line_item, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_line_item_id: ID of orderLineItem to update. (required)
        :param OrderLineItem order_line_item: Attributes of orderLineItem to update. (required)
        :return: OrderLineItem
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_line_item_id', 'order_line_item']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_line_item_id' is set
        if ('order_line_item_id' not in params or
                params['order_line_item_id'] is None):
            raise ValueError("Missing the required parameter `order_line_item_id` when calling `update_order_line_item_by_id`")
        # verify the required parameter 'order_line_item' is set
        if ('order_line_item' not in params or
                params['order_line_item'] is None):
            raise ValueError("Missing the required parameter `order_line_item` when calling `update_order_line_item_by_id`")

        collection_formats = {}

        path_params = {}
        if 'order_line_item_id' in params:
            path_params['orderLineItemId'] = params['order_line_item_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'order_line_item' in params:
            body_params = params['order_line_item']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/orderLineItems/{orderLineItemId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderLineItem',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
