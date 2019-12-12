import ql

ql.get(
    {
        "query": """{
    organization(login: "ucsb-cs16-mirza") {
            membersWithRole {
                nodes {
                    name
                }
            }
        }
    }"""
    }
)

