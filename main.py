import pandas as pd

def combine_and_deduplicate_ips(file_path, output_file='unique_ips.txt'):
    """
    Объединяет IP-адреса из первого, второго и третьего столбцов файла Excel,
    удаляет дубликаты и записывает уникальные IP-адреса в отдельный файл.

    Args:
        file_path (str): Путь к файлу Excel.
        output_file (str, optional): Путь к файлу с уникальными IP-адресами. Defaults to 'unique_ips.txt'.
    """

    df = pd.read_excel(file_path)

    # Получаем списки IP-адресов из каждого столбца
    ip_list_1 = df.iloc[:, 0].tolist()
    ip_list_2 = df.iloc[:, 1].tolist()
    ip_list_3 = df.iloc[:, 2].tolist()

    # Объединяем списки и удаляем дубликаты
    all_ips = set(ip_list_1 + ip_list_2 + ip_list_3)

    # Записываем уникальные IP-адреса в файл
    with open(output_file, 'w') as f:
        for ip in all_ips:
            f.write(str(ip) + '\n')

    print(f"Уникальные IP-адреса записаны в файл: {output_file}")

# Пример использования
file_path = 'D:\\1.xlsx'  # Замените на путь к вашему файлу

combine_and_deduplicate_ips(file_path)