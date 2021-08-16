---
cssclass: blueTable, wideTable
---

# Description
URL : <b>https://........../report/info</b>
Allows you to get information about reports of employees of your company.

***

## Parameters

| Fields                                             | Type         | Description                                                                         |
| :------------------------------------------------- | :----------- | :---------------------------------------------------------------------------------- |
| Token <span style="color: red">*</span>            | string       | Authentification token.                                                             |
| Fields                                             | string, list | Fields you want to get from the database (see list of [[Fields]]).                  |              
| Id-Company <span style="color: red">*</span>       | string       | Id of the company.                                                                  |
| Id-Establishments                                  | string, list | Id of the establishment(s).                                                         |
| Id-Employees                                       | string, list | Id of the employee(s).                                                              |
| Years                                              | string, list | Years for which you search reports.                                                 |
| Months                                             | string, list | Months for which you search reports.                                                |
| Limit                                              | int          | Limit the number of rows to be returned by a query.                                 |           
| Offset                                             | int          | Specifies the number of rows to skip before starting to return rows from the query. |

<span style="color: red">*</span> — Required parameter.

***

## Response

| Fields  | Type              | Description                                                         |
| :------ | :---------------- | :------------------------------------------------------------------ |
| status  | string            | "ok" or "error".                                                    |
| code    | int               | Execution status code (See [[Common API code]]).                    |
| data    | associative array | If status = "ok". Data about the reports.                           |
| message | string            | If status = "error". Describes the encoutered error.                |

***

## Error

| Code | Message                                     | Description                                                                          |
| :--- | :------------------------------------------ | : ---------------------------------------------------------------------------------- |
| 402  | Required field < HEADER > is not specified. | HEADER is missing.                                                                   |
| 402  | Required field < HEADER > is empty.         | HEADER is empty and shouldn't.                                                       |
| 404  | Field < FIELD > not found.                  | FIELD not found in the list of fields available for report sections.                 |   
| 404  | Data not found.                             | Data not found in database.                                                          |   

See [[Common API code]]

***

## Example

Request on : https://............../report/info with those headers :
- Token : XXXXXXXXXXXXXXXX
- Id-Company : 001

Response :

```
{
	"code": 200,
	"data": [
		{
			"CODETAB": "00001",	
			"CODEXERCICE": "2015",
			"CODPERIODE": "12",
			"CODSALARIE": "7037",
			"DATDEBUTPAIE": 1449442800.0,
			"DATFINPAIE": 1451516400.0,
			"DATREMISEPAIE": 1451516400.0
		},
		[...]	
	],
	"status": "ok"
}
		
```