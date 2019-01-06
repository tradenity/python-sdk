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


class FreeItemCoupon(object):
    

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
        'include': 'ItemsSelector',
        'quantity': 'int',
        'free_quantity': 'int'
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
        'include': 'include',
        'quantity': 'quantity',
        'free_quantity': 'freeQuantity'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, description=None, status=None, minimum_order=None, code=None, begins_at=None, ends_at=None, include=None, quantity=None, free_quantity=None):
        """FreeItemCoupon - a model defined in Swagger"""
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
        self._quantity = None
        self._free_quantity = None
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
        if quantity is not None:
            self.quantity = quantity
        if free_quantity is not None:
            self.free_quantity = free_quantity

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
        """Gets the meta of this FreeItemCoupon.


        :return: The meta of this FreeItemCoupon.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this FreeItemCoupon.


        :param meta: The meta of this FreeItemCoupon.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this FreeItemCoupon.


        :return: The name of this FreeItemCoupon.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FreeItemCoupon.


        :param name: The name of this FreeItemCoupon.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this FreeItemCoupon.


        :return: The description of this FreeItemCoupon.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FreeItemCoupon.


        :param description: The description of this FreeItemCoupon.
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this FreeItemCoupon.


        :return: The status of this FreeItemCoupon.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FreeItemCoupon.


        :param status: The status of this FreeItemCoupon.
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
        """Gets the minimum_order of this FreeItemCoupon.


        :return: The minimum_order of this FreeItemCoupon.
        :rtype: int
        """
        return self._minimum_order

    @minimum_order.setter
    def minimum_order(self, minimum_order):
        """Sets the minimum_order of this FreeItemCoupon.


        :param minimum_order: The minimum_order of this FreeItemCoupon.
        :type: int
        """

        self._minimum_order = minimum_order

    @property
    def code(self):
        """Gets the code of this FreeItemCoupon.


        :return: The code of this FreeItemCoupon.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this FreeItemCoupon.


        :param code: The code of this FreeItemCoupon.
        :type: str
        """

        self._code = code

    @property
    def begins_at(self):
        """Gets the begins_at of this FreeItemCoupon.


        :return: The begins_at of this FreeItemCoupon.
        :rtype: datetime
        """
        return self._begins_at

    @begins_at.setter
    def begins_at(self, begins_at):
        """Sets the begins_at of this FreeItemCoupon.


        :param begins_at: The begins_at of this FreeItemCoupon.
        :type: datetime
        """

        self._begins_at = begins_at

    @property
    def ends_at(self):
        """Gets the ends_at of this FreeItemCoupon.


        :return: The ends_at of this FreeItemCoupon.
        :rtype: datetime
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this FreeItemCoupon.


        :param ends_at: The ends_at of this FreeItemCoupon.
        :type: datetime
        """

        self._ends_at = ends_at

    @property
    def include(self):
        """Gets the include of this FreeItemCoupon.


        :return: The include of this FreeItemCoupon.
        :rtype: ItemsSelector
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this FreeItemCoupon.


        :param include: The include of this FreeItemCoupon.
        :type: ItemsSelector
        """

        self._include = include

    @property
    def quantity(self):
        """Gets the quantity of this FreeItemCoupon.


        :return: The quantity of this FreeItemCoupon.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this FreeItemCoupon.


        :param quantity: The quantity of this FreeItemCoupon.
        :type: int
        """

        self._quantity = quantity

    @property
    def free_quantity(self):
        """Gets the free_quantity of this FreeItemCoupon.


        :return: The free_quantity of this FreeItemCoupon.
        :rtype: int
        """
        return self._free_quantity

    @free_quantity.setter
    def free_quantity(self, free_quantity):
        """Sets the free_quantity of this FreeItemCoupon.


        :param free_quantity: The free_quantity of this FreeItemCoupon.
        :type: int
        """

        self._free_quantity = free_quantity

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
        if issubclass(FreeItemCoupon, dict):
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
        if not isinstance(other, FreeItemCoupon):
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
        return cls.list_all_free_item_coupons()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_free_item_coupons(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_free_item_coupons(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_free_item_coupon_by_id(id)

    def create(self):
        new_instance = self.create_free_item_coupon(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_free_item_coupon_by_id(self.id, self)

    def delete(self):
        return self.delete_free_item_coupon_by_id(self.id)



    @classmethod
    def create_free_item_coupon(cls, free_item_coupon, **kwargs):
        """Create FreeItemCoupon

        Create a new FreeItemCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_free_item_coupon(free_item_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param FreeItemCoupon free_item_coupon: Attributes of freeItemCoupon to create (required)
        :return: FreeItemCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_free_item_coupon_with_http_info(free_item_coupon, **kwargs)
        else:
            (data) = cls._create_free_item_coupon_with_http_info(free_item_coupon, **kwargs)
            return data

    @classmethod
    def _create_free_item_coupon_with_http_info(cls, free_item_coupon, **kwargs):
        """Create FreeItemCoupon

        Create a new FreeItemCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_free_item_coupon_with_http_info(free_item_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param FreeItemCoupon free_item_coupon: Attributes of freeItemCoupon to create (required)
        :return: FreeItemCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_item_coupon']
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
        # verify the required parameter 'free_item_coupon' is set
        if ('free_item_coupon' not in params or
                params['free_item_coupon'] is None):
            raise ValueError("Missing the required parameter `free_item_coupon` when calling `create_free_item_coupon`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'free_item_coupon' in params:
            body_params = params['free_item_coupon']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/freeItemCoupons', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FreeItemCoupon',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_free_item_coupon_by_id(cls, free_item_coupon_id, **kwargs):
        """Delete FreeItemCoupon

        Delete an instance of FreeItemCoupon by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_free_item_coupon_by_id(free_item_coupon_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str free_item_coupon_id: ID of freeItemCoupon to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_free_item_coupon_by_id_with_http_info(free_item_coupon_id, **kwargs)
        else:
            (data) = cls._delete_free_item_coupon_by_id_with_http_info(free_item_coupon_id, **kwargs)
            return data

    @classmethod
    def _delete_free_item_coupon_by_id_with_http_info(cls, free_item_coupon_id, **kwargs):
        """Delete FreeItemCoupon

        Delete an instance of FreeItemCoupon by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_free_item_coupon_by_id_with_http_info(free_item_coupon_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str free_item_coupon_id: ID of freeItemCoupon to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_item_coupon_id']
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
        # verify the required parameter 'free_item_coupon_id' is set
        if ('free_item_coupon_id' not in params or
                params['free_item_coupon_id'] is None):
            raise ValueError("Missing the required parameter `free_item_coupon_id` when calling `delete_free_item_coupon_by_id`")

        collection_formats = {}

        path_params = {}
        if 'free_item_coupon_id' in params:
            path_params['freeItemCouponId'] = params['free_item_coupon_id']


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
            '/freeItemCoupons/{freeItemCouponId}', 'DELETE',
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
    def get_free_item_coupon_by_id(cls, free_item_coupon_id, **kwargs):
        """Find FreeItemCoupon

        Return single instance of FreeItemCoupon by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_free_item_coupon_by_id(free_item_coupon_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str free_item_coupon_id: ID of freeItemCoupon to return (required)
        :return: FreeItemCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_free_item_coupon_by_id_with_http_info(free_item_coupon_id, **kwargs)
        else:
            (data) = cls._get_free_item_coupon_by_id_with_http_info(free_item_coupon_id, **kwargs)
            return data

    @classmethod
    def _get_free_item_coupon_by_id_with_http_info(cls, free_item_coupon_id, **kwargs):
        """Find FreeItemCoupon

        Return single instance of FreeItemCoupon by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_free_item_coupon_by_id_with_http_info(free_item_coupon_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str free_item_coupon_id: ID of freeItemCoupon to return (required)
        :return: FreeItemCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_item_coupon_id']
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
        # verify the required parameter 'free_item_coupon_id' is set
        if ('free_item_coupon_id' not in params or
                params['free_item_coupon_id'] is None):
            raise ValueError("Missing the required parameter `free_item_coupon_id` when calling `get_free_item_coupon_by_id`")

        collection_formats = {}

        path_params = {}
        if 'free_item_coupon_id' in params:
            path_params['freeItemCouponId'] = params['free_item_coupon_id']


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
            '/freeItemCoupons/{freeItemCouponId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FreeItemCoupon',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_free_item_coupons(cls, **kwargs):
        """List FreeItemCoupons

        Return a list of FreeItemCoupons
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_free_item_coupons(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[FreeItemCoupon]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_free_item_coupons_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_free_item_coupons_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_free_item_coupons_with_http_info(cls, **kwargs):
        """List FreeItemCoupons

        Return a list of FreeItemCoupons
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_free_item_coupons_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[FreeItemCoupon]
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
            '/freeItemCoupons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[FreeItemCoupon]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_free_item_coupon_by_id(cls, free_item_coupon_id, free_item_coupon, **kwargs):
        """Replace FreeItemCoupon

        Replace all attributes of FreeItemCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_free_item_coupon_by_id(free_item_coupon_id, free_item_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param str free_item_coupon_id: ID of freeItemCoupon to replace (required)
        :param FreeItemCoupon free_item_coupon: Attributes of freeItemCoupon to replace (required)
        :return: FreeItemCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_free_item_coupon_by_id_with_http_info(free_item_coupon_id, free_item_coupon, **kwargs)
        else:
            (data) = cls._replace_free_item_coupon_by_id_with_http_info(free_item_coupon_id, free_item_coupon, **kwargs)
            return data

    @classmethod
    def _replace_free_item_coupon_by_id_with_http_info(cls, free_item_coupon_id, free_item_coupon, **kwargs):
        """Replace FreeItemCoupon

        Replace all attributes of FreeItemCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_free_item_coupon_by_id_with_http_info(free_item_coupon_id, free_item_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param str free_item_coupon_id: ID of freeItemCoupon to replace (required)
        :param FreeItemCoupon free_item_coupon: Attributes of freeItemCoupon to replace (required)
        :return: FreeItemCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_item_coupon_id', 'free_item_coupon']
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
        # verify the required parameter 'free_item_coupon_id' is set
        if ('free_item_coupon_id' not in params or
                params['free_item_coupon_id'] is None):
            raise ValueError("Missing the required parameter `free_item_coupon_id` when calling `replace_free_item_coupon_by_id`")
        # verify the required parameter 'free_item_coupon' is set
        if ('free_item_coupon' not in params or
                params['free_item_coupon'] is None):
            raise ValueError("Missing the required parameter `free_item_coupon` when calling `replace_free_item_coupon_by_id`")

        collection_formats = {}

        path_params = {}
        if 'free_item_coupon_id' in params:
            path_params['freeItemCouponId'] = params['free_item_coupon_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'free_item_coupon' in params:
            body_params = params['free_item_coupon']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/freeItemCoupons/{freeItemCouponId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FreeItemCoupon',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_free_item_coupon_by_id(cls, free_item_coupon_id, free_item_coupon, **kwargs):
        """Update FreeItemCoupon

        Update attributes of FreeItemCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_free_item_coupon_by_id(free_item_coupon_id, free_item_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param str free_item_coupon_id: ID of freeItemCoupon to update. (required)
        :param FreeItemCoupon free_item_coupon: Attributes of freeItemCoupon to update. (required)
        :return: FreeItemCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_free_item_coupon_by_id_with_http_info(free_item_coupon_id, free_item_coupon, **kwargs)
        else:
            (data) = cls._update_free_item_coupon_by_id_with_http_info(free_item_coupon_id, free_item_coupon, **kwargs)
            return data

    @classmethod
    def _update_free_item_coupon_by_id_with_http_info(cls, free_item_coupon_id, free_item_coupon, **kwargs):
        """Update FreeItemCoupon

        Update attributes of FreeItemCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_free_item_coupon_by_id_with_http_info(free_item_coupon_id, free_item_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param str free_item_coupon_id: ID of freeItemCoupon to update. (required)
        :param FreeItemCoupon free_item_coupon: Attributes of freeItemCoupon to update. (required)
        :return: FreeItemCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_item_coupon_id', 'free_item_coupon']
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
        # verify the required parameter 'free_item_coupon_id' is set
        if ('free_item_coupon_id' not in params or
                params['free_item_coupon_id'] is None):
            raise ValueError("Missing the required parameter `free_item_coupon_id` when calling `update_free_item_coupon_by_id`")
        # verify the required parameter 'free_item_coupon' is set
        if ('free_item_coupon' not in params or
                params['free_item_coupon'] is None):
            raise ValueError("Missing the required parameter `free_item_coupon` when calling `update_free_item_coupon_by_id`")

        collection_formats = {}

        path_params = {}
        if 'free_item_coupon_id' in params:
            path_params['freeItemCouponId'] = params['free_item_coupon_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'free_item_coupon' in params:
            body_params = params['free_item_coupon']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/freeItemCoupons/{freeItemCouponId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FreeItemCoupon',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
