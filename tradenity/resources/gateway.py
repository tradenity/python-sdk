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


class Gateway(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'mode': 'str',
        'authorize_only': 'bool',
        'account_id': 'str',
        'status': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'mode': 'mode',
        'authorize_only': 'authorizeOnly',
        'account_id': 'accountId',
        'status': 'status'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, mode=None, authorize_only=None, account_id=None, status=None):
        """Gateway - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._mode = None
        self._authorize_only = None
        self._account_id = None
        self._status = None
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
        """Gets the meta of this Gateway.


        :return: The meta of this Gateway.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Gateway.


        :param meta: The meta of this Gateway.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Gateway.


        :return: The name of this Gateway.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Gateway.


        :param name: The name of this Gateway.
        :type: str
        """

        self._name = name

    @property
    def mode(self):
        """Gets the mode of this Gateway.


        :return: The mode of this Gateway.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Gateway.


        :param mode: The mode of this Gateway.
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
        """Gets the authorize_only of this Gateway.


        :return: The authorize_only of this Gateway.
        :rtype: bool
        """
        return self._authorize_only

    @authorize_only.setter
    def authorize_only(self, authorize_only):
        """Sets the authorize_only of this Gateway.


        :param authorize_only: The authorize_only of this Gateway.
        :type: bool
        """

        self._authorize_only = authorize_only

    @property
    def account_id(self):
        """Gets the account_id of this Gateway.


        :return: The account_id of this Gateway.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Gateway.


        :param account_id: The account_id of this Gateway.
        :type: str
        """

        self._account_id = account_id

    @property
    def status(self):
        """Gets the status of this Gateway.


        :return: The status of this Gateway.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Gateway.


        :param status: The status of this Gateway.
        :type: str
        """
        allowed_values = ["enabled", "disabled"]
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
        if issubclass(Gateway, dict):
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
        if not isinstance(other, Gateway):
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
        return cls.list_all_gateways(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_gateways(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_gateways(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def list_all_gateways(cls, **kwargs):
        """List Gateways

        Return a list of Gateways
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_gateways(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Gateway]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_gateways_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_gateways_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_gateways_with_http_info(cls, **kwargs):
        """List Gateways

        Return a list of Gateways
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_gateways_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Gateway]
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
            '/gateways', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Gateway]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
