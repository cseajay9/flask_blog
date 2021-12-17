from flaskblog import app
print("from run: ", __name__)
def add(number1,number2):
    return number1 + number2


if __name__ == '__main__':
    app.run(debug=True)


