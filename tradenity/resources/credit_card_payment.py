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


class CreditCardPayment(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'amount': 'int',
        'order': 'Order',
        'payment_source': 'PaymentSource',
        'currency': 'Currency',
        'status': 'str',
        'gateway': 'Gateway',
        'payment_mode': 'str',
        'gateway_operation_id': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'amount': 'amount',
        'order': 'order',
        'payment_source': 'paymentSource',
        'currency': 'currency',
        'status': 'status',
        'gateway': 'gateway',
        'payment_mode': 'paymentMode',
        'gateway_operation_id': 'gatewayOperationId'
    }

    api_client = None

    def __init__(self, id=None, meta=None, amount=None, order=None, payment_source=None, currency=None, status=None, gateway=None, payment_mode=None, gateway_operation_id=None):
        """CreditCardPayment - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._amount = None
        self._order = None
        self._payment_source = None
        self._currency = None
        self._status = None
        self._gateway = None
        self._payment_mode = None
        self._gateway_operation_id = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.amount = amount
        self.order = order
        self.payment_source = payment_source
        self.currency = currency
        self.status = status
        self.gateway = gateway
        if payment_mode is not None:
            self.payment_mode = payment_mode
        self.gateway_operation_id = gateway_operation_id

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
        """Gets the meta of this CreditCardPayment.


        :return: The meta of this CreditCardPayment.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this CreditCardPayment.


        :param meta: The meta of this CreditCardPayment.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def amount(self):
        """Gets the amount of this CreditCardPayment.


        :return: The amount of this CreditCardPayment.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CreditCardPayment.


        :param amount: The amount of this CreditCardPayment.
        :type: int
        """

        self._amount = amount

    @property
    def order(self):
        """Gets the order of this CreditCardPayment.


        :return: The order of this CreditCardPayment.
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CreditCardPayment.


        :param order: The order of this CreditCardPayment.
        :type: Order
        """

        self._order = order

    @property
    def payment_source(self):
        """Gets the payment_source of this CreditCardPayment.


        :return: The payment_source of this CreditCardPayment.
        :rtype: PaymentSource
        """
        return self._payment_source

    @payment_source.setter
    def payment_source(self, payment_source):
        """Sets the payment_source of this CreditCardPayment.


        :param payment_source: The payment_source of this CreditCardPayment.
        :type: PaymentSource
        """

        self._payment_source = payment_source

    @property
    def currency(self):
        """Gets the currency of this CreditCardPayment.


        :return: The currency of this CreditCardPayment.
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreditCardPayment.


        :param currency: The currency of this CreditCardPayment.
        :type: Currency
        """

        self._currency = currency

    @property
    def status(self):
        """Gets the status of this CreditCardPayment.


        :return: The status of this CreditCardPayment.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreditCardPayment.


        :param status: The status of this CreditCardPayment.
        :type: str
        """
        allowed_values = ["pending", "awaitingRetry", "successful", "failed"]
        if status is not None and status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def gateway(self):
        """Gets the gateway of this CreditCardPayment.


        :return: The gateway of this CreditCardPayment.
        :rtype: Gateway
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this CreditCardPayment.


        :param gateway: The gateway of this CreditCardPayment.
        :type: Gateway
        """

        self._gateway = gateway

    @property
    def payment_mode(self):
        """Gets the payment_mode of this CreditCardPayment.


        :return: The payment_mode of this CreditCardPayment.
        :rtype: str
        """
        return self._payment_mode

    @payment_mode.setter
    def payment_mode(self, payment_mode):
        """Sets the payment_mode of this CreditCardPayment.


        :param payment_mode: The payment_mode of this CreditCardPayment.
        :type: str
        """
        allowed_values = ["authorize", "capture"]
        if payment_mode is not None and payment_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_mode` ({0}), must be one of {1}"
                .format(payment_mode, allowed_values)
            )

        self._payment_mode = payment_mode

    @property
    def gateway_operation_id(self):
        """Gets the gateway_operation_id of this CreditCardPayment.


        :return: The gateway_operation_id of this CreditCardPayment.
        :rtype: str
        """
        return self._gateway_operation_id

    @gateway_operation_id.setter
    def gateway_operation_id(self, gateway_operation_id):
        """Sets the gateway_operation_id of this CreditCardPayment.


        :param gateway_operation_id: The gateway_operation_id of this CreditCardPayment.
        :type: str
        """

        self._gateway_operation_id = gateway_operation_id

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
        if issubclass(CreditCardPayment, dict):
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
        if not isinstance(other, CreditCardPayment):
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
        return cls.list_all_credit_card_payments()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_credit_card_payments(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_credit_card_payments(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_credit_card_payment_by_id(id)

    def create(self):
        new_instance = self.create_credit_card_payment(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_credit_card_payment_by_id(self.id, self)

    def delete(self):
        return self.delete_credit_card_payment_by_id(self.id)



    @classmethod
    def create_credit_card_payment(cls, credit_card_payment, **kwargs):
        """Create CreditCardPayment

        Create a new CreditCardPayment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_credit_card_payment(credit_card_payment, async=True)
        >>> result = thread.get()

        :param async bool
        :param CreditCardPayment credit_card_payment: Attributes of creditCardPayment to create (required)
        :return: CreditCardPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_credit_card_payment_with_http_info(credit_card_payment, **kwargs)
        else:
            (data) = cls._create_credit_card_payment_with_http_info(credit_card_payment, **kwargs)
            return data

    @classmethod
    def _create_credit_card_payment_with_http_info(cls, credit_card_payment, **kwargs):
        """Create CreditCardPayment

        Create a new CreditCardPayment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_credit_card_payment_with_http_info(credit_card_payment, async=True)
        >>> result = thread.get()

        :param async bool
        :param CreditCardPayment credit_card_payment: Attributes of creditCardPayment to create (required)
        :return: CreditCardPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_card_payment']
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
        # verify the required parameter 'credit_card_payment' is set
        if ('credit_card_payment' not in params or
                params['credit_card_payment'] is None):
            raise ValueError("Missing the required parameter `credit_card_payment` when calling `create_credit_card_payment`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'credit_card_payment' in params:
            body_params = params['credit_card_payment']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/creditCardPayments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreditCardPayment',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_credit_card_payment_by_id(cls, credit_card_payment_id, **kwargs):
        """Delete CreditCardPayment

        Delete an instance of CreditCardPayment by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_credit_card_payment_by_id(credit_card_payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str credit_card_payment_id: ID of creditCardPayment to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_credit_card_payment_by_id_with_http_info(credit_card_payment_id, **kwargs)
        else:
            (data) = cls._delete_credit_card_payment_by_id_with_http_info(credit_card_payment_id, **kwargs)
            return data

    @classmethod
    def _delete_credit_card_payment_by_id_with_http_info(cls, credit_card_payment_id, **kwargs):
        """Delete CreditCardPayment

        Delete an instance of CreditCardPayment by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_credit_card_payment_by_id_with_http_info(credit_card_payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str credit_card_payment_id: ID of creditCardPayment to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_card_payment_id']
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
        # verify the required parameter 'credit_card_payment_id' is set
        if ('credit_card_payment_id' not in params or
                params['credit_card_payment_id'] is None):
            raise ValueError("Missing the required parameter `credit_card_payment_id` when calling `delete_credit_card_payment_by_id`")

        collection_formats = {}

        path_params = {}
        if 'credit_card_payment_id' in params:
            path_params['creditCardPaymentId'] = params['credit_card_payment_id']


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
            '/creditCardPayments/{creditCardPaymentId}', 'DELETE',
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
    def get_credit_card_payment_by_id(cls, credit_card_payment_id, **kwargs):
        """Find CreditCardPayment

        Return single instance of CreditCardPayment by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_credit_card_payment_by_id(credit_card_payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str credit_card_payment_id: ID of creditCardPayment to return (required)
        :return: CreditCardPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_credit_card_payment_by_id_with_http_info(credit_card_payment_id, **kwargs)
        else:
            (data) = cls._get_credit_card_payment_by_id_with_http_info(credit_card_payment_id, **kwargs)
            return data

    @classmethod
    def _get_credit_card_payment_by_id_with_http_info(cls, credit_card_payment_id, **kwargs):
        """Find CreditCardPayment

        Return single instance of CreditCardPayment by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_credit_card_payment_by_id_with_http_info(credit_card_payment_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str credit_card_payment_id: ID of creditCardPayment to return (required)
        :return: CreditCardPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_card_payment_id']
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
        # verify the required parameter 'credit_card_payment_id' is set
        if ('credit_card_payment_id' not in params or
                params['credit_card_payment_id'] is None):
            raise ValueError("Missing the required parameter `credit_card_payment_id` when calling `get_credit_card_payment_by_id`")

        collection_formats = {}

        path_params = {}
        if 'credit_card_payment_id' in params:
            path_params['creditCardPaymentId'] = params['credit_card_payment_id']


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
            '/creditCardPayments/{creditCardPaymentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreditCardPayment',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_credit_card_payments(cls, **kwargs):
        """List CreditCardPayments

        Return a list of CreditCardPayments
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_credit_card_payments(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[CreditCardPayment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_credit_card_payments_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_credit_card_payments_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_credit_card_payments_with_http_info(cls, **kwargs):
        """List CreditCardPayments

        Return a list of CreditCardPayments
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_credit_card_payments_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[CreditCardPayment]
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
            '/creditCardPayments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[CreditCardPayment]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_credit_card_payment_by_id(cls, credit_card_payment_id, credit_card_payment, **kwargs):
        """Replace CreditCardPayment

        Replace all attributes of CreditCardPayment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_credit_card_payment_by_id(credit_card_payment_id, credit_card_payment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str credit_card_payment_id: ID of creditCardPayment to replace (required)
        :param CreditCardPayment credit_card_payment: Attributes of creditCardPayment to replace (required)
        :return: CreditCardPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_credit_card_payment_by_id_with_http_info(credit_card_payment_id, credit_card_payment, **kwargs)
        else:
            (data) = cls._replace_credit_card_payment_by_id_with_http_info(credit_card_payment_id, credit_card_payment, **kwargs)
            return data

    @classmethod
    def _replace_credit_card_payment_by_id_with_http_info(cls, credit_card_payment_id, credit_card_payment, **kwargs):
        """Replace CreditCardPayment

        Replace all attributes of CreditCardPayment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_credit_card_payment_by_id_with_http_info(credit_card_payment_id, credit_card_payment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str credit_card_payment_id: ID of creditCardPayment to replace (required)
        :param CreditCardPayment credit_card_payment: Attributes of creditCardPayment to replace (required)
        :return: CreditCardPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_card_payment_id', 'credit_card_payment']
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
        # verify the required parameter 'credit_card_payment_id' is set
        if ('credit_card_payment_id' not in params or
                params['credit_card_payment_id'] is None):
            raise ValueError("Missing the required parameter `credit_card_payment_id` when calling `replace_credit_card_payment_by_id`")
        # verify the required parameter 'credit_card_payment' is set
        if ('credit_card_payment' not in params or
                params['credit_card_payment'] is None):
            raise ValueError("Missing the required parameter `credit_card_payment` when calling `replace_credit_card_payment_by_id`")

        collection_formats = {}

        path_params = {}
        if 'credit_card_payment_id' in params:
            path_params['creditCardPaymentId'] = params['credit_card_payment_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'credit_card_payment' in params:
            body_params = params['credit_card_payment']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/creditCardPayments/{creditCardPaymentId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreditCardPayment',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_credit_card_payment_by_id(cls, credit_card_payment_id, credit_card_payment, **kwargs):
        """Update CreditCardPayment

        Update attributes of CreditCardPayment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_credit_card_payment_by_id(credit_card_payment_id, credit_card_payment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str credit_card_payment_id: ID of creditCardPayment to update. (required)
        :param CreditCardPayment credit_card_payment: Attributes of creditCardPayment to update. (required)
        :return: CreditCardPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_credit_card_payment_by_id_with_http_info(credit_card_payment_id, credit_card_payment, **kwargs)
        else:
            (data) = cls._update_credit_card_payment_by_id_with_http_info(credit_card_payment_id, credit_card_payment, **kwargs)
            return data

    @classmethod
    def _update_credit_card_payment_by_id_with_http_info(cls, credit_card_payment_id, credit_card_payment, **kwargs):
        """Update CreditCardPayment

        Update attributes of CreditCardPayment
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_credit_card_payment_by_id_with_http_info(credit_card_payment_id, credit_card_payment, async=True)
        >>> result = thread.get()

        :param async bool
        :param str credit_card_payment_id: ID of creditCardPayment to update. (required)
        :param CreditCardPayment credit_card_payment: Attributes of creditCardPayment to update. (required)
        :return: CreditCardPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credit_card_payment_id', 'credit_card_payment']
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
        # verify the required parameter 'credit_card_payment_id' is set
        if ('credit_card_payment_id' not in params or
                params['credit_card_payment_id'] is None):
            raise ValueError("Missing the required parameter `credit_card_payment_id` when calling `update_credit_card_payment_by_id`")
        # verify the required parameter 'credit_card_payment' is set
        if ('credit_card_payment' not in params or
                params['credit_card_payment'] is None):
            raise ValueError("Missing the required parameter `credit_card_payment` when calling `update_credit_card_payment_by_id`")

        collection_formats = {}

        path_params = {}
        if 'credit_card_payment_id' in params:
            path_params['creditCardPaymentId'] = params['credit_card_payment_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'credit_card_payment' in params:
            body_params = params['credit_card_payment']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/creditCardPayments/{creditCardPaymentId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreditCardPayment',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
