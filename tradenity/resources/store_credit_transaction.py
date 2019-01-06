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


class StoreCreditTransaction(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'status': 'str',
        'type': 'str',
        'store_credit': 'StoreCredit'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'status': 'status',
        'type': 'type',
        'store_credit': 'storeCredit'
    }

    api_client = None

    def __init__(self, id=None, meta=None, status=None, type=None, store_credit=None):
        """StoreCreditTransaction - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._status = None
        self._type = None
        self._store_credit = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.status = status
        self.type = type
        self.store_credit = store_credit

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
        """Gets the meta of this StoreCreditTransaction.


        :return: The meta of this StoreCreditTransaction.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this StoreCreditTransaction.


        :param meta: The meta of this StoreCreditTransaction.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def status(self):
        """Gets the status of this StoreCreditTransaction.


        :return: The status of this StoreCreditTransaction.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StoreCreditTransaction.


        :param status: The status of this StoreCreditTransaction.
        :type: str
        """
        allowed_values = ["completed", "pending", "failed"]
        if status is not None and status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this StoreCreditTransaction.


        :return: The type of this StoreCreditTransaction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StoreCreditTransaction.


        :param type: The type of this StoreCreditTransaction.
        :type: str
        """
        allowed_values = ["payment", "refund"]
        if type is not None and type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def store_credit(self):
        """Gets the store_credit of this StoreCreditTransaction.


        :return: The store_credit of this StoreCreditTransaction.
        :rtype: StoreCredit
        """
        return self._store_credit

    @store_credit.setter
    def store_credit(self, store_credit):
        """Sets the store_credit of this StoreCreditTransaction.


        :param store_credit: The store_credit of this StoreCreditTransaction.
        :type: StoreCredit
        """

        self._store_credit = store_credit

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
        if issubclass(StoreCreditTransaction, dict):
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
        if not isinstance(other, StoreCreditTransaction):
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
        return cls.list_all_store_credit_transactions()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_store_credit_transactions(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_store_credit_transactions(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_store_credit_transaction_by_id(id)

    def create(self):
        new_instance = self.create_store_credit_transaction(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_store_credit_transaction_by_id(self.id, self)

    def delete(self):
        return self.delete_store_credit_transaction_by_id(self.id)



    @classmethod
    def create_store_credit_transaction(cls, store_credit_transaction, **kwargs):
        """Create StoreCreditTransaction

        Create a new StoreCreditTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_store_credit_transaction(store_credit_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param StoreCreditTransaction store_credit_transaction: Attributes of storeCreditTransaction to create (required)
        :return: StoreCreditTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_store_credit_transaction_with_http_info(store_credit_transaction, **kwargs)
        else:
            (data) = cls._create_store_credit_transaction_with_http_info(store_credit_transaction, **kwargs)
            return data

    @classmethod
    def _create_store_credit_transaction_with_http_info(cls, store_credit_transaction, **kwargs):
        """Create StoreCreditTransaction

        Create a new StoreCreditTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_store_credit_transaction_with_http_info(store_credit_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param StoreCreditTransaction store_credit_transaction: Attributes of storeCreditTransaction to create (required)
        :return: StoreCreditTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit_transaction']
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
        # verify the required parameter 'store_credit_transaction' is set
        if ('store_credit_transaction' not in params or
                params['store_credit_transaction'] is None):
            raise ValueError("Missing the required parameter `store_credit_transaction` when calling `create_store_credit_transaction`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'store_credit_transaction' in params:
            body_params = params['store_credit_transaction']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/storeCreditTransactions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreCreditTransaction',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_store_credit_transaction_by_id(cls, store_credit_transaction_id, **kwargs):
        """Delete StoreCreditTransaction

        Delete an instance of StoreCreditTransaction by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_store_credit_transaction_by_id(store_credit_transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_transaction_id: ID of storeCreditTransaction to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, **kwargs)
        else:
            (data) = cls._delete_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, **kwargs)
            return data

    @classmethod
    def _delete_store_credit_transaction_by_id_with_http_info(cls, store_credit_transaction_id, **kwargs):
        """Delete StoreCreditTransaction

        Delete an instance of StoreCreditTransaction by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_transaction_id: ID of storeCreditTransaction to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit_transaction_id']
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
        # verify the required parameter 'store_credit_transaction_id' is set
        if ('store_credit_transaction_id' not in params or
                params['store_credit_transaction_id'] is None):
            raise ValueError("Missing the required parameter `store_credit_transaction_id` when calling `delete_store_credit_transaction_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_credit_transaction_id' in params:
            path_params['storeCreditTransactionId'] = params['store_credit_transaction_id']


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
            '/storeCreditTransactions/{storeCreditTransactionId}', 'DELETE',
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
    def get_store_credit_transaction_by_id(cls, store_credit_transaction_id, **kwargs):
        """Find StoreCreditTransaction

        Return single instance of StoreCreditTransaction by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_store_credit_transaction_by_id(store_credit_transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_transaction_id: ID of storeCreditTransaction to return (required)
        :return: StoreCreditTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, **kwargs)
        else:
            (data) = cls._get_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, **kwargs)
            return data

    @classmethod
    def _get_store_credit_transaction_by_id_with_http_info(cls, store_credit_transaction_id, **kwargs):
        """Find StoreCreditTransaction

        Return single instance of StoreCreditTransaction by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_transaction_id: ID of storeCreditTransaction to return (required)
        :return: StoreCreditTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit_transaction_id']
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
        # verify the required parameter 'store_credit_transaction_id' is set
        if ('store_credit_transaction_id' not in params or
                params['store_credit_transaction_id'] is None):
            raise ValueError("Missing the required parameter `store_credit_transaction_id` when calling `get_store_credit_transaction_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_credit_transaction_id' in params:
            path_params['storeCreditTransactionId'] = params['store_credit_transaction_id']


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
            '/storeCreditTransactions/{storeCreditTransactionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreCreditTransaction',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_store_credit_transactions(cls, **kwargs):
        """List StoreCreditTransactions

        Return a list of StoreCreditTransactions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_store_credit_transactions(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[StoreCreditTransaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_store_credit_transactions_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_store_credit_transactions_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_store_credit_transactions_with_http_info(cls, **kwargs):
        """List StoreCreditTransactions

        Return a list of StoreCreditTransactions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_store_credit_transactions_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[StoreCreditTransaction]
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
            '/storeCreditTransactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[StoreCreditTransaction]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_store_credit_transaction_by_id(cls, store_credit_transaction_id, store_credit_transaction, **kwargs):
        """Replace StoreCreditTransaction

        Replace all attributes of StoreCreditTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_store_credit_transaction_by_id(store_credit_transaction_id, store_credit_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_transaction_id: ID of storeCreditTransaction to replace (required)
        :param StoreCreditTransaction store_credit_transaction: Attributes of storeCreditTransaction to replace (required)
        :return: StoreCreditTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, store_credit_transaction, **kwargs)
        else:
            (data) = cls._replace_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, store_credit_transaction, **kwargs)
            return data

    @classmethod
    def _replace_store_credit_transaction_by_id_with_http_info(cls, store_credit_transaction_id, store_credit_transaction, **kwargs):
        """Replace StoreCreditTransaction

        Replace all attributes of StoreCreditTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, store_credit_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_transaction_id: ID of storeCreditTransaction to replace (required)
        :param StoreCreditTransaction store_credit_transaction: Attributes of storeCreditTransaction to replace (required)
        :return: StoreCreditTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit_transaction_id', 'store_credit_transaction']
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
        # verify the required parameter 'store_credit_transaction_id' is set
        if ('store_credit_transaction_id' not in params or
                params['store_credit_transaction_id'] is None):
            raise ValueError("Missing the required parameter `store_credit_transaction_id` when calling `replace_store_credit_transaction_by_id`")
        # verify the required parameter 'store_credit_transaction' is set
        if ('store_credit_transaction' not in params or
                params['store_credit_transaction'] is None):
            raise ValueError("Missing the required parameter `store_credit_transaction` when calling `replace_store_credit_transaction_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_credit_transaction_id' in params:
            path_params['storeCreditTransactionId'] = params['store_credit_transaction_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'store_credit_transaction' in params:
            body_params = params['store_credit_transaction']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/storeCreditTransactions/{storeCreditTransactionId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreCreditTransaction',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_store_credit_transaction_by_id(cls, store_credit_transaction_id, store_credit_transaction, **kwargs):
        """Update StoreCreditTransaction

        Update attributes of StoreCreditTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_store_credit_transaction_by_id(store_credit_transaction_id, store_credit_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_transaction_id: ID of storeCreditTransaction to update. (required)
        :param StoreCreditTransaction store_credit_transaction: Attributes of storeCreditTransaction to update. (required)
        :return: StoreCreditTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, store_credit_transaction, **kwargs)
        else:
            (data) = cls._update_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, store_credit_transaction, **kwargs)
            return data

    @classmethod
    def _update_store_credit_transaction_by_id_with_http_info(cls, store_credit_transaction_id, store_credit_transaction, **kwargs):
        """Update StoreCreditTransaction

        Update attributes of StoreCreditTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_store_credit_transaction_by_id_with_http_info(store_credit_transaction_id, store_credit_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_credit_transaction_id: ID of storeCreditTransaction to update. (required)
        :param StoreCreditTransaction store_credit_transaction: Attributes of storeCreditTransaction to update. (required)
        :return: StoreCreditTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_credit_transaction_id', 'store_credit_transaction']
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
        # verify the required parameter 'store_credit_transaction_id' is set
        if ('store_credit_transaction_id' not in params or
                params['store_credit_transaction_id'] is None):
            raise ValueError("Missing the required parameter `store_credit_transaction_id` when calling `update_store_credit_transaction_by_id`")
        # verify the required parameter 'store_credit_transaction' is set
        if ('store_credit_transaction' not in params or
                params['store_credit_transaction'] is None):
            raise ValueError("Missing the required parameter `store_credit_transaction` when calling `update_store_credit_transaction_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_credit_transaction_id' in params:
            path_params['storeCreditTransactionId'] = params['store_credit_transaction_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'store_credit_transaction' in params:
            body_params = params['store_credit_transaction']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/storeCreditTransactions/{storeCreditTransactionId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreCreditTransaction',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
