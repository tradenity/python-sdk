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


class StripeGateway(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'mode': 'str',
        'authorize_only': 'bool',
        'account_id': 'str',
        'status': 'str',
        'secret_key': 'str',
        'public_key': 'str',
        'test_secret_key': 'str',
        'test_public_key': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'mode': 'mode',
        'authorize_only': 'authorizeOnly',
        'account_id': 'accountId',
        'status': 'status',
        'secret_key': 'secretKey',
        'public_key': 'publicKey',
        'test_secret_key': 'testSecretKey',
        'test_public_key': 'testPublicKey'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, mode=None, authorize_only=None, account_id=None, status=None, secret_key=None, public_key=None, test_secret_key=None, test_public_key=None):
        """StripeGateway - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._mode = None
        self._authorize_only = None
        self._account_id = None
        self._status = None
        self._secret_key = None
        self._public_key = None
        self._test_secret_key = None
        self._test_public_key = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.mode = mode
        if authorize_only is not None:
            self.authorize_only = authorize_only
        if account_id is not None:
            self.account_id = account_id
        self.status = status
        if secret_key is not None:
            self.secret_key = secret_key
        if public_key is not None:
            self.public_key = public_key
        if test_secret_key is not None:
            self.test_secret_key = test_secret_key
        if test_public_key is not None:
            self.test_public_key = test_public_key

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
        """Gets the meta of this StripeGateway.


        :return: The meta of this StripeGateway.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this StripeGateway.


        :param meta: The meta of this StripeGateway.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this StripeGateway.


        :return: The name of this StripeGateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StripeGateway.


        :param name: The name of this StripeGateway.
        :type: str
        """

        self._name = name

    @property
    def mode(self):
        """Gets the mode of this StripeGateway.


        :return: The mode of this StripeGateway.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this StripeGateway.


        :param mode: The mode of this StripeGateway.
        :type: str
        """
        allowed_values = ["test", "live"]
        if mode is not None and mode not in allowed_values:
            raise ValueError(
                "Invalid value for `mode` ({0}), must be one of {1}"
                .format(mode, allowed_values)
            )

        self._mode = mode

    @property
    def authorize_only(self):
        """Gets the authorize_only of this StripeGateway.


        :return: The authorize_only of this StripeGateway.
        :rtype: bool
        """
        return self._authorize_only

    @authorize_only.setter
    def authorize_only(self, authorize_only):
        """Sets the authorize_only of this StripeGateway.


        :param authorize_only: The authorize_only of this StripeGateway.
        :type: bool
        """

        self._authorize_only = authorize_only

    @property
    def account_id(self):
        """Gets the account_id of this StripeGateway.


        :return: The account_id of this StripeGateway.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this StripeGateway.


        :param account_id: The account_id of this StripeGateway.
        :type: str
        """

        self._account_id = account_id

    @property
    def status(self):
        """Gets the status of this StripeGateway.


        :return: The status of this StripeGateway.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StripeGateway.


        :param status: The status of this StripeGateway.
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
    def secret_key(self):
        """Gets the secret_key of this StripeGateway.


        :return: The secret_key of this StripeGateway.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this StripeGateway.


        :param secret_key: The secret_key of this StripeGateway.
        :type: str
        """

        self._secret_key = secret_key

    @property
    def public_key(self):
        """Gets the public_key of this StripeGateway.


        :return: The public_key of this StripeGateway.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this StripeGateway.


        :param public_key: The public_key of this StripeGateway.
        :type: str
        """

        self._public_key = public_key

    @property
    def test_secret_key(self):
        """Gets the test_secret_key of this StripeGateway.


        :return: The test_secret_key of this StripeGateway.
        :rtype: str
        """
        return self._test_secret_key

    @test_secret_key.setter
    def test_secret_key(self, test_secret_key):
        """Sets the test_secret_key of this StripeGateway.


        :param test_secret_key: The test_secret_key of this StripeGateway.
        :type: str
        """

        self._test_secret_key = test_secret_key

    @property
    def test_public_key(self):
        """Gets the test_public_key of this StripeGateway.


        :return: The test_public_key of this StripeGateway.
        :rtype: str
        """
        return self._test_public_key

    @test_public_key.setter
    def test_public_key(self, test_public_key):
        """Sets the test_public_key of this StripeGateway.


        :param test_public_key: The test_public_key of this StripeGateway.
        :type: str
        """

        self._test_public_key = test_public_key

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
        if issubclass(StripeGateway, dict):
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
        if not isinstance(other, StripeGateway):
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
        return cls.list_all_stripe_gateways(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_stripe_gateways(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_stripe_gateways(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_stripe_gateway_by_id(id)

    def create(self):
        new_instance = self.create_stripe_gateway(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_stripe_gateway_by_id(self.id, self)

    def delete(self):
        return self.delete_stripe_gateway_by_id(self.id)



    @classmethod
    def create_stripe_gateway(cls, stripe_gateway, **kwargs):
        """Create StripeGateway

        Create a new StripeGateway
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_stripe_gateway(stripe_gateway, async=True)
        >>> result = thread.get()

        :param async bool
        :param StripeGateway stripe_gateway: Attributes of stripeGateway to create (required)
        :return: StripeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_stripe_gateway_with_http_info(stripe_gateway, **kwargs)
        else:
            (data) = cls._create_stripe_gateway_with_http_info(stripe_gateway, **kwargs)
            return data

    @classmethod
    def _create_stripe_gateway_with_http_info(cls, stripe_gateway, **kwargs):
        """Create StripeGateway

        Create a new StripeGateway
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_stripe_gateway_with_http_info(stripe_gateway, async=True)
        >>> result = thread.get()

        :param async bool
        :param StripeGateway stripe_gateway: Attributes of stripeGateway to create (required)
        :return: StripeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stripe_gateway']
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
        # verify the required parameter 'stripe_gateway' is set
        if ('stripe_gateway' not in params or
                params['stripe_gateway'] is None):
            raise ValueError("Missing the required parameter `stripe_gateway` when calling `create_stripe_gateway`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'stripe_gateway' in params:
            body_params = params['stripe_gateway']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/stripeGateways', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StripeGateway',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_stripe_gateway_by_id(cls, stripe_gateway_id, **kwargs):
        """Delete StripeGateway

        Delete an instance of StripeGateway by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_stripe_gateway_by_id(stripe_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str stripe_gateway_id: ID of stripeGateway to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_stripe_gateway_by_id_with_http_info(stripe_gateway_id, **kwargs)
        else:
            (data) = cls._delete_stripe_gateway_by_id_with_http_info(stripe_gateway_id, **kwargs)
            return data

    @classmethod
    def _delete_stripe_gateway_by_id_with_http_info(cls, stripe_gateway_id, **kwargs):
        """Delete StripeGateway

        Delete an instance of StripeGateway by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_stripe_gateway_by_id_with_http_info(stripe_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str stripe_gateway_id: ID of stripeGateway to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stripe_gateway_id']
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
        # verify the required parameter 'stripe_gateway_id' is set
        if ('stripe_gateway_id' not in params or
                params['stripe_gateway_id'] is None):
            raise ValueError("Missing the required parameter `stripe_gateway_id` when calling `delete_stripe_gateway_by_id`")

        collection_formats = {}

        path_params = {}
        if 'stripe_gateway_id' in params:
            path_params['stripeGatewayId'] = params['stripe_gateway_id']


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
            '/stripeGateways/{stripeGatewayId}', 'DELETE',
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
    def get_stripe_gateway_by_id(cls, stripe_gateway_id, **kwargs):
        """Find StripeGateway

        Return single instance of StripeGateway by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stripe_gateway_by_id(stripe_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str stripe_gateway_id: ID of stripeGateway to return (required)
        :return: StripeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_stripe_gateway_by_id_with_http_info(stripe_gateway_id, **kwargs)
        else:
            (data) = cls._get_stripe_gateway_by_id_with_http_info(stripe_gateway_id, **kwargs)
            return data

    @classmethod
    def _get_stripe_gateway_by_id_with_http_info(cls, stripe_gateway_id, **kwargs):
        """Find StripeGateway

        Return single instance of StripeGateway by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_stripe_gateway_by_id_with_http_info(stripe_gateway_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str stripe_gateway_id: ID of stripeGateway to return (required)
        :return: StripeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stripe_gateway_id']
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
        # verify the required parameter 'stripe_gateway_id' is set
        if ('stripe_gateway_id' not in params or
                params['stripe_gateway_id'] is None):
            raise ValueError("Missing the required parameter `stripe_gateway_id` when calling `get_stripe_gateway_by_id`")

        collection_formats = {}

        path_params = {}
        if 'stripe_gateway_id' in params:
            path_params['stripeGatewayId'] = params['stripe_gateway_id']


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
            '/stripeGateways/{stripeGatewayId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StripeGateway',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_stripe_gateways(cls, **kwargs):
        """List StripeGateways

        Return a list of StripeGateways
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_stripe_gateways(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[StripeGateway]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_stripe_gateways_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_stripe_gateways_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_stripe_gateways_with_http_info(cls, **kwargs):
        """List StripeGateways

        Return a list of StripeGateways
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_stripe_gateways_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[StripeGateway]
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
            '/stripeGateways', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[StripeGateway]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_stripe_gateway_by_id(cls, stripe_gateway_id, stripe_gateway, **kwargs):
        """Replace StripeGateway

        Replace all attributes of StripeGateway
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_stripe_gateway_by_id(stripe_gateway_id, stripe_gateway, async=True)
        >>> result = thread.get()

        :param async bool
        :param str stripe_gateway_id: ID of stripeGateway to replace (required)
        :param StripeGateway stripe_gateway: Attributes of stripeGateway to replace (required)
        :return: StripeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_stripe_gateway_by_id_with_http_info(stripe_gateway_id, stripe_gateway, **kwargs)
        else:
            (data) = cls._replace_stripe_gateway_by_id_with_http_info(stripe_gateway_id, stripe_gateway, **kwargs)
            return data

    @classmethod
    def _replace_stripe_gateway_by_id_with_http_info(cls, stripe_gateway_id, stripe_gateway, **kwargs):
        """Replace StripeGateway

        Replace all attributes of StripeGateway
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_stripe_gateway_by_id_with_http_info(stripe_gateway_id, stripe_gateway, async=True)
        >>> result = thread.get()

        :param async bool
        :param str stripe_gateway_id: ID of stripeGateway to replace (required)
        :param StripeGateway stripe_gateway: Attributes of stripeGateway to replace (required)
        :return: StripeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stripe_gateway_id', 'stripe_gateway']
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
        # verify the required parameter 'stripe_gateway_id' is set
        if ('stripe_gateway_id' not in params or
                params['stripe_gateway_id'] is None):
            raise ValueError("Missing the required parameter `stripe_gateway_id` when calling `replace_stripe_gateway_by_id`")
        # verify the required parameter 'stripe_gateway' is set
        if ('stripe_gateway' not in params or
                params['stripe_gateway'] is None):
            raise ValueError("Missing the required parameter `stripe_gateway` when calling `replace_stripe_gateway_by_id`")

        collection_formats = {}

        path_params = {}
        if 'stripe_gateway_id' in params:
            path_params['stripeGatewayId'] = params['stripe_gateway_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'stripe_gateway' in params:
            body_params = params['stripe_gateway']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/stripeGateways/{stripeGatewayId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StripeGateway',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_stripe_gateway_by_id(cls, stripe_gateway_id, stripe_gateway, **kwargs):
        """Update StripeGateway

        Update attributes of StripeGateway
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_stripe_gateway_by_id(stripe_gateway_id, stripe_gateway, async=True)
        >>> result = thread.get()

        :param async bool
        :param str stripe_gateway_id: ID of stripeGateway to update. (required)
        :param StripeGateway stripe_gateway: Attributes of stripeGateway to update. (required)
        :return: StripeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_stripe_gateway_by_id_with_http_info(stripe_gateway_id, stripe_gateway, **kwargs)
        else:
            (data) = cls._update_stripe_gateway_by_id_with_http_info(stripe_gateway_id, stripe_gateway, **kwargs)
            return data

    @classmethod
    def _update_stripe_gateway_by_id_with_http_info(cls, stripe_gateway_id, stripe_gateway, **kwargs):
        """Update StripeGateway

        Update attributes of StripeGateway
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_stripe_gateway_by_id_with_http_info(stripe_gateway_id, stripe_gateway, async=True)
        >>> result = thread.get()

        :param async bool
        :param str stripe_gateway_id: ID of stripeGateway to update. (required)
        :param StripeGateway stripe_gateway: Attributes of stripeGateway to update. (required)
        :return: StripeGateway
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stripe_gateway_id', 'stripe_gateway']
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
        # verify the required parameter 'stripe_gateway_id' is set
        if ('stripe_gateway_id' not in params or
                params['stripe_gateway_id'] is None):
            raise ValueError("Missing the required parameter `stripe_gateway_id` when calling `update_stripe_gateway_by_id`")
        # verify the required parameter 'stripe_gateway' is set
        if ('stripe_gateway' not in params or
                params['stripe_gateway'] is None):
            raise ValueError("Missing the required parameter `stripe_gateway` when calling `update_stripe_gateway_by_id`")

        collection_formats = {}

        path_params = {}
        if 'stripe_gateway_id' in params:
            path_params['stripeGatewayId'] = params['stripe_gateway_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'stripe_gateway' in params:
            body_params = params['stripe_gateway']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/stripeGateways/{stripeGatewayId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StripeGateway',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
