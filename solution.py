import pandas as pd
import numpy as np


chat_id = 156287560 # Ваш chat ID, не меняйте название переменной

def solution(control_npv, test_npv) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    from scipy.stats import ttest_ind

    # Рассчитываем среднее значение NPV в контрольной группе
    #control_mean = sum(control_npv) / len(control_npv)
    
    # Рассчитываем среднее значение NPV в тестовой группе
    #test_mean = sum(test_npv) / len(test_npv)
    
    # Выполняем t-тест Стьюдента для независимых выборок
    t_stat, p_value = ttest_ind(control_npv, test_npv, equal_var=False)
    
    # Определяем, отклоняем ли нулевую гипотезу
    return p_value < 0.03
