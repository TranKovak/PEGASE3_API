---
cssclass: blueTable, wideTable
---
# Description
URL : <b>https://........../company/info</b>
Allows you to get data about your company.

***

## Parameters

| Fields                                         | Type         | Description                                                        |
| :--------------------------------------------- | :----------- | :----------------------------------------------------------------- |
| Token <span style="color: red">*</span>        | string       | Authentification token.                                            |
| Fields                                         | string, list | Fields you want to get from the database (see list of [[Fields]]). |              
| Name-Company <span style="color: red">*</span> | string       | Name of the company.                                               |

<span style="color: red">*</span> — Required parameter.

***

## Response

| Fields  | Type              | Description                                                         |
| :------ | :---------------- | :------------------------------------------------------------------ |
| status  | string            | "ok" or "error".                                                    |
| code    | int               | Execution status code (See [[Common API code]]).                    |
| data    | associative array | If status = "ok". Data about the company with asked fields as keys. |
| message | string            | If status = "error". Describes the encoutered error.                |

***

## Error

| Code | Message                                     | Description                                                                          |
| :--- | :------------------------------------------ | : ---------------------------------------------------------------------------------- |
| 402  | Required field < HEADER > is not specified. | HEADER is missing.                                                                   |
| 402  | Required field < HEADER > is empty.         | HEADER is empty and shouldn't.                                                       |
| 404  | Field < FIELD > not found.                  | FIELD not found in the list of fields available for company.                         |
| 404  | Data not found.                             | Data not found in database. Could be because of an error in the name of the company. |   

See [[Common API code]]

***

## Example

Request on : https://............../company/info with those headers :
- Token : XXXXXXXXXXXXXXXX
- Name-Company : Test
- Fields : NOMSOCIETE,CODETABPRINCIPAL

Response :

```
{
	"code": 200,
	"data": {
		"NOMSOCIETE": "TEST SA",
		"CODETABPRINCIPAL": "00001"
	},
	"status": "ok"
}
```