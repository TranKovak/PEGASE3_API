---
cssclass: blueTable, wideTable
---

# Description
URL : <b>https://........../company/sections</b>
Allows you to get data about sections of the company.

***

## Parameters

| Fields                                       | Type         | Description                                                        |
| :------------------------------------------- | :----------- | :----------------------------------------------------------------- |
| Token <span style="color: red">*</span>      | string       | Authentification token.                                            |
| Fields                                       | string, list | Fields you want to get from the database (see list of [[Fields]]). |
| Id-Company <span style="color: red">*</span> | string       | Id of the company.                                                 |

<span style="color: red">*</span> — Required parameter.

***

## Response

| Fields  | Type              | Description                                                                |
| :------ | :---------------- | :------------------------------------------------------------------------- |
| status  | string            | "ok" or "error".                                                           |
| code    | int               | Execution status code (See [[Common API code]]).                           |
| data    | associative array | If status = "ok". Data about company's sections with asked fields as keys. |
| message | string            | If status = "error". Describes the encoutered error.                       |

***

## Error

| Code | Message                                     | Description                                                                          |
| :--- | :------------------------------------------ | : ---------------------------------------------------------------------------------- |
| 402  | Required field < HEADER > is not specified. | HEADER is missing.                                                                   |
| 402  | Required field < HEADER > is empty.         | HEADER is empty and shouldn't.                                                       |
| 404  | Field < FIELD > not found.                  | FIELD not found in the list of fields available for company sections.                |   
| 404  | Data not found.                             | Data not found in database.                                                          |   

See [[Common API code]]

***

## Example

Request on : https://............../company/sections with those headers :
- Token : XXXXXXXXXXXXXXXX
- Id-Company : 001
- Fields : CODRUBRIQUE,NOM

Response :

```
{
	"code": 200,
	"data": [
		{
			"CODRUBRIQUE": "380000",
			"NOM": "Absences congés payés"
		},
		{
			"CODRUBRIQUE": "183600",
			"NOM": "Accident Insurance"
		},
		{
			"CODRUBRIQUE": "783005",
			"NOM": "Accident Insurance (No Benefit)"
		},
		{
			"CODRUBRIQUE": "930002",
			"NOM": "Acompte (premier paiement)"
		},
		{
			"CODRUBRIQUE": "930001",
			"NOM": "Acompte sur salaire"
		},
		{
			"CODRUBRIQUE": "394610",
			"NOM": "Act. partielle : Indemn. (employeur) régul 03/2020"
		},
		{
			"CODRUBRIQUE": "394400",
			"NOM": "Act. partielle Allocation (Etat)"
		},
	  	[...]
	],
	"status": "ok"
}
		
```