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


class PaymentCard(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'customer': 'Customer',
        'reusable': 'bool',
        'status': 'str',
        'card_holder_name': 'str',
        'address': 'Address',
        'brand': 'str',
        'expiration_month': 'str',
        'expiration_year': 'str',
        'ccv': 'str',
        'card_number': 'str',
        'card_last_four_digits': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'customer': 'customer',
        'reusable': 'reusable',
        'status': 'status',
        'card_holder_name': 'cardHolderName',
        'address': 'address',
        'brand': 'brand',
        'expiration_month': 'expirationMonth',
        'expiration_year': 'expirationYear',
        'ccv': 'CCV',
        'card_number': 'cardNumber',
        'card_last_four_digits': 'cardLastFourDigits'
    }

    api_client = None

    def __init__(self, id=None, meta=None, customer=None, reusable=None, status=None, card_holder_name=None, address=None, brand=None, expiration_month=None, expiration_year=None, ccv=None, card_number=None, card_last_four_digits=None):
        """PaymentCard - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._customer = None
        self._reusable = None
        self._status = None
        self._card_holder_name = None
        self._address = None
        self._brand = None
        self._expiration_month = None
        self._expiration_year = None
        self._ccv = None
        self._card_number = None
        self._card_last_four_digits = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.customer = customer
        if reusable is not None:
            self.reusable = reusable
        self.status = status
        if card_holder_name is not None:
            self.card_holder_name = card_holder_name
        if address is not None:
            self.address = address
        self.brand = brand
        self.expiration_month = expiration_month
        self.expiration_year = expiration_year
        self.ccv = ccv
        self.card_number = card_number
        self.card_last_four_digits = card_last_four_digits

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
        """Gets the meta of this PaymentCard.


        :return: The meta of this PaymentCard.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this PaymentCard.


        :param meta: The meta of this PaymentCard.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def customer(self):
        """Gets the customer of this PaymentCard.


        :return: The customer of this PaymentCard.
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this PaymentCard.


        :param customer: The customer of this PaymentCard.
        :type: Customer
        """

        self._customer = customer

    @property
    def reusable(self):
        """Gets the reusable of this PaymentCard.


        :return: The reusable of this PaymentCard.
        :rtype: bool
        """
        return self._reusable

    @reusable.setter
    def reusable(self, reusable):
        """Sets the reusable of this PaymentCard.


        :param reusable: The reusable of this PaymentCard.
        :type: bool
        """

        self._reusable = reusable

    @property
    def status(self):
        """Gets the status of this PaymentCard.


        :return: The status of this PaymentCard.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentCard.


        :param status: The status of this PaymentCard.
        :type: str
        """
        allowed_values = ["new", "used", "expired"]
        if status is not None and status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def card_holder_name(self):
        """Gets the card_holder_name of this PaymentCard.


        :return: The card_holder_name of this PaymentCard.
        :rtype: str
        """
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, card_holder_name):
        """Sets the card_holder_name of this PaymentCard.


        :param card_holder_name: The card_holder_name of this PaymentCard.
        :type: str
        """

        self._card_holder_name = card_holder_name

    @property
    def address(self):
        """Gets the address of this PaymentCard.


        :return: The address of this PaymentCard.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PaymentCard.


        :param address: The address of this PaymentCard.
        :type: Address
        """

        self._address = address

    @property
    def brand(self):
        """Gets the brand of this PaymentCard.


        :return: The brand of this PaymentCard.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentCard.


        :param brand: The brand of this PaymentCard.
        :type: str
        """
        allowed_values = ["visa", "mastercard", "americanExpress", "discover"]
        if brand is not None and brand not in allowed_values:
            raise ValueError(
                "Invalid value for `brand` ({0}), must be one of {1}"
                .format(brand, allowed_values)
            )

        self._brand = brand

    @property
    def expiration_month(self):
        """Gets the expiration_month of this PaymentCard.


        :return: The expiration_month of this PaymentCard.
        :rtype: str
        """
        return self._expiration_month

    @expiration_month.setter
    def expiration_month(self, expiration_month):
        """Sets the expiration_month of this PaymentCard.


        :param expiration_month: The expiration_month of this PaymentCard.
        :type: str
        """

        self._expiration_month = expiration_month

    @property
    def expiration_year(self):
        """Gets the expiration_year of this PaymentCard.


        :return: The expiration_year of this PaymentCard.
        :rtype: str
        """
        return self._expiration_year

    @expiration_year.setter
    def expiration_year(self, expiration_year):
        """Sets the expiration_year of this PaymentCard.


        :param expiration_year: The expiration_year of this PaymentCard.
        :type: str
        """

        self._expiration_year = expiration_year

    @property
    def ccv(self):
        """Gets the ccv of this PaymentCard.


        :return: The ccv of this PaymentCard.
        :rtype: str
        """
        return self._ccv

    @ccv.setter
    def ccv(self, ccv):
        """Sets the ccv of this PaymentCard.


        :param ccv: The ccv of this PaymentCard.
        :type: str
        """

        self._ccv = ccv

    @property
    def card_number(self):
        """Gets the card_number of this PaymentCard.


        :return: The card_number of this PaymentCard.
        :rtype: str
        """
        return self._card_number

    @card_number.setter
    def card_number(self, card_number):
        """Sets the card_number of this PaymentCard.


        :param card_number: The card_number of this PaymentCard.
        :type: str
        """

        self._card_number = card_number

    @property
    def card_last_four_digits(self):
        """Gets the card_last_four_digits of this PaymentCard.


        :return: The card_last_four_digits of this PaymentCard.
        :rtype: str
        """
        return self._card_last_four_digits

    @card_last_four_digits.setter
    def card_last_four_digits(self, card_last_four_digits):
        """Sets the card_last_four_digits of this PaymentCard.


        :param card_last_four_digits: The card_last_four_digits of this PaymentCard.
        :type: str
        """

        self._card_last_four_digits = card_last_four_digits

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
        if issubclass(PaymentCard, dict):
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
        if not isinstance(other, PaymentCard):
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
        return cls.list_all_payment_cards(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_payment_cards(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_payment_cards(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_payment_card_by_id(id)

    def create(self):
        new_instance = self.create_payment_card(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_payment_card_by_id(self.id, self)

    def delete(self):
        return self.delete_payment_card_by_id(self.id)



    @classmethod
    def create_payment_card(cls, payment_card, **kwargs):
        """Create PaymentCard

        Create a new PaymentCard
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_payment_card(payment_card, async=True)
        >>> result = thread.get()

        :param async bool
        :param PaymentCard payment_card: Attributes of paymentCard to create (required)
        :return: PaymentCard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_payment_card_with_http_info(payment_card, **kwargs)
        else:
            (data) = cls._create_payment_card_with_http_info(payment_card, **kwargs)
            return data

    @classmethod
    def _create_payment_card_with_http_info(cls, payment_card, **kwargs):
        """Create PaymentCard

        Create a new PaymentCard
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_payment_card_with_http_info(payment_card, async=True)
        >>> result = thread.get()

        :param async bool
        :param PaymentCard payment_card: Attributes of paymentCard to create (required)
        :return: PaymentCard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_card']
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
        # verify the required parameter 'payment_card' is set
        if ('payment_card' not in params or
                params['payment_card'] is None):
            raise ValueError("Missing the required parameter `payment_card` when calling `create_payment_card`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_card' in params:
            body_params = params['payment_card']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/paymentCards', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentCard',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_payment_card_by_id(cls, payment_card_id, **kwargs):
        """Delete PaymentCard

        Delete an instance of PaymentCard by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_payment_card_by_id(payment_card_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_card_id: ID of paymentCard to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_payment_card_by_id_with_http_info(payment_card_id, **kwargs)
        else:
            (data) = cls._delete_payment_card_by_id_with_http_info(payment_card_id, **kwargs)
            return data

    @classmethod
    def _delete_payment_card_by_id_with_http_info(cls, payment_card_id, **kwargs):
        """Delete PaymentCard

        Delete an instance of PaymentCard by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_payment_card_by_id_with_http_info(payment_card_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_card_id: ID of paymentCard to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_card_id']
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
        # verify the required parameter 'payment_card_id' is set
        if ('payment_card_id' not in params or
                params['payment_card_id'] is None):
            raise ValueError("Missing the required parameter `payment_card_id` when calling `delete_payment_card_by_id`")

        collection_formats = {}

        path_params = {}
        if 'payment_card_id' in params:
            path_params['paymentCardId'] = params['payment_card_id']


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
            '/paymentCards/{paymentCardId}', 'DELETE',
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
    def get_payment_card_by_id(cls, payment_card_id, **kwargs):
        """Find PaymentCard

        Return single instance of PaymentCard by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_payment_card_by_id(payment_card_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_card_id: ID of paymentCard to return (required)
        :return: PaymentCard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_payment_card_by_id_with_http_info(payment_card_id, **kwargs)
        else:
            (data) = cls._get_payment_card_by_id_with_http_info(payment_card_id, **kwargs)
            return data

    @classmethod
    def _get_payment_card_by_id_with_http_info(cls, payment_card_id, **kwargs):
        """Find PaymentCard

        Return single instance of PaymentCard by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_payment_card_by_id_with_http_info(payment_card_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_card_id: ID of paymentCard to return (required)
        :return: PaymentCard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_card_id']
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
        # verify the required parameter 'payment_card_id' is set
        if ('payment_card_id' not in params or
                params['payment_card_id'] is None):
            raise ValueError("Missing the required parameter `payment_card_id` when calling `get_payment_card_by_id`")

        collection_formats = {}

        path_params = {}
        if 'payment_card_id' in params:
            path_params['paymentCardId'] = params['payment_card_id']


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
            '/paymentCards/{paymentCardId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentCard',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_payment_cards(cls, **kwargs):
        """List PaymentCards

        Return a list of PaymentCards
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_payment_cards(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[PaymentCard]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_payment_cards_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_payment_cards_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_payment_cards_with_http_info(cls, **kwargs):
        """List PaymentCards

        Return a list of PaymentCards
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_payment_cards_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[PaymentCard]
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
            '/paymentCards', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[PaymentCard]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_payment_card_by_id(cls, payment_card_id, payment_card, **kwargs):
        """Replace PaymentCard

        Replace all attributes of PaymentCard
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_payment_card_by_id(payment_card_id, payment_card, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_card_id: ID of paymentCard to replace (required)
        :param PaymentCard payment_card: Attributes of paymentCard to replace (required)
        :return: PaymentCard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_payment_card_by_id_with_http_info(payment_card_id, payment_card, **kwargs)
        else:
            (data) = cls._replace_payment_card_by_id_with_http_info(payment_card_id, payment_card, **kwargs)
            return data

    @classmethod
    def _replace_payment_card_by_id_with_http_info(cls, payment_card_id, payment_card, **kwargs):
        """Replace PaymentCard

        Replace all attributes of PaymentCard
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_payment_card_by_id_with_http_info(payment_card_id, payment_card, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_card_id: ID of paymentCard to replace (required)
        :param PaymentCard payment_card: Attributes of paymentCard to replace (required)
        :return: PaymentCard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_card_id', 'payment_card']
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
        # verify the required parameter 'payment_card_id' is set
        if ('payment_card_id' not in params or
                params['payment_card_id'] is None):
            raise ValueError("Missing the required parameter `payment_card_id` when calling `replace_payment_card_by_id`")
        # verify the required parameter 'payment_card' is set
        if ('payment_card' not in params or
                params['payment_card'] is None):
            raise ValueError("Missing the required parameter `payment_card` when calling `replace_payment_card_by_id`")

        collection_formats = {}

        path_params = {}
        if 'payment_card_id' in params:
            path_params['paymentCardId'] = params['payment_card_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_card' in params:
            body_params = params['payment_card']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/paymentCards/{paymentCardId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentCard',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_payment_card_by_id(cls, payment_card_id, payment_card, **kwargs):
        """Update PaymentCard

        Update attributes of PaymentCard
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_payment_card_by_id(payment_card_id, payment_card, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_card_id: ID of paymentCard to update. (required)
        :param PaymentCard payment_card: Attributes of paymentCard to update. (required)
        :return: PaymentCard
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_payment_card_by_id_with_http_info(payment_card_id, payment_card, **kwargs)
        else:
            (data) = cls._update_payment_card_by_id_with_http_info(payment_card_id, payment_card, **kwargs)
            return data

    @classmethod
    def _update_payment_card_by_id_with_http_info(cls, payment_card_id, payment_card, **kwargs):
        """Update PaymentCard

        Update attributes of PaymentCard
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_payment_card_by_id_with_http_info(payment_card_id, payment_card, async=True)
        >>> result = thread.get()

        :param async bool
        :param str payment_card_id: ID of paymentCard to update. (required)
        :param PaymentCard payment_card: Attributes of paymentCard to update. (required)
        :return: PaymentCard
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_card_id', 'payment_card']
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
        # verify the required parameter 'payment_card_id' is set
        if ('payment_card_id' not in params or
                params['payment_card_id'] is None):
            raise ValueError("Missing the required parameter `payment_card_id` when calling `update_payment_card_by_id`")
        # verify the required parameter 'payment_card' is set
        if ('payment_card' not in params or
                params['payment_card'] is None):
            raise ValueError("Missing the required parameter `payment_card` when calling `update_payment_card_by_id`")

        collection_formats = {}

        path_params = {}
        if 'payment_card_id' in params:
            path_params['paymentCardId'] = params['payment_card_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payment_card' in params:
            body_params = params['payment_card']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/paymentCards/{paymentCardId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentCard',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
