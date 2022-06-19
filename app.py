import flask
from flask import Flask
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import random

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


def connectDB_getRandomQuestions(questionsCount):
    try:

        connection = mysql.connector.connect(
            host='localhost',
            database='cs_practice',
            user='user',
            password='password'
        )

        if connection.is_connected():

            cursor = connection.cursor()
            cursor.execute(
                "SELECT Qid, Description, OptId1, OptDes1, OptId2, OptDes2, OptId3, OptDes3, OptId4, OptDes4, Answer FROM Questions;")

            i = 1
            data = {"data": {

            }
            }
            for (
            QId, Description, OptId1, OptDes1, OptId2, OptDes2, OptId3, OptDes3, OptId4, OptDes4, Answer) in cursor:
                data['data'][str(i)] = {"QId": QId,
                                        "Description": Description,
                                        "OptId1": OptId1,
                                        "OptDes1": OptDes1,
                                        "OptId2": OptId2,
                                        "OptDes2": OptDes2,
                                        "OptId3": OptId3,
                                        "OptDes3": OptDes3,
                                        "OptId4": OptId4,
                                        "OptDes4": OptDes4,
                                        "Answer": Answer
                                        }
                i += 1

            data2 = {"data": {

            }
            }

            data2_index = 1
            added_list = []

            while data2_index <= questionsCount:
                temp = data['data'][str(random.randint(1, 50))]
                if temp not in added_list:
                    data2['data'][str(data2_index)] = temp
                    added_list.append(temp)
                    data2_index += 1

            # 隨機抽取Qid 1~10的資料
            # print(data['data'][str(random.randint(1, 10))])

            return flask.jsonify(data2)


    except Error as e:
        print("資料庫連接失敗:", e)

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            # 關閉資料庫


def connectDB_getAllQuestions():
    try:

        connection = mysql.connector.connect(
            host='localhost',
            database='cs_practice',
            user='dw',
            password='Wang61224!'
        )

        if connection.is_connected():

            cursor = connection.cursor()
            cursor.execute(
                "SELECT Qid, Description, OptId1, OptDes1, OptId2, OptDes2, OptId3, OptDes3, OptId4, OptDes4, Answer FROM Questions;")

            i = 1
            data = {"data": {

            }
            }

            for (
            QId, Description, OptId1, OptDes1, OptId2, OptDes2, OptId3, OptDes3, OptId4, OptDes4, Answer) in cursor:
                data['data'][str(i)] = {"QId": QId,
                                        "Description": Description,
                                        "OptId1": OptId1,
                                        "OptDes1": OptDes1,
                                        "OptId2": OptId2,
                                        "OptDes2": OptDes2,
                                        "OptId3": OptId3,
                                        "OptDes3": OptDes3,
                                        "OptId4": OptId4,
                                        "OptDes4": OptDes4,
                                        "Answer": Answer
                                        }
                i += 1

            return flask.jsonify(data)


    except Error as e:
        print("資料庫連接失敗:", e)

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            # 關閉資料庫

@app.route('/getQuestions')
def getRandomQuestions():  # put application's code here
    return connectDB_getRandomQuestions(40)

@app.route('/getTestQuestions')
def getTestRandomQuestions():  # put application's code here
    return connectDB_getRandomQuestions(5)

@app.route('/getAllQuestions')
def getAllQuestions():
    return connectDB_getAllQuestions()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3006)
