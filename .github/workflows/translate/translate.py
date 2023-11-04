import argparse
import os

def is_valid_file(parser, arg):
    arg = os.path.normpath(arg)  # Normalize the path
    if os.path.isabs(arg):
        # If the path is absolute, consider it invalid
        parser.error(f"The file path must be a relative path from the project root: {arg}")
    elif not os.path.exists(arg):
        # If the path doesn't exist, consider it invalid
        parser.error(f"The file does not exist: {arg}")
    else:
        # Return the absolute path if it is valid
        return arg

# argparseのパーサーを作成
parser = argparse.ArgumentParser(description='Process a file path.')

# 必須の引数としてfile-pathを追加（相対パス）
parser.add_argument('--file-path', required=True, type=lambda x: is_valid_file(parser, x),
                    help='The relative path from the project root to the file, including the filename.')

# ISO 639-1に基づく選択式の引数としてlocaleを追加
parser.add_argument('--locale', required=True, type=str, choices=['ja'],
                    help='Locale string in ISO 639-1 format. Example choices: ja.')

# 引数を解析
args = parser.parse_args()

# 解析された引数を使用
print(f"The file path is: {args.file_path}")
print(f"The selected locale (ISO 639-1) is: {args.locale}")