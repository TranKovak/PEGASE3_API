---
cssclass: blueTable, wideTable
---

# Description
URL : <b>https://........../employee/list</b>
Allows you to get a list of all the employees of your company.
As data you'll get :
- NOM
- PRENOM
- CODSALARIE
- CODETAB

***

## Parameters

| Fields                                       | Type         | Description                                                                         |
| :------------------------------------------- | :----------- | :---------------------------------------------------------------------------------- |
| Token <span style="color: red">*</span>      | string       | Authentification token.                                                             |
| Id-Company <span style="color: red">*</span> | string       | Id of the company.                                                                  |
| Id-Establishment                             | string, list | Id of the establishment(s) you want to the list of employees.                       |
| Limit                                        | int          |  Limit the number of rows to be returned by a query.                                |           
| Offset                                       | int          | Specifies the number of rows to skip before starting to return rows from the query. |

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
| 404  | Data not found.                             | Data not found in database.                                                          |   

See [[Common API code]]

***

## Example

Request on : https://............../employee/list with those headers :
- Token : XXXXXXXXXXXXXXXX
- Id-Company : 001

Response :

```
{
	"code": 200,
	"data": [
		{
			"CODETAB": "00001",
			"CODSALARIE": "00001",
			"NOM": "DUPONT",
			"PRENOM": "Jean"
		},
		{
			"CODETAB": "00001",
			"CODSALARIE": "00009",
			"NOM": "DUPONT",
			"PRENOM": "Sonia"
		},
		{
			"CODETAB": "00001",
			"CODSALARIE": "46380",
			"NOM": "DUPONT",
			"PRENOM": "Ismael"
		},
		{
			"CODETAB": "00001",
			"CODSALARIE": "60113",
			"NOM": "DUPONT",
			"PRENOM": "Jessica"
		},
		[...]
	],
	"status": "ok"
}
		
```