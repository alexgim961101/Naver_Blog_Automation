import yaml

# 설정 파일 읽기
def readConfig(file_path):
    # setting.yml 파일 경로
    yaml_file = file_path

    with open(yaml_file, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    return data

if __name__ == "__main__":
    config_data = readConfig('setting.yml')


