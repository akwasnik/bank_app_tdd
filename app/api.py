#python3 -m flask --app app/api.py run
from flask import Flask, request, jsonify
from json import dumps
from app.AccountRegistry import AccountRegistry
from app.PersonalAccount import PersonalAccount

app = Flask(__name__)

@app.route("/api/accounts", methods=['POST'])# curl -X POST 127.0.0.1:5000/api/accounts -H "Content-Type: application/json" -d '{"name": "Jan", "surname": "Kowalski", "pesel": "68042661935"}'
def create_account():
    data = request.get_json()
    print(f"Create account request: {data}")
    account=AccountRegistry.search_by_pesel(data["pesel"])
    if account is None:
        konto = PersonalAccount(data["name"], data["surname"], data["pesel"])
        AccountRegistry.add_account(konto)
        return jsonify({"message": "Account created"}), 201
    else:
        return jsonify({"message": "Pesel is in use"}), 409
        

@app.route("/api/accounts/count", methods=['GET'])# curl -X GET 127.0.0.1:5000/api/accounts/count
def account_amount():
    return jsonify({"AccountCount": AccountRegistry.get_accounts_count()}), 200

@app.route("/api/accounts/<pesel>", methods=['GET'])#curl -X GET 127.0.0.1:5000/api/accounts/68042661935
def get_account_by_pesel(pesel):
    account=AccountRegistry.search_by_pesel(pesel)
    if account is not None:
        return jsonify({"name": account.name,"surname": account.surname,"pesel": pesel, "saldo": account.balance}), 200
    else:
        return jsonify({"message": "Account was not found"}), 404

@app.route("/api/accounts/<pesel>", methods=['PATCH'])#curl -X PATCH 127.0.0.1:5000/api/accounts/68042661935 -H "Content-Type: application/json" -d '{"name": "Andrzej"}'
def update_account(pesel):
    data = request.get_json()
    account=AccountRegistry.search_by_pesel(pesel)
    if account is not None:
        for key in data.keys():
            if key == "name":
                setattr(account,key,data[key])
            elif key == "surname":
                setattr(account,key,data[key])
        return jsonify({"message": "Account updated"}), 200
    else:
        return jsonify({"message": "Account was not found"}), 404
    

@app.route("/api/accounts/<pesel>", methods=['DELETE'])#curl -X DELETE 127.0.0.1:5000/api/accounts/68042661935
def delete_account(pesel):
    account=AccountRegistry.search_by_pesel(pesel)
    if account is not None:
        AccountRegistry.registry.remove(account)
        return jsonify({"message": "Account deleted"}), 200
    else:
        return jsonify({"message": "Account was not found"}), 404
    
@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])# curl -X POST 127.0.0.1:5000/api/accounts/68042661935/transfer -H "Content-Type: application/json" -d '{"type":"incoming","amount":"50"}'
def transfer(pesel):
    data = request.get_json()
    print(f"Transfer request: {data}")
    account=AccountRegistry.search_by_pesel(pesel)
    if account is not None:
        if data["type"] == "incoming":
            account.incoming_transfer(data["amount"])
            return jsonify({"message": "Transfer accepted"}), 200
        elif data["type"] == "outgoing":
            if account.outgoing_transfer(data["amount"]):
                return jsonify({"message": "Transfer accepted"}), 200
            else:
                return jsonify({"message": "Transfer accepted"}), 422
        elif data["type"] == "express":
            if account.outgoing_express_transfer(data["amount"]):
                return jsonify({"message": "Transfer accepted"}), 200
            else:
                return jsonify({"message": "Transfer accepted"}), 422
        else:
            return jsonify({"message": "Trasnfer type was not found"}), 404
    else:
        return jsonify({"message": f"Account was not found"}), 404