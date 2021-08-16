---
cssclass: blueTable, wideTable
---

# Description
URL : <b>https://........../login</b>
Allows you to get get your authentification token.

***

## Parameters

| Fields                                      | Type   | Description                                                                         |
| :------------------------------------------ | :----- | :-------------- |
| Password <span style="color: red">*</span>  | string | Your password.  |
| User-Name <span style="color: red">*</span> | string | Your user name. |

<span style="color: red">*</span> — Required parameter.

***

## Response

| Fields  | Type              | Description                                                                   |
| :------ | :---------------- | :---------------------------------------------------------------------------- |
| status  | string            | "ok" or "error".                                                              |
| code    | int               | Execution status code (See [[Common API code]]).                              |
| token   | associative array | If status = "ok". Your authentification token, works for the next 30 minutes. |
| message | string            | If status = "error". Describes the encoutered error.                          |

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

Request on : https://............../login with those headers :
- Password : password_test
- User-Name : user_test

Response :

```
{
	"code": 200,
	"status": "ok",
	"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidXNlcl90ZXN0IiwiZXhwIjoxNjI4NjA1MjA2fQ.sFG8WK8b509wAKSilBylyavIQr_yBuz4vueyzogMjZo"
}
		
```