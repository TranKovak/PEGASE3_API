---
cssclass: blueTable, wideTable
---

# Description
URL : <b>https://........../establishment/list</b>
Allows you to get a list of all the establishment of your company.

***

## Parameters

| Fields                                         | Type         | Description                                                                         |
| :--------------------------------------------- | :----------- | :---------------------------------------------------------------------------------- |
| Token <span style="color: red">*</span>        | string       | Authentification token.                                                             |
| Id-Company <span style="color: red">*</span>   | string       | Id of the company.                                                                  |
| Limit                                          | int          |  Limit the number of rows to be returned by a query.                                |           
| Offset                                         | int          | Specifies the number of rows to skip before starting to return rows from the query. |

<span style="color: red">*</span> — Required parameter.

***

## Response

| Fields  | Type              | Description                                                         |
| :------ | :---------------- | :------------------------------------------------------------------ |
| status  | string            | "ok" or "error".                                                    |
| code    | int               | Execution status code (See [[Common API code]]).                    |
| data    | associative array | If status = "ok". Data about the establishments.                    |
| message | string            | If status = "error". Describes the encoutered error.                |

***

## Error

| Code | Message                                     | Description                                                                          |
| :--- | :------------------------------------------ | : ---------------------------------------------------------------------------------- |
| 402  | Required field < HEADER > is not specified. | HEADER is missing.                                                                   |
| 402  | Required field < HEADER > is empty.         | HEADER is empty and shouldn't.                                                       |  
| 404  | Data not found.                             | Data not found in database.                                                          |   

See [[Common API code]]

***

## Example

Request on : https://............../establishment/list with those headers :
- Token : XXXXXXXXXXXXXXXX
- Id-Company : 001

Response :

```
{
	"code": 200,
	"data": [
		{
			"CODETAB": "00001",
			"NOMETAB": "XXXXXXX"
		},
		{
			"CODETAB": "00002",
			"NOMETAB": "XXXXXXX"
		},
		{
			"CODETAB": "00003",
			"NOMETAB": "XXXXXXX"
		},
		{
			"CODETAB": "00004",
			"NOMETAB": "XXXXXXX"
		},
		{
			"CODETAB": "00005",
			"NOMETAB": "XXXXXXX"
		},
		{
			"CODETAB": "00006",
			"NOMETAB": "XXXXXXX"
		}
	],
	"status": "ok"
}		
```