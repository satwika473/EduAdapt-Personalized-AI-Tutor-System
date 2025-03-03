from flask import Flask, request, jsonify
from models.model_training import AdaptiveEngine
from database.db_utils import get_student_data, update_student_progress

app = Flask(__name__)

@app.route('/assess', methods=['POST'])
def assess_student():
    data = request.json
    student_id = data['student_id']
    responses = data['responses']
    
    # Fetch student data
    student_data = get_student_data(student_id)
    
    # Evaluate responses using adaptive engine
    engine = AdaptiveEngine()
    progress_report = engine.evaluate_responses(responses, student_data)
    
    # Update student progress
    update_student_progress(student_id, progress_report)
    
    return jsonify(progress_report)

if __name__ == '__main__':
    app.run(debug=True)