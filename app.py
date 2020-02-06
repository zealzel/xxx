from flask import Flask, render_template, request, abort


app = Flask(__name__)


@app.route('/')
def index():
    print('request', request)
    if request.method == 'GET':
        r = request.args
        a = request.args.get('a')
        b = request.args.get('b')
        name = request.args.get('name')
        try:
            assert a
            assert b
            assert name
        except AssertionError:
            abort(404)
        else:
            a = float(a)
            b = float(b)
            print('a', a, 'b', b)
    return render_template('index.html', name=name, a=a, b=b)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5008)
