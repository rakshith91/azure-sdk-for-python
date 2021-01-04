# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ErrorResponse(msrest.serialization.Model):
    """Describes the format of Error response.

    :param code: Error code.
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class InfoField(msrest.serialization.Model):
    """Key-value pairs of instance details in the legacy format.

    :param project: Identifies the name of the instance provisioned by the user.
    :type project: str
    """

    _attribute_map = {
        'project': {'key': 'project', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InfoField, self).__init__(**kwargs)
        self.project = kwargs.get('project', None)


class MeterInfo(msrest.serialization.Model):
    """Detailed information about the meter.

    :param meter_id: The unique identifier of the resource.
    :type meter_id: str
    :param meter_name: The name of the meter, within the given meter category.
    :type meter_name: str
    :param meter_category: The category of the meter, e.g., 'Cloud services', 'Networking', etc..
    :type meter_category: str
    :param meter_sub_category: The subcategory of the meter, e.g., 'A6 Cloud services',
     'ExpressRoute (IXP)', etc..
    :type meter_sub_category: str
    :param unit: The unit in which the meter consumption is charged, e.g., 'Hours', 'GB', etc.
    :type unit: str
    :param meter_tags: Provides additional meter data. 'Third Party' indicates a meter with no
     discount. Blanks indicate First Party.
    :type meter_tags: list[str]
    :param meter_region: The region in which the Azure service is available.
    :type meter_region: str
    :param meter_rates: The list of key/value pairs for the meter rates, in the format
     'key':'value' where key = the meter quantity, and value = the corresponding price.
    :type meter_rates: dict[str, float]
    :param effective_date: Indicates the date from which the meter rate is effective.
    :type effective_date: ~datetime.datetime
    :param included_quantity: The resource quantity that is included in the offer at no cost.
     Consumption beyond this quantity will be charged.
    :type included_quantity: float
    """

    _attribute_map = {
        'meter_id': {'key': 'MeterId', 'type': 'str'},
        'meter_name': {'key': 'MeterName', 'type': 'str'},
        'meter_category': {'key': 'MeterCategory', 'type': 'str'},
        'meter_sub_category': {'key': 'MeterSubCategory', 'type': 'str'},
        'unit': {'key': 'Unit', 'type': 'str'},
        'meter_tags': {'key': 'MeterTags', 'type': '[str]'},
        'meter_region': {'key': 'MeterRegion', 'type': 'str'},
        'meter_rates': {'key': 'MeterRates', 'type': '{float}'},
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'included_quantity': {'key': 'IncludedQuantity', 'type': 'float'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MeterInfo, self).__init__(**kwargs)
        self.meter_id = kwargs.get('meter_id', None)
        self.meter_name = kwargs.get('meter_name', None)
        self.meter_category = kwargs.get('meter_category', None)
        self.meter_sub_category = kwargs.get('meter_sub_category', None)
        self.unit = kwargs.get('unit', None)
        self.meter_tags = kwargs.get('meter_tags', None)
        self.meter_region = kwargs.get('meter_region', None)
        self.meter_rates = kwargs.get('meter_rates', None)
        self.effective_date = kwargs.get('effective_date', None)
        self.included_quantity = kwargs.get('included_quantity', None)


class OfferTermInfo(msrest.serialization.Model):
    """Describes the offer term.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: MonetaryCommitment, MonetaryCredit, RecurringCharge.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the offer term.Constant filled by server.  Possible values
     include: "Recurring Charge", "Monetary Commitment", "Monetary Credit".
    :type name: str or ~azure.mgmt.commerce.models.OfferTermInfoEnum
    :param effective_date: Indicates the date from which the offer term is effective.
    :type effective_date: ~datetime.datetime
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
    }

    _subtype_map = {
        'name': {'Monetary Commitment': 'MonetaryCommitment', 'Monetary Credit': 'MonetaryCredit', 'Recurring Charge': 'RecurringCharge'}
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OfferTermInfo, self).__init__(**kwargs)
        self.name = None  # type: Optional[str]
        self.effective_date = kwargs.get('effective_date', None)


