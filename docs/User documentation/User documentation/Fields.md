---
cssclass: blueTable, wideTable
---

# Available Fields
***

## Company

| Field            | Type   | Description                                                       |
| :--------------- | :----- | :---------------------------------------------------------------- | 
| IDSOCIETE        | int    | Id of the society in the database. Usefull in a lot of API calls. |   
| NOMSOCIETE       | string | Name of the society.                                              |
| ADR1             | string | First part of the address of the society.                         |
| ADR2             | string | Second part of the address of the society.                        |
| ADR3             | string | Third part of the address of the society.                         |
| ADRCPOST         | string | Postal code of the address of the society.                        |
| ADRBDIST         | string | City of the address of the society.                               |
| NUMSIREN         | string | SIREN number of the society.                                      |
| NAF              | string | NAF code of the society.                                          |
| CODETABPRINCIPAL | string | Code of the main establishment.                                   |

***

## Employee

| Field         | Type      | Description                                                    |
| :------------ | :-------- | :------------------------------------------------------------- |
| NOM           | string    | Last name of the employee.                                     |
| PRENOM        | string    | First name of the employee.                                    |
| ADR1          | string    | First part of the address of the employee.                     |
| ADR2          | string    | Second part of the address of the employee.                    |
| ADR3          | string    | Third part of the address of the employee.                     |
| ADRCPOST      | string    | Postal code of the address of the employee.                    |
| ADRBDIST      | string    | City of the address of the employee.                           |
| NUMSECU       | string    | Security number of the employee.                               |
| EMPLOI        | string    | Name of the job of the employee.                               |
| CODSALARIE    | string    | Employee's code. Usefull in other API calls.                   |
| DATANCIENNETE | timestamp | Date at which the employee entered the society. **GMT +01:00** |

***

## Establishment

| Field             | Type   | Description                                          |
| :---------------- | :----- | :--------------------------------------------------- |
| CODETAB           | string | Code of the establishment.                           |
| NOMETAB           | string | Name of the establishment.                           |
| ADR1              | string | First part of the address of the establishment.      |
| ADR2              | string | Second part of the address of the establishment.     |
| ADR3              | string | Third part of the address of the establishment.      |
| ADRCPOST          | string | Postal code of the address of the establishment.     |
| ADRBDIST          | string | City of the address of the establishment.            |
| NIC               | string | NIC code of the establishment.                       |
| NAF               | string | NAF code of the establishment.                       |
| NOMRESP           | string | Name of the employee in charge of the establishment. |
| QUALITERESP       | string | Job of the employee in charge of the establishment.  |
| NOMSIGNATAIRE     | string | Naem of the signatory of the establishment.          |
| QUALITESIGNATAIRE | string | Job of the signatory of the establishment.           |

***

## Report

| Field         | Type      | Description                                                          |
| :------------ | :-------- | :------------------------------------------------------------------- |
| CODETAB       | string    | Code of the establishment.                                           |
| CODSALARIE    | string    | Employee's code.                                                     |
| CODEXERCICE   | string    | Year of the report.                                                  |
| CODPERIODE    | string    | Month of the report.                                                 |
| DATDEBUTPAIE  | timestamp | Date of the beginning of the paiement period. **GMT +01:00**         |
| DATFINPAIE    | timestamp | Date of the ending of the paiement period. **GMT +01:00**            |
| DATREMISEPAIE | timestamp | Date of paiement. **GMT +01:00**                                     |

***

## Report details

| Field       | Type   | Description                |
| :---------- | :----- | :------------------------- |
| CODETAB     | string | Code of the establishment. |
| CODSALARIE  | string | Employee's code.           |
| CODEXERCICE | string | Year of the report.        |
| CODBULLETIN | int    | ???                        |
| CODPERIODE  | string | Month of the report.       |
| CODRUBRIQUE | string | Code of the report detail. |
| NOM         | string | Name of the report detail. |

***

## Sections

| Field        | Type   | Description                 |
| :----------- | :----- | :-------------------------- |
| CODRUBRIQUE  | string | Code of the section.        |
| CODPROFIL    | string | ???                         |
| NOM          | string | Name of the section.        |
| ZONEBULLETIN | int    | Report zone of the section. |

***

## Holidays

| Field  | Type      | Description                |
| :----- | :-------- | :------------------------- |
| DATEJF | timestamp | Date of the public holiday |