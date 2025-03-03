from fairlearn.metrics import demographic_parity_difference
import pandas as pd

def evaluate_fairness(predictions, sensitive_features):
    # Calculate demographic parity difference
    disparity = demographic_parity_difference(
        y_true=predictions['true_labels'],
        y_pred=predictions['predicted_labels'],
        sensitive_features=sensitive_features
    )
    return disparity

# Example usage
if __name__ == '__main__':
    data = pd.read_csv('student_data.csv')
    disparity = evaluate_fairness(data['predictions'], data['location'])
    print(f"Demographic Parity Difference: {disparity}")