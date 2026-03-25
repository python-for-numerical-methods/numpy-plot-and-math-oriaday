import numpy as np

def normalized_array(data):
    """
    מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.
    
    הנוסחה לביצוע:
    x_norm = (x - min) / (max - min)
    
    פרמטרים:
    data (list or np.array): מערך של מספרים.
    
    מחזירה:
    np.array: מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים.
    """
    data = np.array(data)
    data_min = np.min(data)
    data_max = np.max(data)
    
    # בדיקה האם כל הערכים זהים (מניעת חלוקה באפס)
    if data_min == data_max:
        # יצירת מערך אפסים באותו גודל, מסוג float
        new_array = np.zeros_like(data, dtype=float)
    else:
        # נרמול וקטורי של כל איברי המערך ללא לולאות
        new_array = (data - data_min) / (data_max - data_min)
        
    return new_array
    
if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
