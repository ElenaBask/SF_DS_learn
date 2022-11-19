def accurate_forecast(number:int=1) -> int:
    """ Guessing the number by binary search
    Args:
        number (int, optional): The hidden number_. Defaults to 1.

    Returns:
        int: Number of attempts_
    """
    count = 0
    lower_bound, upper_bound = 0, 101
    while True:
        count += 1
        predict_number =  lower_bound + (upper_bound - lower_bound)//2
        if number > predict_number:
            lower_bound = predict_number
        elif number < predict_number:
            upper_bound = predict_number
        else:
            break
    return count

import numpy as np
def algorithm_evaluation(repetitions:int=1000) -> int:
    """We check the algorithm's ability to guess the number
       in less than 20 attempts with 1000 or more repetitions

    Args:
        repetitions (int, optional): number of repetitions. Defaults to 1000.

    Returns:
        int: Average number of attempts
    """
    counter = 0
    for i in range(1, repetitions+1):
        number = np.random.randint(1, 101) # загадываем число
        counter += accurate_forecast(number)
    return round(counter/1000)

if __name__ == '__main__':
    rept = int(input('Enter the number of repetitions to test the algorithm '))
    print(algorithm_evaluation())