---
cssclass: blueTable, wideTable
---

# COMMON API CODE

| Code | Status | Message                                               | Description                                                             |
| :--- | :----- | :---------------------------------------------------- | :---------------------------------------------------------------------- |
| 200  | ok     |                                                       | Call is a success and returns data.                                     |
| 201  | ok     | User created.                                         | Call is a success and created data.									  |
| 401  | error  | Token not valid.			                            | The provided authentification token is not valid.                       |  
| 401  | error  | User doesn't exists.			                        | Password and User-Name does not match any user.                         |  
| 402  | error  | Required field < HEADER > is not specified. 			| HEADER is missing.                                                      |
| 402  | error  | Required field < HEADER > is empty.         			| HEADER is empty and shouldn't.                                          |
| 404  | error  | Field < field > not found.                            | FIELD not found in the list of fields available for the thing you query |  
| 404  | error  | Data not found.                                       | Data not found in database. Could be because of a typo in headers       |  
| 498  | ok     | Token has expired.                                    | The authentification token provided has expired.                        |