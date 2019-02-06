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


class ReturnOperation(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'order': 'Order',
        'payment': 'Payment',
        'transaction': 'Transaction',
        'items': 'list[ReturnLineItem]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'order': 'order',
        'payment': 'payment',
        'transaction': 'transaction',
        'items': 'items'
    }

    api_client = None

    def __init__(self, id=None, meta=None, order=None, payment=None, transaction=None, items=None):
        """ReturnOperation - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._order = None
        self._payment = None
        self._transaction = None
        self._items = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.order = order
        self.payment = payment
        if transaction is not None:
            self.transaction = transaction
        if items is not None:
            self.items = items

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
        """Gets the meta of this ReturnOperation.


        :return: The meta of this ReturnOperation.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ReturnOperation.


        :param meta: The meta of this ReturnOperation.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def order(self):
        """Gets the order of this ReturnOperation.


        :return: The order of this ReturnOperation.
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ReturnOperation.


        :param order: The order of this ReturnOperation.
        :type: Order
        """

        self._order = order

    @property
    def payment(self):
        """Gets the payment of this ReturnOperation.


        :return: The payment of this ReturnOperation.
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this ReturnOperation.


        :param payment: The payment of this ReturnOperation.
        :type: Payment
        """

        self._payment = payment

    @property
    def transaction(self):
        """Gets the transaction of this ReturnOperation.


        :return: The transaction of this ReturnOperation.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ReturnOperation.


        :param transaction: The transaction of this ReturnOperation.
        :type: Transaction
        """

        self._transaction = transaction

    @property
    def items(self):
        """Gets the items of this ReturnOperation.


        :return: The items of this ReturnOperation.
        :rtype: list[ReturnLineItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ReturnOperation.


        :param items: The items of this ReturnOperation.
        :type: list[ReturnLineItem]
        """

        self._items = items

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
        if issubclass(ReturnOperation, dict):
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
        if not isinstance(other, ReturnOperation):
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
        return cls.list_all_return_operations(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_return_operations(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_return_operations(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_return_operation_by_id(id)

    def create(self):
        new_instance = self.create_return_operation(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_return_operation_by_id(self.id, self)

    def delete(self):
        return self.delete_return_operation_by_id(self.id)



    @classmethod
    def create_return_operation(cls, return_operation, **kwargs):
        """Create ReturnOperation

        Create a new ReturnOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_return_operation(return_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param ReturnOperation return_operation: Attributes of returnOperation to create (required)
        :return: ReturnOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_return_operation_with_http_info(return_operation, **kwargs)
        else:
            (data) = cls._create_return_operation_with_http_info(return_operation, **kwargs)
            return data

    @classmethod
    def _create_return_operation_with_http_info(cls, return_operation, **kwargs):
        """Create ReturnOperation

        Create a new ReturnOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_return_operation_with_http_info(return_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param ReturnOperation return_operation: Attributes of returnOperation to create (required)
        :return: ReturnOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['return_operation']
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
        # verify the required parameter 'return_operation' is set
        if ('return_operation' not in params or
                params['return_operation'] is None):
            raise ValueError("Missing the required parameter `return_operation` when calling `create_return_operation`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'return_operation' in params:
            body_params = params['return_operation']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/returnOperations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReturnOperation',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_return_operation_by_id(cls, return_operation_id, **kwargs):
        """Delete ReturnOperation

        Delete an instance of ReturnOperation by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_return_operation_by_id(return_operation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str return_operation_id: ID of returnOperation to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_return_operation_by_id_with_http_info(return_operation_id, **kwargs)
        else:
            (data) = cls._delete_return_operation_by_id_with_http_info(return_operation_id, **kwargs)
            return data

    @classmethod
    def _delete_return_operation_by_id_with_http_info(cls, return_operation_id, **kwargs):
        """Delete ReturnOperation

        Delete an instance of ReturnOperation by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_return_operation_by_id_with_http_info(return_operation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str return_operation_id: ID of returnOperation to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['return_operation_id']
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
        # verify the required parameter 'return_operation_id' is set
        if ('return_operation_id' not in params or
                params['return_operation_id'] is None):
            raise ValueError("Missing the required parameter `return_operation_id` when calling `delete_return_operation_by_id`")

        collection_formats = {}

        path_params = {}
        if 'return_operation_id' in params:
            path_params['returnOperationId'] = params['return_operation_id']


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
            '/returnOperations/{returnOperationId}', 'DELETE',
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
    def get_return_operation_by_id(cls, return_operation_id, **kwargs):
        """Find ReturnOperation

        Return single instance of ReturnOperation by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_return_operation_by_id(return_operation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str return_operation_id: ID of returnOperation to return (required)
        :return: ReturnOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_return_operation_by_id_with_http_info(return_operation_id, **kwargs)
        else:
            (data) = cls._get_return_operation_by_id_with_http_info(return_operation_id, **kwargs)
            return data

    @classmethod
    def _get_return_operation_by_id_with_http_info(cls, return_operation_id, **kwargs):
        """Find ReturnOperation

        Return single instance of ReturnOperation by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_return_operation_by_id_with_http_info(return_operation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str return_operation_id: ID of returnOperation to return (required)
        :return: ReturnOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['return_operation_id']
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
        # verify the required parameter 'return_operation_id' is set
        if ('return_operation_id' not in params or
                params['return_operation_id'] is None):
            raise ValueError("Missing the required parameter `return_operation_id` when calling `get_return_operation_by_id`")

        collection_formats = {}

        path_params = {}
        if 'return_operation_id' in params:
            path_params['returnOperationId'] = params['return_operation_id']


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
            '/returnOperations/{returnOperationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReturnOperation',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_return_operations(cls, **kwargs):
        """List ReturnOperations

        Return a list of ReturnOperations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_return_operations(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[ReturnOperation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_return_operations_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_return_operations_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_return_operations_with_http_info(cls, **kwargs):
        """List ReturnOperations

        Return a list of ReturnOperations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_return_operations_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[ReturnOperation]
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
            '/returnOperations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[ReturnOperation]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_return_operation_by_id(cls, return_operation_id, return_operation, **kwargs):
        """Replace ReturnOperation

        Replace all attributes of ReturnOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_return_operation_by_id(return_operation_id, return_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param str return_operation_id: ID of returnOperation to replace (required)
        :param ReturnOperation return_operation: Attributes of returnOperation to replace (required)
        :return: ReturnOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_return_operation_by_id_with_http_info(return_operation_id, return_operation, **kwargs)
        else:
            (data) = cls._replace_return_operation_by_id_with_http_info(return_operation_id, return_operation, **kwargs)
            return data

    @classmethod
    def _replace_return_operation_by_id_with_http_info(cls, return_operation_id, return_operation, **kwargs):
        """Replace ReturnOperation

        Replace all attributes of ReturnOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_return_operation_by_id_with_http_info(return_operation_id, return_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param str return_operation_id: ID of returnOperation to replace (required)
        :param ReturnOperation return_operation: Attributes of returnOperation to replace (required)
        :return: ReturnOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['return_operation_id', 'return_operation']
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
        # verify the required parameter 'return_operation_id' is set
        if ('return_operation_id' not in params or
                params['return_operation_id'] is None):
            raise ValueError("Missing the required parameter `return_operation_id` when calling `replace_return_operation_by_id`")
        # verify the required parameter 'return_operation' is set
        if ('return_operation' not in params or
                params['return_operation'] is None):
            raise ValueError("Missing the required parameter `return_operation` when calling `replace_return_operation_by_id`")

        collection_formats = {}

        path_params = {}
        if 'return_operation_id' in params:
            path_params['returnOperationId'] = params['return_operation_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'return_operation' in params:
            body_params = params['return_operation']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/returnOperations/{returnOperationId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReturnOperation',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_return_operation_by_id(cls, return_operation_id, return_operation, **kwargs):
        """Update ReturnOperation

        Update attributes of ReturnOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_return_operation_by_id(return_operation_id, return_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param str return_operation_id: ID of returnOperation to update. (required)
        :param ReturnOperation return_operation: Attributes of returnOperation to update. (required)
        :return: ReturnOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_return_operation_by_id_with_http_info(return_operation_id, return_operation, **kwargs)
        else:
            (data) = cls._update_return_operation_by_id_with_http_info(return_operation_id, return_operation, **kwargs)
            return data

    @classmethod
    def _update_return_operation_by_id_with_http_info(cls, return_operation_id, return_operation, **kwargs):
        """Update ReturnOperation

        Update attributes of ReturnOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_return_operation_by_id_with_http_info(return_operation_id, return_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param str return_operation_id: ID of returnOperation to update. (required)
        :param ReturnOperation return_operation: Attributes of returnOperation to update. (required)
        :return: ReturnOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['return_operation_id', 'return_operation']
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
        # verify the required parameter 'return_operation_id' is set
        if ('return_operation_id' not in params or
                params['return_operation_id'] is None):
            raise ValueError("Missing the required parameter `return_operation_id` when calling `update_return_operation_by_id`")
        # verify the required parameter 'return_operation' is set
        if ('return_operation' not in params or
                params['return_operation'] is None):
            raise ValueError("Missing the required parameter `return_operation` when calling `update_return_operation_by_id`")

        collection_formats = {}

        path_params = {}
        if 'return_operation_id' in params:
            path_params['returnOperationId'] = params['return_operation_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'return_operation' in params:
            body_params = params['return_operation']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/returnOperations/{returnOperationId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReturnOperation',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
