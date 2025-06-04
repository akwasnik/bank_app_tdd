def pesel_checksum(pesel):
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
    control_digit = ((10 - (checksum % 10)) % 10)
    return control_digit == int(pesel[-1])

def pesel_checkLength(pesel):
    if len(pesel) != 11:
        return True
    return False

def nip_checksum(nip):
    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    control_digit = sum(int(nip[i]) * weights[i] for i in range(9)) % 11
    return control_digit == int(nip[-1])

def nip_checkLength(nip):
    if len(nip) != 10:
        return True
    return False

def promo_code_check(user_input,correct_promoCode):
    if user_input == correct_promoCode:
        return True
    return False

def yob_check(pesel):
    if int(pesel[0:2]) > 60 and int(pesel[2:4]) in range(1,13):
        return True
    elif int(pesel[2:4]) in range(21,33):
        return True
    else:
        return False
    
def last_3_incoming_check(history):
    if len(history) >= 3 and history[-1] > 0 and history[-2] > 0 and history[-3] > 0:
        return True
    else:
        return False
    
def last_5_transaction_sum(history):
    if len(history) >= 5:
        return sum(history[-1:-6:-1])
    else:
        return 0
    
def company_Account_Loan_Condition(balance,history: list,loan):
    if loan == 0:
        return False
    if loan*2 < balance:
        if history.count(1775) > 0:
            return True
    return False