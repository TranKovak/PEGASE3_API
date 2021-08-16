---
cssclass: blueTable, wideTable
---

# Description
URL : <b>https://........../establishment/info</b>
Allows you to get information about establishments of your company.

***

## Parameters

| Fields                                             | Type         | Description                                                                         |
| :------------------------------------------------- | :----------- | :---------------------------------------------------------------------------------- |
| Token <span style="color: red">*</span>            | string       | Authentification token.                                                             |
| Fields                                             | string, list | Fields you want to get from the database (see list of [[Fields]]).                  |              
| Id-Company <span style="color: red">*</span>       | string       | Id of the company.                                                                  |
| Id-Establishment <span style="color: red">*</span> | string, list | Id of the establishment(s).                             |
| Limit                                              | int          |  Limit the number of rows to be returned by a query.                                |           
| Offset                                             | int          | Specifies the number of rows to skip before starting to return rows from the query. |

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
| 404  | Field < FIELD > not found.                  | FIELD not found in the list of fields available for establishment sections.          |   
| 404  | Data not found.                             | Data not found in database.                                                          |   

See [[Common API code]]

***

## Example

Request on : https://............../establishment/info with those headers :
- Token : XXXXXXXXXXXXXXXX
- Id-Company : 001
- Id-Establishments : 00027,00035

Response :

```
{
	"code": 200,
	"data": [
		{
			"ADR1": "XXXXXXXXXXXXXXXXXXX",
			"ADR2": "XXXX",
			"ADR3": null,
			"ADRBDIST": "XXXXXXXXX",
			"ADRCPOST": "XXXXX",
			"CODETAB": "00027",
			"NAF": "XXXXX",
			"NIC": "XXXXX",
			"NOMETAB": "XXXXX",
			"NOMRESP": "XXXX XXXXX",
			"NOMSIGNATAIRE": "XXXX XXXXX",
			"QUALITERESP": "D.R.H.",
			"QUALITESIGNATAIRE": "D.R.H."
		},
		{
			"ADR1": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
			"ADR2": "XXXXXX",
			"ADR3": null,
			"ADRBDIST": "XXXXXXXXXXXX",
			"ADRCPOST": "XXXXXX",
			"CODETAB": "XXXXX",
			"NAF": "XXXXX",
			"NIC": "XXXXX",
			"NOMETAB": "XXXXXXXXX",
			"NOMRESP": "XXXX XXXXXX",
			"NOMSIGNATAIRE": "XXXX XXXXXX",
			"QUALITERESP": "D.R.H.",
			"QUALITESIGNATAIRE": "D.R.H."
		}
	],
	"status": "ok"
}
		
```