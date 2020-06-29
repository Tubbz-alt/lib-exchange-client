# BaseOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ord_type** | **str** |  | [optional] 
**cl_ord_id** | **str** | Reference field provided by client and cannot exceed 20 characters | 
**symbol** | **str** | Blockchain symbol identifier | 
**side** | [**Side**](Side.md) |  | 
**order_qty** | **float** | The order size in the terms of the base currency | 
**time_in_force** | [**TimeInForce**](TimeInForce.md) |  | [optional] 
**price** | **float** | The limit price for the order | [optional] 
**expire_date** | **int** | expiry date in the format YYYYMMDD | [optional] 
**min_qty** | **float** | The minimum quantity required for an IOC fill | [optional] 
**stop_px** | **float** | The limit price for the order | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

