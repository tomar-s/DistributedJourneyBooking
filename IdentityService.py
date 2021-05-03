import mysql.connector
import uuid
import redis_connector as cache

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="admin",
  database="mydatabase"
)

mycursor = mydb.cursor()

def authenticate_user(userId, token):
    saved_token = cache.check_cache_user_token(userId)
    
    token_Matched = False
    if token == saved_token:
        token_Matched = True
    print("status: ", token_Matched)
    return token_Matched

def register_user(userId):
    user_token = str(uuid.uuid4())
    query = "INSERT INTO user_profile (owner_unique_Id, user_token) VALUES (%s, %s)"
    val = (userId, user_token)
    try:
        mycursor.execute(query, val)
        mydb.commit()
        print("user_token is: ", user_token)
    except Exception as e:
        user_token = None
        print(e)
        pass
    return user_token

# def main():
# #   register_user("Rupasmita1")
#   user_token = "4a265670-c0e5-4e95-8e2b-b3eb2ec9c3a4"
#   authenticate_user("Rupasmita123",user_token)

# if __name__ == "__main__":
#     main()

