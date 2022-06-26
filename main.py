from api_call import make_restcountries_call,os
from dataframe import make_dataframe
from db import insert_data,_create_connection

if __name__ == "__main__":
    db_file = os.getcwd() + r"\tanegelo_test.db"
    conn = _create_connection(db_file)
    if not conn:
        print("Error to connect DB!")
    else: 
        while True:
            print("\n\tWelcome to API COUNTRIES")
            print("\n1)Make a request")
            print("\n2)exit\n")
            try:
                op = int(input("Enter option: "))
                if op == 2: break
                countrie = input("Enter countrie: ")
                data = make_restcountries_call(countrie)
                df, values  = make_dataframe(data)
                insert = insert_data(conn,values)
                if insert:
                    df.to_json("data.json")
                else:
                    print("Something was wrong!!")
            except Exception as e:
                print(e)
        
    