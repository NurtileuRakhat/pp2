import psycopg2
import re

def connect():
  config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='postgres',    
    password='Nurtiley17'
)
  cursor = config.cursor()
  return config,cursor

def return_all_record():
  # Connect to the database
  conn, cur = connect()

  # Construct the SQL query to retrieve all records from the phonebook table
  sql = '''SELECT id, name, number FROM phonebook ORDER BY id;'''

  # Execute the query and fetch all the results
  cur.execute(sql)
  rows = cur.fetchall()

  # Loop over the results and print each row
  for row in rows:
    print(row)

  # Commit the transaction and close the cursor and connection
  conn.commit()
  cur.close()
  conn.close()

def insert_or_update_user(id,name, number):
    # Connect to the database
    config,cursor = connect()

    # Check if a user with the given name already exists in the database
    cursor.execute("SELECT COUNT(*) FROM phonebook WHERE name = %s", (name,))
    user_count = cursor.fetchone()[0]

    # If the user does not exist, insert a new record into the database
    if user_count == 0:
        cursor.execute("INSERT INTO phonebook (id,name, number) VALUES (%s,%s, %s)", (id,name, number))
        print(f"Added user {name} with phone number {number}.")

    # If the user already exists, update their phone number
    else:
        cursor.execute("UPDATE phonebook SET number = %s WHERE name = %s", (number, name))
        print(f"Phone number for user {name} updated to {number}.")
    
    # Commit the changes to the database and close the cursor and connection
    config.commit()
    cursor.close()
    config.close()

def insert_users(id,names, phones):
  incorrect_phones = []
  # Connect to the database
  config,cursor = connect()
  
  for name, phone in zip(names, phones):
      if is_valid_phone(phone):
          # insert user into database
          cursor.execute("INSERT INTO phonebook (id,name, number) VALUES (%s,%s, %s)", (id ,name, phone))
      else:
          # add incorrect phone to list
          incorrect_phones.append((name, phone))
  # commit changes and close connection
  config.commit()
  cursor.close()
  config.close()
  # return list of incorrect phone numbers
  return incorrect_phones

def is_valid_phone(phone):
    # check if phone number has correct format
    x = re.search(r'^87\d{9}', phone)
    y = re.search(r'^\+77\d{9}', phone)
    z = re.search(r'^7\d{9}', phone)
    if x is not None and phone == x.group():
        return True
    elif y is not None and phone == y.group():
        return True
    elif z is not None and phone == z.group():
        return True
    else:
        return False


def query_with_pagination(table_name, limit, offset):
    # Connect to the database
    config,cursor = connect()

    # Query the data with pagination
    cursor.execute(f"SELECT * FROM {table_name} ORDER BY id ASC LIMIT {limit} OFFSET {offset};")
    rows = cursor.fetchall()

    # Close the database connection
    cursor.close()
    config.close()

    return rows

def delete_user_by_username_or_phone(name=None, number=None):
    # Connect to the database
    config,cursor = connect()

    # Delete the user(s) by name or phone
    if name is not None:
        cursor.execute(f"DELETE FROM phonebook WHERE name = '{name}';")
    elif number is not None:
        cursor.execute(f"DELETE FROM phonebook WHERE number = '{number}';")
    else:
        raise ValueError("Either name or phone must be provided for deletion")

    # Commit the changes and close the database connection
    config.commit()
    cursor.close()
    config.close()

# # Example usage
# print(query_with_pagination('phonebook',10,2))
# names = ["123", "123", "123"]
# phones = ["87076039179", "7777777777777777777777777", "7777777777777777777777777"]
# incorrect_phones = insert_users(5,names, phones)
# print("Incorrect phones:", incorrect_phones)
# insert_or_update_user(4,'Nurtileu1', '87076039456')
# return_all_record()
# delete_user_by_username_or_phone("Nurtileu1")