import json
import os
import argparse

def merge_json_files(input_dir, output_file):
    merged_data = {}
    sites_data = []
    lives_data = []
    parses_data = []
    ads_data = []

    # 遍历输入目录下的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(input_dir, filename)
            
            # 读取JSON文件
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON file {file_path}: {e}")
                continue  # 跳过无法解码的文件
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
                continue  # 跳过其他读取错误
            
            # 合并数据
            # for key, value in data.items():
            #     if key in merged_data:
            #         # 如果键已存在且不想覆盖，则将新值添加到列表中
            #         if not overwrite:
            #             if isinstance(merged_data[key], list):
            #                 merged_data[key].append(value)
            #             else:
            #                 merged_data[key] = [merged_data[key], value]
            #         else:
            #             # 否则，直接覆盖旧值
            #             merged_data[key] = value
            #     else:
            #         merged_data[key] = value

            sites_data_temp = data.get('sites')
            lives_data_temp = data.get('lives')
            parses_data_temp = data.get('parses')
            ads_data_temp = data.get('ads')

            for element in sites_data_temp:
                if element not in sites_data:
                    sites_data.append(element)
            for element in lives_data_temp:
                if element not in lives_data:
                    lives_data.append(element)
            for element in parses_data_temp:
                if element not in parses_data:
                    parses_data.append(element)
            for element in ads_data_temp:
                if element not in ads_data:
                    ads_data.append(element)

    merged_data['sites'] = sites_data
    merged_data['lives'] = lives_data
    merged_data['parses'] = parses_data
    merged_data['ads'] = ads_data


    # 将合并后的数据写入输出文件
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error writing output file {output_file}: {e}")
        exit(1)

    print(f"Merged JSON files successfully and saved to {output_file}")

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="Merge multiple JSON files into one.")
    parser.add_argument("input_dir", type=str, help="The directory containing the JSON files to merge.")
    parser.add_argument("output_file", type=str, help="The file to save the merged JSON data to.")
    
    args = parser.parse_args()

    # 检查输入目录是否存在
    if not os.path.isdir(args.input_dir):
        print(f"Error: The directory '{args.input_dir}' does not exist.")
        exit(1)

    # 调用合并函数
    merge_json_files(args.input_dir, args.output_file)