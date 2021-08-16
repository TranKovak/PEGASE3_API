---
cssclass: blueTable, wideTable
---
# Description
URL : <b>https://........../company/holidays</b>
Allows you to get all the public holidays for a period.

***

## Parameters

| Fields                                         | Type         | Description                                                             |
| :--------------------------------------------- | :----- | :---------------------------------------------------------------------------- |
| Token <span style="color: red">*</span>        | string | Authentification token.                                                       |
| Starting-Date                                  | string | Starting date of the period with this format Year-Day-Month (ex: 2021-01-12). |
| Ending-Date                                    | string | Ending date of the period with this format Year-Day-Month (ex: 2021-01-12).   |

<span style="color: red">*</span> — Required parameter.

***

## Response

| Fields  | Type              | Description                                                         |
| :------ | :---------------- | :------------------------------------------------------------------ |
| status  | string            | "ok" or "error".                                                    |
| code    | int               | Execution status code (See [[Common API code]]).                    |
| data    | associative array | If status = "ok". Data about the public holidays.                   |
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

Request on : https://............../company/holidays with those headers :
- Token : XXXXXXXXXXXXXXXX

Response :

```
{
	"code": 200,
	"data": [
		{
			"DATEJF": 7340400.0
		},
		[...]
	"status": "ok"
	}
```