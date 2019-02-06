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


class RefundTransaction(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'status': 'str',
        'type': 'str',
        'refund_operation': 'RefundOperation'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'status': 'status',
        'type': 'type',
        'refund_operation': 'refundOperation'
    }

    api_client = None

    def __init__(self, id=None, meta=None, status=None, type=None, refund_operation=None):
        """RefundTransaction - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._status = None
        self._type = None
        self._refund_operation = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.status = status
        self.type = type
        self.refund_operation = refund_operation

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
        """Gets the meta of this RefundTransaction.


        :return: The meta of this RefundTransaction.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this RefundTransaction.


        :param meta: The meta of this RefundTransaction.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def status(self):
        """Gets the status of this RefundTransaction.


        :return: The status of this RefundTransaction.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RefundTransaction.


        :param status: The status of this RefundTransaction.
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
        """Gets the type of this RefundTransaction.


        :return: The type of this RefundTransaction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RefundTransaction.


        :param type: The type of this RefundTransaction.
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
    def refund_operation(self):
        """Gets the refund_operation of this RefundTransaction.


        :return: The refund_operation of this RefundTransaction.
        :rtype: RefundOperation
        """
        return self._refund_operation

    @refund_operation.setter
    def refund_operation(self, refund_operation):
        """Sets the refund_operation of this RefundTransaction.


        :param refund_operation: The refund_operation of this RefundTransaction.
        :type: RefundOperation
        """

        self._refund_operation = refund_operation

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
        if issubclass(RefundTransaction, dict):
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
        if not isinstance(other, RefundTransaction):
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
        return cls.list_all_refund_transactions(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_refund_transactions(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_refund_transactions(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_refund_transaction_by_id(id)

    def create(self):
        new_instance = self.create_refund_transaction(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_refund_transaction_by_id(self.id, self)

    def delete(self):
        return self.delete_refund_transaction_by_id(self.id)



    @classmethod
    def create_refund_transaction(cls, refund_transaction, **kwargs):
        """Create RefundTransaction

        Create a new RefundTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_refund_transaction(refund_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param RefundTransaction refund_transaction: Attributes of refundTransaction to create (required)
        :return: RefundTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_refund_transaction_with_http_info(refund_transaction, **kwargs)
        else:
            (data) = cls._create_refund_transaction_with_http_info(refund_transaction, **kwargs)
            return data

    @classmethod
    def _create_refund_transaction_with_http_info(cls, refund_transaction, **kwargs):
        """Create RefundTransaction

        Create a new RefundTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_refund_transaction_with_http_info(refund_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param RefundTransaction refund_transaction: Attributes of refundTransaction to create (required)
        :return: RefundTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refund_transaction']
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
        # verify the required parameter 'refund_transaction' is set
        if ('refund_transaction' not in params or
                params['refund_transaction'] is None):
            raise ValueError("Missing the required parameter `refund_transaction` when calling `create_refund_transaction`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'refund_transaction' in params:
            body_params = params['refund_transaction']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/refundTransactions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RefundTransaction',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_refund_transaction_by_id(cls, refund_transaction_id, **kwargs):
        """Delete RefundTransaction

        Delete an instance of RefundTransaction by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_refund_transaction_by_id(refund_transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str refund_transaction_id: ID of refundTransaction to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_refund_transaction_by_id_with_http_info(refund_transaction_id, **kwargs)
        else:
            (data) = cls._delete_refund_transaction_by_id_with_http_info(refund_transaction_id, **kwargs)
            return data

    @classmethod
    def _delete_refund_transaction_by_id_with_http_info(cls, refund_transaction_id, **kwargs):
        """Delete RefundTransaction

        Delete an instance of RefundTransaction by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_refund_transaction_by_id_with_http_info(refund_transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str refund_transaction_id: ID of refundTransaction to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refund_transaction_id']
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
        # verify the required parameter 'refund_transaction_id' is set
        if ('refund_transaction_id' not in params or
                params['refund_transaction_id'] is None):
            raise ValueError("Missing the required parameter `refund_transaction_id` when calling `delete_refund_transaction_by_id`")

        collection_formats = {}

        path_params = {}
        if 'refund_transaction_id' in params:
            path_params['refundTransactionId'] = params['refund_transaction_id']


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
            '/refundTransactions/{refundTransactionId}', 'DELETE',
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
    def get_refund_transaction_by_id(cls, refund_transaction_id, **kwargs):
        """Find RefundTransaction

        Return single instance of RefundTransaction by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_refund_transaction_by_id(refund_transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str refund_transaction_id: ID of refundTransaction to return (required)
        :return: RefundTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_refund_transaction_by_id_with_http_info(refund_transaction_id, **kwargs)
        else:
            (data) = cls._get_refund_transaction_by_id_with_http_info(refund_transaction_id, **kwargs)
            return data

    @classmethod
    def _get_refund_transaction_by_id_with_http_info(cls, refund_transaction_id, **kwargs):
        """Find RefundTransaction

        Return single instance of RefundTransaction by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_refund_transaction_by_id_with_http_info(refund_transaction_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str refund_transaction_id: ID of refundTransaction to return (required)
        :return: RefundTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refund_transaction_id']
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
        # verify the required parameter 'refund_transaction_id' is set
        if ('refund_transaction_id' not in params or
                params['refund_transaction_id'] is None):
            raise ValueError("Missing the required parameter `refund_transaction_id` when calling `get_refund_transaction_by_id`")

        collection_formats = {}

        path_params = {}
        if 'refund_transaction_id' in params:
            path_params['refundTransactionId'] = params['refund_transaction_id']


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
            '/refundTransactions/{refundTransactionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RefundTransaction',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_refund_transactions(cls, **kwargs):
        """List RefundTransactions

        Return a list of RefundTransactions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_refund_transactions(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[RefundTransaction]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_refund_transactions_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_refund_transactions_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_refund_transactions_with_http_info(cls, **kwargs):
        """List RefundTransactions

        Return a list of RefundTransactions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_refund_transactions_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[RefundTransaction]
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
            '/refundTransactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[RefundTransaction]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_refund_transaction_by_id(cls, refund_transaction_id, refund_transaction, **kwargs):
        """Replace RefundTransaction

        Replace all attributes of RefundTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_refund_transaction_by_id(refund_transaction_id, refund_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param str refund_transaction_id: ID of refundTransaction to replace (required)
        :param RefundTransaction refund_transaction: Attributes of refundTransaction to replace (required)
        :return: RefundTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_refund_transaction_by_id_with_http_info(refund_transaction_id, refund_transaction, **kwargs)
        else:
            (data) = cls._replace_refund_transaction_by_id_with_http_info(refund_transaction_id, refund_transaction, **kwargs)
            return data

    @classmethod
    def _replace_refund_transaction_by_id_with_http_info(cls, refund_transaction_id, refund_transaction, **kwargs):
        """Replace RefundTransaction

        Replace all attributes of RefundTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_refund_transaction_by_id_with_http_info(refund_transaction_id, refund_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param str refund_transaction_id: ID of refundTransaction to replace (required)
        :param RefundTransaction refund_transaction: Attributes of refundTransaction to replace (required)
        :return: RefundTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refund_transaction_id', 'refund_transaction']
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
        # verify the required parameter 'refund_transaction_id' is set
        if ('refund_transaction_id' not in params or
                params['refund_transaction_id'] is None):
            raise ValueError("Missing the required parameter `refund_transaction_id` when calling `replace_refund_transaction_by_id`")
        # verify the required parameter 'refund_transaction' is set
        if ('refund_transaction' not in params or
                params['refund_transaction'] is None):
            raise ValueError("Missing the required parameter `refund_transaction` when calling `replace_refund_transaction_by_id`")

        collection_formats = {}

        path_params = {}
        if 'refund_transaction_id' in params:
            path_params['refundTransactionId'] = params['refund_transaction_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'refund_transaction' in params:
            body_params = params['refund_transaction']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/refundTransactions/{refundTransactionId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RefundTransaction',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_refund_transaction_by_id(cls, refund_transaction_id, refund_transaction, **kwargs):
        """Update RefundTransaction

        Update attributes of RefundTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_refund_transaction_by_id(refund_transaction_id, refund_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param str refund_transaction_id: ID of refundTransaction to update. (required)
        :param RefundTransaction refund_transaction: Attributes of refundTransaction to update. (required)
        :return: RefundTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_refund_transaction_by_id_with_http_info(refund_transaction_id, refund_transaction, **kwargs)
        else:
            (data) = cls._update_refund_transaction_by_id_with_http_info(refund_transaction_id, refund_transaction, **kwargs)
            return data

    @classmethod
    def _update_refund_transaction_by_id_with_http_info(cls, refund_transaction_id, refund_transaction, **kwargs):
        """Update RefundTransaction

        Update attributes of RefundTransaction
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_refund_transaction_by_id_with_http_info(refund_transaction_id, refund_transaction, async=True)
        >>> result = thread.get()

        :param async bool
        :param str refund_transaction_id: ID of refundTransaction to update. (required)
        :param RefundTransaction refund_transaction: Attributes of refundTransaction to update. (required)
        :return: RefundTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refund_transaction_id', 'refund_transaction']
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
        # verify the required parameter 'refund_transaction_id' is set
        if ('refund_transaction_id' not in params or
                params['refund_transaction_id'] is None):
            raise ValueError("Missing the required parameter `refund_transaction_id` when calling `update_refund_transaction_by_id`")
        # verify the required parameter 'refund_transaction' is set
        if ('refund_transaction' not in params or
                params['refund_transaction'] is None):
            raise ValueError("Missing the required parameter `refund_transaction` when calling `update_refund_transaction_by_id`")

        collection_formats = {}

        path_params = {}
        if 'refund_transaction_id' in params:
            path_params['refundTransactionId'] = params['refund_transaction_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'refund_transaction' in params:
            body_params = params['refund_transaction']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/refundTransactions/{refundTransactionId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RefundTransaction',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
