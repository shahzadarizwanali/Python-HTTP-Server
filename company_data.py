companies = {
    "TechMatrix": {
        "owner": "Hassan",
        "address": "DHA phase 3",
        "zip": "54000",
        "country": "Pakistan",
    },
    "GreenSolutions": {
        "owner": "Awais",
        "address": "45 Ali view Garden",
        "zip": "45600",
        "country": "Pakistan",
    },
    "Synares": {
        "owner": "Asif Malik",
        "address": "Dha Phase 8",
        "zip": "89256",
        "country": "Pakistan",
    },
    "Netsol": {
        "owner": "Salim ghauri",
        "address": "452 Airport Road",
        "zip": "98742",
        "country": "Pakistan",
    },
}


def list_companies():
    return list(companies.keys())


def get_company(name):
    return companies.get(name, {"error": "Company not found"})
