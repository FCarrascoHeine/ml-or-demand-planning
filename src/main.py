from create_input import create_input
from optimization import run_optimization
from post_processing import post_processing

input_data = create_input()
output_data = run_optimization(input_data)
post_processing(output_data)
