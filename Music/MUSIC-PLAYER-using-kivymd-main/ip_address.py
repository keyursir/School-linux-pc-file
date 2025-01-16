from firebase import firebase
firebase = firebase.FirebaseApplication("https://abhay-121-default-rtdb.firebaseio.com/", None)
import socket

res = firebase.get("abhay-121-default-rtdb/Users/Threat", "")
print(len(res))
ak = res["-OGc4iUklSpojmYBetTc"]["ip_address"]

print(ak)
