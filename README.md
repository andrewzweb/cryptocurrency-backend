# cryptocurrency-backend

A backend that allows users to look at the list of cryptocurrencies.
Registration users can add currencies to their dashboard, which is updated in real time when the price changes.

## Requirements 

Check doc how make enviroments [make-workspace](doc/make-workflow.md)

# Backend look like RESTApi 


Currency
---

| URL             | Method | Result                 |
| -----           | -----  | -----                  |
| api/currency/   | GET    | Get list all currency  |
| api/currency/   | POST   | Create currency item   |
| api/currency/id | GET    | Get currency item data |
| api/currency/id | PUT    | Update currency item   |
| api/currency/id | DELETE | Delete currency item   |

Dashboard
---

| URL              | Method | Result                  |
| -----            | -----  | -----                   |
| api/dashboard/   | GET    | Get list all dashboard  |
| api/dashboard/   | POST   | Create dashboard item   |
| api/dashboard/id | GET    | Get dashboard item data |
| api/dashboard/id | PUT    | Update dashboard item   |
| api/dashboard/id | DELETE | Delete dashboard item   |

User
---

| URL                 | Method | Result           |
| -----               | -----  | -----            |
| account/login/      | POST   | Login user       |
| account/logout/     | GET    | Logout user      |
| account/token-auth/ | GET    | Get token data   |
| api/current_user/   | GET    | Return user name |
| api/user/           | POST   | Create new user  |





