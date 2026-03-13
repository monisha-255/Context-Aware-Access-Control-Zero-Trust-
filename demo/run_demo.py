import sys
import os

# Add the engine directory to the path so we can import the modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'engine')))

from decision_engine import evaluate_access
from context_collector import collect_context

def run_test_case(name, context):
    print(f"--- Running Test Case: {name} ---")
    result = evaluate_access(context)
    print(f"Context: {context}")
    print(f"Risk Score: {result['risk_score']}")
    print(f"Final Decision: {result['decision']}\n")

if __name__ == "__main__":
    # Test Case 1: Employee, Corporate Laptop, Office Network, Email
    case1 = collect_context("emp_01", "corporate", "local", "office", "email")
    run_test_case("Test Case 1 (Low Risk)", case1)

    # Test Case 2: Employee, Personal Laptop, Home Network, Internal Tool
    case2 = collect_context("emp_01", "personal", "local", "home", "internal_tool")
    run_test_case("Test Case 2 (Medium Risk)", case2)

    # Test Case 3: Unknown Device, Public WiFi, Foreign Location, Finance App
    case3 = collect_context("unknown", "personal", "foreign", "public_wifi", "finance")
    run_test_case("Test Case 3 (Critical Risk)", case3)

    # Test Case 4: High risk app from personal device at home
    case4 = collect_context("emp_01", "personal", "local", "home", "finance")
    run_test_case("Test Case 4 (Policy Check)", case4)
