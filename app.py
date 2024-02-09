from flask import Flask, render_template, request, jsonify
import xmltodict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_xml_to_json():
    try:
        xml_data = request.form['xml_data']
        json_data = xmltodict.parse(xml_data)
        return jsonify(json_data)
    except Exception as e:
        return jsonify({'error': str(e)}),400

if __name__ == '__main__':
    app.run(debug=True)
