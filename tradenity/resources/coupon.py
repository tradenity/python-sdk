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


class Coupon(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'description': 'str',
        'status': 'str',
        'minimum_order': 'int',
        'code': 'str',
        'begins_at': 'datetime',
        'ends_at': 'datetime',
        'include': 'ItemsSelector'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'minimum_order': 'minimumOrder',
        'code': 'code',
        'begins_at': 'beginsAt',
        'ends_at': 'endsAt',
        'include': 'include'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, description=None, status=None, minimum_order=None, code=None, begins_at=None, ends_at=None, include=None):
        """Coupon - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._description = None
        self._status = None
        self._minimum_order = None
        self._code = None
        self._begins_at = None
        self._ends_at = None
        self._include = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        if description is not None:
            self.description = description
        self.status = status
        if minimum_order is not None:
            self.minimum_order = minimum_order
        self.code = code
        if begins_at is not None:
            self.begins_at = begins_at
        if ends_at is not None:
            self.ends_at = ends_at
        if include is not None:
            self.include = include

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
        """Gets the meta of this Coupon.


        :return: The meta of this Coupon.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Coupon.


        :param meta: The meta of this Coupon.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Coupon.


        :return: The name of this Coupon.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Coupon.


        :param name: The name of this Coupon.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Coupon.


        :return: The description of this Coupon.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Coupon.


        :param description: The description of this Coupon.
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Coupon.


        :return: The status of this Coupon.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Coupon.


        :param status: The status of this Coupon.
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
    def minimum_order(self):
        """Gets the minimum_order of this Coupon.


        :return: The minimum_order of this Coupon.
        :rtype: int
        """
        return self._minimum_order

    @minimum_order.setter
    def minimum_order(self, minimum_order):
        """Sets the minimum_order of this Coupon.


        :param minimum_order: The minimum_order of this Coupon.
        :type: int
        """

        self._minimum_order = minimum_order

    @property
    def code(self):
        """Gets the code of this Coupon.


        :return: The code of this Coupon.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Coupon.


        :param code: The code of this Coupon.
        :type: str
        """

        self._code = code

    @property
    def begins_at(self):
        """Gets the begins_at of this Coupon.


        :return: The begins_at of this Coupon.
        :rtype: datetime
        """
        return self._begins_at

    @begins_at.setter
    def begins_at(self, begins_at):
        """Sets the begins_at of this Coupon.


        :param begins_at: The begins_at of this Coupon.
        :type: datetime
        """

        self._begins_at = begins_at

    @property
    def ends_at(self):
        """Gets the ends_at of this Coupon.


        :return: The ends_at of this Coupon.
        :rtype: datetime
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this Coupon.


        :param ends_at: The ends_at of this Coupon.
        :type: datetime
        """

        self._ends_at = ends_at

    @property
    def include(self):
        """Gets the include of this Coupon.


        :return: The include of this Coupon.
        :rtype: ItemsSelector
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this Coupon.


        :param include: The include of this Coupon.
        :type: ItemsSelector
        """

        self._include = include

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
        if issubclass(Coupon, dict):
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
        if not isinstance(other, Coupon):
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
        return cls.list_all_coupons(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_coupons(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_coupons(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def list_all_coupons(cls, **kwargs):
        """List Coupons

        Return a list of Coupons
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_coupons(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Coupon]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_coupons_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_coupons_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_coupons_with_http_info(cls, **kwargs):
        """List Coupons

        Return a list of Coupons
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_coupons_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Coupon]
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
            '/coupons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Coupon]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
