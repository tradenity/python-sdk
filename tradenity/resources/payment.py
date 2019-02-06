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


class Payment(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'amount': 'int',
        'order': 'Order',
        'payment_source': 'PaymentSource',
        'currency': 'Currency',
        'status': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'amount': 'amount',
        'order': 'order',
        'payment_source': 'paymentSource',
        'currency': 'currency',
        'status': 'status'
    }

    api_client = None

    def __init__(self, id=None, meta=None, amount=None, order=None, payment_source=None, currency=None, status=None):
        """Payment - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._amount = None
        self._order = None
        self._payment_source = None
        self._currency = None
        self._status = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.amount = amount
        self.order = order
        self.payment_source = payment_source
        self.currency = currency
        self.status = status

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
        """Gets the meta of this Payment.


        :return: The meta of this Payment.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Payment.


        :param meta: The meta of this Payment.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def amount(self):
        """Gets the amount of this Payment.


        :return: The amount of this Payment.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.


        :param amount: The amount of this Payment.
        :type: int
        """

        self._amount = amount

    @property
    def order(self):
        """Gets the order of this Payment.


        :return: The order of this Payment.
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this Payment.


        :param order: The order of this Payment.
        :type: Order
        """

        self._order = order

    @property
    def payment_source(self):
        """Gets the payment_source of this Payment.


        :return: The payment_source of this Payment.
        :rtype: PaymentSource
        """
        return self._payment_source

    @payment_source.setter
    def payment_source(self, payment_source):
        """Sets the payment_source of this Payment.


        :param payment_source: The payment_source of this Payment.
        :type: PaymentSource
        """

        self._payment_source = payment_source

    @property
    def currency(self):
        """Gets the currency of this Payment.


        :return: The currency of this Payment.
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Payment.


        :param currency: The currency of this Payment.
        :type: Currency
        """

        self._currency = currency

    @property
    def status(self):
        """Gets the status of this Payment.


        :return: The status of this Payment.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Payment.


        :param status: The status of this Payment.
        :type: str
        """
        allowed_values = ["pending", "awaitingRetry", "successful", "failed"]
        if status is not None and status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(Payment, dict):
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
        if not isinstance(other, Payment):
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
    def find_all(cls, **kwargs):
        return cls.list_all_payments(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_payments(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_payments(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def list_all_payments(cls, **kwargs):
        """List Payments

        Return a list of Payments
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_payments(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Payment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_payments_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_payments_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_payments_with_http_info(cls, **kwargs):
        """List Payments

        Return a list of Payments
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_payments_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Payment]
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
            '/payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Payment]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
