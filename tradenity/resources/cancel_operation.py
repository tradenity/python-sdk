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


class CancelOperation(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'order': 'Order',
        'payment': 'Payment',
        'transaction': 'Transaction'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'order': 'order',
        'payment': 'payment',
        'transaction': 'transaction'
    }

    api_client = None

    def __init__(self, id=None, meta=None, order=None, payment=None, transaction=None):
        """CancelOperation - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._order = None
        self._payment = None
        self._transaction = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.order = order
        self.payment = payment
        if transaction is not None:
            self.transaction = transaction

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
        """Gets the meta of this CancelOperation.


        :return: The meta of this CancelOperation.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this CancelOperation.


        :param meta: The meta of this CancelOperation.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def order(self):
        """Gets the order of this CancelOperation.


        :return: The order of this CancelOperation.
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CancelOperation.


        :param order: The order of this CancelOperation.
        :type: Order
        """

        self._order = order

    @property
    def payment(self):
        """Gets the payment of this CancelOperation.


        :return: The payment of this CancelOperation.
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this CancelOperation.


        :param payment: The payment of this CancelOperation.
        :type: Payment
        """

        self._payment = payment

    @property
    def transaction(self):
        """Gets the transaction of this CancelOperation.


        :return: The transaction of this CancelOperation.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this CancelOperation.


        :param transaction: The transaction of this CancelOperation.
        :type: Transaction
        """

        self._transaction = transaction

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
        if issubclass(CancelOperation, dict):
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
        if not isinstance(other, CancelOperation):
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
        return cls.list_all_cancel_operations(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_cancel_operations(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_cancel_operations(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_cancel_operation_by_id(id)

    def create(self):
        new_instance = self.create_cancel_operation(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_cancel_operation_by_id(self.id, self)

    def delete(self):
        return self.delete_cancel_operation_by_id(self.id)



    @classmethod
    def create_cancel_operation(cls, cancel_operation, **kwargs):
        """Create CancelOperation

        Create a new CancelOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_cancel_operation(cancel_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param CancelOperation cancel_operation: Attributes of cancelOperation to create (required)
        :return: CancelOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_cancel_operation_with_http_info(cancel_operation, **kwargs)
        else:
            (data) = cls._create_cancel_operation_with_http_info(cancel_operation, **kwargs)
            return data

    @classmethod
    def _create_cancel_operation_with_http_info(cls, cancel_operation, **kwargs):
        """Create CancelOperation

        Create a new CancelOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_cancel_operation_with_http_info(cancel_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param CancelOperation cancel_operation: Attributes of cancelOperation to create (required)
        :return: CancelOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cancel_operation']
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
        # verify the required parameter 'cancel_operation' is set
        if ('cancel_operation' not in params or
                params['cancel_operation'] is None):
            raise ValueError("Missing the required parameter `cancel_operation` when calling `create_cancel_operation`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cancel_operation' in params:
            body_params = params['cancel_operation']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/cancelOperations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOperation',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_cancel_operation_by_id(cls, cancel_operation_id, **kwargs):
        """Delete CancelOperation

        Delete an instance of CancelOperation by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_cancel_operation_by_id(cancel_operation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cancel_operation_id: ID of cancelOperation to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_cancel_operation_by_id_with_http_info(cancel_operation_id, **kwargs)
        else:
            (data) = cls._delete_cancel_operation_by_id_with_http_info(cancel_operation_id, **kwargs)
            return data

    @classmethod
    def _delete_cancel_operation_by_id_with_http_info(cls, cancel_operation_id, **kwargs):
        """Delete CancelOperation

        Delete an instance of CancelOperation by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_cancel_operation_by_id_with_http_info(cancel_operation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cancel_operation_id: ID of cancelOperation to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cancel_operation_id']
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
        # verify the required parameter 'cancel_operation_id' is set
        if ('cancel_operation_id' not in params or
                params['cancel_operation_id'] is None):
            raise ValueError("Missing the required parameter `cancel_operation_id` when calling `delete_cancel_operation_by_id`")

        collection_formats = {}

        path_params = {}
        if 'cancel_operation_id' in params:
            path_params['cancelOperationId'] = params['cancel_operation_id']


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
            '/cancelOperations/{cancelOperationId}', 'DELETE',
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
    def get_cancel_operation_by_id(cls, cancel_operation_id, **kwargs):
        """Find CancelOperation

        Return single instance of CancelOperation by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cancel_operation_by_id(cancel_operation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cancel_operation_id: ID of cancelOperation to return (required)
        :return: CancelOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_cancel_operation_by_id_with_http_info(cancel_operation_id, **kwargs)
        else:
            (data) = cls._get_cancel_operation_by_id_with_http_info(cancel_operation_id, **kwargs)
            return data

    @classmethod
    def _get_cancel_operation_by_id_with_http_info(cls, cancel_operation_id, **kwargs):
        """Find CancelOperation

        Return single instance of CancelOperation by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_cancel_operation_by_id_with_http_info(cancel_operation_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cancel_operation_id: ID of cancelOperation to return (required)
        :return: CancelOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cancel_operation_id']
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
        # verify the required parameter 'cancel_operation_id' is set
        if ('cancel_operation_id' not in params or
                params['cancel_operation_id'] is None):
            raise ValueError("Missing the required parameter `cancel_operation_id` when calling `get_cancel_operation_by_id`")

        collection_formats = {}

        path_params = {}
        if 'cancel_operation_id' in params:
            path_params['cancelOperationId'] = params['cancel_operation_id']


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
            '/cancelOperations/{cancelOperationId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOperation',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_cancel_operations(cls, **kwargs):
        """List CancelOperations

        Return a list of CancelOperations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_cancel_operations(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[CancelOperation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_cancel_operations_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_cancel_operations_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_cancel_operations_with_http_info(cls, **kwargs):
        """List CancelOperations

        Return a list of CancelOperations
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_cancel_operations_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[CancelOperation]
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
            '/cancelOperations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[CancelOperation]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_cancel_operation_by_id(cls, cancel_operation_id, cancel_operation, **kwargs):
        """Replace CancelOperation

        Replace all attributes of CancelOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_cancel_operation_by_id(cancel_operation_id, cancel_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cancel_operation_id: ID of cancelOperation to replace (required)
        :param CancelOperation cancel_operation: Attributes of cancelOperation to replace (required)
        :return: CancelOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_cancel_operation_by_id_with_http_info(cancel_operation_id, cancel_operation, **kwargs)
        else:
            (data) = cls._replace_cancel_operation_by_id_with_http_info(cancel_operation_id, cancel_operation, **kwargs)
            return data

    @classmethod
    def _replace_cancel_operation_by_id_with_http_info(cls, cancel_operation_id, cancel_operation, **kwargs):
        """Replace CancelOperation

        Replace all attributes of CancelOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_cancel_operation_by_id_with_http_info(cancel_operation_id, cancel_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cancel_operation_id: ID of cancelOperation to replace (required)
        :param CancelOperation cancel_operation: Attributes of cancelOperation to replace (required)
        :return: CancelOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cancel_operation_id', 'cancel_operation']
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
        # verify the required parameter 'cancel_operation_id' is set
        if ('cancel_operation_id' not in params or
                params['cancel_operation_id'] is None):
            raise ValueError("Missing the required parameter `cancel_operation_id` when calling `replace_cancel_operation_by_id`")
        # verify the required parameter 'cancel_operation' is set
        if ('cancel_operation' not in params or
                params['cancel_operation'] is None):
            raise ValueError("Missing the required parameter `cancel_operation` when calling `replace_cancel_operation_by_id`")

        collection_formats = {}

        path_params = {}
        if 'cancel_operation_id' in params:
            path_params['cancelOperationId'] = params['cancel_operation_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cancel_operation' in params:
            body_params = params['cancel_operation']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/cancelOperations/{cancelOperationId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOperation',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_cancel_operation_by_id(cls, cancel_operation_id, cancel_operation, **kwargs):
        """Update CancelOperation

        Update attributes of CancelOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_cancel_operation_by_id(cancel_operation_id, cancel_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cancel_operation_id: ID of cancelOperation to update. (required)
        :param CancelOperation cancel_operation: Attributes of cancelOperation to update. (required)
        :return: CancelOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_cancel_operation_by_id_with_http_info(cancel_operation_id, cancel_operation, **kwargs)
        else:
            (data) = cls._update_cancel_operation_by_id_with_http_info(cancel_operation_id, cancel_operation, **kwargs)
            return data

    @classmethod
    def _update_cancel_operation_by_id_with_http_info(cls, cancel_operation_id, cancel_operation, **kwargs):
        """Update CancelOperation

        Update attributes of CancelOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_cancel_operation_by_id_with_http_info(cancel_operation_id, cancel_operation, async=True)
        >>> result = thread.get()

        :param async bool
        :param str cancel_operation_id: ID of cancelOperation to update. (required)
        :param CancelOperation cancel_operation: Attributes of cancelOperation to update. (required)
        :return: CancelOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cancel_operation_id', 'cancel_operation']
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
        # verify the required parameter 'cancel_operation_id' is set
        if ('cancel_operation_id' not in params or
                params['cancel_operation_id'] is None):
            raise ValueError("Missing the required parameter `cancel_operation_id` when calling `update_cancel_operation_by_id`")
        # verify the required parameter 'cancel_operation' is set
        if ('cancel_operation' not in params or
                params['cancel_operation'] is None):
            raise ValueError("Missing the required parameter `cancel_operation` when calling `update_cancel_operation_by_id`")

        collection_formats = {}

        path_params = {}
        if 'cancel_operation_id' in params:
            path_params['cancelOperationId'] = params['cancel_operation_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cancel_operation' in params:
            body_params = params['cancel_operation']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/cancelOperations/{cancelOperationId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CancelOperation',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
