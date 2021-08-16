---
cssclass: blueTable, wideTable
---

# Description
URL : <b>https://........../report/info</b>
Allows you to get information about reports details.

***

## Parameters

| Fields                                             | Type         | Description                                                                         |
| :------------------------------------------------- | :----------- | :---------------------------------------------------------------------------------- |
| Token <span style="color: red">*</span>            | string       | Authentification token.                                                             |
| Fields                                             | string, list | Fields you want to get from the database (see list of [[Fields]]).                  |              
| Id-Company <span style="color: red">*</span>       | string       | Id of the company.                                                                  |
| Id-Establishments                                  | string, list | Id of the establishment(s).                                                         |
| Id-Employees <span style="color: red">*</span>     | string, list | Id of the employee(s).                                                              |
| Years <span style="color: red">*</span>            | string, list | Years for which you search reports.                                                 |
| Months <span style="color: red">*</span>           | string, list | Months for which you search reports.                                                |
| Limit                                              | int          | Limit the number of rows to be returned by a query.                                 |           
| Offset                                             | int          | Specifies the number of rows to skip before starting to return rows from the query. |

<span style="color: red">*</span> — Required parameter.

***

## Response

| Fields  | Type              | Description                                                         |
| :------ | :---------------- | :------------------------------------------------------------------ |
| status  | string            | "ok" or "error".                                                    |
| code    | int               | Execution status code (See [[Common API code]]).                    |
| data    | associative array | If status = "ok". Data about the reports details.                   |
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

Request on : https://............../report/details with those headers :
- Token : XXXXXXXXXXXXXXXX
- Id-Company : 001
- Id-Employees : 10035,10049
- Years : 2019
- Months : 08,09,10

Response :

```
{
	"code": 200,
	"data": {
		"10035": {
			"2019": {
				"08": [
					{
						"CODBULLETIN": 6,
						"CODETAB": "00001",
						"CODEXERCICE": "2019",
						"CODPERIODE": "08",
						"CODRUBRIQUE": "001600",
						"CODSALARIE": "10035",
						"NOM": "Nb jours calendaires du mois"
					},
					[...]
				],
				"09": [
					[...]
				]
				[...]
	"status": "ok"
}
		
```