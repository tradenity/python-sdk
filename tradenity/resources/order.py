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


class Order(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'status': 'str',
        'subtotal': 'int',
        'total': 'int',
        'shipping_cost': 'int',
        'items_tax_amount': 'int',
        'total_items_discount': 'int',
        'purchase_day': 'date',
        'purchased_at': 'datetime',
        'completed_at': 'datetime',
        'customer': 'Customer',
        'shipping_address': 'Address',
        'billing_address': 'Address',
        'currency': 'Currency',
        'shipping_method': 'ShippingMethod',
        'promotions': 'list[Promotion]',
        'coupons': 'list[Coupon]',
        'items': 'list[OrderLineItem]',
        'payments': 'list[Payment]',
        'transactions': 'list[PaymentTransaction]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'status': 'status',
        'subtotal': 'subtotal',
        'total': 'total',
        'shipping_cost': 'shippingCost',
        'items_tax_amount': 'itemsTaxAmount',
        'total_items_discount': 'totalItemsDiscount',
        'purchase_day': 'purchaseDay',
        'purchased_at': 'purchasedAt',
        'completed_at': 'completedAt',
        'customer': 'customer',
        'shipping_address': 'shippingAddress',
        'billing_address': 'billingAddress',
        'currency': 'currency',
        'shipping_method': 'shippingMethod',
        'promotions': 'promotions',
        'coupons': 'coupons',
        'items': 'items',
        'payments': 'payments',
        'transactions': 'transactions'
    }

    api_client = None

    def __init__(self, id=None, meta=None, status=None, subtotal=None, total=None, shipping_cost=None, items_tax_amount=None, total_items_discount=None, purchase_day=None, purchased_at=None, completed_at=None, customer=None, shipping_address=None, billing_address=None, currency=None, shipping_method=None, promotions=None, coupons=None, items=None, payments=None, transactions=None):
        """Order - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._status = None
        self._subtotal = None
        self._total = None
        self._shipping_cost = None
        self._items_tax_amount = None
        self._total_items_discount = None
        self._purchase_day = None
        self._purchased_at = None
        self._completed_at = None
        self._customer = None
        self._shipping_address = None
        self._billing_address = None
        self._currency = None
        self._shipping_method = None
        self._promotions = None
        self._coupons = None
        self._items = None
        self._payments = None
        self._transactions = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.status = status
        self.subtotal = subtotal
        self.total = total
        if shipping_cost is not None:
            self.shipping_cost = shipping_cost
        if items_tax_amount is not None:
            self.items_tax_amount = items_tax_amount
        if total_items_discount is not None:
            self.total_items_discount = total_items_discount
        self.purchase_day = purchase_day
        self.purchased_at = purchased_at
        if completed_at is not None:
            self.completed_at = completed_at
        self.customer = customer
        if shipping_address is not None:
            self.shipping_address = shipping_address
        self.billing_address = billing_address
        self.currency = currency
        if shipping_method is not None:
            self.shipping_method = shipping_method
        if promotions is not None:
            self.promotions = promotions
        if coupons is not None:
            self.coupons = coupons
        if items is not None:
            self.items = items
        if payments is not None:
            self.payments = payments
        if transactions is not None:
            self.transactions = transactions

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
        """Gets the meta of this Order.


        :return: The meta of this Order.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Order.


        :param meta: The meta of this Order.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def status(self):
        """Gets the status of this Order.


        :return: The status of this Order.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Order.


        :param status: The status of this Order.
        :type: str
        """
        allowed_values = ["new", "inProgress", "pending", "shipping", "completed", "refunded"]
        if status is not None and status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def subtotal(self):
        """Gets the subtotal of this Order.


        :return: The subtotal of this Order.
        :rtype: int
        """
        return self._subtotal

    @subtotal.setter
    def subtotal(self, subtotal):
        """Sets the subtotal of this Order.


        :param subtotal: The subtotal of this Order.
        :type: int
        """

        self._subtotal = subtotal

    @property
    def total(self):
        """Gets the total of this Order.


        :return: The total of this Order.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Order.


        :param total: The total of this Order.
        :type: int
        """

        self._total = total

    @property
    def shipping_cost(self):
        """Gets the shipping_cost of this Order.


        :return: The shipping_cost of this Order.
        :rtype: int
        """
        return self._shipping_cost

    @shipping_cost.setter
    def shipping_cost(self, shipping_cost):
        """Sets the shipping_cost of this Order.


        :param shipping_cost: The shipping_cost of this Order.
        :type: int
        """

        self._shipping_cost = shipping_cost

    @property
    def items_tax_amount(self):
        """Gets the items_tax_amount of this Order.


        :return: The items_tax_amount of this Order.
        :rtype: int
        """
        return self._items_tax_amount

    @items_tax_amount.setter
    def items_tax_amount(self, items_tax_amount):
        """Sets the items_tax_amount of this Order.


        :param items_tax_amount: The items_tax_amount of this Order.
        :type: int
        """

        self._items_tax_amount = items_tax_amount

    @property
    def total_items_discount(self):
        """Gets the total_items_discount of this Order.


        :return: The total_items_discount of this Order.
        :rtype: int
        """
        return self._total_items_discount

    @total_items_discount.setter
    def total_items_discount(self, total_items_discount):
        """Sets the total_items_discount of this Order.


        :param total_items_discount: The total_items_discount of this Order.
        :type: int
        """

        self._total_items_discount = total_items_discount

    @property
    def purchase_day(self):
        """Gets the purchase_day of this Order.


        :return: The purchase_day of this Order.
        :rtype: date
        """
        return self._purchase_day

    @purchase_day.setter
    def purchase_day(self, purchase_day):
        """Sets the purchase_day of this Order.


        :param purchase_day: The purchase_day of this Order.
        :type: date
        """

        self._purchase_day = purchase_day

    @property
    def purchased_at(self):
        """Gets the purchased_at of this Order.


        :return: The purchased_at of this Order.
        :rtype: datetime
        """
        return self._purchased_at

    @purchased_at.setter
    def purchased_at(self, purchased_at):
        """Sets the purchased_at of this Order.


        :param purchased_at: The purchased_at of this Order.
        :type: datetime
        """

        self._purchased_at = purchased_at

    @property
    def completed_at(self):
        """Gets the completed_at of this Order.


        :return: The completed_at of this Order.
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this Order.


        :param completed_at: The completed_at of this Order.
        :type: datetime
        """

        self._completed_at = completed_at

    @property
    def customer(self):
        """Gets the customer of this Order.


        :return: The customer of this Order.
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Order.


        :param customer: The customer of this Order.
        :type: Customer
        """

        self._customer = customer

    @property
    def shipping_address(self):
        """Gets the shipping_address of this Order.


        :return: The shipping_address of this Order.
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Order.


        :param shipping_address: The shipping_address of this Order.
        :type: Address
        """

        self._shipping_address = shipping_address

    @property
    def billing_address(self):
        """Gets the billing_address of this Order.


        :return: The billing_address of this Order.
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this Order.


        :param billing_address: The billing_address of this Order.
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def currency(self):
        """Gets the currency of this Order.


        :return: The currency of this Order.
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Order.


        :param currency: The currency of this Order.
        :type: Currency
        """

        self._currency = currency

    @property
    def shipping_method(self):
        """Gets the shipping_method of this Order.


        :return: The shipping_method of this Order.
        :rtype: ShippingMethod
        """
        return self._shipping_method

    @shipping_method.setter
    def shipping_method(self, shipping_method):
        """Sets the shipping_method of this Order.


        :param shipping_method: The shipping_method of this Order.
        :type: ShippingMethod
        """

        self._shipping_method = shipping_method

    @property
    def promotions(self):
        """Gets the promotions of this Order.


        :return: The promotions of this Order.
        :rtype: list[Promotion]
        """
        return self._promotions

    @promotions.setter
    def promotions(self, promotions):
        """Sets the promotions of this Order.


        :param promotions: The promotions of this Order.
        :type: list[Promotion]
        """

        self._promotions = promotions

    @property
    def coupons(self):
        """Gets the coupons of this Order.


        :return: The coupons of this Order.
        :rtype: list[Coupon]
        """
        return self._coupons

    @coupons.setter
    def coupons(self, coupons):
        """Sets the coupons of this Order.


        :param coupons: The coupons of this Order.
        :type: list[Coupon]
        """

        self._coupons = coupons

    @property
    def items(self):
        """Gets the items of this Order.


        :return: The items of this Order.
        :rtype: list[OrderLineItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Order.


        :param items: The items of this Order.
        :type: list[OrderLineItem]
        """

        self._items = items

    @property
    def payments(self):
        """Gets the payments of this Order.


        :return: The payments of this Order.
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """Sets the payments of this Order.


        :param payments: The payments of this Order.
        :type: list[Payment]
        """

        self._payments = payments

    @property
    def transactions(self):
        """Gets the transactions of this Order.


        :return: The transactions of this Order.
        :rtype: list[PaymentTransaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this Order.


        :param transactions: The transactions of this Order.
        :type: list[PaymentTransaction]
        """

        self._transactions = transactions

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
        if issubclass(Order, dict):
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
        if not isinstance(other, Order):
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
        return cls.list_all_orders()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_orders(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_orders(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_order_by_id(id)

    def create(self):
        new_instance = self.create_order(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_order_by_id(self.id, self)

    def delete(self):
        return self.delete_order_by_id(self.id)



    @classmethod
    def create_order(cls, order, **kwargs):
        """Create Order

        Create a new Order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_order(order, async=True)
        >>> result = thread.get()

        :param async bool
        :param Order order: Attributes of order to create (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_order_with_http_info(order, **kwargs)
        else:
            (data) = cls._create_order_with_http_info(order, **kwargs)
            return data

    @classmethod
    def _create_order_with_http_info(cls, order, **kwargs):
        """Create Order

        Create a new Order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_order_with_http_info(order, async=True)
        >>> result = thread.get()

        :param async bool
        :param Order order: Attributes of order to create (required)
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
            raise ValueError("Missing the required parameter `order` when calling `create_order`")

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
            '/orders', 'POST',
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
    def delete_order_by_id(cls, order_id, **kwargs):
        """Delete Order

        Delete an instance of Order by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_order_by_id(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: ID of order to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_order_by_id_with_http_info(order_id, **kwargs)
        else:
            (data) = cls._delete_order_by_id_with_http_info(order_id, **kwargs)
            return data

    @classmethod
    def _delete_order_by_id_with_http_info(cls, order_id, **kwargs):
        """Delete Order

        Delete an instance of Order by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_order_by_id_with_http_info(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: ID of order to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']
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
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `delete_order_by_id`")

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']


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
            '/orders/{orderId}', 'DELETE',
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
    def get_order_by_id(cls, order_id, **kwargs):
        """Find Order

        Return single instance of Order by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_by_id(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: ID of order to return (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_order_by_id_with_http_info(order_id, **kwargs)
        else:
            (data) = cls._get_order_by_id_with_http_info(order_id, **kwargs)
            return data

    @classmethod
    def _get_order_by_id_with_http_info(cls, order_id, **kwargs):
        """Find Order

        Return single instance of Order by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_order_by_id_with_http_info(order_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: ID of order to return (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']
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
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `get_order_by_id`")

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']


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
            '/orders/{orderId}', 'GET',
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
    def list_all_orders(cls, **kwargs):
        """List Orders

        Return a list of Orders
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_orders(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Order]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_orders_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_orders_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_orders_with_http_info(cls, **kwargs):
        """List Orders

        Return a list of Orders
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_orders_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Order]
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
            '/orders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Order]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_order_by_id(cls, order_id, order, **kwargs):
        """Replace Order

        Replace all attributes of Order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_order_by_id(order_id, order, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: ID of order to replace (required)
        :param Order order: Attributes of order to replace (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_order_by_id_with_http_info(order_id, order, **kwargs)
        else:
            (data) = cls._replace_order_by_id_with_http_info(order_id, order, **kwargs)
            return data

    @classmethod
    def _replace_order_by_id_with_http_info(cls, order_id, order, **kwargs):
        """Replace Order

        Replace all attributes of Order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_order_by_id_with_http_info(order_id, order, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: ID of order to replace (required)
        :param Order order: Attributes of order to replace (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id', 'order']
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
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `replace_order_by_id`")
        # verify the required parameter 'order' is set
        if ('order' not in params or
                params['order'] is None):
            raise ValueError("Missing the required parameter `order` when calling `replace_order_by_id`")

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']


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
            '/orders/{orderId}', 'PUT',
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
    def update_order_by_id(cls, order_id, order, **kwargs):
        """Update Order

        Update attributes of Order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_order_by_id(order_id, order, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: ID of order to update. (required)
        :param Order order: Attributes of order to update. (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_order_by_id_with_http_info(order_id, order, **kwargs)
        else:
            (data) = cls._update_order_by_id_with_http_info(order_id, order, **kwargs)
            return data

    @classmethod
    def _update_order_by_id_with_http_info(cls, order_id, order, **kwargs):
        """Update Order

        Update attributes of Order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_order_by_id_with_http_info(order_id, order, async=True)
        >>> result = thread.get()

        :param async bool
        :param str order_id: ID of order to update. (required)
        :param Order order: Attributes of order to update. (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id', 'order']
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
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `update_order_by_id`")
        # verify the required parameter 'order' is set
        if ('order' not in params or
                params['order'] is None):
            raise ValueError("Missing the required parameter `order` when calling `update_order_by_id`")

        collection_formats = {}

        path_params = {}
        if 'order_id' in params:
            path_params['orderId'] = params['order_id']


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
            '/orders/{orderId}', 'PATCH',
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
