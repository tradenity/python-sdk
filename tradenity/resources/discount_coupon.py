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


class DiscountCoupon(object):
    

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
        'type': 'str',
        'amount': 'int'
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
        'type': 'type',
        'amount': 'amount'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, description=None, status=None, minimum_order=None, code=None, begins_at=None, ends_at=None, include=None, type=None, amount=None):
        """DiscountCoupon - a model defined in Swagger"""
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
        self._type = None
        self._amount = None
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
        self.type = type
        self.amount = amount

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
        """Gets the meta of this DiscountCoupon.


        :return: The meta of this DiscountCoupon.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this DiscountCoupon.


        :param meta: The meta of this DiscountCoupon.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this DiscountCoupon.


        :return: The name of this DiscountCoupon.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiscountCoupon.


        :param name: The name of this DiscountCoupon.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DiscountCoupon.


        :return: The description of this DiscountCoupon.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DiscountCoupon.


        :param description: The description of this DiscountCoupon.
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this DiscountCoupon.


        :return: The status of this DiscountCoupon.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DiscountCoupon.


        :param status: The status of this DiscountCoupon.
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
        """Gets the minimum_order of this DiscountCoupon.


        :return: The minimum_order of this DiscountCoupon.
        :rtype: int
        """
        return self._minimum_order

    @minimum_order.setter
    def minimum_order(self, minimum_order):
        """Sets the minimum_order of this DiscountCoupon.


        :param minimum_order: The minimum_order of this DiscountCoupon.
        :type: int
        """

        self._minimum_order = minimum_order

    @property
    def code(self):
        """Gets the code of this DiscountCoupon.


        :return: The code of this DiscountCoupon.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DiscountCoupon.


        :param code: The code of this DiscountCoupon.
        :type: str
        """

        self._code = code

    @property
    def begins_at(self):
        """Gets the begins_at of this DiscountCoupon.


        :return: The begins_at of this DiscountCoupon.
        :rtype: datetime
        """
        return self._begins_at

    @begins_at.setter
    def begins_at(self, begins_at):
        """Sets the begins_at of this DiscountCoupon.


        :param begins_at: The begins_at of this DiscountCoupon.
        :type: datetime
        """

        self._begins_at = begins_at

    @property
    def ends_at(self):
        """Gets the ends_at of this DiscountCoupon.


        :return: The ends_at of this DiscountCoupon.
        :rtype: datetime
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this DiscountCoupon.


        :param ends_at: The ends_at of this DiscountCoupon.
        :type: datetime
        """

        self._ends_at = ends_at

    @property
    def include(self):
        """Gets the include of this DiscountCoupon.


        :return: The include of this DiscountCoupon.
        :rtype: ItemsSelector
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this DiscountCoupon.


        :param include: The include of this DiscountCoupon.
        :type: ItemsSelector
        """

        self._include = include

    @property
    def type(self):
        """Gets the type of this DiscountCoupon.


        :return: The type of this DiscountCoupon.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DiscountCoupon.


        :param type: The type of this DiscountCoupon.
        :type: str
        """
        allowed_values = ["percentage", "fixedRate"]
        if type is not None and type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def amount(self):
        """Gets the amount of this DiscountCoupon.


        :return: The amount of this DiscountCoupon.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DiscountCoupon.


        :param amount: The amount of this DiscountCoupon.
        :type: int
        """

        self._amount = amount

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
        if issubclass(DiscountCoupon, dict):
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
        if not isinstance(other, DiscountCoupon):
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
        return cls.list_all_discount_coupons()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_discount_coupons(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_discount_coupons(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_discount_coupon_by_id(id)

    def create(self):
        new_instance = self.create_discount_coupon(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_discount_coupon_by_id(self.id, self)

    def delete(self):
        return self.delete_discount_coupon_by_id(self.id)



    @classmethod
    def create_discount_coupon(cls, discount_coupon, **kwargs):
        """Create DiscountCoupon

        Create a new DiscountCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_discount_coupon(discount_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param DiscountCoupon discount_coupon: Attributes of discountCoupon to create (required)
        :return: DiscountCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_discount_coupon_with_http_info(discount_coupon, **kwargs)
        else:
            (data) = cls._create_discount_coupon_with_http_info(discount_coupon, **kwargs)
            return data

    @classmethod
    def _create_discount_coupon_with_http_info(cls, discount_coupon, **kwargs):
        """Create DiscountCoupon

        Create a new DiscountCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_discount_coupon_with_http_info(discount_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param DiscountCoupon discount_coupon: Attributes of discountCoupon to create (required)
        :return: DiscountCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['discount_coupon']
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
        # verify the required parameter 'discount_coupon' is set
        if ('discount_coupon' not in params or
                params['discount_coupon'] is None):
            raise ValueError("Missing the required parameter `discount_coupon` when calling `create_discount_coupon`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'discount_coupon' in params:
            body_params = params['discount_coupon']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/discountCoupons', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiscountCoupon',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_discount_coupon_by_id(cls, discount_coupon_id, **kwargs):
        """Delete DiscountCoupon

        Delete an instance of DiscountCoupon by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_discount_coupon_by_id(discount_coupon_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str discount_coupon_id: ID of discountCoupon to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_discount_coupon_by_id_with_http_info(discount_coupon_id, **kwargs)
        else:
            (data) = cls._delete_discount_coupon_by_id_with_http_info(discount_coupon_id, **kwargs)
            return data

    @classmethod
    def _delete_discount_coupon_by_id_with_http_info(cls, discount_coupon_id, **kwargs):
        """Delete DiscountCoupon

        Delete an instance of DiscountCoupon by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_discount_coupon_by_id_with_http_info(discount_coupon_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str discount_coupon_id: ID of discountCoupon to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['discount_coupon_id']
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
        # verify the required parameter 'discount_coupon_id' is set
        if ('discount_coupon_id' not in params or
                params['discount_coupon_id'] is None):
            raise ValueError("Missing the required parameter `discount_coupon_id` when calling `delete_discount_coupon_by_id`")

        collection_formats = {}

        path_params = {}
        if 'discount_coupon_id' in params:
            path_params['discountCouponId'] = params['discount_coupon_id']


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
            '/discountCoupons/{discountCouponId}', 'DELETE',
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
    def get_discount_coupon_by_id(cls, discount_coupon_id, **kwargs):
        """Find DiscountCoupon

        Return single instance of DiscountCoupon by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_discount_coupon_by_id(discount_coupon_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str discount_coupon_id: ID of discountCoupon to return (required)
        :return: DiscountCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_discount_coupon_by_id_with_http_info(discount_coupon_id, **kwargs)
        else:
            (data) = cls._get_discount_coupon_by_id_with_http_info(discount_coupon_id, **kwargs)
            return data

    @classmethod
    def _get_discount_coupon_by_id_with_http_info(cls, discount_coupon_id, **kwargs):
        """Find DiscountCoupon

        Return single instance of DiscountCoupon by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_discount_coupon_by_id_with_http_info(discount_coupon_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str discount_coupon_id: ID of discountCoupon to return (required)
        :return: DiscountCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['discount_coupon_id']
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
        # verify the required parameter 'discount_coupon_id' is set
        if ('discount_coupon_id' not in params or
                params['discount_coupon_id'] is None):
            raise ValueError("Missing the required parameter `discount_coupon_id` when calling `get_discount_coupon_by_id`")

        collection_formats = {}

        path_params = {}
        if 'discount_coupon_id' in params:
            path_params['discountCouponId'] = params['discount_coupon_id']


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
            '/discountCoupons/{discountCouponId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiscountCoupon',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_discount_coupons(cls, **kwargs):
        """List DiscountCoupons

        Return a list of DiscountCoupons
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_discount_coupons(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[DiscountCoupon]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_discount_coupons_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_discount_coupons_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_discount_coupons_with_http_info(cls, **kwargs):
        """List DiscountCoupons

        Return a list of DiscountCoupons
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_discount_coupons_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[DiscountCoupon]
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
            '/discountCoupons', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[DiscountCoupon]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_discount_coupon_by_id(cls, discount_coupon_id, discount_coupon, **kwargs):
        """Replace DiscountCoupon

        Replace all attributes of DiscountCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_discount_coupon_by_id(discount_coupon_id, discount_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param str discount_coupon_id: ID of discountCoupon to replace (required)
        :param DiscountCoupon discount_coupon: Attributes of discountCoupon to replace (required)
        :return: DiscountCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_discount_coupon_by_id_with_http_info(discount_coupon_id, discount_coupon, **kwargs)
        else:
            (data) = cls._replace_discount_coupon_by_id_with_http_info(discount_coupon_id, discount_coupon, **kwargs)
            return data

    @classmethod
    def _replace_discount_coupon_by_id_with_http_info(cls, discount_coupon_id, discount_coupon, **kwargs):
        """Replace DiscountCoupon

        Replace all attributes of DiscountCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_discount_coupon_by_id_with_http_info(discount_coupon_id, discount_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param str discount_coupon_id: ID of discountCoupon to replace (required)
        :param DiscountCoupon discount_coupon: Attributes of discountCoupon to replace (required)
        :return: DiscountCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['discount_coupon_id', 'discount_coupon']
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
        # verify the required parameter 'discount_coupon_id' is set
        if ('discount_coupon_id' not in params or
                params['discount_coupon_id'] is None):
            raise ValueError("Missing the required parameter `discount_coupon_id` when calling `replace_discount_coupon_by_id`")
        # verify the required parameter 'discount_coupon' is set
        if ('discount_coupon' not in params or
                params['discount_coupon'] is None):
            raise ValueError("Missing the required parameter `discount_coupon` when calling `replace_discount_coupon_by_id`")

        collection_formats = {}

        path_params = {}
        if 'discount_coupon_id' in params:
            path_params['discountCouponId'] = params['discount_coupon_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'discount_coupon' in params:
            body_params = params['discount_coupon']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/discountCoupons/{discountCouponId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiscountCoupon',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_discount_coupon_by_id(cls, discount_coupon_id, discount_coupon, **kwargs):
        """Update DiscountCoupon

        Update attributes of DiscountCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_discount_coupon_by_id(discount_coupon_id, discount_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param str discount_coupon_id: ID of discountCoupon to update. (required)
        :param DiscountCoupon discount_coupon: Attributes of discountCoupon to update. (required)
        :return: DiscountCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_discount_coupon_by_id_with_http_info(discount_coupon_id, discount_coupon, **kwargs)
        else:
            (data) = cls._update_discount_coupon_by_id_with_http_info(discount_coupon_id, discount_coupon, **kwargs)
            return data

    @classmethod
    def _update_discount_coupon_by_id_with_http_info(cls, discount_coupon_id, discount_coupon, **kwargs):
        """Update DiscountCoupon

        Update attributes of DiscountCoupon
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_discount_coupon_by_id_with_http_info(discount_coupon_id, discount_coupon, async=True)
        >>> result = thread.get()

        :param async bool
        :param str discount_coupon_id: ID of discountCoupon to update. (required)
        :param DiscountCoupon discount_coupon: Attributes of discountCoupon to update. (required)
        :return: DiscountCoupon
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['discount_coupon_id', 'discount_coupon']
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
        # verify the required parameter 'discount_coupon_id' is set
        if ('discount_coupon_id' not in params or
                params['discount_coupon_id'] is None):
            raise ValueError("Missing the required parameter `discount_coupon_id` when calling `update_discount_coupon_by_id`")
        # verify the required parameter 'discount_coupon' is set
        if ('discount_coupon' not in params or
                params['discount_coupon'] is None):
            raise ValueError("Missing the required parameter `discount_coupon` when calling `update_discount_coupon_by_id`")

        collection_formats = {}

        path_params = {}
        if 'discount_coupon_id' in params:
            path_params['discountCouponId'] = params['discount_coupon_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'discount_coupon' in params:
            body_params = params['discount_coupon']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/discountCoupons/{discountCouponId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DiscountCoupon',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