class MonetaryCommitment(OfferTermInfo):
    """Indicates that a monetary commitment is required for this offer.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the offer term.Constant filled by server.  Possible values
     include: "Recurring Charge", "Monetary Commitment", "Monetary Credit".
    :type name: str or ~azure.mgmt.commerce.models.OfferTermInfoEnum
    :param effective_date: Indicates the date from which the offer term is effective.
    :type effective_date: ~datetime.datetime
    :param tiered_discount: The list of key/value pairs for the tiered meter rates, in the format
     'key':'value' where key = price, and value = the corresponding discount percentage. This field
     is used only by offer terms of type 'Monetary Commitment'.
    :type tiered_discount: dict[str, float]
    :param excluded_meter_ids: An array of meter ids that are excluded from the given offer terms.
    :type excluded_meter_ids: list[str]
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'tiered_discount': {'key': 'TieredDiscount', 'type': '{float}'},
        'excluded_meter_ids': {'key': 'ExcludedMeterIds', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MonetaryCommitment, self).__init__(**kwargs)
        self.name = 'Monetary Commitment'  # type: str
        self.tiered_discount = kwargs.get('tiered_discount', None)
        self.excluded_meter_ids = kwargs.get('excluded_meter_ids', None)


class MonetaryCredit(OfferTermInfo):
    """Indicates that this is a monetary credit offer.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the offer term.Constant filled by server.  Possible values
     include: "Recurring Charge", "Monetary Commitment", "Monetary Credit".
    :type name: str or ~azure.mgmt.commerce.models.OfferTermInfoEnum
    :param effective_date: Indicates the date from which the offer term is effective.
    :type effective_date: ~datetime.datetime
    :param credit: The amount of credit provided under the terms of the given offer level.
    :type credit: float
    :param excluded_meter_ids: An array of meter ids that are excluded from the given offer terms.
    :type excluded_meter_ids: list[str]
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'credit': {'key': 'Credit', 'type': 'float'},
        'excluded_meter_ids': {'key': 'ExcludedMeterIds', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MonetaryCredit, self).__init__(**kwargs)
        self.name = 'Monetary Credit'  # type: str
        self.credit = kwargs.get('credit', None)
        self.excluded_meter_ids = kwargs.get('excluded_meter_ids', None)


