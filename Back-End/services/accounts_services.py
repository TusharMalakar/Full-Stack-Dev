import json
from data.database import cursor


def getallaccounts():
    try:
        accounts = cursor.execute('select * from [dbo].[Account]').fetchall()
        if accounts is None:
            return json.dumps({'error': "No account details found"})
        else:
            return json.dumps(accounts)
    except Exception:
        return json.dumps({'error': "Server error while checking database"})

