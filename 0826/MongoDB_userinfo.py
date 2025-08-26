import pymongo

def Basic_Login(user_id, user_pw): #로그인
    with open('mongodb_account.txt', 'r') as f:
        url = f.readline()

    try:
        client = pymongo.MongoClient(url)
        db = client['pyqt6'] #pyqt6라는 db
        collection = db['userinfo'] #pyqt6 DB에 있는 userinfo라는 컬렉션

        # collection.insert_one({'id':user_id, 'password':user_pw}) #값 삽입
        # print('회원가입 성공')

        find_account = collection.find_one({'id':user_id, 'password':user_pw})
        if find_account == None: #입력한 정보의 유저 정보가 없다면
            print('ID 또는 PW정보가 틀림')

            client.close()
            return 'Do Register?'
    
        print(f'{user_id} 계정으로 로그인 성공')
        #===================================# 이하 로그인 성공 후 가능한 이벤트

        return 'Success To Login'

    except Exception as e:
        print(f'[MongoDB_userinfo.py] Basci_Login 에러: {e}')        
        return False
    
    finally:
        client.close()

def Basic_Register(user_id, user_pw): #-> Basic_Login에서 Do Register? 이 return 될 경우 수행할 func
    print(f'debug-user_id = {list(user_id)}')
    
    #1. 길이 검사
    if not(5 <= len(user_id) <= 17): #5~17자가 아닌 경우
        return 'length error'
    
    #2. 알파벳 & 숫자 검사
    for word in user_id:
        res = word.isalnum() #word가 alphabet 또는 num이면 True 리턴

        if res == False: #알파벳 또는 숫자가 아닌 경우
            return 'alphabet or num only included'
    
    with open('mongodb_account.txt', 'r') as f:
        url = f.readline()

    try:
        client = pymongo.MongoClient(url)
        db = client['pyqt6']
        collections = db['userinfo']

        collections.insert_one({'id':user_id, 'password':user_pw})
        
        print('회원가입 성공')
        return 'success to login'
    
    except Exception as e:
        print(f'[MongoDB_userinfo.py] Basic_Register 에러: {e}')
        return 'db connect error'
    
    finally:
        client.close()

