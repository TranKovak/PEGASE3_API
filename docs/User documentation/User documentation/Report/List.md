---
cssclass: blueTable, wideTable
---

# Description
URL : <b>https://........../report/list</b>
Allows you to get a list of all the reports of the employees of your company.

***

## Parameters

| Fields                                         | Type         | Description                                                                         |
| :--------------------------------------------- | :----------- | :---------------------------------------------------------------------------------- |
| Token <span style="color: red">*</span>        | string       | Authentification token.                                                             |
| Id-Company <span style="color: red">*</span>   | string       | Id of the company.                                                                  |
| Id-Establishments                              | string, list | Id of the establishment(s).                                                         |
| Id-Employees                                   | string, list | Id of the employee(s).                                                              |
| Years                                          | string, list | Years for which you search reports.                                                 |
| Months                                         | string, list | Months for which you search reports.                                                |
| Limit                                          | int          |  Limit the number of rows to be returned by a query.                                |           
| Offset                                         | int          | Specifies the number of rows to skip before starting to return rows from the query. |

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
| 404  | Data not found.                             | Data not found in database.                                                          |   

See [[Common API code]]

***

## Example

Request on : https://............../establishment/list with those headers :
- Token : XXXXXXXXXXXXXXXX
- Id-Company : 001
- Years : 2019
- Months : 06,07,08

Response :

```
{
	"code": 200,
	"data": [
		{
			"CODETAB": "00001",
			"CODEXERCICE": "2019",
			"CODPERIODE": "06",
			"CODSALARIE": "10035"
		},
		[...]
	],
	"status": "ok"
}		
```