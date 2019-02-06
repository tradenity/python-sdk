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


class Customer(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'username': 'str',
        'password': 'str',
        'status': 'str',
        'photo': 'Photo',
        'billing_address': 'Address',
        'shipping_address': 'Address',
        'customer_groups': 'list[CustomerGroup]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'username': 'username',
        'password': 'password',
        'status': 'status',
        'photo': 'photo',
        'billing_address': 'billingAddress',
        'shipping_address': 'shippingAddress',
        'customer_groups': 'customerGroups'
    }

    api_client = None

    def __init__(self, id=None, meta=None, first_name=None, last_name=None, email=None, username=None, password=None, status=None, photo=None, billing_address=None, shipping_address=None, customer_groups=None):
        """Customer - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._username = None
        self._password = None
        self._status = None
        self._photo = None
        self._billing_address = None
        self._shipping_address = None
        self._customer_groups = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.status = status
        if photo is not None:
            self.photo = photo
        if billing_address is not None:
            self.billing_address = billing_address
        if shipping_address is not None:
            self.shipping_address = shipping_address
        if customer_groups is not None:
            self.customer_groups = customer_groups

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
        """Gets the meta of this Customer.


        :return: The meta of this Customer.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Customer.


        :param meta: The meta of this Customer.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def first_name(self):
        """Gets the first_name of this Customer.


        :return: The first_name of this Customer.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Customer.


        :param first_name: The first_name of this Customer.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Customer.


        :return: The last_name of this Customer.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Customer.


        :param last_name: The last_name of this Customer.
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this Customer.


        :return: The email of this Customer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Customer.


        :param email: The email of this Customer.
        :type: str
        """

        self._email = email

    @property
    def username(self):
        """Gets the username of this Customer.


        :return: The username of this Customer.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Customer.


        :param username: The username of this Customer.
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this Customer.


        :return: The password of this Customer.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Customer.


        :param password: The password of this Customer.
        :type: str
        """

        self._password = password

    @property
    def status(self):
        """Gets the status of this Customer.


        :return: The status of this Customer.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Customer.


        :param status: The status of this Customer.
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
    def photo(self):
        """Gets the photo of this Customer.


        :return: The photo of this Customer.
        :rtype: Photo
        """
        return self._photo

    @photo.setter
    def photo(self, photo):
        """Sets the photo of this Customer.


        :param photo: The photo of this Customer.
        :type: Photo
        """

        self._photo = photo

    @property
    def billing_address(self):
        """Gets the billing_address of this Customer.


        :return: The billing_address of this Customer.
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this Customer.


        :param billing_address: The billing_address of this Customer.
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this Customer.


        :return: The shipping_address of this Customer.
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Customer.


        :param shipping_address: The shipping_address of this Customer.
        :type: Address
        """

        self._shipping_address = shipping_address

    @property
    def customer_groups(self):
        """Gets the customer_groups of this Customer.


        :return: The customer_groups of this Customer.
        :rtype: list[CustomerGroup]
        """
        return self._customer_groups

    @customer_groups.setter
    def customer_groups(self, customer_groups):
        """Sets the customer_groups of this Customer.


        :param customer_groups: The customer_groups of this Customer.
        :type: list[CustomerGroup]
        """

        self._customer_groups = customer_groups

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
        if issubclass(Customer, dict):
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
        if not isinstance(other, Customer):
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
        return cls.list_all_customers(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_customers(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_customers(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_customer_by_id(id)

    def create(self):
        new_instance = self.create_customer(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_customer_by_id(self.id, self)

    def delete(self):
        return self.delete_customer_by_id(self.id)



    @classmethod
    def create_customer(cls, customer, **kwargs):
        """Create Customer

        Create a new Customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_customer(customer, async=True)
        >>> result = thread.get()

        :param async bool
        :param Customer customer: Attributes of customer to create (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_customer_with_http_info(customer, **kwargs)
        else:
            (data) = cls._create_customer_with_http_info(customer, **kwargs)
            return data

    @classmethod
    def _create_customer_with_http_info(cls, customer, **kwargs):
        """Create Customer

        Create a new Customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_customer_with_http_info(customer, async=True)
        >>> result = thread.get()

        :param async bool
        :param Customer customer: Attributes of customer to create (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer']
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
        # verify the required parameter 'customer' is set
        if ('customer' not in params or
                params['customer'] is None):
            raise ValueError("Missing the required parameter `customer` when calling `create_customer`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'customer' in params:
            body_params = params['customer']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/customers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customer',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_customer_by_id(cls, customer_id, **kwargs):
        """Delete Customer

        Delete an instance of Customer by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_customer_by_id(customer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: ID of customer to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_customer_by_id_with_http_info(customer_id, **kwargs)
        else:
            (data) = cls._delete_customer_by_id_with_http_info(customer_id, **kwargs)
            return data

    @classmethod
    def _delete_customer_by_id_with_http_info(cls, customer_id, **kwargs):
        """Delete Customer

        Delete an instance of Customer by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_customer_by_id_with_http_info(customer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: ID of customer to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id']
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
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `delete_customer_by_id`")

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']


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
            '/customers/{customerId}', 'DELETE',
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
    def get_customer_by_id(cls, customer_id, **kwargs):
        """Find Customer

        Return single instance of Customer by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_customer_by_id(customer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: ID of customer to return (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_customer_by_id_with_http_info(customer_id, **kwargs)
        else:
            (data) = cls._get_customer_by_id_with_http_info(customer_id, **kwargs)
            return data

    @classmethod
    def _get_customer_by_id_with_http_info(cls, customer_id, **kwargs):
        """Find Customer

        Return single instance of Customer by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_customer_by_id_with_http_info(customer_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: ID of customer to return (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id']
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
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_by_id`")

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']


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
            '/customers/{customerId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customer',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_customers(cls, **kwargs):
        """List Customers

        Return a list of Customers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_customers(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Customer]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_customers_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_customers_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_customers_with_http_info(cls, **kwargs):
        """List Customers

        Return a list of Customers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_customers_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Customer]
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
            '/customers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Customer]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_customer_by_id(cls, customer_id, customer, **kwargs):
        """Replace Customer

        Replace all attributes of Customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_customer_by_id(customer_id, customer, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: ID of customer to replace (required)
        :param Customer customer: Attributes of customer to replace (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_customer_by_id_with_http_info(customer_id, customer, **kwargs)
        else:
            (data) = cls._replace_customer_by_id_with_http_info(customer_id, customer, **kwargs)
            return data

    @classmethod
    def _replace_customer_by_id_with_http_info(cls, customer_id, customer, **kwargs):
        """Replace Customer

        Replace all attributes of Customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_customer_by_id_with_http_info(customer_id, customer, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: ID of customer to replace (required)
        :param Customer customer: Attributes of customer to replace (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'customer']
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
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `replace_customer_by_id`")
        # verify the required parameter 'customer' is set
        if ('customer' not in params or
                params['customer'] is None):
            raise ValueError("Missing the required parameter `customer` when calling `replace_customer_by_id`")

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'customer' in params:
            body_params = params['customer']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/customers/{customerId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customer',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_customer_by_id(cls, customer_id, customer, **kwargs):
        """Update Customer

        Update attributes of Customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_customer_by_id(customer_id, customer, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: ID of customer to update. (required)
        :param Customer customer: Attributes of customer to update. (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_customer_by_id_with_http_info(customer_id, customer, **kwargs)
        else:
            (data) = cls._update_customer_by_id_with_http_info(customer_id, customer, **kwargs)
            return data

    @classmethod
    def _update_customer_by_id_with_http_info(cls, customer_id, customer, **kwargs):
        """Update Customer

        Update attributes of Customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_customer_by_id_with_http_info(customer_id, customer, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customer_id: ID of customer to update. (required)
        :param Customer customer: Attributes of customer to update. (required)
        :return: Customer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'customer']
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
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `update_customer_by_id`")
        # verify the required parameter 'customer' is set
        if ('customer' not in params or
                params['customer'] is None):
            raise ValueError("Missing the required parameter `customer` when calling `update_customer_by_id`")

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'customer' in params:
            body_params = params['customer']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/customers/{customerId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Customer',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