class RateCardQueryParameters(msrest.serialization.Model):
    """Parameters that are used in the odata $filter query parameter for providing RateCard information.

    All required parameters must be populated in order to send to Azure.

    :param offer_durable_id: Required. The Offer ID parameter consists of the 'MS-AZR-' prefix,
     plus the Offer ID number (e.g., MS-AZR-0026P). See https://azure.microsoft.com/en-
     us/support/legal/offer-details/ for more information on the list of available Offer IDs,
     country/region availability, and billing currency.
    :type offer_durable_id: str
    :param currency: Required. The currency in which the rates need to be provided.
    :type currency: str
    :param locale: Required. The culture in which the resource metadata needs to be localized.
    :type locale: str
    :param region_info: Required. 2 letter ISO code where the offer was purchased.
    :type region_info: str
    """

    _validation = {
        'offer_durable_id': {'required': True, 'pattern': r'^MS-AZR-\d{4}P(-\d{4}P)*$'},
        'currency': {'required': True},
        'locale': {'required': True},
        'region_info': {'required': True},
    }

    _attribute_map = {
        'offer_durable_id': {'key': 'OfferDurableId', 'type': 'str'},
        'currency': {'key': 'Currency', 'type': 'str'},
        'locale': {'key': 'Locale', 'type': 'str'},
        'region_info': {'key': 'RegionInfo', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RateCardQueryParameters, self).__init__(**kwargs)
        self.offer_durable_id = kwargs['offer_durable_id']
        self.currency = kwargs['currency']
        self.locale = kwargs['locale']
        self.region_info = kwargs['region_info']


class RecurringCharge(OfferTermInfo):
    """Indicates a recurring charge is present for this offer.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the offer term.Constant filled by server.  Possible values
     include: "Recurring Charge", "Monetary Commitment", "Monetary Credit".
    :type name: str or ~azure.mgmt.commerce.models.OfferTermInfoEnum
    :param effective_date: Indicates the date from which the offer term is effective.
    :type effective_date: ~datetime.datetime
    :param recurring_charge: The amount of recurring charge as per the offer term.
    :type recurring_charge: int
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'effective_date': {'key': 'EffectiveDate', 'type': 'iso-8601'},
        'recurring_charge': {'key': 'RecurringCharge', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RecurringCharge, self).__init__(**kwargs)
        self.name = 'Recurring Charge'  # type: str
        self.recurring_charge = kwargs.get('recurring_charge', None)


class ResourceRateCardInfo(msrest.serialization.Model):
    """Price and Metadata information for resources.

    :param currency: The currency in which the rates are provided.
    :type currency: str
    :param locale: The culture in which the resource information is localized.
    :type locale: str
    :param is_tax_included: All rates are pretax, so this will always be returned as 'false'.
    :type is_tax_included: bool
    :param offer_terms: A list of offer terms.
    :type offer_terms: list[~azure.mgmt.commerce.models.OfferTermInfo]
    :param meters: A list of meters.
    :type meters: list[~azure.mgmt.commerce.models.MeterInfo]
    """

    _attribute_map = {
        'currency': {'key': 'Currency', 'type': 'str'},
        'locale': {'key': 'Locale', 'type': 'str'},
        'is_tax_included': {'key': 'IsTaxIncluded', 'type': 'bool'},
        'offer_terms': {'key': 'OfferTerms', 'type': '[OfferTermInfo]'},
        'meters': {'key': 'Meters', 'type': '[MeterInfo]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ResourceRateCardInfo, self).__init__(**kwargs)
        self.currency = kwargs.get('currency', None)
        self.locale = kwargs.get('locale', None)
        self.is_tax_included = kwargs.get('is_tax_included', None)
        self.offer_terms = kwargs.get('offer_terms', None)
        self.meters = kwargs.get('meters', None)


class UsageAggregation(msrest.serialization.Model):
    """Describes the usageAggregation.

    :param id: Unique Id for the usage aggregate.
    :type id: str
    :param name: Name of the usage aggregate.
    :type name: str
    :param type: Type of the resource being returned.
    :type type: str
    :param subscription_id: The subscription identifier for the Azure user.
    :type subscription_id: str
    :param meter_id: Unique ID for the resource that was consumed (aka ResourceID).
    :type meter_id: str
    :param usage_start_time: UTC start time for the usage bucket to which this usage aggregate
     belongs.
    :type usage_start_time: ~datetime.datetime
    :param usage_end_time: UTC end time for the usage bucket to which this usage aggregate belongs.
    :type usage_end_time: ~datetime.datetime
    :param quantity: The amount of the resource consumption that occurred in this time frame.
    :type quantity: float
    :param unit: The unit in which the usage for this resource is being counted, e.g. Hours, GB.
    :type unit: str
    :param meter_name: Friendly name of the resource being consumed.
    :type meter_name: str
    :param meter_category: Category of the consumed resource.
    :type meter_category: str
    :param meter_sub_category: Sub-category of the consumed resource.
    :type meter_sub_category: str
    :param meter_region: Region of the meterId used for billing purposes.
    :type meter_region: str
    :param info_fields: Key-value pairs of instance details (legacy format).
    :type info_fields: ~azure.mgmt.commerce.models.InfoField
    :param instance_data: Key-value pairs of instance details represented as a string.
    :type instance_data: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'subscription_id': {'key': 'properties.subscriptionId', 'type': 'str'},
        'meter_id': {'key': 'properties.meterId', 'type': 'str'},
        'usage_start_time': {'key': 'properties.usageStartTime', 'type': 'iso-8601'},
        'usage_end_time': {'key': 'properties.usageEndTime', 'type': 'iso-8601'},
        'quantity': {'key': 'properties.quantity', 'type': 'float'},
        'unit': {'key': 'properties.unit', 'type': 'str'},
        'meter_name': {'key': 'properties.meterName', 'type': 'str'},
        'meter_category': {'key': 'properties.meterCategory', 'type': 'str'},
        'meter_sub_category': {'key': 'properties.meterSubCategory', 'type': 'str'},
        'meter_region': {'key': 'properties.meterRegion', 'type': 'str'},
        'info_fields': {'key': 'properties.infoFields', 'type': 'InfoField'},
        'instance_data': {'key': 'properties.instanceData', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UsageAggregation, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.meter_id = kwargs.get('meter_id', None)
        self.usage_start_time = kwargs.get('usage_start_time', None)
        self.usage_end_time = kwargs.get('usage_end_time', None)
        self.quantity = kwargs.get('quantity', None)
        self.unit = kwargs.get('unit', None)
        self.meter_name = kwargs.get('meter_name', None)
        self.meter_category = kwargs.get('meter_category', None)
        self.meter_sub_category = kwargs.get('meter_sub_category', None)
        self.meter_region = kwargs.get('meter_region', None)
        self.info_fields = kwargs.get('info_fields', None)
        self.instance_data = kwargs.get('instance_data', None)


class UsageAggregationListResult(msrest.serialization.Model):
    """The Get UsageAggregates operation response.

    :param value: Gets or sets details for the requested aggregation.
    :type value: list[~azure.mgmt.commerce.models.UsageAggregation]
    :param next_link: Gets or sets the link to the next set of results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[UsageAggregation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UsageAggregationListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)
