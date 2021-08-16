---
cssclass: blueTable, wideTable
---

# Description
URL : <b>https://........../employee/info</b>
Allows you to get information about employees of your company.

***

## Parameters

| Fields                                         | Type         | Description                                                                         |
| :--------------------------------------------- | :----------- | :---------------------------------------------------------------------------------- |
| Token <span style="color: red">*</span>        | string       | Authentification token.                                                             |
| Fields                                         | string, list | Fields you want to get from the database (see list of [[Fields]]).                  |              
| Id-Company <span style="color: red">*</span>   | string       | Id of the company.                                                                  |
| Id-Establishment                               | string, list | Id of the establishment(s) in which is the employee(s).                             |
| Id-Employees <span style="color: red">*</span> | string, list | Id of the employee(s) you want to the data from.                                    |
| Limit                                          | int          |  Limit the number of rows to be returned by a query.                                |           
| Offset                                         | int          | Specifies the number of rows to skip before starting to return rows from the query. |

<span style="color: red">*</span> — Required parameter.

***

## Response

| Fields  | Type              | Description                                                         |
| :------ | :---------------- | :------------------------------------------------------------------ |
| status  | string            | "ok" or "error".                                                    |
| code    | int               | Execution status code (See [[Common API code]]).                    |
| data    | associative array | If status = "ok". Data about the employees.                         |
| message | string            | If status = "error". Describes the encoutered error.                |

***

## Error

| Code | Message                                     | Description                                                                          |
| :--- | :------------------------------------------ | : ---------------------------------------------------------------------------------- |
| 402  | Required field < HEADER > is not specified. | HEADER is missing.                                                                   |
| 402  | Required field < HEADER > is empty.         | HEADER is empty and shouldn't.                                                       |
| 404  | Field < FIELD > not found.                  | FIELD not found in the list of fields available for employee sections.               |   
| 404  | Data not found.                             | Data not found in database.                                                          |   

See [[Common API code]]

***

## Example

Request on : https://............../employee/info with those headers :
- Token : XXXXXXXXXXXXXXXX
- Id-Company : 001
- Id-Employees : 10035,10049

Response :

```
{
	"code": 200,
	"data": [
		{
			"ADR1": "29 Rue Abbet Coutoure",
			"ADR2": null,
			"ADR3": null,
			"ADRBDIST": "MIRAMAS",
			"ADRCPOST": "13140",
			"CODSALARIE": "10035",
			"DATANCIENNETE": 1545087600.0,
			"EMPLOI": "Copilote",
			"NOM": "PERICHAUD",
			"NUMSECU": "111111111111111",
			"PRENOM": "François"
		},
		{
			"ADR1": "Avenue du Boisyl 9",
			"ADR2": null,
			"ADR3": "1004 LAUSANNE",
			"ADRBDIST": null,
			"ADRCPOST": null,
			"CODSALARIE": "10049",
			"DATANCIENNETE": 1544742000.0,
			"EMPLOI": "Pilote",
			"NOM": "CROUMP",
			"NUMSECU": "222222222222222",
			"PRENOM": "Frédéric"
		},
	],
	"status": "ok"
}
		
```