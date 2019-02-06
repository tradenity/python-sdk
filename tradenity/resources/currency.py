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


class Currency(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'code': 'str',
        'symbol': 'str',
        'decimal_point_placement': 'int',
        'smallest_unit': 'int',
        'status': 'str',
        'exchange_rate': 'float'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'code': 'code',
        'symbol': 'symbol',
        'decimal_point_placement': 'decimalPointPlacement',
        'smallest_unit': 'smallestUnit',
        'status': 'status',
        'exchange_rate': 'exchangeRate'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, code=None, symbol=None, decimal_point_placement=None, smallest_unit=None, status=None, exchange_rate=None):
        """Currency - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._code = None
        self._symbol = None
        self._decimal_point_placement = None
        self._smallest_unit = None
        self._status = None
        self._exchange_rate = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.code = code
        if symbol is not None:
            self.symbol = symbol
        if decimal_point_placement is not None:
            self.decimal_point_placement = decimal_point_placement
        if smallest_unit is not None:
            self.smallest_unit = smallest_unit
        self.status = status
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate

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
        """Gets the meta of this Currency.


        :return: The meta of this Currency.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Currency.


        :param meta: The meta of this Currency.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Currency.


        :return: The name of this Currency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Currency.


        :param name: The name of this Currency.
        :type: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this Currency.


        :return: The code of this Currency.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Currency.


        :param code: The code of this Currency.
        :type: str
        """

        self._code = code

    @property
    def symbol(self):
        """Gets the symbol of this Currency.


        :return: The symbol of this Currency.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Currency.


        :param symbol: The symbol of this Currency.
        :type: str
        """

        self._symbol = symbol

    @property
    def decimal_point_placement(self):
        """Gets the decimal_point_placement of this Currency.


        :return: The decimal_point_placement of this Currency.
        :rtype: int
        """
        return self._decimal_point_placement

    @decimal_point_placement.setter
    def decimal_point_placement(self, decimal_point_placement):
        """Sets the decimal_point_placement of this Currency.


        :param decimal_point_placement: The decimal_point_placement of this Currency.
        :type: int
        """

        self._decimal_point_placement = decimal_point_placement

    @property
    def smallest_unit(self):
        """Gets the smallest_unit of this Currency.


        :return: The smallest_unit of this Currency.
        :rtype: int
        """
        return self._smallest_unit

    @smallest_unit.setter
    def smallest_unit(self, smallest_unit):
        """Sets the smallest_unit of this Currency.


        :param smallest_unit: The smallest_unit of this Currency.
        :type: int
        """

        self._smallest_unit = smallest_unit

    @property
    def status(self):
        """Gets the status of this Currency.


        :return: The status of this Currency.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Currency.


        :param status: The status of this Currency.
        :type: str
        """
        allowed_values = ["enabled", "disabled"]
        if status is not None and status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this Currency.


        :return: The exchange_rate of this Currency.
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this Currency.


        :param exchange_rate: The exchange_rate of this Currency.
        :type: float
        """

        self._exchange_rate = exchange_rate

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
        if issubclass(Currency, dict):
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
        if not isinstance(other, Currency):
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
        return cls.list_all_currencies(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_currencies(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_currencies(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_currency_by_id(id)

    def create(self):
        new_instance = self.create_currency(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_currency_by_id(self.id, self)

    def delete(self):
        return self.delete_currency_by_id(self.id)



    @classmethod
    def create_currency(cls, currency, **kwargs):
        """Create Currency

        Create a new Currency
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_currency(currency, async=True)
        >>> result = thread.get()

        :param async bool
        :param Currency currency: Attributes of currency to create (required)
        :return: Currency
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_currency_with_http_info(currency, **kwargs)
        else:
            (data) = cls._create_currency_with_http_info(currency, **kwargs)
            return data

    @classmethod
    def _create_currency_with_http_info(cls, currency, **kwargs):
        """Create Currency

        Create a new Currency
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_currency_with_http_info(currency, async=True)
        >>> result = thread.get()

        :param async bool
        :param Currency currency: Attributes of currency to create (required)
        :return: Currency
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency']
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
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `create_currency`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'currency' in params:
            body_params = params['currency']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/currencies', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Currency',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_currency_by_id(cls, currency_id, **kwargs):
        """Delete Currency

        Delete an instance of Currency by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_currency_by_id(currency_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_id: ID of currency to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_currency_by_id_with_http_info(currency_id, **kwargs)
        else:
            (data) = cls._delete_currency_by_id_with_http_info(currency_id, **kwargs)
            return data

    @classmethod
    def _delete_currency_by_id_with_http_info(cls, currency_id, **kwargs):
        """Delete Currency

        Delete an instance of Currency by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_currency_by_id_with_http_info(currency_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_id: ID of currency to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_id']
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
        # verify the required parameter 'currency_id' is set
        if ('currency_id' not in params or
                params['currency_id'] is None):
            raise ValueError("Missing the required parameter `currency_id` when calling `delete_currency_by_id`")

        collection_formats = {}

        path_params = {}
        if 'currency_id' in params:
            path_params['currencyId'] = params['currency_id']


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
            '/currencies/{currencyId}', 'DELETE',
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
    def get_currency_by_id(cls, currency_id, **kwargs):
        """Find Currency

        Return single instance of Currency by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_currency_by_id(currency_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_id: ID of currency to return (required)
        :return: Currency
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_currency_by_id_with_http_info(currency_id, **kwargs)
        else:
            (data) = cls._get_currency_by_id_with_http_info(currency_id, **kwargs)
            return data

    @classmethod
    def _get_currency_by_id_with_http_info(cls, currency_id, **kwargs):
        """Find Currency

        Return single instance of Currency by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_currency_by_id_with_http_info(currency_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_id: ID of currency to return (required)
        :return: Currency
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_id']
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
        # verify the required parameter 'currency_id' is set
        if ('currency_id' not in params or
                params['currency_id'] is None):
            raise ValueError("Missing the required parameter `currency_id` when calling `get_currency_by_id`")

        collection_formats = {}

        path_params = {}
        if 'currency_id' in params:
            path_params['currencyId'] = params['currency_id']


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
            '/currencies/{currencyId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Currency',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_currencies(cls, **kwargs):
        """List Currencies

        Return a list of Currencies
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_currencies(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Currency]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_currencies_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_currencies_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_currencies_with_http_info(cls, **kwargs):
        """List Currencies

        Return a list of Currencies
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_currencies_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Currency]
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
            '/currencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Currency]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_currency_by_id(cls, currency_id, currency, **kwargs):
        """Replace Currency

        Replace all attributes of Currency
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_currency_by_id(currency_id, currency, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_id: ID of currency to replace (required)
        :param Currency currency: Attributes of currency to replace (required)
        :return: Currency
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_currency_by_id_with_http_info(currency_id, currency, **kwargs)
        else:
            (data) = cls._replace_currency_by_id_with_http_info(currency_id, currency, **kwargs)
            return data

    @classmethod
    def _replace_currency_by_id_with_http_info(cls, currency_id, currency, **kwargs):
        """Replace Currency

        Replace all attributes of Currency
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_currency_by_id_with_http_info(currency_id, currency, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_id: ID of currency to replace (required)
        :param Currency currency: Attributes of currency to replace (required)
        :return: Currency
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_id', 'currency']
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
        # verify the required parameter 'currency_id' is set
        if ('currency_id' not in params or
                params['currency_id'] is None):
            raise ValueError("Missing the required parameter `currency_id` when calling `replace_currency_by_id`")
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `replace_currency_by_id`")

        collection_formats = {}

        path_params = {}
        if 'currency_id' in params:
            path_params['currencyId'] = params['currency_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'currency' in params:
            body_params = params['currency']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/currencies/{currencyId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Currency',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_currency_by_id(cls, currency_id, currency, **kwargs):
        """Update Currency

        Update attributes of Currency
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_currency_by_id(currency_id, currency, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_id: ID of currency to update. (required)
        :param Currency currency: Attributes of currency to update. (required)
        :return: Currency
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_currency_by_id_with_http_info(currency_id, currency, **kwargs)
        else:
            (data) = cls._update_currency_by_id_with_http_info(currency_id, currency, **kwargs)
            return data

    @classmethod
    def _update_currency_by_id_with_http_info(cls, currency_id, currency, **kwargs):
        """Update Currency

        Update attributes of Currency
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_currency_by_id_with_http_info(currency_id, currency, async=True)
        >>> result = thread.get()

        :param async bool
        :param str currency_id: ID of currency to update. (required)
        :param Currency currency: Attributes of currency to update. (required)
        :return: Currency
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency_id', 'currency']
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
        # verify the required parameter 'currency_id' is set
        if ('currency_id' not in params or
                params['currency_id'] is None):
            raise ValueError("Missing the required parameter `currency_id` when calling `update_currency_by_id`")
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `update_currency_by_id`")

        collection_formats = {}

        path_params = {}
        if 'currency_id' in params:
            path_params['currencyId'] = params['currency_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'currency' in params:
            body_params = params['currency']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/currencies/{currencyId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Currency',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
