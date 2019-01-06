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


class ShoppingCart(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'items': 'list[LineItem]',
        'subtotal': 'int',
        'total': 'int',
        'shipping_cost': 'int',
        'items_tax_amount': 'int',
        'total_items_discount': 'int',
        'promotions': 'list[Promotion]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'items': 'items',
        'subtotal': 'subtotal',
        'total': 'total',
        'shipping_cost': 'shippingCost',
        'items_tax_amount': 'itemsTaxAmount',
        'total_items_discount': 'totalItemsDiscount',
        'promotions': 'promotions'
    }

    api_client = None

    def __init__(self, id=None, meta=None, items=None, subtotal=None, total=None, shipping_cost=None, items_tax_amount=None, total_items_discount=None, promotions=None):
        """ShoppingCart - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._items = None
        self._subtotal = None
        self._total = None
        self._shipping_cost = None
        self._items_tax_amount = None
        self._total_items_discount = None
        self._promotions = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if items is not None:
            self.items = items
        self.subtotal = subtotal
        self.total = total
        if shipping_cost is not None:
            self.shipping_cost = shipping_cost
        if items_tax_amount is not None:
            self.items_tax_amount = items_tax_amount
        if total_items_discount is not None:
            self.total_items_discount = total_items_discount
        if promotions is not None:
            self.promotions = promotions

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
        """Gets the meta of this ShoppingCart.


        :return: The meta of this ShoppingCart.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ShoppingCart.


        :param meta: The meta of this ShoppingCart.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def items(self):
        """Gets the items of this ShoppingCart.


        :return: The items of this ShoppingCart.
        :rtype: list[LineItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ShoppingCart.


        :param items: The items of this ShoppingCart.
        :type: list[LineItem]
        """

        self._items = items

    @property
    def subtotal(self):
        """Gets the subtotal of this ShoppingCart.


        :return: The subtotal of this ShoppingCart.
        :rtype: int
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this ShoppingCart.


        :param subtotal: The subtotal of this ShoppingCart.
        :type: int
        """

        self._subtotal = subtotal

    @property
    def total(self):
        """Gets the total of this ShoppingCart.


        :return: The total of this ShoppingCart.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShoppingCart.


        :param total: The total of this ShoppingCart.
        :type: int
        """

        self._total = total

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this ShoppingCart.


        :return: The shipping_cost of this ShoppingCart.
        :rtype: int
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this ShoppingCart.


        :param shipping_cost: The shipping_cost of this ShoppingCart.
        :type: int
        """

        self._shipping_cost = shipping_cost

    @property
    def items_tax_amount(self):
        """Gets the items_tax_amount of this ShoppingCart.


        :return: The items_tax_amount of this ShoppingCart.
        :rtype: int
        """
        return self._items_tax_amount

    @items_tax_amount.setter
    def items_tax_amount(self, items_tax_amount):
        """Sets the items_tax_amount of this ShoppingCart.


        :param items_tax_amount: The items_tax_amount of this ShoppingCart.
        :type: int
        """

        self._items_tax_amount = items_tax_amount

    @property
    def total_items_discount(self):
        """Gets the total_items_discount of this ShoppingCart.


        :return: The total_items_discount of this ShoppingCart.
        :rtype: int
        """
        return self._total_items_discount

    @total_items_discount.setter
    def total_items_discount(self, total_items_discount):
        """Sets the total_items_discount of this ShoppingCart.


        :param total_items_discount: The total_items_discount of this ShoppingCart.
        :type: int
        """

        self._total_items_discount = total_items_discount

    @property
    def promotions(self):
        """Gets the promotions of this ShoppingCart.


        :return: The promotions of this ShoppingCart.
        :rtype: list[Promotion]
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """Sets the promotions of this ShoppingCart.


        :param promotions: The promotions of this ShoppingCart.
        :type: list[Promotion]
        """

        self._promotions = promotions

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
        if issubclass(ShoppingCart, dict):
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
        if not isinstance(other, ShoppingCart):
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
    def add_item(cls, item, **kwargs):
        """Add item.

        Add new item to the shopping cart.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_item(item, async=True)
        >>> result = thread.get()

        :param async bool
        :param LineItem item: Line item to add to cart (required)
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._add_item_with_http_info(item, **kwargs)
        else:
            (data) = cls._add_item_with_http_info(item, **kwargs)
            return data

    @classmethod
    def _add_item_with_http_info(cls, item, **kwargs):
        """Add item.

        Add new item to the shopping cart.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.add_item_with_http_info(item, async=True)
        >>> result = thread.get()

        :param async bool
        :param LineItem item: Line item to add to cart (required)
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item']
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
        # verify the required parameter 'item' is set
        if ('item' not in params or
                params['item'] is None):
            raise ValueError("Missing the required parameter `item` when calling `add_item`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'item' in params:
            body_params = params['item']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/shoppingCarts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShoppingCart',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def checkout(cls, order, **kwargs):
        """Checkout cart.

        Checkout cart, Making an order.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.checkout(order, async=True)
        >>> result = thread.get()

        :param async bool
        :param Order order: Required order details. (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._checkout_with_http_info(order, **kwargs)
        else:
            (data) = cls._checkout_with_http_info(order, **kwargs)
            return data

    @classmethod
    def _checkout_with_http_info(cls, order, **kwargs):
        """Checkout cart.

        Checkout cart, Making an order.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.checkout_with_http_info(order, async=True)
        >>> result = thread.get()

        :param async bool
        :param Order order: Required order details. (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order']
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
        # verify the required parameter 'order' is set
        if ('order' not in params or
                params['order'] is None):
            raise ValueError("Missing the required parameter `order` when calling `checkout`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'order' in params:
            body_params = params['order']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/shoppingCarts/checkout', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Order',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_item(cls, item_id, **kwargs):
        """Remove item.

        Remove item from shopping cart
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_item(item_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str item_id: Item ID to delete. (required)
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_item_with_http_info(item_id, **kwargs)
        else:
            (data) = cls._delete_item_with_http_info(item_id, **kwargs)
            return data

    @classmethod
    def _delete_item_with_http_info(cls, item_id, **kwargs):
        """Remove item.

        Remove item from shopping cart
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_item_with_http_info(item_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str item_id: Item ID to delete. (required)
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id']
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
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `delete_item`")

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']


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
            '/shoppingCarts/{itemId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShoppingCart',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def empty(cls, **kwargs):
        """Empty cart.

        Empty the shopping cart.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.empty(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._empty_with_http_info(**kwargs)
        else:
            (data) = cls._empty_with_http_info(**kwargs)
            return data

    @classmethod
    def _empty_with_http_info(cls, **kwargs):
        """Empty cart.

        Empty the shopping cart.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.empty_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
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
            '/shoppingCarts', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShoppingCart',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def get(cls, **kwargs):
        """Get cart.

        Retrieve the shopping cart of the current session.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_with_http_info(**kwargs)
        else:
            (data) = cls._get_with_http_info(**kwargs)
            return data

    @classmethod
    def _get_with_http_info(cls, **kwargs):
        """Get cart.

        Retrieve the shopping cart of the current session.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
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
            '/shoppingCarts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShoppingCart',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_item(cls, item_id, item, **kwargs):
        """Update cart.

        Update cart item.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_item(item_id, item, async=True)
        >>> result = thread.get()

        :param async bool
        :param str item_id: Item ID to update. (required)
        :param LineItem item: Line item to update. (required)
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_item_with_http_info(item_id, item, **kwargs)
        else:
            (data) = cls._update_item_with_http_info(item_id, item, **kwargs)
            return data

    @classmethod
    def _update_item_with_http_info(cls, item_id, item, **kwargs):
        """Update cart.

        Update cart item.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_item_with_http_info(item_id, item, async=True)
        >>> result = thread.get()

        :param async bool
        :param str item_id: Item ID to update. (required)
        :param LineItem item: Line item to update. (required)
        :return: ShoppingCart
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_id', 'item']
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
        # verify the required parameter 'item_id' is set
        if ('item_id' not in params or
                params['item_id'] is None):
            raise ValueError("Missing the required parameter `item_id` when calling `update_item`")
        # verify the required parameter 'item' is set
        if ('item' not in params or
                params['item'] is None):
            raise ValueError("Missing the required parameter `item` when calling `update_item`")

        collection_formats = {}

        path_params = {}
        if 'item_id' in params:
            path_params['itemId'] = params['item_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'item' in params:
            body_params = params['item']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/shoppingCarts/{itemId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShoppingCart',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
