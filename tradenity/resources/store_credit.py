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


class StoreCredit(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'amount': 'int',
        'customer': 'Customer',
        'currency': 'Currency',
        'transactions': 'list[Transaction]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'amount': 'amount',
        'customer': 'customer',
        'currency': 'currency',
        'transactions': 'transactions'
    }

    api_client = None

    def __init__(self, id=None, meta=None, amount=None, customer=None, currency=None, transactions=None):
        """StoreCredit - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._amount = None
        self._customer = None
        self._currency = None
        self._transactions = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        if amount is not None:
            self.amount = amount
        self.customer = customer
        self.currency = currency
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
        """Gets the meta of this StoreCredit.


        :return: The meta of this StoreCredit.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this StoreCredit.


        :param meta: The meta of this StoreCredit.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def amount(self):
        """Gets the amount of this StoreCredit.


        :return: The amount of this StoreCredit.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this StoreCredit.


        :param amount: The amount of this StoreCredit.
        :type: int
        """

        self._amount = amount

    @property
    def customer(self):
        """Gets the customer of this StoreCredit.


        :return: The customer of this StoreCredit.
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this StoreCredit.


        :param customer: The customer of this StoreCredit.
        :type: Customer
        """

        self._customer = customer

    @property
    def currency(self):
        """Gets the currency of this StoreCredit.


        :return: The currency of this StoreCredit.
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this StoreCredit.


        :param currency: The currency of this StoreCredit.
        :type: Currency
        """

        self._currency = currency

    @property
    def transactions(self):
        """Gets the transactions of this StoreCredit.


        :return: The transactions of this StoreCredit.
        :rtype: list[Transaction]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this StoreCredit.


        :param transactions: The transactions of this StoreCredit.
        :type: list[Transaction]
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
        if issubclass(StoreCredit, dict):
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
        if not isinstance(other, StoreCredit):
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
        return cls.list_all_store_credits(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_store_credits(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_store_credits(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_store_credit_by_id(id)

    def create(self):
        new_instance = self.create_store_credit(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_store_credit_by_id(self.id, self)

    def delete(self):
        return self.delete_store_credit_by_id(self.id)



    @classmethod
    def create_store_credit(cls, store_credit, **kwargs):
        """Create StoreCredit

        Create a new StoreCredit
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_store_credit(store_credit, async=True)
        >>> result = thread.get()

        :param async bool
        :param StoreCredit store_credit: Attributes of storeCredit to create (required)
        :return: StoreCredit
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_store_credit_with_http_info(store_credit, **kwargs)
        else:
            (data) = cls._create_store_credit_with_http_info(store_credit, **kwargs)
            return data

    @classmethod
    def _create_store_credit_with_http_info(cls, store_credit, **kwargs):
        """Create StoreCredit

        Create a new StoreCredit
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_store_credit_with_http_info(store_credit, async=True)
        >>> result = thread.get()

        :param async bool
        :param StoreCredit store_credit: Attributes of storeCredit to create (required)
        :return: StoreCredit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit']
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
        # verify the required parameter 'store_credit' is set
        if ('store_credit' not in params or
                params['store_credit'] is None):
            raise ValueError("Missing the required parameter `store_credit` when calling `create_store_credit`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'store_credit' in params:
            body_params = params['store_credit']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/storeCredits', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreCredit',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_store_credit_by_id(cls, store_credit_id, **kwargs):
        """Delete StoreCredit

        Delete an instance of StoreCredit by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_store_credit_by_id(store_credit_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_id: ID of storeCredit to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_store_credit_by_id_with_http_info(store_credit_id, **kwargs)
        else:
            (data) = cls._delete_store_credit_by_id_with_http_info(store_credit_id, **kwargs)
            return data

    @classmethod
    def _delete_store_credit_by_id_with_http_info(cls, store_credit_id, **kwargs):
        """Delete StoreCredit

        Delete an instance of StoreCredit by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_store_credit_by_id_with_http_info(store_credit_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_id: ID of storeCredit to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit_id']
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
        # verify the required parameter 'store_credit_id' is set
        if ('store_credit_id' not in params or
                params['store_credit_id'] is None):
            raise ValueError("Missing the required parameter `store_credit_id` when calling `delete_store_credit_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_credit_id' in params:
            path_params['storeCreditId'] = params['store_credit_id']


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
            '/storeCredits/{storeCreditId}', 'DELETE',
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
    def get_store_credit_by_id(cls, store_credit_id, **kwargs):
        """Find StoreCredit

        Return single instance of StoreCredit by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_store_credit_by_id(store_credit_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_id: ID of storeCredit to return (required)
        :return: StoreCredit
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_store_credit_by_id_with_http_info(store_credit_id, **kwargs)
        else:
            (data) = cls._get_store_credit_by_id_with_http_info(store_credit_id, **kwargs)
            return data

    @classmethod
    def _get_store_credit_by_id_with_http_info(cls, store_credit_id, **kwargs):
        """Find StoreCredit

        Return single instance of StoreCredit by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_store_credit_by_id_with_http_info(store_credit_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_id: ID of storeCredit to return (required)
        :return: StoreCredit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit_id']
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
        # verify the required parameter 'store_credit_id' is set
        if ('store_credit_id' not in params or
                params['store_credit_id'] is None):
            raise ValueError("Missing the required parameter `store_credit_id` when calling `get_store_credit_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_credit_id' in params:
            path_params['storeCreditId'] = params['store_credit_id']


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
            '/storeCredits/{storeCreditId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreCredit',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_store_credits(cls, **kwargs):
        """List StoreCredits

        Return a list of StoreCredits
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_store_credits(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[StoreCredit]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_store_credits_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_store_credits_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_store_credits_with_http_info(cls, **kwargs):
        """List StoreCredits

        Return a list of StoreCredits
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_store_credits_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[StoreCredit]
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
            '/storeCredits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[StoreCredit]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_store_credit_by_id(cls, store_credit_id, store_credit, **kwargs):
        """Replace StoreCredit

        Replace all attributes of StoreCredit
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_store_credit_by_id(store_credit_id, store_credit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_id: ID of storeCredit to replace (required)
        :param StoreCredit store_credit: Attributes of storeCredit to replace (required)
        :return: StoreCredit
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_store_credit_by_id_with_http_info(store_credit_id, store_credit, **kwargs)
        else:
            (data) = cls._replace_store_credit_by_id_with_http_info(store_credit_id, store_credit, **kwargs)
            return data

    @classmethod
    def _replace_store_credit_by_id_with_http_info(cls, store_credit_id, store_credit, **kwargs):
        """Replace StoreCredit

        Replace all attributes of StoreCredit
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_store_credit_by_id_with_http_info(store_credit_id, store_credit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_id: ID of storeCredit to replace (required)
        :param StoreCredit store_credit: Attributes of storeCredit to replace (required)
        :return: StoreCredit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit_id', 'store_credit']
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
        # verify the required parameter 'store_credit_id' is set
        if ('store_credit_id' not in params or
                params['store_credit_id'] is None):
            raise ValueError("Missing the required parameter `store_credit_id` when calling `replace_store_credit_by_id`")
        # verify the required parameter 'store_credit' is set
        if ('store_credit' not in params or
                params['store_credit'] is None):
            raise ValueError("Missing the required parameter `store_credit` when calling `replace_store_credit_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_credit_id' in params:
            path_params['storeCreditId'] = params['store_credit_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'store_credit' in params:
            body_params = params['store_credit']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/storeCredits/{storeCreditId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreCredit',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_store_credit_by_id(cls, store_credit_id, store_credit, **kwargs):
        """Update StoreCredit

        Update attributes of StoreCredit
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_store_credit_by_id(store_credit_id, store_credit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_id: ID of storeCredit to update. (required)
        :param StoreCredit store_credit: Attributes of storeCredit to update. (required)
        :return: StoreCredit
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_store_credit_by_id_with_http_info(store_credit_id, store_credit, **kwargs)
        else:
            (data) = cls._update_store_credit_by_id_with_http_info(store_credit_id, store_credit, **kwargs)
            return data

    @classmethod
    def _update_store_credit_by_id_with_http_info(cls, store_credit_id, store_credit, **kwargs):
        """Update StoreCredit

        Update attributes of StoreCredit
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_store_credit_by_id_with_http_info(store_credit_id, store_credit, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_id: ID of storeCredit to update. (required)
        :param StoreCredit store_credit: Attributes of storeCredit to update. (required)
        :return: StoreCredit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit_id', 'store_credit']
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
        # verify the required parameter 'store_credit_id' is set
        if ('store_credit_id' not in params or
                params['store_credit_id'] is None):
            raise ValueError("Missing the required parameter `store_credit_id` when calling `update_store_credit_by_id`")
        # verify the required parameter 'store_credit' is set
        if ('store_credit' not in params or
                params['store_credit'] is None):
            raise ValueError("Missing the required parameter `store_credit` when calling `update_store_credit_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_credit_id' in params:
            path_params['storeCreditId'] = params['store_credit_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'store_credit' in params:
            body_params = params['store_credit']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/storeCredits/{storeCreditId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreCredit',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
