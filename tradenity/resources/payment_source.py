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


class PaymentSource(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'customer': 'Customer',
        'reusable': 'bool',
        'status': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'customer': 'customer',
        'reusable': 'reusable',
        'status': 'status'
    }

    api_client = None

    def __init__(self, id=None, meta=None, customer=None, reusable=None, status=None):
        """PaymentSource - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._customer = None
        self._reusable = None
        self._status = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.customer = customer
        if reusable is not None:
            self.reusable = reusable
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
        """Gets the meta of this PaymentSource.


        :return: The meta of this PaymentSource.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this PaymentSource.


        :param meta: The meta of this PaymentSource.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def customer(self):
        """Gets the customer of this PaymentSource.


        :return: The customer of this PaymentSource.
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this PaymentSource.


        :param customer: The customer of this PaymentSource.
        :type: Customer
        """

        self._customer = customer

    @property
    def reusable(self):
        """Gets the reusable of this PaymentSource.


        :return: The reusable of this PaymentSource.
        :rtype: bool
        """
        return self._reusable

    @reusable.setter
    def reusable(self, reusable):
        """Sets the reusable of this PaymentSource.


        :param reusable: The reusable of this PaymentSource.
        :type: bool
        """

        self._reusable = reusable

    @property
    def status(self):
        """Gets the status of this PaymentSource.


        :return: The status of this PaymentSource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentSource.


        :param status: The status of this PaymentSource.
        :type: str
        """
        allowed_values = ["new", "used", "expired"]
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
        if issubclass(PaymentSource, dict):
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
        if not isinstance(other, PaymentSource):
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
        return cls.list_all_payment_sources()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_payment_sources(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_payment_sources(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def list_all_payment_sources(cls, **kwargs):
        """List PaymentSources

        Return a list of PaymentSources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_payment_sources(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[PaymentSource]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_payment_sources_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_payment_sources_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_payment_sources_with_http_info(cls, **kwargs):
        """List PaymentSources

        Return a list of PaymentSources
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_payment_sources_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[PaymentSource]
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
            '/paymentSources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[PaymentSource]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
