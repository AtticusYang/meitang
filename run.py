from meitang import create_app 

app = create_app()

if __name__ == '__main__':
    app.run('10.11.215.157', debug=True)
